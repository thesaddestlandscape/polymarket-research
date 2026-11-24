# Hipótesis automáticas — 2026-11-24 13:19 UTC
_Generado por shadow_postmortem.py sobre 1478337 resoluciones (PNL=+209595.22€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=724)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1111)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `60.0` → IC=+0.171 (n=360)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 60.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8116` → IC=+0.269 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8116 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.257` → IC=+0.195 (n=349)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.257 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1139)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4616.8913` → IC=+0.127 (n=475)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4616.8913 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=554)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.194 (n=974)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.180 (n=307)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 63.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8111` → IC=+0.265 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8111 (IC base=+0.125)

- **PATRÓN** `banda_z` > `8.316` → IC=+0.194 (n=305)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.316 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.137 (n=827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 8.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=1039)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `5097.9637` → IC=+0.128 (n=415)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 5097.9637 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8588.5981` → IC=+0.127 (n=247)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 8588.5981 (IC base=+0.019)

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
- **FILTRO** `restante_s_al_confirmar` < `130.42` → IC=-0.220 (n=12875)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.42
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=38626)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.82` → IC=-0.160 (n=3582)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.82
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=10750)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=30684)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7776.5412` → IC=+0.152 (n=2497)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7776.5412 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=27203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=33053)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=24589)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=8872)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6267.5343` → IC=+0.138 (n=3485)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 6267.5343 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=2230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=2731)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `16198.2845` → IC=+0.181 (n=710)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16198.2845 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2789)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16036.8816` → IC=+0.186 (n=720)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16036.8816 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=679)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.073)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.120 (n=2216)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.45 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=5617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.378 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.200 (n=2695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=3140)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.194)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=978)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.645` → IC=+0.235 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.645 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1206)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2043.2368` → IC=+0.138 (n=973)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2043.2368 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.230 (n=2043)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.428 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.144 (n=1485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.144)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=486)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.162 (n=486)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.55 (IC base=+0.049)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.135 (n=1065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.254 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=27241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=23026)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.220 (n=8711)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `8407.3041` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8407.3041 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=6211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.174 (n=5992)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.161)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=3835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=2570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.244 (n=1839)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.204)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=6046)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.173 (n=5127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6188)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4764)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.258 (n=4773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.252)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=5909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=3762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1931)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.184)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=1034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=1030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `14030.2627` → IC=+0.449 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14030.2627 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `15264.989` → IC=+0.444 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15264.989 (IC base=+0.439)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.408 (n=151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.417 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.402)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=35538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=35073)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.185 (n=5319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=11461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=16425)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=14858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.189 (n=6102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=12599)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=4978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5745)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.258 (n=6091)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5866)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.251 (n=6390)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=5922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5926)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7332)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=12779)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=14019)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.29` → IC=+0.140 (n=11980)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.29 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6209)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6365)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=7934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.76` → IC=+0.141 (n=7832)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.76 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6570)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.135 (n=8458)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.89` → IC=+0.136 (n=7900)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.89 (IC base=+0.116)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.370 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=93)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.370 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=93)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5082` → IC=+0.140 (n=20411)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5082 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=20659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=14244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9737` → IC=+0.247 (n=6810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9737 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8821` → IC=+0.293 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8821 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.459` → IC=+0.190 (n=10236)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.459 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.268 (n=5580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6953 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3031` → IC=+0.256 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3031 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7392` → IC=+0.235 (n=4932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7392 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=9831)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4903.9964` → IC=+0.152 (n=6803)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4903.9964 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.122 (n=12919)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0066 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.5641` → IC=+0.145 (n=25835)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5641 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.6787` → IC=+0.193 (n=1771)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6787 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.1776` → IC=+0.196 (n=10552)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1776 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.197 (n=7190)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.856 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.231 (n=2614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.2821` → IC=+0.212 (n=8290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2821 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=18265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.088)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.304` → IC=+0.215 (n=3808)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.304 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=4551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2904)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9823` → IC=+0.274 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9823 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.801` → IC=+0.289 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.801 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.261 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4379` → IC=+0.214 (n=4157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4379 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2046.68` → IC=+0.216 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.68 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.221 (n=3579)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.245 (n=1786)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0966` → IC=+0.270 (n=1313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0966 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1807)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0794` → IC=+0.277 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0794 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.961` → IC=+0.244 (n=4033)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.961 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0724` → IC=+0.242 (n=3402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0724 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.246 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.5528` → IC=+0.240 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5528 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.855` → IC=+0.242 (n=2516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.855 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=4336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.231 (n=1241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1152` → IC=+0.245 (n=1633)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1152 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.8906` → IC=+0.255 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8906 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.7572` → IC=+0.234 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7572 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.741` → IC=+0.261 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.741 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6966` → IC=+0.229 (n=3311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6966 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.266 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4399` → IC=+0.246 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4399 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.159 (n=3593)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0835` → IC=+0.158 (n=1363)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0835 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7098` → IC=+0.172 (n=4075)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7098 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1553` → IC=+0.152 (n=3982)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1553 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.97` → IC=+0.142 (n=3756)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.97 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.157 (n=1360)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6279 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.159 (n=1476)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4451` → IC=+0.144 (n=3944)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4451 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4188` → IC=+0.137 (n=3944)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4188 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5294)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.188 (n=1300)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.212 (n=2080)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.879` → IC=+0.277 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.879 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.193 (n=4118)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.224 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7283` → IC=+0.210 (n=2035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7283 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5540)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1908.6184` → IC=+0.201 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.6184 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.226 (n=1898)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.4692` → IC=+0.226 (n=3796)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4692 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=1965)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0529` → IC=+0.267 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0529 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.639` → IC=+0.266 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.639 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3454` → IC=+0.255 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3454 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.152` → IC=+0.231 (n=2779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.152 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1891.2501` → IC=+0.224 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1891.2501 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.223 (n=4186)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.171 (n=256)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5541)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.134 (n=981)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0047 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.252 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.351 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.5966` → IC=+0.344 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5966 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.174` → IC=+0.216 (n=1637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.174 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.8708` → IC=+0.344 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8708 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2486` → IC=+0.366 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2486 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.165` → IC=+0.349 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.165 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.357 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.363 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.2782` → IC=+0.355 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2782 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.350 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0865` → IC=+0.189 (n=1450)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0865 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.3642` → IC=+0.156 (n=730)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3642 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1535` → IC=+0.159 (n=2711)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1535 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.8255` → IC=+0.164 (n=1905)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8255 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.192 (n=361)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.4311` → IC=+0.172 (n=918)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.4311 (IC base=+0.060)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.183 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=893)

- **FILTRO** `ibs_20min` > `0.1935` → IC=-0.126 (n=5438)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1935
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=2698)

- **FILTRO** `sigma_ewma_delta_pct` > `8.27` → IC=-0.233 (n=882)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.27
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=7254)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.172 (n=361)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.75 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.270 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `1.3465` → IC=+0.267 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.3465 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.673` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 6.673 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.320 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.1724` → IC=+0.279 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1724 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.5438` → IC=+0.261 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5438 (IC base=+0.020)

- **PATRÓN** `ibs_20min` < `0.1935` → IC=+0.161 (n=2698)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1935 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.8367` → IC=+0.295 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8367 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.3228` → IC=+0.293 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3228 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.6921` → IC=+0.304 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6921 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `1.041` → IC=+0.295 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.041 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0782` → IC=+0.320 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0782 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.305 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4394 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5251` → IC=+0.299 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5251 (IC base=-0.031)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7981` → IC=-0.160 (n=4197)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7981
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=2163)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.180 (n=1306)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=5054)

- **FILTRO** `ibs_20min` > `0.7213` → IC=-0.190 (n=2192)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7213
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=6580)

- **PATRÓN** `ibs_20min` > `0.7981` → IC=+0.146 (n=2163)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7981 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.4525` → IC=+0.342 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4525 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.318 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.319 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5276` → IC=+0.315 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5276 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1045` → IC=+0.288 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1045 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` < `0.2346` → IC=+0.263 (n=2601)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2346 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.6364` → IC=+0.276 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6364 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.2131` → IC=+0.279 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2131 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.291` → IC=+0.281 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.291 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.270 (n=2488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.188 (n=8934)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0112 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8659` → IC=+0.284 (n=12140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8659 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0061` → IC=+0.306 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0061 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.457` → IC=+0.167 (n=12053)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.457 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.280 (n=8905)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.297 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6429` → IC=+0.289 (n=5178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6429 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=15184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.154 (n=11823)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0093 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5161` → IC=+0.175 (n=22929)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.5161 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2049` → IC=+0.284 (n=8863)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2049 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.8571` → IC=+0.280 (n=5942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8571 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1869` → IC=+0.285 (n=2971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1869 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.322 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4534` → IC=+0.303 (n=4422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4534 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2702` → IC=+0.305 (n=6013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2702 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.313 (n=13271)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8155` → IC=-0.148 (n=4742)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8155
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2445)

- **FILTRO** `ibs_20min` > `0.7` → IC=-0.243 (n=1619)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=4872)

- **FILTRO** `sigma_ewma_delta_pct` > `4.057` → IC=-0.240 (n=1360)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.057
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5131)

- **PATRÓN** `ibs_20min` > `0.8155` → IC=+0.313 (n=2445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8155 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.142` → IC=+0.174 (n=2674)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 2.142 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.332 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.293 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2229` → IC=+0.316 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2229 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.316 (n=2031)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1707` → IC=+0.173 (n=1624)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1707 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1546` → IC=+0.388 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1546 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6476` → IC=+0.395 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6476 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1826` → IC=+0.231 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1826 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.222 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6953 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.247 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.229 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4593` → IC=+0.220 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4593 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `368.0` → IC=+0.233 (n=2588)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 368.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.575` → IC=+0.258 (n=2335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.575 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.0184` → IC=+0.269 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0184 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.285 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.256 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1506` → IC=+0.262 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1506 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.275 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 196.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.320 (n=1660)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=3673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.572` → IC=+0.306 (n=2485)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.572 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.13` → IC=+0.294 (n=3406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.13 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `3.2543` → IC=+0.302 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2543 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2022.0197` → IC=+0.299 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2022.0197 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.303 (n=2272)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.336 (n=2277)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.309)

- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.328 (n=1503)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.309)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=1310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.309)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.313 (n=1549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.309)

- **PATRÓN** `ibs_20min` < `0.0306` → IC=+0.309 (n=1503)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0306 (IC base=+0.309)

- **PATRÓN** `ibs_20min` > `0.1563` → IC=+0.321 (n=2277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1563 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.983` → IC=+0.318 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.983 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` < `0.1986` → IC=+0.309 (n=3396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1986 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` > `0.3445` → IC=+0.317 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3445 (IC base=+0.309)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.327 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.309)

- **PATRÓN** `libro_liquidez` > `2004.564` → IC=+0.320 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.564 (IC base=+0.309)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.314 (n=3287)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.309)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1598` → IC=+0.241 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1598 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.6409` → IC=+0.236 (n=2683)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6409 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.1717` → IC=+0.238 (n=2446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1717 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.5961` → IC=+0.236 (n=2446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5961 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.238 (n=2570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1025` → IC=+0.242 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1025 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4071` → IC=+0.244 (n=2377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4071 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4958` → IC=+0.238 (n=2123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4958 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.254 (n=2429)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.0918` → IC=+0.151 (n=1690)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0918 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.3861` → IC=+0.262 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3861 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `1.1719` → IC=+0.264 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1719 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` > `0.6137` → IC=+0.260 (n=1800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6137 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.265 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.283 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.7812` → IC=+0.283 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7812 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.4157` → IC=+0.271 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4157 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.282 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.013)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.248 (n=2746)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.316 (n=2766)

- **FILTRO** `ibs_20min` > `0.6047` → IC=-0.236 (n=1297)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6047
  - _Potencial_: sin este filtro IC_bueno=+0.169 (n=3897)

- **FILTRO** `sigma_ewma_delta_pct` > `8.222` → IC=-0.261 (n=596)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.222
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=4598)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.316 (n=2766)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `1.1107` → IC=+0.354 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1107 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.448` → IC=+0.159 (n=2251)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.448 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.349 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6979` → IC=+0.337 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6979 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.338 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.369 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7921` → IC=+0.357 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7921 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.354 (n=1772)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6047` → IC=+0.169 (n=3897)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6047 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.3257` → IC=+0.276 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3257 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.727` → IC=+0.136 (n=4073)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.727 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6884` → IC=+0.288 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6884 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.301 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.1387` → IC=+0.281 (n=1748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1387 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.293 (n=2027)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.351 (n=2576)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=2909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=3027)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.651` → IC=+0.336 (n=2883)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.651 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2206` → IC=+0.336 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2206 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.777` → IC=+0.339 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.777 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.6289` → IC=+0.323 (n=2883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6289 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2849` → IC=+0.344 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2849 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.324 (n=2787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `3005.9944` → IC=+0.322 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3005.9944 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.330 (n=3121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=3131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` < `0.39` → IC=+0.328 (n=3119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.39 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `1.3044` → IC=+0.323 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3044 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` < `0.2594` → IC=+0.317 (n=3069)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2594 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.689` → IC=+0.327 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.689 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` < `0.6358` → IC=+0.319 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6358 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.2096` → IC=+0.338 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2096 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.361 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` < `1.4152` → IC=+0.325 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4152 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `2.1531` → IC=+0.318 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1531 (IC base=+0.314)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.221 (n=6528)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1272` → IC=+0.194 (n=8609)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1272 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=20346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.229 (n=19569)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5357 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.206 (n=7403)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.715` → IC=+0.260 (n=3830)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.715 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.152 (n=13051)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1741 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6204` → IC=+0.151 (n=13052)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6204 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2931` → IC=+0.208 (n=2824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2931 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6009` → IC=+0.185 (n=6354)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6009 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.192 (n=18521)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.194 (n=8633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0062 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.187 (n=13060)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.223 (n=6528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=9396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5263` → IC=+0.238 (n=19578)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5263 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1976` → IC=+0.181 (n=14265)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1976 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.395` → IC=+0.191 (n=3073)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.395 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.489` → IC=+0.192 (n=17510)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.489 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.6996` → IC=+0.176 (n=6101)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6996 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.218 (n=2932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.5633` → IC=+0.186 (n=8242)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.5633 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6333` → IC=+0.196 (n=6244)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6333 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=18559)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.266 (n=1072)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.0756` → IC=+0.267 (n=1070)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0756 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=2183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `0.9425` → IC=+0.292 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9425 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.46` → IC=+0.328 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.46 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.285 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.8304` → IC=+0.228 (n=2049)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8304 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.229 (n=3072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.254 (n=2727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.252)

- **PATRÓN** `drift_60min` |x|≤ `0.1017` → IC=+0.308 (n=1199)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1017 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.256 (n=2807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=2480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` < `0.0054` → IC=+0.308 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0054 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.944` → IC=+0.258 (n=2692)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.944 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.255 (n=2407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.263 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` < `1.5501` → IC=+0.267 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5501 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `2.6782` → IC=+0.253 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6782 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.260 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `1931.809` → IC=+0.253 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.809 (IC base=+0.252)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.191 (n=999)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0033 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0676` → IC=+0.174 (n=999)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0676 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2499` → IC=+0.202 (n=2995)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2499 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1973` → IC=+0.211 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1973 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.547` → IC=+0.203 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.547 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8524` → IC=+0.132 (n=1997)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8524 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0475` → IC=+0.129 (n=1358)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.0475 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.172 (n=456)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.129 (n=1298)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4553` → IC=+0.142 (n=983)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4553 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `385.0` → IC=+0.131 (n=2917)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 385.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.182 (n=2859)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0061 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2578` → IC=+0.176 (n=2854)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2578 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.6128` → IC=+0.212 (n=3244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6128 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.2217` → IC=+0.177 (n=3517)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2217 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.933` → IC=+0.177 (n=595)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.933 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.021` → IC=+0.158 (n=2858)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.021 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.164 (n=3244)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2068 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0716` → IC=+0.156 (n=2716)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0716 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.144` → IC=+0.160 (n=2742)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.144 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `203.0` → IC=+0.197 (n=1349)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 203.0 (IC base=+0.154)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.231 (n=1498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2573` → IC=+0.234 (n=2202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2573 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.285 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.988` → IC=+0.304 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.988 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.232 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7115` → IC=+0.224 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7115 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2020.2384` → IC=+0.222 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2020.2384 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.243 (n=2999)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0123 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.2556` → IC=+0.265 (n=2000)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2556 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.274 (n=1138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0438` → IC=+0.291 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0438 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.736` → IC=+0.285 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.736 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.287 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7655` → IC=+0.239 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7655 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1786` → IC=+0.251 (n=1938)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1786 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1883.5184` → IC=+0.246 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1883.5184 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.237 (n=2908)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.195 (n=1082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.004 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0821` → IC=+0.172 (n=1076)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0821 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2441` → IC=+0.190 (n=3225)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2441 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1491` → IC=+0.190 (n=1829)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1491 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.182` → IC=+0.203 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.182 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8362` → IC=+0.140 (n=2151)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8362 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.1745` → IC=+0.128 (n=1075)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.1745 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.180 (n=485)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5167` → IC=+0.126 (n=1390)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5167 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5007` → IC=+0.138 (n=1053)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5007 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6908.9474` → IC=+0.198 (n=1462)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6908.9474 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.128 (n=3163)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 123.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.174 (n=2309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0057 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4312` → IC=+0.150 (n=3460)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4312 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6685` → IC=+0.190 (n=3460)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6685 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1727` → IC=+0.158 (n=3539)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1727 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.521` → IC=+0.143 (n=1181)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 6.521 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.153 (n=2307)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8509 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2376` → IC=+0.164 (n=712)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2376 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.1869` → IC=+0.136 (n=2901)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1869 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4087` → IC=+0.137 (n=3297)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4087 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `6675.8703` → IC=+0.192 (n=1569)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6675.8703 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.139 (n=3284)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 121.0 (IC base=+0.134)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.177 (n=1203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0131 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.205 (n=3610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7992` → IC=+0.213 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7992 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.921` → IC=+0.284 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.921 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1668` → IC=+0.131 (n=3603)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1668 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6243` → IC=+0.125 (n=3602)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6243 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.124 (n=3679)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.129 (n=502)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.544` → IC=+0.128 (n=1540)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.544 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2718.2425` → IC=+0.200 (n=1633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2718.2425 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.128 (n=2315)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.153 (n=3329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0112 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.119` → IC=+0.171 (n=1261)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.119 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=3858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.222 (n=3782)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.2286` → IC=+0.149 (n=3746)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2286 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.148 (n=3353)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1789` → IC=+0.131 (n=3782)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1789 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8579` → IC=+0.126 (n=2522)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8579 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.128 (n=3747)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2777` → IC=+0.147 (n=528)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2777 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4407` → IC=+0.142 (n=1199)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4407 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4616` → IC=+0.135 (n=1199)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4616 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2614.0715` → IC=+0.190 (n=1715)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2614.0715 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.133 (n=3606)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 43.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.249 (n=2887)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1692` → IC=+0.240 (n=1421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1692 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=3361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2925)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.255 (n=3232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1879` → IC=+0.233 (n=1994)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1879 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8349` → IC=+0.227 (n=3329)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8349 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.439` → IC=+0.271 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.439 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6174` → IC=+0.233 (n=3230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6174 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2351` → IC=+0.267 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2351 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.4929` → IC=+0.227 (n=3154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4929 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4368` → IC=+0.228 (n=3153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4368 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2627.1049` → IC=+0.230 (n=2153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2627.1049 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0162` → IC=+0.248 (n=2248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0162 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6207` → IC=+0.249 (n=3372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6207 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0381` → IC=+0.296 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0381 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `1.185` → IC=+0.250 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.185 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.997` → IC=+0.272 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.997 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.245 (n=2248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `1.0472` → IC=+0.241 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0472 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.299 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.853` → IC=+0.236 (n=2134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.853 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.5572` → IC=+0.240 (n=2859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5572 (IC base=+0.239)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.204 (n=1723)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.145` → IC=+0.170 (n=2273)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.145 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=5396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.6563` → IC=+0.222 (n=3442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6563 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9192` → IC=+0.178 (n=787)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9192 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.547` → IC=+0.208 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.547 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8557` → IC=+0.162 (n=3141)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8557 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1873` → IC=+0.158 (n=1571)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1873 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1555` → IC=+0.170 (n=1327)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1555 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.527` → IC=+0.158 (n=2219)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.527 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.4195` → IC=+0.154 (n=5042)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4195 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=5671)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7186.4299` → IC=+0.193 (n=2341)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7186.4299 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5905` → IC=+0.154 (n=4982)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5905 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.121 (n=5516)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 136.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.206 (n=1243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.239 (n=415)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.229 (n=1122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.6215` → IC=+0.258 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6215 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.689` → IC=+0.240 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.689 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.975` → IC=+0.219 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.975 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8703` → IC=+0.216 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8703 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0899` → IC=+0.213 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0899 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.1509` → IC=+0.208 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1509 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.4026` → IC=+0.200 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4026 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `13761.2202` → IC=+0.206 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13761.2202 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.149 (n=688)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.2189` → IC=+0.188 (n=686)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.2189 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.141 (n=1018)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 234.0 (IC base=+0.068)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.239 (n=534)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1344` → IC=+0.157 (n=701)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1344 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=1652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.258 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1568` → IC=+0.166 (n=761)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1568 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.976` → IC=+0.181 (n=224)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.976 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8293` → IC=+0.154 (n=1061)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8293 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2175` → IC=+0.186 (n=278)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2175 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.771` → IC=+0.157 (n=1046)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.771 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `7846.5169` → IC=+0.174 (n=722)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7846.5169 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.142 (n=529)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 30.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.124 (n=1589)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0081 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.407` → IC=+0.182 (n=1059)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.407 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6744` → IC=+0.143 (n=698)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6744 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2225` → IC=+0.136 (n=270)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2225 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.3997` → IC=+0.143 (n=516)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.3997 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `5566.218` → IC=+0.149 (n=1058)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5566.218 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.148 (n=686)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 40.0 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.152 (n=466)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0072 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.137 (n=1398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.7188` → IC=+0.219 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7188 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.045` → IC=+0.151 (n=250)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 1.045 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.867` → IC=+0.226 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.867 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.0438` → IC=+0.128 (n=1229)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0438 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.222` → IC=+0.140 (n=237)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.222 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4156` → IC=+0.152 (n=452)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4156 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `3056.5696` → IC=+0.150 (n=466)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3056.5696 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.167 (n=1362)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.5588 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `2764.626` → IC=+0.164 (n=701)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2764.626 (IC base=+0.088)

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

- **PATRÓN** `volumen_regimen` < `1.2424` → IC=+0.183 (n=537)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.2424 (IC base=+0.163)

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

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.177 (n=518)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 19.0 (IC base=+0.163)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.228 (n=8628)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=27026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.966` → IC=+0.300 (n=8623)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.966 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9545` → IC=+0.217 (n=3009)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9545 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.876` → IC=+0.260 (n=6326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.876 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.867` → IC=+0.163 (n=11634)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.867 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.292` → IC=+0.217 (n=3392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.292 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6249` → IC=+0.194 (n=8431)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6249 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=24504)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.208 (n=8038)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1549` → IC=+0.203 (n=10610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1549 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=8999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4885` → IC=+0.253 (n=21206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4885 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1929` → IC=+0.183 (n=15349)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1929 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.503` → IC=+0.206 (n=22472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.503 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0523` → IC=+0.177 (n=14207)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0523 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.254 (n=3309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6241` → IC=+0.211 (n=7731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6241 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.215 (n=23007)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.382` → IC=+0.236 (n=4119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.382 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2776)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8611` → IC=+0.294 (n=2746)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8611 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.029` → IC=+0.301 (n=2709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.029 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.288 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2784` → IC=+0.244 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2784 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2046.68` → IC=+0.240 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.68 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.267 (n=3789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.265)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.267 (n=1716)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1287` → IC=+0.291 (n=1665)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1287 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.268 (n=1413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.268 (n=3414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.4697` → IC=+0.287 (n=3330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4697 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.266 (n=3834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.285 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5624` → IC=+0.267 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5624 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6397` → IC=+0.270 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6397 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.270 (n=2550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1934.24` → IC=+0.266 (n=1716)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.24 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.270 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.172 (n=1429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0034 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0839` → IC=+0.147 (n=1422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0839 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.189` → IC=+0.187 (n=4259)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.189 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.741` → IC=+0.211 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.741 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.264` → IC=+0.171 (n=876)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.264 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6331` → IC=+0.156 (n=1420)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6331 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0664` → IC=+0.143 (n=1931)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0664 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.191 (n=596)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.166` → IC=+0.144 (n=3687)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.166 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5213` → IC=+0.145 (n=3743)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5213 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `353.0` → IC=+0.149 (n=3645)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 353.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.171 (n=3322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0061 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.084` → IC=+0.173 (n=1260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.084 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.682` → IC=+0.192 (n=3773)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.682 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1555` → IC=+0.163 (n=3697)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1555 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.001` → IC=+0.148 (n=1778)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.001 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.201` → IC=+0.151 (n=3853)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.201 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0414` → IC=+0.157 (n=3320)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0414 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2217` → IC=+0.197 (n=685)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2217 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.432` → IC=+0.152 (n=3661)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.432 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.153 (n=2442)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=4900)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.182 (n=1210)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 212.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.240 (n=1952)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.932` → IC=+0.315 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.932 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2042` → IC=+0.233 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2042 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7559` → IC=+0.241 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7559 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1906.6648` → IC=+0.238 (n=1950)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1906.6648 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.247 (n=1840)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1862` → IC=+0.258 (n=1836)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1862 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.069` → IC=+0.297 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.069 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.89` → IC=+0.303 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.89 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.298 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.1676` → IC=+0.256 (n=2692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1676 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2005.7184` → IC=+0.251 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2005.7184 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.247 (n=3976)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.244)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.191 (n=1496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3564` → IC=+0.149 (n=3936)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3564 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.877` → IC=+0.266 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.877 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1504` → IC=+0.170 (n=2217)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1504 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.028` → IC=+0.165 (n=1740)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.028 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8566` → IC=+0.155 (n=2983)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8566 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.201 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5173` → IC=+0.157 (n=1925)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5173 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1486` → IC=+0.145 (n=1983)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1486 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `5864.2905` → IC=+0.233 (n=2028)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5864.2905 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.144 (n=2909)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 85.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.170 (n=3789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4625` → IC=+0.161 (n=3788)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4625 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5704` → IC=+0.214 (n=3334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5704 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.641` → IC=+0.159 (n=4382)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.641 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.069` → IC=+0.157 (n=757)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.069 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.043` → IC=+0.154 (n=3297)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.043 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.0394` → IC=+0.160 (n=3334)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0394 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.29` → IC=+0.205 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.29 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1935` → IC=+0.158 (n=3231)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1935 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5223` → IC=+0.159 (n=3280)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.5223 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `6737.5602` → IC=+0.215 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6737.5602 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.172 (n=1260)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.156 (n=1520)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0132 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.6964` → IC=+0.256 (n=3039)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6964 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.8126` → IC=+0.196 (n=1023)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8126 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.192` → IC=+0.268 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.192 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2095` → IC=+0.126 (n=4560)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2095 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.123 (n=4344)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.142 (n=573)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `2.4959` → IC=+0.125 (n=4453)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4959 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2476.871` → IC=+0.225 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2476.871 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.161 (n=3740)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0113 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1431` → IC=+0.152 (n=1417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1431 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=2006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5408` → IC=+0.247 (n=3740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5408 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2276` → IC=+0.154 (n=3902)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2276 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.018` → IC=+0.162 (n=4130)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.018 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1922` → IC=+0.144 (n=4250)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1922 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2316` → IC=+0.200 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2316 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.164 (n=1353)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4884` → IC=+0.144 (n=1353)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4884 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2656.0724` → IC=+0.222 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2656.0724 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.152 (n=4097)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.256 (n=4159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=4352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.240 (n=2791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.302 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.2047` → IC=+0.251 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2047 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.962` → IC=+0.296 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.962 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2159` → IC=+0.237 (n=4159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2159 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6415` → IC=+0.242 (n=4158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6415 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.254 (n=1650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.5147` → IC=+0.256 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5147 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=5371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2644.5329` → IC=+0.240 (n=2772)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2644.5329 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0247` → IC=+0.271 (n=1446)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0247 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.251 (n=4079)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.1398` → IC=+0.306 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1398 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.1909` → IC=+0.251 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1909 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2323` → IC=+0.250 (n=4165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2323 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.94` → IC=+0.281 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.94 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.7123` → IC=+0.248 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7123 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.265 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2876` → IC=+0.309 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2876 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4335` → IC=+0.249 (n=4119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4335 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.244 (n=2815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.241 (n=2472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.5385` → IC=+0.232 (n=7394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5385 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=7428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9282` → IC=+0.258 (n=2465)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9282 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.9629` → IC=+0.227 (n=6032)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9629 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.427` → IC=+0.233 (n=2463)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.427 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.7072` → IC=+0.228 (n=2303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7072 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.8813` → IC=+0.226 (n=3488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8813 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.234 (n=2078)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4503` → IC=+0.235 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4503 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=5282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3755.477` → IC=+0.231 (n=4930)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3755.477 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.231 (n=1765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.213 (n=2394)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4169` → IC=+0.223 (n=4646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4169 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.225 (n=2375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.6132` → IC=+0.216 (n=4646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6132 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7151` → IC=+0.219 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7151 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2566` → IC=+0.204 (n=4631)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2566 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.702` → IC=+0.226 (n=4791)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.702 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.0959` → IC=+0.213 (n=4211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0959 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.216 (n=4878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5327` → IC=+0.217 (n=2288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5327 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8167` → IC=+0.218 (n=3466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8167 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.236 (n=3480)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.212)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.281 (n=637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.272)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.304 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.282 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` < `0.4706` → IC=+0.287 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4706 (IC base=+0.272)

- **PATRÓN** `dist_vwap_pct` < `0.3339` → IC=+0.283 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3339 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.272)

- **PATRÓN** `volumen_regimen` > `0.8786` → IC=+0.293 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8786 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.280 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.272)

- **PATRÓN** `libro_liquidez` > `12917.5095` → IC=+0.284 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12917.5095 (IC base=+0.272)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3879` → IC=+0.186 (n=1545)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3879 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.177 (n=580)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.191 (n=681)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.3612` → IC=+0.175 (n=333)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3612 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.5553` → IC=+0.172 (n=1851)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.5553 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.194 (n=1517)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.0909` → IC=+0.185 (n=1359)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.0909 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.186 (n=473)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `2.496` → IC=+0.178 (n=1537)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.496 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.175 (n=697)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1732 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `14611.4186` → IC=+0.173 (n=701)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 14611.4186 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `700.0` → IC=+0.188 (n=1499)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 700.0 (IC base=+0.172)

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
- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.221 (n=2024)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.4737` → IC=+0.219 (n=2025)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4737 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.225 (n=1810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.472` → IC=+0.226 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.472 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.8323` → IC=+0.216 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8323 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.4246` → IC=+0.224 (n=2015)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4246 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.908` → IC=+0.222 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.908 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.8665` → IC=+0.215 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8665 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.218 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.214 (n=1875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.1597` → IC=+0.215 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1597 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4057` → IC=+0.226 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4057 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.4955` → IC=+0.215 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4955 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.243 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.5101` → IC=+0.221 (n=1641)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5101 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.0842` → IC=+0.214 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0842 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.7294` → IC=+0.223 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7294 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.241` → IC=+0.211 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.241 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.6374` → IC=+0.221 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6374 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.7178` → IC=+0.211 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7178 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.226 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1647` → IC=+0.209 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1647 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7747` → IC=+0.212 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7747 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=2153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.211 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.207)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.229 (n=864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.224 (n=432)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.299 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `1.0964` → IC=+0.242 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0964 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.269 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.246 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.218 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.238 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `2.4968` → IC=+0.225 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4968 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3372.142` → IC=+0.242 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3372.142 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.222 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.255 (n=647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.247)

- **PATRÓN** `drift_60min` |x|≤ `0.6917` → IC=+0.261 (n=970)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6917 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.268 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.273 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.247)

- **PATRÓN** `dist_vwap_pct` < `0.332` → IC=+0.258 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.332 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.99` → IC=+0.268 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.99 (IC base=+0.247)

- **PATRÓN** `volumen_regimen` < `0.7517` → IC=+0.262 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7517 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.260 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` > `1.8448` → IC=+0.263 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8448 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `4016.542` → IC=+0.270 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4016.542 (IC base=+0.247)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.278 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.247)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.144 (n=929)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0042 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.417` → IC=+0.132 (n=2680)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.417 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.155 (n=1267)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.137 (n=579)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.5838` → IC=+0.179 (n=2101)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5838 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.547` → IC=+0.129 (n=927)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.547 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.185 (n=589)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.095)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5478` → IC=-0.121 (n=341)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5478
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=694)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.180 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0029 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5478` → IC=+0.158 (n=694)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5478 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.166 (n=363)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.066)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.127 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0037 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.250 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.146 (n=314)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.057)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.496` → IC=-0.128 (n=264)

  - _Acción_: SKIP cuando `ibs_20min` > 0.496
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=514)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.154 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0043 (IC base=+0.062)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.120 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.5241` → IC=+0.156 (n=719)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.5241 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.1909` → IC=+0.157 (n=348)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1909 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.939` → IC=+0.163 (n=176)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.939 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.0953` → IC=+0.280 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0953 (IC base=+0.045)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.144 (n=610)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.72 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.7653` → IC=+0.158 (n=223)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.7653 (IC base=+0.035)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.179 (n=409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0103 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.197 (n=585)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` < `0.2223` → IC=+0.157 (n=575)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2223 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.907` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.907 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `1.1084` → IC=+0.184 (n=194)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1084 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.188 (n=152)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `2.2044` → IC=+0.127 (n=486)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.2044 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `1.8607` → IC=+0.143 (n=368)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8607 (IC base=+0.101)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.375 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.305)

- **PATRÓN** `drift_60min` |x|≤ `0.2821` → IC=+0.328 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2821 (IC base=+0.305)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.305)

- **PATRÓN** `ibs_20min` > `0.6246` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6246 (IC base=+0.305)

- **PATRÓN** `dist_vwap_pct` > `0.4912` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4912 (IC base=+0.305)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.192` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.192 (IC base=+0.305)

- **PATRÓN** `volumen_regimen` < `0.9791` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9791 (IC base=+0.305)

- **PATRÓN** `volumen_regimen` > `0.6039` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6039 (IC base=+0.305)

- **PATRÓN** `volumen_pendiente_norm` < `0.0555` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0555 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` < `2.5614` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5614 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` > `2.0841` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0841 (IC base=+0.305)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.305)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.389 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.336 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.338)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.406 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.338)

- **PATRÓN** `ibs_20min` < `0.1183` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1183 (IC base=+0.338)

- **PATRÓN** `ibs_20min` > `0.4553` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4553 (IC base=+0.338)

- **PATRÓN** `dist_vwap_pct` < `0.6346` → IC=+0.370 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6346 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.59` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.59 (IC base=+0.338)

- **PATRÓN** `volumen_regimen` > `0.6174` → IC=+0.381 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6174 (IC base=+0.338)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.338)

- **PATRÓN** `volumen_spike_ratio` < `1.5039` → IC=+0.382 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5039 (IC base=+0.338)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.338)

- **PATRÓN** `libro_liquidez` > `46.39` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 46.39 (IC base=+0.338)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0062` → IC=-0.250 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=210)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=322)

- **FILTRO** `volumen_regimen` < `0.8799` → IC=-0.306 (n=137)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8799
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=279)

- **FILTRO** `ibs_20min` > `0.681` → IC=-0.318 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` > 0.681
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=253)

- **FILTRO** `dist_vwap_pct` > `0.4617` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4617
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=347)

- **FILTRO** `sigma_ewma_delta_pct` > `9.288` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.288
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=353)

- **FILTRO** `volumen_pendiente_norm` > `0.0463` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0463
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=258)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=100)

- **FILTRO** `ibs_20min` < `0.018` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.018
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=98)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.321 (n=37)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=115)

- **FILTRO** `volumen_spike_ratio` > `1.3298` → IC=-0.302 (n=79)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.3298
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.003` → IC=-0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.003
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=103)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.472 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=103)

- **FILTRO** `volumen_regimen` < `0.7594` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7594
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=103)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.372 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=103)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.338 (n=35)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=70)

- **FILTRO** `volumen_spike_ratio` < `1.4493` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4493
  - _Potencial_: sin este filtro IC_bueno=-0.290 (n=79)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=125)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.368 (n=36)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=112)

- **FILTRO** `volumen_spike_ratio` < `1.57` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.57
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=93)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.342 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=53)

- **FILTRO** `volumen_regimen` < `0.9252` → IC=-0.460 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9252
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=47)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2613` → IC=-0.159 (n=338)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2613
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=1015)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.249 (n=396)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.6871` → IC=+0.205 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6871 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.89` → IC=+0.309 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.89 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.629` → IC=+0.192 (n=381)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.629 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.194 (n=289)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6244 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.1982` → IC=+0.173 (n=289)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1982 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` < `0.0673` → IC=+0.192 (n=661)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0673 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.7512` → IC=+0.193 (n=510)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.7512 (IC base=+0.166)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.155 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0066 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.7315` → IC=+0.142 (n=244)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.7315 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.7249` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7249 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2613` → IC=+0.132 (n=452)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2613 (IC base=+0.071)

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
- **FILTRO** `ibs_20min` > `0.2459` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2459
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=175)

- **FILTRO** `volumen_spike_ratio` > `1.9711` → IC=-0.132 (n=66)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.9711
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=129)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.321 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.287 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.298 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.7712` → IC=+0.405 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7712 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `0.7978` → IC=+0.297 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7978 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.0893` → IC=+0.311 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0893 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.485` → IC=+0.320 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.485 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.3741` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3741 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.275 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `739.9655` → IC=+0.268 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 739.9655 (IC base=+0.269)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=202)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5446` → IC=+0.352 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5446 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `209.4` → IC=+0.395 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.4 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.6678` → IC=+0.387 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6678 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.381 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1039.0` → IC=+0.426 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1039.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.292 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.278)

- **PATRÓN** `elapsed_s` > `232.0` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.0 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `2.354` → IC=+0.309 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.354 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.296 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.278)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `1275.0` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1275.0 (IC base=+0.278)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=202)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5446` → IC=+0.352 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5446 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `209.4` → IC=+0.395 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.4 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.6678` → IC=+0.387 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6678 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.381 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1039.0` → IC=+0.426 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1039.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.292 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.278)

- **PATRÓN** `elapsed_s` > `232.0` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.0 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `2.354` → IC=+0.309 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.354 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.296 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.278)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `1275.0` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1275.0 (IC base=+0.278)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=291)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=236)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=291)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1535)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `liq_n` > 2.0 (IC base=+0.096)

- **PATRÓN** `liq_usd_total` > `153.37` → IC=+0.129 (n=157)

  - _Acción_: Kelly boost +0.64€ cuando `liq_usd_total` > 153.37 (IC base=+0.096)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.096)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.137 (n=89)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.5 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.096)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.150 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.185 (n=87)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=110)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.185 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 8.0 (IC base=+0.083)

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
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=282)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4265)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=254)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=211)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.199 (n=81)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=160)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 50.0 (IC base=+0.024)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.133 (n=295)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.194)

- **PATRÓN** `liq_usd_total` > `862.23` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 862.23 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.218 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.225 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.194)

- **PATRÓN** `ballena_activa_n` < `3.0` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 3.0 (IC base=+0.194)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1676)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1630)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `ballena_activa_n` > `133.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 133.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=766)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=775)

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
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=590)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=571)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=240)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=-0.002)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=1167)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=1167)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1573)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1573)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=369)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=369)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.144 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=299)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=414)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=463)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=340)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=443)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=443)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=436)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.130 (n=3641)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=9395)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.145 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=145)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=89)

- **FILTRO** `restante_min` < `3.99` → IC=-0.130 (n=71)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.142 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

- **FILTRO** `lag_apertura_s` > `60.89` → IC=-0.130 (n=71)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.89
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.161 (n=437)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1051)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.144 (n=346)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=939)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.145 (n=446)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.51 (IC base=-0.007)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.129 (n=203)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=466)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.120 (n=506)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=535)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=744)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=792)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.140 (n=365)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=786)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.129 (n=572)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=718)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=597)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=634)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.133 (n=649)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=754)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9281)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=28972)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=9653)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=29900)

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
- **FILTRO** `py_entrada` > `0.575` → IC=-0.176 (n=1369)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4208)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.179 (n=1399)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4278)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3375)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4327)

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
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=374)

