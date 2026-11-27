# Hipótesis automáticas — 2026-11-27 05:31 UTC
_Generado por shadow_postmortem.py sobre 1511338 resoluciones (PNL=+214704.79€)_

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
- **FILTRO** `restante_s_al_confirmar` < `130.21` → IC=-0.219 (n=12982)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.21
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=38946)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#BTC#15min
- **PATRÓN** `restante_s_al_confirmar` < `641.55` → IC=+0.135 (n=2571)

  - _Acción_: Kelly boost +0.67€ cuando `restante_s_al_confirmar` < 641.55 (IC base=+0.093)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.42` → IC=-0.162 (n=3678)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.42
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=11034)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=31290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7658.2475` → IC=+0.151 (n=2543)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7658.2475 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.126 (n=27987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=33848)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=25206)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=9020)

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

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2817)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.378 (n=1942)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=2767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.329 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=3212)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.192)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.143 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.144 (n=998)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.244 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1219)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.076)

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
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.144)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.165 (n=493)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.052)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.135 (n=1084)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.255 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=27952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=23595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.219 (n=8872)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.336 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `5024.6381` → IC=+0.335 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5024.6381 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=6361)
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

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=2648)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.244 (n=1883)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.203)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=6197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=5249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6355)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4888)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=4899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.251 (n=2376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1685)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=6048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=3844)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.198 (n=1951)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=35831)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.184 (n=5471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.175 (n=11724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=16882)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=15226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6418)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=6272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=12899)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.230 (n=5117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5899)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=6213)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=6035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.252 (n=6523)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=6100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=6088)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7510)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=13102)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=14449)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.31` → IC=+0.138 (n=16141)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.31 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6366)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6571)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.73` → IC=+0.142 (n=8044)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.73 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6736)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.134 (n=8697)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.95 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.86` → IC=+0.134 (n=8098)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5109` → IC=+0.140 (n=20997)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5109 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=21250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=14603)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.973` → IC=+0.246 (n=7001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.973 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8821` → IC=+0.289 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8821 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.463` → IC=+0.190 (n=10531)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.463 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.266 (n=5753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3027` → IC=+0.255 (n=2168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3027 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.742` → IC=+0.233 (n=5082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.742 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=10063)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `5007.2196` → IC=+0.150 (n=6999)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5007.2196 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.123 (n=13281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0067 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5651` → IC=+0.144 (n=26556)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5651 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6805` → IC=+0.193 (n=1808)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6805 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1796` → IC=+0.194 (n=10910)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1796 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.196 (n=7400)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8561 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.230 (n=2690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.2857` → IC=+0.212 (n=8533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2857 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.227 (n=18806)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3062` → IC=+0.212 (n=3922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3062 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=2171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9823` → IC=+0.272 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9823 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.799` → IC=+0.286 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.799 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.259 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4379` → IC=+0.212 (n=4285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4379 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2059.42` → IC=+0.214 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2059.42 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.244 (n=1840)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0975` → IC=+0.266 (n=1353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0975 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1863)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0827` → IC=+0.273 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0827 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0727` → IC=+0.239 (n=3508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0727 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.245 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.8558` → IC=+0.242 (n=2590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8558 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=4347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.229 (n=1697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1164` → IC=+0.245 (n=1687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1164 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=4018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.220 (n=2732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.8881` → IC=+0.247 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8881 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.2059` → IC=+0.228 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2059 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.5771` → IC=+0.220 (n=4229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5771 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.687` → IC=+0.261 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.687 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6957` → IC=+0.226 (n=3423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6957 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.262 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.4328` → IC=+0.244 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4328 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.158 (n=3692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0062 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3654` → IC=+0.144 (n=4193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3654 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=1575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.3638` → IC=+0.199 (n=2794)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3638 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1569` → IC=+0.151 (n=4114)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1569 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.576` → IC=+0.138 (n=655)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.576 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.972` → IC=+0.142 (n=3860)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.972 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.157 (n=1398)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6279 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0979` → IC=+0.158 (n=1520)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0979 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4465` → IC=+0.143 (n=4059)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4465 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.185 (n=1346)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.211 (n=2141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.891` → IC=+0.276 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.891 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.193 (n=4237)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.224 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7337` → IC=+0.210 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7337 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5543)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1899.9284` → IC=+0.202 (n=2141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1899.9284 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.226 (n=1948)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.221 (n=2011)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3084` → IC=+0.229 (n=2952)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3084 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=2019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.268 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.611` → IC=+0.266 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.611 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.253 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1563` → IC=+0.230 (n=2854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1563 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1881.672` → IC=+0.224 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.672 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.220 (n=4255)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.170 (n=265)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5698)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.137 (n=767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9414` → IC=+0.247 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9414 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1615` → IC=+0.348 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1615 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.377` → IC=+0.341 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.377 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.222` → IC=+0.216 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.222 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.8661` → IC=+0.342 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8661 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2462` → IC=+0.361 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2462 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1652` → IC=+0.344 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1652 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.358 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4167` → IC=+0.365 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4167 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.2749` → IC=+0.346 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2749 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.350 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.070)

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

- **FILTRO** `ibs_20min` > `0.1923` → IC=-0.125 (n=5596)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1923
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2764)

- **FILTRO** `sigma_ewma_delta_pct` > `8.315` → IC=-0.226 (n=907)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.315
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=7453)

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

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.159 (n=2764)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1923 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.8369` → IC=+0.299 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8369 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2408` → IC=+0.291 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2408 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.6944` → IC=+0.307 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6944 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0787` → IC=+0.319 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0787 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4493` → IC=+0.305 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4493 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.525` → IC=+0.299 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.525 (IC base=-0.031)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7949` → IC=-0.161 (n=4290)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7949
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=2212)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.177 (n=1378)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=5124)

- **FILTRO** `ibs_20min` > `0.72` → IC=-0.190 (n=2246)

  - _Acción_: SKIP cuando `ibs_20min` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=6774)

- **PATRÓN** `ibs_20min` > `0.7949` → IC=+0.147 (n=2212)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7949 (IC base=-0.056)

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

- **PATRÓN** `volumen_regimen` < `0.636` → IC=+0.274 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.636 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.213` → IC=+0.277 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.213 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1083` → IC=+0.273 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1083 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.5121` → IC=+0.262 (n=2567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5121 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.446` → IC=+0.267 (n=2567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.446 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.186 (n=9202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0113 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.284 (n=12506)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0083` → IC=+0.304 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0083 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.456` → IC=+0.169 (n=12420)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.456 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.279 (n=9215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.296 (n=2280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6501` → IC=+0.289 (n=5346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6501 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=15688)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.137 (n=17876)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0073 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5158` → IC=+0.174 (n=23585)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5158 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2836` → IC=+0.282 (n=9537)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2836 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.6917` → IC=+0.279 (n=4046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6917 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1862` → IC=+0.286 (n=3064)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1862 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.322 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4546` → IC=+0.302 (n=4561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4546 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2761` → IC=+0.304 (n=6202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2761 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.312 (n=13666)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8198` → IC=-0.149 (n=4869)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8198
  - _Potencial_: sin este filtro IC_bueno=+0.316 (n=2509)

- **FILTRO** `ibs_20min` > `0.6977` → IC=-0.241 (n=1675)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6977
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=5027)

- **FILTRO** `sigma_ewma_delta_pct` > `4.059` → IC=-0.241 (n=1404)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.059
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5298)

- **PATRÓN** `ibs_20min` > `0.8198` → IC=+0.316 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8198 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.164` → IC=+0.177 (n=2744)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 2.164 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.334 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.296 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2336` → IC=+0.319 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2336 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.326 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.170 (n=1677)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1702 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1559` → IC=+0.383 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1559 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.6476` → IC=+0.387 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6476 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1841` → IC=+0.229 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1841 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.5278` → IC=+0.214 (n=2990)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5278 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.694` → IC=+0.221 (n=2406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.694 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.243 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4151` → IC=+0.231 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4151 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4477` → IC=+0.223 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4477 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `312.0` → IC=+0.237 (n=2346)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 312.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.7508` → IC=+0.258 (n=2462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7508 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.0128` → IC=+0.268 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0128 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.281 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5313` → IC=+0.257 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5313 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1523` → IC=+0.261 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1523 (IC base=+0.005)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `2.564` → IC=+0.306 (n=2559)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.564 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.1306` → IC=+0.293 (n=3492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1306 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.1664` → IC=+0.296 (n=2439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1664 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2012.7984` → IC=+0.300 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2012.7984 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.301 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.337 (n=1586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.189` → IC=+0.328 (n=1542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.189 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.322 (n=1344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.312 (n=1584)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1579` → IC=+0.322 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1579 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.949` → IC=+0.321 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.949 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.199` → IC=+0.308 (n=3479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.199 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.315 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7501` → IC=+0.325 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7501 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1572.032` → IC=+0.313 (n=3125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1572.032 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.310 (n=3012)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1622` → IC=+0.237 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1622 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.3876` → IC=+0.232 (n=2562)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3876 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.1742` → IC=+0.234 (n=2548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1742 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.5964` → IC=+0.231 (n=2547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5964 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.235 (n=2680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.237 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4071` → IC=+0.239 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4071 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.249 (n=2530)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.3915` → IC=+0.260 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3915 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.1719` → IC=+0.262 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1719 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6129` → IC=+0.258 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6129 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.285 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.7813` → IC=+0.282 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7813 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4232` → IC=+0.267 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4232 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.283 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.249 (n=2805)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=2855)

- **FILTRO** `ibs_20min` > `0.6` → IC=-0.234 (n=1334)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=4017)

- **FILTRO** `sigma_ewma_delta_pct` > `8.256` → IC=-0.259 (n=613)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.256
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=4738)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.317 (n=2855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `1.1223` → IC=+0.354 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1223 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.461` → IC=+0.161 (n=2318)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.461 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.842` → IC=+0.352 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.842 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `0.695` → IC=+0.338 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.695 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.339 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.369 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.7946` → IC=+0.357 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7946 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.357 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.168 (n=4017)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.3259` → IC=+0.273 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3259 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.725` → IC=+0.136 (n=4194)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.725 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.284 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6872 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.299 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.807` → IC=+0.283 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.807 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.289 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.349 (n=2667)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=3007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=3136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.6508` → IC=+0.336 (n=2985)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6508 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2206` → IC=+0.336 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2206 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.735` → IC=+0.342 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.735 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.323 (n=2986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.342 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.5404` → IC=+0.326 (n=2580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5404 (IC base=+0.312)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.314 (n=3783)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `2997.2954` → IC=+0.322 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2997.2954 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.331 (n=3208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=3213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` < `0.39` → IC=+0.327 (n=3207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.39 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `1.3078` → IC=+0.323 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3078 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` < `0.2595` → IC=+0.316 (n=3167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2595 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.65` → IC=+0.329 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.65 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` < `0.6348` → IC=+0.318 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6348 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.2096` → IC=+0.340 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2096 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.357 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` < `1.4172` → IC=+0.323 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4172 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `2.1642` → IC=+0.318 (n=1368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1642 (IC base=+0.314)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.219 (n=6725)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1286` → IC=+0.194 (n=8874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1286 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=20933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5342` → IC=+0.228 (n=20155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5342 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1715` → IC=+0.205 (n=7569)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1715 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.685` → IC=+0.259 (n=3953)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.685 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.172` → IC=+0.152 (n=13449)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.172 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6193` → IC=+0.151 (n=13451)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6193 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.207 (n=2901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6056` → IC=+0.185 (n=6550)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6056 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.192 (n=19122)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.193 (n=8854)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0063 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.222 (n=6701)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=9640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5292` → IC=+0.236 (n=20096)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5292 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.1994` → IC=+0.179 (n=14704)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1994 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.369` → IC=+0.189 (n=3155)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.369 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.483` → IC=+0.191 (n=17991)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.483 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.166 (n=14230)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1894 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.216 (n=3015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5649` → IC=+0.184 (n=8467)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5649 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6394` → IC=+0.195 (n=6414)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6394 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.198 (n=19085)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 90.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0765` → IC=+0.267 (n=1105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0765 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=2241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9415` → IC=+0.291 (n=2206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9415 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.476` → IC=+0.325 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.476 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.285 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8308` → IC=+0.226 (n=2114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8308 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.227 (n=3171)

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

- **PATRÓN** `drift_60min` |x|≤ `0.0683` → IC=+0.174 (n=1030)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0683 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2428` → IC=+0.201 (n=3090)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2428 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1983` → IC=+0.210 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1983 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.497` → IC=+0.203 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.497 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.136 (n=2060)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8509 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.128 (n=1030)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.1915 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.170 (n=473)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.130 (n=1340)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4536` → IC=+0.138 (n=1015)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4536 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `382.0` → IC=+0.130 (n=3014)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 382.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.181 (n=2950)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0062 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.169 (n=3348)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.176 (n=1601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6188` → IC=+0.209 (n=3348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6188 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2269` → IC=+0.175 (n=3640)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2269 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.87` → IC=+0.177 (n=617)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.87 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.023` → IC=+0.156 (n=2946)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.023 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2049` → IC=+0.162 (n=3348)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2049 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.155 (n=2809)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4845` → IC=+0.157 (n=3221)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4845 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.197 (n=1392)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 202.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.231 (n=1542)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2603` → IC=+0.235 (n=2267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2603 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.004` → IC=+0.304 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.004 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.235 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.1692` → IC=+0.218 (n=2218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1692 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2011.1284` → IC=+0.223 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2011.1284 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.242 (n=3071)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.265 (n=2048)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.272 (n=1159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0465` → IC=+0.290 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0465 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.689` → IC=+0.280 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.689 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3529` → IC=+0.279 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3529 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7646` → IC=+0.241 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7646 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1802` → IC=+0.249 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1802 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1878.6774` → IC=+0.247 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1878.6774 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.236 (n=2971)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.189 (n=1114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.004 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.169 (n=1111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2413` → IC=+0.187 (n=3329)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.2413 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1514` → IC=+0.188 (n=1870)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1514 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.177` → IC=+0.199 (n=566)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.177 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.835` → IC=+0.138 (n=2220)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.835 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.177 (n=500)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.515` → IC=+0.125 (n=1435)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.515 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4985` → IC=+0.136 (n=1087)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4985 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6919.7421` → IC=+0.196 (n=1509)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6919.7421 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.128 (n=3266)

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
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.176 (n=1239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0132 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.206 (n=3709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.801` → IC=+0.213 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.801 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.862` → IC=+0.281 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.862 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1665` → IC=+0.132 (n=3707)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1665 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.126 (n=3707)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6235 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.125 (n=3783)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.133 (n=515)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5452` → IC=+0.128 (n=1585)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5452 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2710.971` → IC=+0.198 (n=1681)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2710.971 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.130 (n=2361)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 26.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.152 (n=3421)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0113 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1194` → IC=+0.170 (n=1296)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1194 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.220 (n=3885)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2295` → IC=+0.146 (n=3859)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2295 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.146 (n=3442)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.129 (n=3884)

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

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.132 (n=3694)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 42.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.248 (n=2970)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.4636` → IC=+0.232 (n=2926)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4636 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=3453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.253 (n=3324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1868` → IC=+0.233 (n=2044)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1868 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.842` → IC=+0.226 (n=3437)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.842 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.504` → IC=+0.264 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.504 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6165` → IC=+0.233 (n=3324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6165 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2901` → IC=+0.266 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2901 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.5393` → IC=+0.227 (n=2902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5393 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=4244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2870.0504` → IC=+0.230 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2870.0504 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0159` → IC=+0.247 (n=2301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0159 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6217` → IC=+0.247 (n=3451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6217 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1550)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0388` → IC=+0.297 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0388 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `1.1962` → IC=+0.254 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1962 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.985` → IC=+0.272 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.985 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8643` → IC=+0.244 (n=2300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8643 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0483` → IC=+0.238 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0483 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.299 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.856` → IC=+0.237 (n=2184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.856 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5615` → IC=+0.238 (n=2926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5615 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.201 (n=1762)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1457` → IC=+0.168 (n=2319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1457 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=5501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.2961` → IC=+0.189 (n=5265)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2961 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9188` → IC=+0.179 (n=798)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9188 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.508` → IC=+0.211 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.508 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8537` → IC=+0.163 (n=3207)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8537 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1862` → IC=+0.158 (n=1604)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1862 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1551` → IC=+0.173 (n=1355)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1551 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.5251` → IC=+0.157 (n=2263)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5251 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.806` → IC=+0.156 (n=3428)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.806 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.155 (n=5795)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7302.6535` → IC=+0.190 (n=2387)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7302.6535 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.7108` → IC=+0.141 (n=5798)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.7108 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.138 (n=2559)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 22.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.203 (n=1143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.231 (n=433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.224 (n=1173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.6069` → IC=+0.250 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6069 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.6942` → IC=+0.240 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6942 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.832` → IC=+0.229 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.832 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.8658` → IC=+0.210 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8658 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.0881` → IC=+0.215 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0881 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.1491` → IC=+0.203 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1491 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.4006` → IC=+0.195 (n=1275)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4006 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `15568.6179` → IC=+0.206 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15568.6179 (IC base=+0.192)

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

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.135 (n=475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0129 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.122 (n=472)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.140 (n=1416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.7273` → IC=+0.224 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7273 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.5099` → IC=+0.148 (n=452)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.5099 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.863` → IC=+0.231 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.863 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.0411` → IC=+0.132 (n=1245)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0411 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.7008` → IC=+0.126 (n=1264)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.7008 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.149 (n=243)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4156` → IC=+0.154 (n=458)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4156 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=1429)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3048.1866` → IC=+0.150 (n=472)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3048.1866 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.137 (n=441)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 9.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6923` → IC=+0.145 (n=1584)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6923 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `2742.0503` → IC=+0.161 (n=718)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2742.0503 (IC base=+0.079)

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
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.226 (n=8900)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=27829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9656` → IC=+0.298 (n=8885)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9656 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9569` → IC=+0.216 (n=3077)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9569 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.863` → IC=+0.259 (n=6518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.863 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.865` → IC=+0.163 (n=11986)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.865 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.217 (n=3492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6338` → IC=+0.193 (n=8692)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6338 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1765.9775` → IC=+0.181 (n=26654)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1765.9775 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.199 (n=25305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.199 (n=8267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0056 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.207 (n=8272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4032` → IC=+0.201 (n=21810)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4032 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=9270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.49` → IC=+0.251 (n=21818)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.49 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1946` → IC=+0.182 (n=15859)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1946 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.491` → IC=+0.205 (n=23139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.491 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.626` → IC=+0.182 (n=5540)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.626 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.255 (n=3406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6298` → IC=+0.210 (n=7957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6298 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.220 (n=20915)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3104` → IC=+0.236 (n=3736)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3104 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2848)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.9701` → IC=+0.310 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9701 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.038` → IC=+0.299 (n=2792)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.038 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.288 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2822` → IC=+0.241 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2822 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2059.4978` → IC=+0.237 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2059.4978 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.267 (n=1299)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.263)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.263 (n=1769)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.263)

- **PATRÓN** `drift_60min` |x|≤ `0.1299` → IC=+0.289 (n=1715)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1299 (IC base=+0.263)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.265 (n=4041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.263)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.264 (n=3513)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` < `0.4711` → IC=+0.284 (n=3428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4711 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.265 (n=3562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.285 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` < `1.5664` → IC=+0.263 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5664 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `2.6409` → IC=+0.270 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6409 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=4182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.263)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.264 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.263)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.168 (n=1937)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.147 (n=1464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.1869` → IC=+0.186 (n=4388)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.1869 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.208 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.003` → IC=+0.174 (n=685)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.003 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6326` → IC=+0.157 (n=1463)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6326 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.0625` → IC=+0.141 (n=1989)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0625 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.191 (n=612)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.143 (n=3801)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5201` → IC=+0.145 (n=3858)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5201 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.151 (n=2856)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 288.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.169 (n=3413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0062 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.175 (n=1293)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=1433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.3239` → IC=+0.232 (n=2585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3239 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1577` → IC=+0.162 (n=3814)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1577 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.188` → IC=+0.150 (n=3959)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.188 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0397` → IC=+0.157 (n=3410)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0397 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.198 (n=707)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.434` → IC=+0.151 (n=3763)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.434 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.152 (n=2508)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=5031)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.183 (n=1229)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 211.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.242 (n=2016)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=4653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.224 (n=3953)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.887` → IC=+0.312 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.887 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.204` → IC=+0.234 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.204 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.7692` → IC=+0.231 (n=3880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7692 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1897.1675` → IC=+0.237 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1897.1675 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.248 (n=1886)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1863` → IC=+0.259 (n=1882)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1863 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1960)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0707` → IC=+0.295 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0707 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.86` → IC=+0.303 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.86 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.3463` → IC=+0.299 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3463 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.255 (n=2763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1993.1118` → IC=+0.253 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1993.1118 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.246 (n=3635)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.187 (n=1544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3614` → IC=+0.147 (n=4058)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3614 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8747` → IC=+0.261 (n=1538)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8747 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.169 (n=2264)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.064` → IC=+0.169 (n=683)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.064 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.153 (n=3076)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.856 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.201 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5173` → IC=+0.154 (n=1986)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5173 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.142 (n=2045)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5911.3854` → IC=+0.229 (n=2090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5911.3854 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.142 (n=2999)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.170 (n=3908)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4669` → IC=+0.163 (n=3904)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4669 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.3466` → IC=+0.240 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3466 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.8834` → IC=+0.156 (n=4710)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.8834 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.033` → IC=+0.157 (n=779)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.033 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.02` → IC=+0.155 (n=3402)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.02 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.162 (n=2603)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8497 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.29` → IC=+0.210 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.29 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1945` → IC=+0.156 (n=3332)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1945 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.523` → IC=+0.159 (n=3382)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.523 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `6722.1308` → IC=+0.216 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6722.1308 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.171 (n=1281)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.157 (n=1567)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0133 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.697` → IC=+0.256 (n=3129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.697 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.0684` → IC=+0.199 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0684 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.196` → IC=+0.269 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.196 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2087` → IC=+0.127 (n=4694)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2087 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1018` → IC=+0.124 (n=4475)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1018 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.141 (n=589)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `2.5079` → IC=+0.126 (n=4588)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.5079 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2771.6472` → IC=+0.238 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2771.6472 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.158 (n=3859)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0114 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.144` → IC=+0.150 (n=1462)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.144 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=4507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.246 (n=3867)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5455 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.2284` → IC=+0.152 (n=4045)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2284 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.021` → IC=+0.161 (n=4262)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.021 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1935` → IC=+0.142 (n=4384)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1935 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.201 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.163 (n=1398)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4969` → IC=+0.143 (n=1397)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4969 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2645.755` → IC=+0.225 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.755 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.150 (n=4217)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 47.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.254 (n=4290)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=4485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.240 (n=2868)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.302 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.2042` → IC=+0.249 (n=2174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2042 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.925` → IC=+0.298 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.925 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.6394` → IC=+0.241 (n=4287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6394 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.260 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.5294` → IC=+0.254 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5294 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=5451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2645.437` → IC=+0.238 (n=2858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.437 (IC base=+0.235)

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

- **PATRÓN** `dist_vwap_pct` < `0.232` → IC=+0.250 (n=4289)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.232 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.91` → IC=+0.282 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.91 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.6361` → IC=+0.248 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6361 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2193` → IC=+0.266 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2193 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.312 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4366` → IC=+0.250 (n=4233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4366 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.246 (n=3701)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.233 (n=6627)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.5404` → IC=+0.234 (n=7527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5404 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=7547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.260 (n=2510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` < `0.9686` → IC=+0.230 (n=6190)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9686 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.436` → IC=+0.237 (n=2512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.436 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `0.7048` → IC=+0.231 (n=2361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7048 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.8776` → IC=+0.229 (n=3576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8776 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.236 (n=2105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4493` → IC=+0.237 (n=2470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4493 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.231 (n=5373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `3770.877` → IC=+0.234 (n=5018)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3770.877 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.229 (n=1806)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.212 (n=2453)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.4191` → IC=+0.221 (n=4753)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4191 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=2449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.6134` → IC=+0.215 (n=4753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6134 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.7156` → IC=+0.220 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7156 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.68` → IC=+0.224 (n=4916)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.68 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2534` → IC=+0.211 (n=4906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2534 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.7288` → IC=+0.204 (n=4383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7288 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.213 (n=4996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.217 (n=2341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5357 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8218` → IC=+0.219 (n=3546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8218 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.236 (n=3565)

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

- **PATRÓN** `drift_60min` |x|≤ `0.474` → IC=+0.222 (n=2084)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.474 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.4677` → IC=+0.231 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4677 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.8315` → IC=+0.216 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8315 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.4289` → IC=+0.225 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4289 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.248` → IC=+0.221 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.248 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8621` → IC=+0.217 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8621 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.0645` → IC=+0.220 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0645 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.217 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.216 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.159 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4004` → IC=+0.234 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4004 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4929` → IC=+0.216 (n=1818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4929 (IC base=+0.215)

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

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.232 (n=445)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.222 (n=1216)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.9919` → IC=+0.303 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9919 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `1.0952` → IC=+0.244 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0952 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.038` → IC=+0.273 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.038 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.251 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `1.2446` → IC=+0.224 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2446 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.224 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2758` → IC=+0.250 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2758 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.5096` → IC=+0.231 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5096 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `3376.312` → IC=+0.246 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3376.312 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0141` → IC=+0.247 (n=1009)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0141 (IC base=+0.247)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.256 (n=673)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.247)

- **PATRÓN** `drift_60min` |x|≤ `0.685` → IC=+0.260 (n=1009)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.685 (IC base=+0.247)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.266 (n=700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` < `0.6444` → IC=+0.271 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6444 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.043` → IC=+0.265 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.043 (IC base=+0.247)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.260 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.255 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` < `1.4777` → IC=+0.246 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4777 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` > `2.2218` → IC=+0.273 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2218 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.250 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `4039.5604` → IC=+0.267 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4039.5604 (IC base=+0.247)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.275 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.247)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.145 (n=980)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0043 (IC base=+0.079)

- **PATRÓN** `ibs_20min` > `0.4221` → IC=+0.142 (n=2844)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.4221 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.1608` → IC=+0.161 (n=1316)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1608 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.154 (n=622)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.5796` → IC=+0.178 (n=2258)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5796 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.538` → IC=+0.133 (n=1002)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 2.538 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.181 (n=634)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.1603` → IC=+0.122 (n=1914)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.1603 (IC base=+0.098)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5656` → IC=-0.121 (n=349)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5656
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=709)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.122 (n=726)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0057 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5656` → IC=+0.161 (n=709)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5656 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.167 (n=367)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.0639` → IC=+0.247 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0639 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2135` → IC=+0.158 (n=153)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2135 (IC base=+0.054)

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

- **PATRÓN** `ibs_20min` > `0.5307` → IC=+0.162 (n=738)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5307 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1364` → IC=+0.160 (n=395)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1364 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.029` → IC=+0.179 (n=182)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 12.029 (IC base=+0.068)

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
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0103 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.196 (n=614)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` < `0.2223` → IC=+0.150 (n=610)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2223 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.112` → IC=+0.240 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.112 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `1.1167` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1167 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.177 (n=159)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `1.8607` → IC=+0.139 (n=389)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8607 (IC base=+0.098)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.387 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.382 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.295)

- **PATRÓN** `ibs_20min` > `0.5721` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5721 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2984` → IC=+0.369 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2984 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.242` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.242 (IC base=+0.295)

- **PATRÓN** `volumen_regimen` < `1.0244` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0244 (IC base=+0.295)

- **PATRÓN** `volumen_regimen` > `1.1852` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1852 (IC base=+0.295)

- **PATRÓN** `volumen_pendiente_norm` > `0.1895` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1895 (IC base=+0.295)

- **PATRÓN** `volumen_spike_ratio` < `2.8251` → IC=+0.335 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.8251 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `1592.384` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.384 (IC base=+0.295)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.386 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.371 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.335)

- **PATRÓN** `ibs_20min` < `0.04` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.04 (IC base=+0.335)

- **PATRÓN** `ibs_20min` > `0.482` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.482 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.308` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.308 (IC base=+0.335)

- **PATRÓN** `volumen_regimen` > `0.6174` → IC=+0.378 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6174 (IC base=+0.335)

- **PATRÓN** `volumen_pendiente_norm` > `0.1736` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1736 (IC base=+0.335)

- **PATRÓN** `volumen_spike_ratio` < `1.547` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.547 (IC base=+0.335)

- **PATRÓN** `volumen_spike_ratio` > `3.2641` → IC=+0.382 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2641 (IC base=+0.335)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `37.4` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 37.4 (IC base=+0.335)

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

- **FILTRO** `ibs_20min` > `0.7197` → IC=-0.264 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7197
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=103)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.200 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.89` → IC=+0.311 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.89 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.180 (n=539)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.6198` → IC=+0.189 (n=307)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6198 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.175 (n=306)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.1915 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` < `0.2102` → IC=+0.184 (n=936)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2102 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4189` → IC=+0.211 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4189 (IC base=+0.168)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.133 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0059 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.7306` → IC=+0.138 (n=252)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7306 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.3355` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3355 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.2563` → IC=+0.133 (n=464)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2563 (IC base=+0.072)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.163 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0073 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.136 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.145 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.7994` → IC=+0.178 (n=243)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7994 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.8305` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8305 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1156` → IC=+0.153 (n=217)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1156 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.063` → IC=+0.151 (n=279)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 9.063 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6195 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.1834` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1834 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` < `0.0508` → IC=+0.184 (n=223)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.0508 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.7116` → IC=+0.177 (n=162)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.7116 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=224)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1706.9595` → IC=+0.176 (n=270)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1706.9595 (IC base=+0.133)

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
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1700)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `liq_n` > 2.0 (IC base=+0.081)

- **PATRÓN** `liq_usd_total` > `1217.25` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `liq_usd_total` > 1217.25 (IC base=+0.081)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.081)

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
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=288)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4330)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.137 (n=301)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1724)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1678)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=776)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=785)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1642)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1642)

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
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=428)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=477)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=3831)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=9812)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.147 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=149)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=59)

- **FILTRO** `restante_min` < `3.79` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `restante_min` < 3.79
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.194 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=75)

- **FILTRO** `lag_apertura_s` > `72.79` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `lag_apertura_s` > 72.79
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.164 (n=462)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1114)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.145 (n=364)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=989)

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
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=29149)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9700)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=30206)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4366)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7644` → IC=-0.148 (n=1323)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7644
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3976)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.181 (n=1442)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=4382)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=26161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=59163)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=20776)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=64548)

- **FILTRO** `ibs_7min` < `0.2105` → IC=-0.237 (n=21329)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2105
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=63995)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.154 (n=28146)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=57178)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26379)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=80112)

- **FILTRO** `ibs_7min` > `0.2781` → IC=-0.183 (n=26615)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2781
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=79876)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.127 (n=3490)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=10912)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=3529)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=10873)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.212 (n=3600)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10802)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.204 (n=3599)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=10803)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=3362)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=11385)

- **FILTRO** `ibs_7min` > `0.2643` → IC=-0.188 (n=3686)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2643
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=11061)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.177 (n=3683)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=11064)

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
- **FILTRO** `py_entrada` < `0.33` → IC=-0.275 (n=3220)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10876)

- **FILTRO** `ibs_7min` < `0.7119` → IC=-0.201 (n=3524)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7119
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10572)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.195 (n=3519)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=10577)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3410)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=11199)

- **FILTRO** `ibs_7min` > `0.2715` → IC=-0.177 (n=3652)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2715
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=10957)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.173 (n=3566)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=11043)

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
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1040)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1329)

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
- **FILTRO** `pct_vs_K` |x|> `4.4525` → IC=-0.197 (n=130)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4525
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=132)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.151 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0048 (IC base=-0.029)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.271 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.005)

- **PATRÓN** `pct_vs_K` |x|≤ `2.0557` → IC=+0.222 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 2.0557 (IC base=+0.005)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0113` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0113
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=73)

- **FILTRO** `pct_vs_K` |x|> `7.5593` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.5593
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=72)

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
- **FILTRO** `sigma_h` < `0.0119` → IC=-0.258 (n=676)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0119
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=226)

- **FILTRO** `T_h` > `66.9347` → IC=-0.259 (n=603)

  - _Acción_: SKIP cuando `T_h` > 66.9347
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=299)

- **FILTRO** `sigma_h` < `0.0066` → IC=-0.170 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=577)

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
- **FILTRO** `pct_vs_K` |x|> `2.8122` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8122
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
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.192 (n=24)
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

- **PATRÓN** `edge` > `0.099` → IC=+0.425 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.099 (IC base=+0.393)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.417 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.393)

- **PATRÓN** `T_h` < `0.7258` → IC=+0.418 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7258 (IC base=+0.393)

- **PATRÓN** `dist_50` > `0.368` → IC=+0.441 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.368 (IC base=+0.393)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=351)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.393)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.0939` → IC=+0.279 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0939 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.271 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.204)

- **PATRÓN** `T_h` < `0.659` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.659 (IC base=+0.204)

- **PATRÓN** `T_h` > `1.3612` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.3612 (IC base=+0.204)

- **PATRÓN** `dist_50` > `0.3235` → IC=+0.305 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3235 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.236 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.204)

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

- **PATRÓN** `edge` > `0.0997` → IC=+0.468 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.438 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.417)

- **PATRÓN** `T_h` < `1.178` → IC=+0.443 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.178 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.484 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.417)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.405 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=503)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=538)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.139 (n=167)

  - _Acción_: Kelly boost +0.70€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.021)

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
- **PATRÓN** `streak_estiramiento` < `0.3854` → IC=+0.130 (n=133)

  - _Acción_: Kelly boost +0.65€ cuando `streak_estiramiento` < 0.3854 (IC base=+0.038)

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

- **PATRÓN** `streak_estiramiento` < `0.5723` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `streak_estiramiento` < 0.5723 (IC base=+0.009)

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

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6237 (IC base=+0.031)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=5729)

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
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3425)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.183 (n=2245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0059 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2337` → IC=+0.158 (n=6733)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2337 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1273` → IC=+0.133 (n=6733)

  - _Acción_: Kelly boost +0.66€ cuando `drift_15min` |x|≤ 1.1273 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.133 (n=6732)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0992` → IC=+0.143 (n=2124)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0992 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.551` → IC=+0.206 (n=6015)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.551 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.956` → IC=+0.226 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.956 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3519)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4322.2356` → IC=+0.171 (n=2245)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4322.2356 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2625)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.248 (n=304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.247 (n=401)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2662` → IC=+0.226 (n=304)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2662 (IC base=+0.206)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2237` → IC=+0.220 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2237 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7013` → IC=+0.275 (n=912)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7013 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.3946` → IC=+0.236 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3946 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5528` → IC=+0.208 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5528 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.939` → IC=+0.298 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.939 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.220 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.146 (n=1032)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0068 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.145 (n=782)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.083` → IC=+0.137 (n=1048)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.083 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.4761` → IC=+0.216 (n=1173)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4761 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.143 (n=727)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.132 (n=1331)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.946` → IC=+0.277 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.946 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6122.7931` → IC=+0.176 (n=532)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 6122.7931 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8333` → IC=+0.145 (n=703)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` > 0.8333 (IC base=+0.046)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.143 (n=1699)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0118 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2398` → IC=+0.176 (n=1699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2398 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0586` → IC=+0.140 (n=1699)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0586 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.184 (n=533)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=1550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.143 (n=1498)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6944` → IC=+0.232 (n=1133)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6944 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2145` → IC=+0.142 (n=780)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2145 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.9137` → IC=+0.142 (n=1963)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.9137 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.874` → IC=+0.184 (n=394)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 16.874 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2939.0564` → IC=+0.179 (n=771)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2939.0564 (IC base=+0.137)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.383 (n=381)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1502` → IC=+0.362 (n=738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1502 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.375 (n=559)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1013` → IC=+0.381 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1013 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.373 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.7872` → IC=+0.391 (n=839)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7872 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2713` → IC=+0.385 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2713 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.716` → IC=+0.389 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.716 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `9681.5596` → IC=+0.372 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9681.5596 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.359 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.1527` → IC=+0.365 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1527 (IC base=+0.360)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.366 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.370 (n=182)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.401 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.8042` → IC=+0.379 (n=402)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8042 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.396 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.536` → IC=+0.379 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.536 (IC base=+0.360)

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
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.203 (n=3114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=3115)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2761)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3468)

- **FILTRO** `libro_liquidez` < `4435.323` → IC=-0.172 (n=4111)

  - _Acción_: SKIP cuando `libro_liquidez` < 4435.323
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=2118)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.278 (n=1374)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.206 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1169 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` < `0.5978` → IC=+0.200 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5978 (IC base=-0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2274` → IC=+0.268 (n=2056)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2274 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.3775` → IC=+0.281 (n=6164)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3775 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.7089` → IC=+0.264 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7089 (IC base=+0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.046` → IC=-0.225 (n=2791)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=1375)

- **FILTRO** `sigma_h` < `0.0041` → IC=-0.207 (n=1041)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=3125)

- **FILTRO** `sigma_ewma_delta_pct` > `22.158` → IC=-0.234 (n=584)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.158
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3582)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.288 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.066)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.313 (n=495)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1068` → IC=+0.283 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1068 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.5498` → IC=+0.285 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5498 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.676` → IC=+0.139 (n=247)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 21.676 (IC base=+0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.227 (n=86)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.179)

- **PATRÓN** `ibs_15` < `0.6283` → IC=+0.295 (n=86)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6283 (IC base=-0.179)

- **PATRÓN** `dist_vwap_pct` < `0.05` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.05 (IC base=-0.179)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.316 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.179)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=909)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.160 (n=695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0067 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.161 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.183 (n=550)

  - _Acción_: Kelly boost +0.91€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5632` → IC=+0.240 (n=695)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5632 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6666` → IC=+0.169 (n=137)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6666 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.150 (n=532)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.357` → IC=+0.242 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.357 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=909)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5213.5522` → IC=+0.171 (n=463)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5213.5522 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.251 (n=1628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4867` → IC=+0.242 (n=2441)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4867 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.8321` → IC=+0.248 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8321 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1963` → IC=+0.256 (n=1107)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1963 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.240 (n=1083)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.1944` → IC=+0.293 (n=1629)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1944 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.2404` → IC=+0.248 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2404 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.498` → IC=+0.240 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.498 (IC base=+0.234)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.286 (n=1528)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2165` → IC=+0.289 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2165 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=1593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.309 (n=1529)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.316 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2752 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.521` → IC=+0.383 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.521 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13050.0559` → IC=+0.299 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13050.0559 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.307 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.298 (n=355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.279)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0708` → IC=+0.279 (n=804)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0708 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2264` → IC=+0.293 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2264 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.303 (n=741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.8544` → IC=+0.306 (n=718)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8544 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2607` → IC=+0.312 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2607 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.34` → IC=+0.388 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.34 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `14412.9472` → IC=+0.312 (n=365)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.551 sube el IC de +0.132 a +0.206 en UPDOWN_GBM#15min (n=6015). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7013 sube el IC de +0.206 a +0.275 en UPDOWN_GBM#BTC#15min (n=912). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4761 sube el IC de +0.131 a +0.216 en UPDOWN_GBM#ETH#15min (n=1173). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.6944 sube el IC de +0.137 a +0.232 en UPDOWN_GBM#XRP#15min (n=1133). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6288 sube el IC de -0.086 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1374). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3775 sube el IC de +0.001 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=6164). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.066 a +0.313 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=495). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.179 a +0.295 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=86). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5632 sube el IC de +0.149 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=695). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1944 sube el IC de +0.234 a +0.293 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1629). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.204 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.026 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=1016). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.008 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1427). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.096 a +0.312 en UPDOWN_GBM_ETH_15M_HORA7 (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.096 a +0.312 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.284 a +0.309 en UPDOWN_GBM_IBS_ALTO (n=1529). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8544 sube el IC de +0.279 a +0.306 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=718). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8444 sube el IC de +0.289 a +0.316 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=727). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7872 sube el IC de +0.362 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=839). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8042 sube el IC de +0.360 a +0.379 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=402). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
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
| ✅ BALLENAS_TARDIAS | 51928 | -0.086 | -6648.44€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3427 | +0.093 | -323.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48501 | -0.099 | -6324.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3427 | +0.093 | -323.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3427 | +0.093 | -323.61€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14712 | -0.043 | -1380.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14712 | -0.043 | -1380.10€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 58712 | -0.012 | +2523.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 15133 | +0.004 | +1465.40€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 43579 | -0.017 | +1058.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 58712 | -0.012 | +2523.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 15133 | +0.004 | +1465.40€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 43579 | -0.017 | +1058.11€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 217850 | +0.112 | -8985.80€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#15min | 23813 | +0.178 | -771.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 1021 | +0.023 | -81.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 180664 | +0.104 | -7714.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12352 | +0.095 | -417.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 29953 | +0.101 | -2162.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 91 | -0.199 | +8.40€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 29825 | +0.102 | -2180.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 40716 | +0.122 | -689.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5755 | +0.175 | -235.04€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 29904 | +0.119 | -254.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 5015 | +0.080 | -178.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 30004 | +0.098 | -2098.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 115 | -0.098 | +21.30€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 29861 | +0.099 | -2112.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 13 | -0.065 | +4.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 46676 | +0.123 | -1007.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11620 | +0.177 | -345.46€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 30397 | +0.105 | -573.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4647 | +0.103 | -79.89€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 40538 | +0.111 | -1697.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6131 | +0.199 | -238.16€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 924 | +0.046 | -27.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 30831 | +0.095 | -1244.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2652 | +0.108 | -187.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 29963 | +0.106 | -1330.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 101 | -0.131 | +17.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 29846 | +0.106 | -1350.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 35582 | +0.188 | -2731.73€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 35582 | +0.188 | -2731.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 8053 | +0.159 | -973.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 8053 | +0.159 | -973.29€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5392 | +0.192 | -244.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5392 | +0.192 | -244.57€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7856 | +0.171 | -736.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7856 | +0.171 | -736.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6512 | +0.251 | -238.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6512 | +0.251 | -238.71€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7690 | +0.182 | -552.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7690 | +0.182 | -552.90€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 125680 | +0.199 | -9171.24€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 125680 | +0.199 | -9171.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21794 | +0.174 | -2594.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21794 | +0.174 | -2594.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 20251 | +0.223 | -674.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 20251 | +0.223 | -674.28€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21550 | +0.180 | -2264.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21550 | +0.180 | -2264.44€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 20432 | +0.218 | -785.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 20432 | +0.218 | -785.58€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20728 | +0.206 | -1202.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20728 | +0.206 | -1202.52€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20925 | +0.197 | -1650.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20925 | +0.197 | -1650.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 48876 | +0.116 | +384.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 48876 | +0.116 | +384.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 24338 | +0.117 | +263.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 24338 | +0.117 | +263.61€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 24538 | +0.115 | +120.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 24538 | +0.115 | +120.39€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 100134 | +0.101 | -2119.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 8126 | +0.097 | +190.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 92008 | +0.101 | -2310.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 54620 | +0.105 | -458.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 8126 | +0.097 | +190.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 46494 | +0.106 | -649.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 21576 | +0.109 | -109.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 21576 | +0.109 | -109.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 23938 | +0.083 | -1552.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 23938 | +0.083 | -1552.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 943 | +0.174 | -108.45€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 943 | +0.174 | -108.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 943 | +0.174 | -108.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 943 | +0.174 | -108.45€ | 2 | 4 |
| ✅ GBM_LATE_15M | 68229 | +0.102 | +38401.64€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 68229 | +0.102 | +38401.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11344 | +0.223 | +9667.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11344 | +0.223 | +9667.76€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 10694 | +0.176 | +8623.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10694 | +0.176 | +8623.41€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 12198 | +0.207 | +9615.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 12198 | +0.207 | +9615.98€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 9022 | +0.063 | +3071.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 9022 | +0.063 | +3071.81€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 9449 | -0.025 | +2462.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9449 | -0.025 | +2462.38€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 15522 | -0.019 | +4960.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15522 | -0.019 | +4960.29€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 72468 | +0.088 | +42575.26€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 72468 | +0.088 | +42575.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 14080 | -0.002 | +7451.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 14080 | -0.002 | +7451.37€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15570 | +0.008 | +4331.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15570 | +0.008 | +4331.65€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9670 | +0.296 | +11086.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9670 | +0.296 | +11086.38€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13883 | +0.020 | +4476.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13883 | +0.020 | +4476.49€ | 0 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 11011 | +0.052 | +5190.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 11011 | +0.052 | +5190.99€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8254 | +0.313 | +10038.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8254 | +0.313 | +10038.38€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 53667 | +0.179 | +44619.79€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 53667 | +0.179 | +44619.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 8138 | +0.238 | +7513.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 8138 | +0.238 | +7513.02€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8582 | +0.141 | +6491.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8582 | +0.141 | +6491.26€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8626 | +0.224 | +7459.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8626 | +0.224 | +7459.99€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 9170 | +0.130 | +7191.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 9170 | +0.130 | +7191.92€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 10120 | +0.123 | +7851.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 10120 | +0.123 | +7851.26€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 9031 | +0.231 | +8112.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 9031 | +0.231 | +8112.34€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14750 | +0.125 | +7487.56€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14750 | +0.125 | +7487.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3898 | +0.125 | +2080.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3898 | +0.125 | +2080.52€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4311 | +0.126 | +2175.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4311 | +0.126 | +2175.05€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3996 | +0.099 | +1634.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3996 | +0.099 | +1634.98€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1356 | +0.168 | +866.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1356 | +0.168 | +866.50€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 68580 | +0.189 | +57086.81€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 68580 | +0.189 | +57086.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10852 | +0.248 | +10375.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10852 | +0.248 | +10375.41€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 11016 | +0.143 | +8048.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 11016 | +0.143 | +8048.92€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11610 | +0.234 | +10435.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11610 | +0.234 | +10435.80€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11352 | +0.145 | +8558.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11352 | +0.145 | +8558.70€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 12103 | +0.129 | +8868.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 12103 | +0.129 | +8868.95€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11647 | +0.240 | +10799.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11647 | +0.240 | +10799.03€ | 0 | 22 |
| ✅ GBM_LATE_5M | 17235 | +0.220 | +14613.97€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 17235 | +0.220 | +14613.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3346 | +0.209 | +2852.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3346 | +0.209 | +2852.58€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1592 | +0.218 | +1323.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1592 | +0.218 | +1323.49€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 5024 | +0.211 | +3974.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 5024 | +0.211 | +3974.43€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3118 | +0.233 | +2801.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3118 | +0.233 | +2801.13€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 2207 | +0.212 | +1763.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2207 | +0.212 | +1763.61€ | 0 | 0 |
| ✅ GBM_LATE_60M | 7025 | +0.088 | +2546.78€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 7025 | +0.088 | +2546.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 253 | +0.284 | +288.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 253 | +0.284 | +288.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2129 | +0.061 | +627.54€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2129 | +0.061 | +627.54€ | 1 | 5 |
| ✅ GBM_LATE_60M#DOGE | 248 | +0.308 | +295.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 248 | +0.308 | +295.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1981 | +0.059 | +605.95€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1981 | +0.059 | +605.95€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 2163 | +0.064 | +428.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2163 | +0.064 | +428.83€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 251 | +0.318 | +300.73€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 251 | +0.318 | +300.73€ | 0 | 22 |
| 🚫 GBM_LATE_60M_FADE | 824 | -0.247 | -39.89€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 824 | -0.247 | -39.89€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 289 | -0.260 | -22.86€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 289 | -0.260 | -22.86€ | 6 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 281 | -0.246 | -9.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 281 | -0.246 | -9.46€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 229 | -0.245 | -11.34€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 229 | -0.245 | -11.34€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2676 | +0.092 | +717.45€ | 1 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2676 | +0.092 | +717.45€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 953 | +0.071 | +240.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 953 | +0.071 | +240.47€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 59 | +0.205 | +35.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 59 | +0.205 | +35.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 834 | +0.054 | +160.87€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 834 | +0.054 | +160.87€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 699 | +0.152 | +242.72€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 699 | +0.152 | +242.72€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 131 | +0.117 | +37.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 131 | +0.117 | +37.75€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 442 | +0.302 | +522.43€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 442 | +0.302 | +522.43€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 442 | +0.302 | +522.43€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 442 | +0.302 | +522.43€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 5146 | +0.094 | +1105.90€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 5146 | +0.094 | +1105.90€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 5146 | +0.094 | +1105.90€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 5146 | +0.094 | +1105.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 2035 | +0.017 | +98.42€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 2035 | +0.017 | +98.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 266 | +0.078 | +43.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 266 | +0.078 | +43.60€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M#BTC | 374 | -0.011 | +8.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 374 | -0.011 | +8.62€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 171 | +0.043 | +19.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 171 | +0.043 | +19.58€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 441 | +0.026 | +23.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 441 | +0.026 | +23.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 362 | -0.025 | -0.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 362 | -0.025 | -0.93€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 421 | +0.020 | +4.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 421 | +0.020 | +4.23€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4705 | +0.020 | +220.54€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4705 | +0.020 | +220.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 873 | +0.018 | +54.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 873 | +0.018 | +54.01€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 367 | +0.072 | +100.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 367 | +0.072 | +100.84€ | 0 | 4 |
| ✅ LIQUIDACIONES_5M#ETH | 1776 | +0.024 | +40.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1776 | +0.024 | +40.78€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 826 | +0.013 | +4.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 826 | +0.013 | +4.95€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 622 | -0.005 | +26.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 622 | -0.005 | +26.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2937 | -0.037 | -17.30€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2937 | -0.037 | -17.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 884 | -0.041 | -20.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 884 | -0.041 | -20.50€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1067 | -0.023 | +11.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1067 | -0.023 | +11.31€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 956 | -0.051 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 956 | -0.051 | -7.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 25 | +0.018 | -0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 25 | +0.018 | -0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 22500 | -0.032 | -226.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10956 | -0.031 | -65.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11544 | -0.034 | -161.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 781 | -0.052 | -37.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 403 | -0.038 | -5.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 378 | -0.066 | -32.07€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 6106 | -0.026 | -31.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2918 | -0.021 | +19.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3188 | -0.031 | -50.97€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 2025 | -0.035 | -19.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1044 | -0.039 | -22.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 981 | -0.031 | +3.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 5188 | -0.029 | -27.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2518 | -0.025 | +12.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2670 | -0.034 | -39.33€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4279 | -0.027 | +22.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2096 | -0.028 | +7.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2183 | -0.026 | +15.14€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 4121 | -0.045 | -133.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1977 | -0.049 | -76.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2144 | -0.042 | -57.56€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 78437 | -0.001 | +4156.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 78437 | -0.001 | +4156.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 11180 | -0.038 | -151.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 11180 | -0.038 | -151.18€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 11123 | -0.054 | -314.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 11123 | -0.054 | -314.31€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M | 3781 | +0.003 | -5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3781 | +0.003 | -5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 593 | -0.001 | -8.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 593 | -0.001 | -8.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1327 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1327 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 191815 | -0.078 | +2111.23€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 191815 | -0.078 | +2111.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 29149 | -0.101 | -1419.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 29149 | -0.101 | -1419.56€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 28705 | -0.101 | -1028.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 28705 | -0.101 | -1028.34€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9429 | -0.035 | -180.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9429 | -0.035 | -180.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1014 | -0.017 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1014 | -0.017 | -18.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2218 | -0.046 | -29.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2218 | -0.046 | -29.37€ | 3 | 0 |
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
| ✅ ORDER_FLOW_5M_REACTIVO | 2614 | -0.023 | -60.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2614 | -0.023 | -60.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 453 | +0.003 | +17.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 453 | +0.003 | +17.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 470 | -0.053 | -36.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 470 | -0.053 | -36.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 630 | -0.044 | -46.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 630 | -0.044 | -46.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 543 | -0.014 | -12.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 543 | -0.014 | -12.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 518 | -0.004 | +16.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 518 | -0.004 | +16.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1388 | -0.042 | +141.11€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 642 | -0.068 | +27.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 502 | -0.066 | +52.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 140 | -0.077 | -25.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 489 | -0.007 | +75.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 355 | +0.010 | +85.80€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 134 | -0.051 | -9.98€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 257 | -0.044 | +37.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 219 | -0.043 | +33.44€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 38 | -0.050 | +4.42€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1076 | -0.036 | +171.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 312 | -0.064 | -30.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1762 | -0.185 | -33.42€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 697 | -0.174 | -6.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 617 | -0.172 | -3.22€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 80 | -0.183 | -3.68€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 593 | -0.198 | -32.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 523 | -0.203 | -36.89€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 70 | -0.153 | +4.60€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 472 | -0.186 | +5.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 438 | -0.182 | +2.63€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 34 | -0.222 | +3.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1578 | -0.185 | -37.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 184 | -0.183 | +4.06€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 616 | +0.374 | +534.92€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 142 | +0.181 | +100.74€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 142 | +0.181 | +100.74€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 141 | +0.374 | +109.17€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 141 | +0.374 | +109.17€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#SOL | 333 | +0.452 | +325.01€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 333 | +0.452 | +325.01€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 616 | +0.374 | +534.92€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1079 | +0.043 | +96.34€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1079 | +0.043 | +96.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 361 | +0.018 | +4.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 361 | +0.018 | +4.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 83 | +0.029 | +3.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 83 | +0.029 | +3.15€ | 1 | 3 |
| ✅ STREAK_FADE_15M#SOL | 87 | +0.039 | +10.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 87 | +0.039 | +10.03€ | 2 | 3 |
| ✅ STREAK_FADE_15M#XRP | 548 | +0.062 | +78.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 548 | +0.062 | +78.41€ | 0 | 3 |
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
| ✅ STREAK_FADE_60M | 166 | +0.012 | -0.04€ | 1 | 2 |
| ✅ STREAK_FADE_60M#60min | 166 | +0.012 | -0.04€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB | 11 | +0.106 | +6.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB#60min | 11 | +0.106 | +6.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#DOGE | 5 | +0.018 | +1.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#DOGE#60min | 5 | +0.018 | +1.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 51 | -0.028 | -2.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 51 | -0.028 | -2.40€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 90 | +0.000 | -5.51€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 90 | +0.000 | -5.51€ | 1 | 1 |
| ✅ STREAK_FADE_60M#XRP | 9 | +0.021 | -0.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#XRP#60min | 9 | +0.021 | -0.37€ | 0 | 0 |
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
| ✅ STRUCT_NO_15M | 14334 | +0.019 | +5.50€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 14334 | +0.019 | +5.50€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5748 | +0.022 | +11.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5748 | +0.022 | +11.72€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5127 | +0.019 | -0.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5127 | +0.019 | -0.13€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3459 | +0.013 | -6.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3459 | +0.013 | -6.09€ | 1 | 0 |
| ✅ UPDOWN_GBM | 129329 | +0.060 | +12350.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 32287 | +0.078 | +6307.30€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3676 | -0.000 | +41.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 85145 | +0.062 | +5870.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7778 | -0.001 | +135.95€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11323 | +0.103 | +2092.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2141 | +0.164 | +998.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 9092 | +0.090 | +1096.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 29394 | +0.056 | +2578.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4395 | +0.081 | +982.83€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1088 | +0.000 | +22.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 20240 | +0.065 | +1485.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3512 | -0.003 | +84.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 159 | -0.065 | +4.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14412 | +0.074 | +1590.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 12242 | +0.061 | +697.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 30419 | +0.049 | +2163.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7533 | +0.069 | +1162.01€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1050 | +0.006 | +15.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18822 | +0.052 | +942.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2866 | -0.001 | +41.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 148 | -0.100 | +1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26581 | +0.041 | +1543.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8691 | +0.033 | +500.70€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 965 | -0.011 | +7.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15440 | +0.054 | +1033.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1351 | +0.004 | +9.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 134 | -0.140 | -8.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 17198 | +0.073 | +2384.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7443 | +0.089 | +1770.05€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9309 | +0.064 | +614.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 49 | +0.010 | +1.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 441 | -0.101 | -2.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1118 | +0.362 | +421.38€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1118 | +0.362 | +421.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 535 | +0.360 | +188.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 535 | +0.360 | +188.60€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 583 | +0.361 | +232.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 583 | +0.361 | +232.79€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 30638 | -0.017 | +7719.55€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 30638 | -0.017 | +7719.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2422 | -0.046 | +637.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2422 | -0.046 | +637.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5675 | -0.114 | +358.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5675 | -0.114 | +358.99€ | 3 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4180 | +0.215 | +2614.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4180 | +0.215 | +2614.42€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8588 | -0.057 | +1302.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8588 | -0.057 | +1302.38€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8479 | -0.052 | +1743.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8479 | -0.052 | +1743.70€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 387 | +0.060 | +38.14€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 387 | +0.060 | +38.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 387 | +0.060 | +38.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 387 | +0.060 | +38.14€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 2038 | +0.284 | +1743.64€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 2038 | +0.284 | +1743.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1071 | +0.279 | +863.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1071 | +0.279 | +863.85€ | 0 | 10 |
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
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.034) — sin ventaja clara. oversold(IBS<0.3): IC=+0.072 n=45553 | neutral: IC=+0.063 n=48422 | overbought(IBS>0.7): IC=+0.097 n=43508
  - _Datos_: n=142788 IC=+0.078 PNL=+21666.66€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 858 celda(s) pasan gate riguroso completo de 3094 evaluadas (n>=40) y 4215 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=8688 IC=+0.033 PNL=+500.44€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=2158/15 IC=+0.283 PNL=+881.12€ | BTC: n=2178/15 IC=+0.246 PNL=+343.73€ | SOL: n=1231/15 IC=+0.382 PNL=+1185.20€

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
  - _Estado_: 129208 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=1202/60 | contraria IC=+0.187 n=1268 | gap=-0.046 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=665, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 395 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2865/40 IC=-0.002 PNL=+40.53€ | BTC#60min: n=3510/40 IC=-0.003 PNL=+84.43€ | SOL#60min: n=1350/40 IC=+0.004 PNL=+8.58€ | XRP#60min: n=49/40 IC=+0.010 PNL=+1.35€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=860386 | tras_1loss IC=+0.103 n=650041 | tras_2loss IC=+0.074 n=257707/40 | gap=-0.030 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.039 n=19337 | contrario_BTC IC=+0.058 n=17074/40 | gap=+0.018 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=1328 PNL=+743.74€
  - _Datos_: n=1328 IC=+0.150 PNL=+743.74€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.08 con n=1559 PNL=+712.26€
  - _Datos_: n=1559 IC=+0.128 PNL=+712.26€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=95 PNL=+29.76€
  - _Datos_: n=95 IC=+0.098 PNL=+29.76€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.329 > 0.1 con n=4587 PNL=+2555.15€
  - _Datos_: n=4587 IC=+0.329 PNL=+2555.15€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1313 IC=+0.061 PNL=+128.10€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1313 IC=+0.061 PNL=+128.10€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=122 IC=+0.153 PNL=+67.70€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=122 IC=+0.153 PNL=+67.70€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=125200 IC=+0.059 PNL=+12034.71€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=125200 IC=+0.059 PNL=+12034.71€

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
  - _Estado_: 3/20 ops en el filtro definido (IC actual=-0.015 PNL=-2.12€)
  - _Datos_: n=3 IC=-0.015 PNL=-2.12€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=5096 IC=-0.007 PNL=-59.00€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5096 IC=-0.007 PNL=-59.00€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2678 IC=+0.010 PNL=+193.90€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2678 IC=+0.010 PNL=+193.90€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1572 IC=+0.029 PNL=+82.75€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1572 IC=+0.029 PNL=+82.75€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.1 con n=8972 PNL=+4225.41€
  - _Datos_: n=8972 IC=+0.132 PNL=+4225.41€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2938 IC=+0.068 PNL=+221.44€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2938 IC=+0.068 PNL=+221.44€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=4392 IC=+0.081 PNL=+980.48€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=4392 IC=+0.081 PNL=+980.48€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.091 > 0.08 con n=18664 PNL=+4567.45€
  - _Datos_: n=18664 IC=+0.091 PNL=+4567.45€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=893 IC=-0.191 PNL=+50.84€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=893 IC=-0.191 PNL=+50.84€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=865 IC=-0.007 PNL=+5.39€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=865 IC=-0.007 PNL=+5.39€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=1763 IC=+0.044 PNL=+148.76€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1763 IC=+0.044 PNL=+148.76€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=221 IC=-0.025 PNL=-6.32€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=221 IC=-0.025 PNL=-6.32€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=15186 IC=+0.045 PNL=+866.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=15186 IC=+0.045 PNL=+866.38€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.085 > 0.08 con n=912 PNL=+155.23€
  - _Datos_: n=912 IC=+0.085 PNL=+155.23€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.302 n=442) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=442 IC=+0.302 PNL=+522.43€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=21518 IC=+0.057 PNL=+1935.10€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=21518 IC=+0.057 PNL=+1935.10€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=8732 IC=+0.057 PNL=+1189.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8732 IC=+0.057 PNL=+1189.99€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=867 PNL=+289.46€
  - _Datos_: n=867 IC=+0.111 PNL=+289.46€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=2436 PNL=+544.51€
  - _Datos_: n=2436 IC=+0.100 PNL=+544.51€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.082 > 0.08 con n=2017 PNL=+707.72€
  - _Datos_: n=2017 IC=+0.082 PNL=+707.72€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=122379 IC=+0.128 PNL=+51593.25€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=122379 IC=+0.128 PNL=+51593.25€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=108932 IC=+0.143 PNL=+50162.44€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=108932 IC=+0.143 PNL=+50162.44€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=20571 IC=+0.062 PNL=+2119.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=20571 IC=+0.062 PNL=+2119.73€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.02 con n=1433 PNL=+567.12€
  - _Datos_: n=1433 IC=+0.115 PNL=+567.12€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=289 IC=-0.122 PNL=+2.67€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=289 IC=-0.122 PNL=+2.67€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.443 > 0.1 con n=2447 PNL=+2157.45€
  - _Datos_: n=2447 IC=+0.443 PNL=+2157.45€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=53300 IC=+0.069 PNL=+7139.86€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=53300 IC=+0.069 PNL=+7139.86€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.1 con n=10408 PNL=+5956.71€
  - _Datos_: n=10408 IC=+0.196 PNL=+5956.71€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.117 < -0.1 con n=894 PNL=+160.46€
  - _Datos_: n=894 IC=-0.117 PNL=+160.46€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=5177 IC=+0.068 PNL=+618.02€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=5177 IC=+0.068 PNL=+618.02€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=225 IC=-0.090 PNL=+2.54€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=225 IC=-0.090 PNL=+2.54€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1428 IC=+0.099 PNL=+345.73€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1428 IC=+0.099 PNL=+345.73€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 8/20 ops en el filtro definido (IC actual=-0.040 PNL=-0.55€)
  - _Datos_: n=8 IC=-0.040 PNL=-0.55€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=51301 IC=-0.137 PNL=+3326.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=51301 IC=-0.137 PNL=+3326.11€

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
  - _Estado_: n=5585 IC=+0.136 PNL=+3947.78€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5585 IC=+0.136 PNL=+3947.78€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.190 > 0.08 con n=6326 PNL=+4416.37€
  - _Datos_: n=6326 IC=+0.190 PNL=+4416.37€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=13475 IC=+0.057 PNL=+1161.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13475 IC=+0.057 PNL=+1161.37€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=5633 PNL=+3211.96€
  - _Datos_: n=5633 IC=+0.103 PNL=+3211.96€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.08 con n=1211 PNL=+706.64€
  - _Datos_: n=1211 IC=+0.206 PNL=+706.64€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.218 < -0.1 con n=5667 PNL=-419.75€
  - _Datos_: n=5667 IC=-0.218 PNL=-419.75€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.222 > 0.2 con n=14257 PNL=+11770.08€
  - _Datos_: n=14257 IC=+0.222 PNL=+11770.08€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=183 PNL=+73.86€
  - _Datos_: n=183 IC=+0.111 PNL=+73.86€

**🟡 H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=4852 PNL=+1974.60€
  - _Datos_: n=4852 IC=+0.100 PNL=+1974.60€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.174 > 0.08 con n=4895 PNL=+3939.21€
  - _Datos_: n=4895 IC=+0.174 PNL=+3939.21€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=8092 IC=-0.017 PNL=+2459.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8092 IC=-0.017 PNL=+2459.11€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=774 IC=+0.079 PNL=-16.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=774 IC=+0.079 PNL=-16.04€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.241 > 0.08 con n=6276 PNL=-478.69€
  - _Datos_: n=6276 IC=+0.241 PNL=-478.69€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=137 IC=+0.075 PNL=+23.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=137 IC=+0.075 PNL=+23.44€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.095 n=2630) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2630 IC=+0.095 PNL=+513.60€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.310 > 0.08 con n=765 PNL=+201.95€
  - _Datos_: n=765 IC=+0.310 PNL=+201.95€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=700) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=700 IC=+0.412 PNL=+1021.99€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=21784 IC=+0.175 PNL=-2591.13€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=21784 IC=+0.175 PNL=-2591.13€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.230 > 0.1 con n=361 PNL=+251.23€
  - _Datos_: n=361 IC=+0.230 PNL=+251.23€