- **FILTRO** `drift_20min_pct` |x|> `0.1999` → IC=-0.134 (n=121)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1999
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=366)

- **FILTRO** `libro_liquidez` < `3248.8853` → IC=-0.185 (n=160)

  - _Acción_: SKIP cuando `libro_liquidez` < 3248.8853
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=327)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.224 (n=310)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=957)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=230)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.023)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=25903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=58680)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20605)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=63978)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27809)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=56774)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.154 (n=28629)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=55954)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26205)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=79549)

- **FILTRO** `ibs_7min` > `0.2782` → IC=-0.183 (n=26437)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2782
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=79317)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=3382)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=10657)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3430)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10609)

- **FILTRO** `ibs_7min` < `0.7112` → IC=-0.214 (n=3508)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7112
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10531)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.204 (n=3498)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10541)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=3276)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=11098)

- **FILTRO** `ibs_7min` > `0.2635` → IC=-0.189 (n=3591)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2635
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10783)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.177 (n=3588)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10786)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.120 (n=4500)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=9218)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=3123)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10595)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.202 (n=3427)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10291)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.199 (n=3397)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=10321)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=3322)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=10923)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.178 (n=3559)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=10686)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.171 (n=3502)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10743)

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
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1036)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1325)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.165 (n=183)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=681)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=931)

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

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=556)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.144 (n=774)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `456.9956` → IC=+0.166 (n=569)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 456.9956 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3675.377` → IC=+0.129 (n=774)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3675.377 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.184 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 14.0 (IC base=+0.144)

- **PATRÓN** `total_vol_5m` < `381.605` → IC=+0.167 (n=346)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 381.605 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.146 (n=357)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.04 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.158 (n=276)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 9.0 (IC base=+0.144)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.135 (n=357)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=332)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.120 (n=435)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.162 (n=208)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `877.8133` → IC=+0.159 (n=312)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 877.8133 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 59.0 (IC base=+0.128)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4315` → IC=+0.209 (n=132)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4315 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.157 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 6.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.179 (n=194)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4761.643 (IC base=+0.130)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.129 (n=313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 13.0 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=218)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.1729` → IC=-0.222 (n=88)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.1729
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=172)

- **FILTRO** `pct_vs_K` |x|> `2.8903` → IC=-0.126 (n=509)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8903
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=510)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.155 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0047 (IC base=-0.030)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.260 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.002)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9196` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.9196 (IC base=+0.002)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0113` → IC=-0.152 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0113
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=73)

- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0153` → IC=-0.200 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0153
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=146)

- **FILTRO** `T_h` < `75.359` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `T_h` < 75.359
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=130)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0147` → IC=-0.167 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0147
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0118` → IC=-0.252 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0118
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=218)

- **FILTRO** `T_h` > `66.9091` → IC=-0.251 (n=581)

  - _Acción_: SKIP cuando `T_h` > 66.9091
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=289)

- **FILTRO** `sigma_h` < `0.0081` → IC=-0.159 (n=414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=415)

- **FILTRO** `pct_vs_K` |x|> `2.9643` → IC=-0.376 (n=207)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9643
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=622)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `49.2927` → IC=-0.239 (n=213)

  - _Acción_: SKIP cuando `T_h` > 49.2927
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=73)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.162 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=105)

- **FILTRO** `pct_vs_K` |x|> `2.368` → IC=-0.330 (n=104)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.368
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=203)

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
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.322 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=127)

- **FILTRO** `T_h` > `133.1543` → IC=-0.315 (n=63)

  - _Acción_: SKIP cuando `T_h` > 133.1543
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=191)

- **FILTRO** `T_h` < `69.35` → IC=-0.312 (n=83)

  - _Acción_: SKIP cuando `T_h` < 69.35
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=171)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.151 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=164)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=186)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9843` → IC=+0.161 (n=125)

  - _Acción_: Kelly boost +0.81€ cuando `pct_vs_K` |x|≤ 1.9843 (IC base=-0.100)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` < `145.6184` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `T_h` < 145.6184
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.013` → IC=-0.220 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=158)

- **FILTRO** `sigma_h` < `0.01` → IC=-0.237 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=160)

- **FILTRO** `T_h` > `61.9454` → IC=-0.222 (n=178)

  - _Acción_: SKIP cuando `T_h` > 61.9454
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=60)

- **FILTRO** `sigma_h` > `0.014` → IC=-0.297 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.014
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=122)

- **FILTRO** `sigma_h` < `0.0097` → IC=-0.250 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=138)

- **FILTRO** `T_h` < `73.3227` → IC=-0.149 (n=92)

  - _Acción_: SKIP cuando `T_h` < 73.3227
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=92)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1171` → IC=+0.448 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1171 (IC base=+0.339)

- **PATRÓN** `sigma_h` < `0.0147` → IC=+0.353 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0147 (IC base=+0.339)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.350 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.339)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.339)

- **PATRÓN** `T_h` > `0.4307` → IC=+0.361 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4307 (IC base=+0.339)

- **PATRÓN** `dist_50` > `0.3296` → IC=+0.439 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3296 (IC base=+0.339)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.355 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.339)

- **PATRÓN** `edge` > `0.0995` → IC=+0.427 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0995 (IC base=+0.392)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.406 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.368` → IC=+0.440 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.368 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=348)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.392)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1021` → IC=+0.284 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1021 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.241 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.195)

- **PATRÓN** `T_h` < `0.7026` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7026 (IC base=+0.195)

- **PATRÓN** `T_h` > `1.4764` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4764 (IC base=+0.195)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.195)

### RESOLUTION_SNIPER#ETH#sniper
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
- **PATRÓN** `edge` > `0.1581` → IC=+0.487 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1581 (IC base=+0.441)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.470 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.441)

- **PATRÓN** `T_h` > `0.5804` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5804 (IC base=+0.441)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.473 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.441)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=493)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=524)

- **PATRÓN** `streak_estiramiento` < `0.3783` → IC=+0.133 (n=164)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.3783 (IC base=+0.020)

- **PATRÓN** `streak_estiramiento` < `0.8333` → IC=+0.122 (n=363)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.8333 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 14.0 (IC base=+0.057)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.080)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=25)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.048)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.2662` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.2662 (IC base=+0.036)

- **PATRÓN** `streak_estiramiento` < `0.5992` → IC=+0.152 (n=185)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.5992 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.135 (n=198)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 35.0 (IC base=+0.081)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=102)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=122)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=43)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=38)

- **FILTRO** `streak_estiramiento` > `0.6393` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6393
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=31)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **PATRÓN** `streak_estiramiento` < `0.6237` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6237 (IC base=+0.040)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1110)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1356)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5573)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3376)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.184 (n=2193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.2332` → IC=+0.158 (n=6577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2332 (IC base=+0.131)

- **PATRÓN** `drift_15min` |x|≤ `1.1239` → IC=+0.133 (n=6576)

  - _Acción_: Kelly boost +0.66€ cuando `drift_15min` |x|≤ 1.1239 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0645` → IC=+0.132 (n=6575)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0645 (IC base=+0.131)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0999` → IC=+0.143 (n=2072)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0999 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6086)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.5532` → IC=+0.207 (n=5875)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5532 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.995` → IC=+0.231 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.995 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3445)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4310.1831` → IC=+0.170 (n=2192)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4310.1831 (IC base=+0.131)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2537)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.253 (n=297)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.248 (n=391)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.228 (n=296)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.206)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2251` → IC=+0.218 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2251 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7031` → IC=+0.274 (n=888)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7031 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.3997` → IC=+0.232 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3997 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5531` → IC=+0.209 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5531 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.192` → IC=+0.298 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.192 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `11859.2402` → IC=+0.222 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11859.2402 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.148 (n=1000)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0067 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.146 (n=759)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0834` → IC=+0.137 (n=1016)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0834 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4807` → IC=+0.217 (n=1137)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4807 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1238` → IC=+0.146 (n=713)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1238 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.132 (n=1289)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.946` → IC=+0.286 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.946 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6114.254` → IC=+0.174 (n=516)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6114.254 (IC base=+0.132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8346` → IC=+0.147 (n=676)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` > 0.8346 (IC base=+0.045)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.142 (n=1668)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0119 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2399` → IC=+0.174 (n=1669)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2399 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0582` → IC=+0.140 (n=1668)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0582 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.184 (n=523)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.142 (n=1524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.141 (n=1469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.6981` → IC=+0.232 (n=1112)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6981 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.2145` → IC=+0.145 (n=765)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.2145 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.9054` → IC=+0.140 (n=1923)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.9054 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.99` → IC=+0.187 (n=385)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 16.99 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2944.984` → IC=+0.183 (n=758)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2944.984 (IC base=+0.136)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.364 (n=544)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.377 (n=543)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1057` → IC=+0.377 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1057 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.371 (n=862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7881` → IC=+0.394 (n=815)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7881 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2719` → IC=+0.383 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2719 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.84` → IC=+0.397 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.84 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.376 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9610.6074 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.362 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1523` → IC=+0.364 (n=344)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1523 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.362 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2175` → IC=+0.377 (n=177)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2175 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.399 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.362 (n=397)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.383 (n=390)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.394 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.785` → IC=+0.383 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.785 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `15150.2605` → IC=+0.388 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15150.2605 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.384 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 409.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.362 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.377 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.367 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1264` → IC=+0.377 (n=283)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1264 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.369 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.379 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.397 (n=425)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.377 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.6907` → IC=+0.362 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6907 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.857` → IC=+0.399 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.857 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `4314.8149` → IC=+0.372 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4314.8149 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2709)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3414)

- **FILTRO** `libro_liquidez` < `4391.961` → IC=-0.172 (n=4041)

  - _Acción_: SKIP cuando `libro_liquidez` < 4391.961
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=2082)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.278 (n=1344)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` > `0.117` → IC=+0.208 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.117 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` < `0.6021` → IC=+0.197 (n=1424)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.6021 (IC base=-0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.228` → IC=+0.267 (n=2012)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.228 (IC base=+0.002)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.282 (n=6034)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.7089` → IC=+0.264 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7089 (IC base=+0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` < `0.004` → IC=-0.209 (n=1006)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3020)

- **FILTRO** `sigma_ewma_delta_pct` > `22.233` → IC=-0.239 (n=569)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.233
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3457)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.184 (n=93)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=3933)

- **FILTRO** `libro_liquidez` < `10159.2138` → IC=-0.193 (n=1328)

  - _Acción_: SKIP cuando `libro_liquidez` < 10159.2138
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2698)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.145 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0033 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.279 (n=161)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.281 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.064)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.317 (n=483)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1067` → IC=+0.287 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1067 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.5498` → IC=+0.284 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5498 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.793` → IC=+0.142 (n=241)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 21.793 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.107` → IC=+0.224 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.107 (IC base=-0.181)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1389` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1389 (IC base=-0.181)

- **PATRÓN** `ibs_15` < `0.6283` → IC=+0.288 (n=83)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6283 (IC base=-0.181)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.181)

- **PATRÓN** `ballena_activa_n` < `392.0` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 392.0 (IC base=-0.181)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=886)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.162 (n=678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0066 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.173 (n=298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.184 (n=536)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5656` → IC=+0.240 (n=678)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5656 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6788` → IC=+0.181 (n=133)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6788 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.258 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=886)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5210.4456` → IC=+0.167 (n=452)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5210.4456 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.255 (n=1036)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.4821` → IC=+0.242 (n=2354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4821 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `0.8254` → IC=+0.249 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8254 (IC base=+0.236)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1983` → IC=+0.256 (n=1070)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1983 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.239 (n=1613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.236)

- **PATRÓN** `ibs_15` < `0.3918` → IC=+0.268 (n=2354)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3918 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.2382` → IC=+0.245 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2382 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.511` → IC=+0.243 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.511 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.283` → IC=+0.239 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.283 (IC base=+0.236)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1999` → IC=-0.299 (n=367)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1999
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1103)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.282 (n=499)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=971)

- **FILTRO** `drift_15min` |x|> `1.0228` → IC=-0.305 (n=367)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0228
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1103)

- **FILTRO** `sigma_ewma_delta_pct` > `5.969` → IC=-0.214 (n=323)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.969
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1147)

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

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.298 (n=997)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2005` → IC=+0.257 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2005 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0143` → IC=-0.251 (n=1149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0143
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=567)

- **FILTRO** `drift_60min` |x|> `0.1231` → IC=-0.243 (n=582)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1231
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=1134)

- **FILTRO** `drift_15min` |x|> `1.2992` → IC=-0.284 (n=428)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2992
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=1288)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1695)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.283 (n=1249)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=-0.008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.287 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3297` → IC=+0.292 (n=1397)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3297 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.7886` → IC=+0.325 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7886 (IC base=-0.008)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.172 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0063 (IC base=+0.081)

- **PATRÓN** `drift_15min` |x|≤ `0.7362` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.7362 (IC base=+0.081)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.306 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1929` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1929 (IC base=+0.052)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.172 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0063 (IC base=+0.081)

- **PATRÓN** `drift_15min` |x|≤ `0.7362` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.7362 (IC base=+0.081)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.306 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1929` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1929 (IC base=+0.052)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.300 (n=498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.292 (n=498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0715` → IC=+0.307 (n=660)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0715 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.285 (n=995)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2178` → IC=+0.288 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2178 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8361` → IC=+0.309 (n=1494)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8361 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2764` → IC=+0.316 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2764 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.738` → IC=+0.387 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.738 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13082.2536` → IC=+0.300 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13082.2536 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.307 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.299 (n=346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.279)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.280 (n=262)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2292` → IC=+0.286 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2292 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.302 (n=724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.8568` → IC=+0.307 (n=702)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8568 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2612` → IC=+0.310 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2612 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.592` → IC=+0.391 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.592 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `14498.4435` → IC=+0.307 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14498.4435 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.299 (n=312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.324 (n=236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.293 (n=708)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.307 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.289 (n=354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8447` → IC=+0.314 (n=708)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8447 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.315 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2918 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.914` → IC=+0.381 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.914 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1089` → IC=-0.161 (n=234)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1089
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=116)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.145 (n=240)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=120)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.167 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=384)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.198 (n=124)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=126)

### UPDOWN_OU_5M#BNB#5min
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
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=168)

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
- **FILTRO** `sigma_h` < `0.0081` → IC=-0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.103` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.103
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=27)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.235 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=33)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0549` → IC=-0.222 (n=16)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=49)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9866` → IC=+0.253 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9866 (IC base=+0.123)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.355 (n=3337)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.333)

- **PATRÓN** `ratio` > `1.0158` → IC=+0.384 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0158 (IC base=+0.333)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9756` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `ratio` < 0.9756 (IC base=+0.064)

- **PATRÓN** `T_h` > `109.7804` → IC=+0.327 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.7804 (IC base=+0.304)

- **PATRÓN** `ratio` > `1.0005` → IC=+0.293 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0005 (IC base=+0.304)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9775` → IC=+0.364 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.187)

- **PATRÓN** `T_h` > `111.9956` → IC=+0.350 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9956 (IC base=+0.316)

- **PATRÓN** `ratio` > `1.023` → IC=+0.403 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.023 (IC base=+0.316)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0386` → IC=+0.413 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0386 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5532 sube el IC de +0.131 a +0.207 en UPDOWN_GBM#15min (n=5875). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7031 sube el IC de +0.206 a +0.274 en UPDOWN_GBM#BTC#15min (n=888). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4807 sube el IC de +0.132 a +0.217 en UPDOWN_GBM#ETH#15min (n=1137). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.6981 sube el IC de +0.136 a +0.232 en UPDOWN_GBM#XRP#15min (n=1112). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6288 sube el IC de -0.088 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1344). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.002 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=6034). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.064 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=483). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.181 a +0.288 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=83). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5656 sube el IC de +0.146 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=678). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3918 sube el IC de +0.236 a +0.268 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2354). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.026 a +0.298 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=997). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3297 sube el IC de -0.008 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1397). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.081 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7 (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.081 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8361 sube el IC de +0.284 a +0.309 en UPDOWN_GBM_IBS_ALTO (n=1494). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8568 sube el IC de +0.279 a +0.307 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=702). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8447 sube el IC de +0.289 a +0.314 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=708). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7881 sube el IC de +0.363 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=815). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.362 a +0.383 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.363 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=425). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2356 | +0.084 | +253.92€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2356 | +0.084 | +253.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1944 | +0.085 | +214.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1944 | +0.085 | +214.43€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1491 | -0.028 | +55.82€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1491 | -0.028 | +55.82€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1167 | -0.040 | +43.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1167 | -0.040 | +43.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51501 | -0.087 | -6589.09€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3380 | +0.096 | -317.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48121 | -0.099 | -6271.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3380 | +0.096 | -317.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3380 | +0.096 | -317.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14332 | -0.044 | -1327.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14332 | -0.044 | -1327.14€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 57080 | -0.012 | +2621.07€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14724 | +0.003 | +1465.23€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 42356 | -0.017 | +1155.84€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 57080 | -0.012 | +2621.07€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14724 | +0.003 | +1465.23€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 42356 | -0.017 | +1155.84€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 212727 | +0.112 | -8666.18€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23434 | +0.179 | -745.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 995 | +0.021 | -79.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 176222 | +0.105 | -7446.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12076 | +0.095 | -393.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 29221 | +0.101 | -2097.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 87 | -0.197 | +9.66€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 29097 | +0.102 | -2116.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 39829 | +0.123 | -620.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5717 | +0.177 | -224.69€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 29172 | +0.119 | -215.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4898 | +0.081 | -158.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 29267 | +0.098 | -2044.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 106 | -0.102 | +22.72€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 29134 | +0.099 | -2060.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 12 | -0.043 | +5.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 45525 | +0.123 | -960.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11331 | +0.178 | -321.42€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 29640 | +0.106 | -547.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4542 | +0.103 | -82.50€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 39651 | +0.111 | -1675.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6093 | +0.200 | -245.28€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 898 | +0.044 | -25.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 30061 | +0.096 | -1221.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2599 | +0.107 | -182.56€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 29234 | +0.106 | -1268.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 100 | -0.137 | +13.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 29118 | +0.107 | -1284.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 34658 | +0.189 | -2620.58€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 34658 | +0.189 | -2620.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7857 | +0.160 | -940.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7857 | +0.160 | -940.27€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5209 | +0.194 | -223.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5209 | +0.194 | -223.18€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7660 | +0.172 | -712.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7660 | +0.172 | -712.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6344 | +0.252 | -217.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6344 | +0.252 | -217.36€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7509 | +0.182 | -541.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7509 | +0.182 | -541.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1335 | +0.425 | -50.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1335 | +0.425 | -50.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 570 | +0.439 | -5.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 570 | +0.439 | -5.45€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 223 | +0.402 | -17.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 223 | +0.402 | -17.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 122546 | +0.199 | -8979.09€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 122546 | +0.199 | -8979.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21247 | +0.175 | -2518.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21247 | +0.175 | -2518.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19745 | +0.223 | -659.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19745 | +0.223 | -659.90€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21016 | +0.180 | -2212.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21016 | +0.180 | -2212.20€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19928 | +0.217 | -784.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19928 | +0.217 | -784.23€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20212 | +0.205 | -1185.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20212 | +0.205 | -1185.46€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20398 | +0.196 | -1618.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20398 | +0.196 | -1618.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 47652 | +0.117 | +407.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 47652 | +0.117 | +407.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 23727 | +0.117 | +265.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 23727 | +0.117 | +265.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 23925 | +0.116 | +141.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 23925 | +0.116 | +141.80€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2057 | +0.063 | -109.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1332 | +0.072 | -45.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1623 | +0.069 | -64.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1332 | +0.072 | -45.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 97402 | +0.101 | -2046.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7905 | +0.097 | +189.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 89497 | +0.101 | -2236.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 53154 | +0.105 | -436.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7905 | +0.097 | +189.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 45249 | +0.106 | -626.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 20953 | +0.109 | -78.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 20953 | +0.109 | -78.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 23295 | +0.083 | -1532.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 23295 | +0.083 | -1532.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 918 | +0.186 | -105.97€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 918 | +0.186 | -105.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 918 | +0.186 | -105.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 918 | +0.186 | -105.97€ | 1 | 4 |
| ✅ GBM_LATE_15M | 66351 | +0.103 | +37479.29€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 66351 | +0.103 | +37479.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11018 | +0.225 | +9476.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11018 | +0.225 | +9476.53€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 10374 | +0.177 | +8403.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10374 | +0.177 | +8403.75€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 11868 | +0.207 | +9376.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11868 | +0.207 | +9376.06€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8768 | +0.063 | +3005.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8768 | +0.063 | +3005.41€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 9191 | -0.025 | +2382.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9191 | -0.025 | +2382.49€ | 3 | 15 |
| ✅ GBM_LATE_15M#XRP | 15132 | -0.019 | +4835.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15132 | -0.019 | +4835.05€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 70428 | +0.088 | +41295.59€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 70428 | +0.088 | +41295.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13678 | -0.002 | +7166.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13678 | -0.002 | +7166.25€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15145 | +0.007 | +4207.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15145 | +0.007 | +4207.57€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9432 | +0.297 | +10843.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9432 | +0.297 | +10843.38€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13466 | +0.019 | +4321.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13466 | +0.019 | +4321.84€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10706 | +0.051 | +5019.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10706 | +0.051 | +5019.19€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8001 | +0.313 | +9737.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8001 | +0.313 | +9737.36€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 52181 | +0.180 | +43524.51€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 52181 | +0.180 | +43524.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7909 | +0.240 | +7376.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7909 | +0.240 | +7376.17€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8317 | +0.141 | +6288.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8317 | +0.141 | +6288.70€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8399 | +0.224 | +7264.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8399 | +0.224 | +7264.73€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8912 | +0.131 | +7017.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8912 | +0.131 | +7017.27€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9844 | +0.124 | +7638.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9844 | +0.124 | +7638.02€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8800 | +0.232 | +7939.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8800 | +0.232 | +7939.61€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14432 | +0.126 | +7384.88€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14432 | +0.126 | +7384.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3733 | +0.125 | +2018.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3733 | +0.125 | +2018.06€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4236 | +0.127 | +2145.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4236 | +0.127 | +2145.57€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3921 | +0.102 | +1630.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3921 | +0.102 | +1630.44€ | 0 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1355 | +0.168 | +858.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1355 | +0.168 | +858.78€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 66617 | +0.190 | +55682.38€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 66617 | +0.190 | +55682.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10536 | +0.250 | +10165.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10536 | +0.250 | +10165.76€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10708 | +0.143 | +7837.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10708 | +0.143 | +7837.76€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11293 | +0.234 | +10181.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11293 | +0.234 | +10181.36€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11013 | +0.146 | +8355.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11013 | +0.146 | +8355.44€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11744 | +0.129 | +8621.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11744 | +0.129 | +8621.84€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11323 | +0.241 | +10520.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11323 | +0.241 | +10520.21€ | 0 | 23 |
| ✅ GBM_LATE_5M | 16896 | +0.219 | +14282.53€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 16896 | +0.219 | +14282.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3331 | +0.210 | +2855.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3331 | +0.210 | +2855.10€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1591 | +0.218 | +1323.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1591 | +0.218 | +1323.18€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4885 | +0.210 | +3853.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4885 | +0.210 | +3853.18€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3013 | +0.230 | +2683.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3013 | +0.230 | +2683.97€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 2128 | +0.208 | +1668.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2128 | +0.208 | +1668.37€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6597 | +0.080 | +2268.77€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 6597 | +0.080 | +2268.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 182 | +0.266 | +197.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 182 | +0.266 | +197.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2066 | +0.061 | +624.62€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2066 | +0.061 | +624.62€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 176 | +0.320 | +218.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 176 | +0.320 | +218.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1920 | +0.055 | +592.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1920 | +0.055 | +592.99€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 2076 | +0.061 | +420.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2076 | +0.061 | +420.30€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 177 | +0.327 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 177 | +0.327 | +215.28€ | 0 | 24 |
| 🚫 GBM_LATE_60M_FADE | 803 | -0.244 | -32.13€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 803 | -0.244 | -32.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 282 | -0.254 | -19.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 282 | -0.254 | -19.29€ | 4 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 277 | -0.242 | -7.42€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 277 | -0.242 | -7.42€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 219 | -0.247 | -9.19€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 219 | -0.247 | -9.19€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2517 | +0.089 | +665.02€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2517 | +0.089 | +665.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 927 | +0.070 | +237.53€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 927 | +0.070 | +237.53€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 22 | +0.167 | +12.04€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 22 | +0.167 | +12.04€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 832 | +0.053 | +160.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 832 | +0.053 | +160.11€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 672 | +0.151 | +239.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 672 | +0.151 | +239.06€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 64 | +0.121 | +16.27€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 64 | +0.121 | +16.27€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 425 | +0.306 | +505.51€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 425 | +0.306 | +505.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 425 | +0.306 | +505.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 425 | +0.306 | +505.51€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4972 | +0.095 | +1079.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4972 | +0.095 | +1079.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4972 | +0.095 | +1079.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4972 | +0.095 | +1079.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1863 | +0.021 | +110.24€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1863 | +0.021 | +110.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 234 | +0.093 | +48.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 234 | +0.093 | +48.52€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M#BTC | 355 | -0.010 | +8.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 355 | -0.010 | +8.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 135 | +0.047 | +23.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 135 | +0.047 | +23.00€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 413 | +0.025 | +22.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 413 | +0.025 | +22.07€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 356 | -0.020 | +0.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 356 | -0.020 | +0.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 370 | +0.030 | +7.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 370 | +0.030 | +7.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4625 | +0.019 | +211.79€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4625 | +0.019 | +211.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 867 | +0.015 | +49.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 867 | +0.015 | +49.10€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 352 | +0.073 | +99.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 352 | +0.073 | +99.32€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1728 | +0.023 | +37.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1728 | +0.023 | +37.79€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 816 | +0.016 | +6.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 816 | +0.016 | +6.95€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 621 | -0.006 | +24.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 621 | -0.006 | +24.80€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2835 | -0.035 | -11.59€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2835 | -0.035 | -11.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 862 | -0.039 | -18.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 862 | -0.039 | -18.92€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1024 | -0.016 | +18.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1024 | -0.016 | +18.80€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 924 | -0.055 | -11.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 924 | -0.055 | -11.31€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 20 | +0.045 | +0.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 20 | +0.045 | +0.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 21463 | -0.032 | -205.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10405 | -0.032 | -102.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11058 | -0.032 | -103.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 758 | -0.054 | -42.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 388 | -0.041 | -9.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 370 | -0.067 | -33.33€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5783 | -0.025 | -15.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2757 | -0.022 | +10.13€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3026 | -0.028 | -25.62€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1954 | -0.033 | -5.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1002 | -0.038 | -18.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 952 | -0.027 | +13.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4924 | -0.032 | -59.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2372 | -0.029 | -15.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2552 | -0.035 | -44.03€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4082 | -0.025 | +39.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1993 | -0.028 | +3.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2089 | -0.022 | +36.23€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3962 | -0.044 | -121.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1893 | -0.048 | -72.24€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2069 | -0.040 | -49.58€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 77806 | -0.000 | +4198.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 77806 | -0.000 | +4198.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10843 | -0.038 | -148.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10843 | -0.038 | -148.20€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10829 | -0.053 | -275.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10829 | -0.053 | -275.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7497 | -0.052 | -104.92€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7497 | -0.052 | -104.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2159 | -0.058 | -19.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2159 | -0.058 | -19.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 821 | -0.116 | -32.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 821 | -0.116 | -32.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2274 | -0.065 | -10.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2274 | -0.065 | -10.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 871 | -0.019 | -28.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 871 | -0.019 | -28.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3386 | +0.003 | +0.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3386 | +0.003 | +0.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 199 | +0.007 | -1.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 199 | +0.007 | -1.73€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 190337 | -0.078 | +2126.02€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 190337 | -0.078 | +2126.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 28413 | -0.102 | -1429.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 28413 | -0.102 | -1429.81€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 27963 | -0.101 | -1003.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 27963 | -0.101 | -1003.30€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9394 | -0.035 | -186.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9394 | -0.035 | -186.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1012 | -0.017 | -19.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1012 | -0.017 | -19.26€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2204 | -0.046 | -29.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2204 | -0.046 | -29.15€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2682 | -0.024 | -31.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2682 | -0.024 | -31.64€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1316 | -0.063 | -30.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1316 | -0.063 | -30.57€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1171 | -0.040 | -44.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1171 | -0.040 | -44.00€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2410 | +0.120 | +969.48€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2274 | +0.124 | +956.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 524 | +0.144 | +278.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 524 | +0.144 | +278.06€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 476 | +0.117 | +168.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 476 | +0.117 | +168.16€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 415 | +0.128 | +191.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 415 | +0.128 | +191.95€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 387 | +0.130 | +182.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 387 | +0.130 | +182.45€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 472 | +0.097 | +136.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 472 | +0.097 | +136.26€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2539 | -0.023 | -52.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2539 | -0.023 | -52.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 447 | +0.006 | +20.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 447 | +0.006 | +20.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 463 | -0.051 | -33.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 463 | -0.051 | -33.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 613 | -0.045 | -43.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 613 | -0.045 | -43.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 529 | -0.007 | -2.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 529 | -0.007 | -2.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 487 | -0.013 | +7.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 487 | -0.013 | +7.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1346 | -0.043 | +134.81€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 622 | -0.069 | +24.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 484 | -0.066 | +49.83€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 138 | -0.079 | -24.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 474 | -0.011 | +72.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 343 | +0.007 | +82.02€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 131 | -0.056 | -9.68€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 250 | -0.040 | +37.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 212 | -0.037 | +33.09€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 38 | -0.050 | +4.42€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1039 | -0.036 | +164.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 307 | -0.066 | -30.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1699 | -0.185 | -35.36€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 672 | -0.172 | -8.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 593 | -0.171 | -5.74€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 79 | -0.179 | -3.17€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 571 | -0.198 | -32.97€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 502 | -0.204 | -38.08€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 69 | -0.148 | +5.11€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 456 | -0.186 | +6.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 422 | -0.182 | +3.38€ | 6 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 34 | -0.222 | +3.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1517 | -0.185 | -40.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 182 | -0.179 | +5.08€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 600 | +0.377 | +538.69€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 137 | +0.176 | +100.99€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 137 | +0.176 | +100.99€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 138 | +0.371 | +107.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 138 | +0.371 | +107.96€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 325 | +0.460 | +329.75€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 325 | +0.460 | +329.75€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 600 | +0.377 | +538.69€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1055 | +0.039 | +84.14€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1055 | +0.039 | +84.14€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 80 | +0.024 | +1.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 80 | +0.024 | +1.80€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 531 | +0.059 | +72.39€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 531 | +0.059 | +72.39€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3663 | -0.023 | -142.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3663 | -0.023 | -142.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1129 | -0.022 | -40.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1129 | -0.022 | -40.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 631 | -0.028 | -26.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 631 | -0.028 | -26.87€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 178 | -0.050 | -16.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 178 | -0.050 | -16.31€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1725 | -0.018 | -59.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1725 | -0.018 | -59.44€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 154 | +0.013 | +0.66€ | 2 | 1 |
| ✅ STREAK_FADE_60M#60min | 154 | +0.013 | +0.66€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB | 7 | +0.097 | +7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB#60min | 7 | +0.097 | +7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 51 | -0.028 | -2.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 51 | -0.028 | -2.40€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 88 | +0.000 | -5.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 88 | +0.000 | -5.44€ | 1 | 1 |
| ✅ STREAK_FADE_60M#XRP | 5 | +0.018 | -0.23€ | 0 | 0 |
| ✅ STREAK_FADE_60M#XRP#60min | 5 | +0.018 | -0.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 11713 | +0.013 | +63.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11713 | +0.013 | +63.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3010 | +0.017 | +20.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3010 | +0.017 | +20.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3129 | +0.013 | +24.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3129 | +0.013 | +24.65€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2952 | +0.009 | -1.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2952 | +0.009 | -1.23€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2622 | +0.014 | +18.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2622 | +0.014 | +18.81€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13964 | +0.019 | +6.92€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13964 | +0.019 | +6.92€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5592 | +0.021 | +5.92€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5592 | +0.021 | +5.92€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4962 | +0.019 | +3.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4962 | +0.019 | +3.88€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3410 | +0.014 | -2.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3410 | +0.014 | -2.88€ | 1 | 0 |
| ✅ UPDOWN_GBM | 126243 | +0.060 | +12071.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 31535 | +0.077 | +6166.29€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3584 | -0.001 | +40.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 83197 | +0.062 | +5736.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7497 | -0.002 | +130.97€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11032 | +0.104 | +2047.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2092 | +0.165 | +979.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8850 | +0.091 | +1069.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 28538 | +0.057 | +2524.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4225 | +0.081 | +952.69€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1056 | +0.000 | +21.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19709 | +0.066 | +1462.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3394 | -0.004 | +83.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 154 | -0.064 | +4.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14131 | +0.075 | +1572.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11961 | +0.061 | +679.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 29578 | +0.049 | +2106.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7302 | +0.070 | +1140.41€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1020 | +0.005 | +15.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18329 | +0.051 | +907.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2783 | -0.002 | +40.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 144 | -0.096 | +2.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26093 | +0.041 | +1500.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8525 | +0.032 | +477.26€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 935 | -0.011 | +7.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15197 | +0.054 | +1015.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1306 | +0.003 | +7.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 130 | -0.136 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16869 | +0.073 | +2322.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7307 | +0.088 | +1722.60€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9151 | +0.064 | +601.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 14 | +0.000 | -0.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 428 | -0.098 | -0.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1086 | +0.363 | +412.54€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1086 | +0.363 | +412.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 520 | +0.362 | +186.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 520 | +0.362 | +186.53€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 566 | +0.363 | +226.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 566 | +0.363 | +226.01€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 29871 | -0.017 | +7536.59€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 29871 | -0.017 | +7536.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2350 | -0.045 | +632.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2350 | -0.045 | +632.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5504 | -0.115 | +334.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5504 | -0.115 | +334.76€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4041 | +0.216 | +2546.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4041 | +0.216 | +2546.30€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8386 | -0.057 | +1270.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8386 | -0.057 | +1270.18€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8296 | -0.052 | +1689.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8296 | -0.052 | +1689.73€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 377 | +0.059 | +31.96€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 377 | +0.059 | +31.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 377 | +0.059 | +31.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 377 | +0.059 | +31.96€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1990 | +0.284 | +1699.79€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1990 | +0.284 | +1699.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1047 | +0.279 | +846.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1047 | +0.279 | +846.28€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 943 | +0.289 | +853.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 943 | +0.289 | +853.52€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 903 | -0.120 | -94.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 903 | -0.120 | -94.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 290 | -0.086 | -23.04€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 290 | -0.086 | -23.04€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 125 | -0.193 | -7.08€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 125 | -0.193 | -7.08€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5424 | +0.291 | +2360.42€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2122 | +0.247 | +323.50€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2098 | +0.284 | +868.54€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1204 | +0.381 | +1168.38€ | 0 | 1 |