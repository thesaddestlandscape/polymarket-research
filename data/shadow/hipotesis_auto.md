# Hipótesis automáticas — 2026-11-24 15:40 UTC
_Generado por shadow_postmortem.py sobre 1479611 resoluciones (PNL=+209753.72€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=725)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1111)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `60.0` → IC=+0.172 (n=361)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 60.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8116` → IC=+0.269 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8116 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.232` → IC=+0.196 (n=350)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.232 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1140)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4618.7388` → IC=+0.127 (n=475)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4618.7388 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=555)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.194 (n=974)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.181 (n=308)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 63.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8111` → IC=+0.265 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8111 (IC base=+0.125)

- **PATRÓN** `banda_z` > `8.316` → IC=+0.194 (n=305)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.316 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.137 (n=828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1040)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `5097.9637` → IC=+0.128 (n=415)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 5097.9637 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8596.0083` → IC=+0.127 (n=247)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 8596.0083 (IC base=+0.018)

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
- **FILTRO** `restante_s_al_confirmar` < `130.42` → IC=-0.220 (n=12878)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.42
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=38636)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.84` → IC=-0.161 (n=3586)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.84
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=10759)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=30703)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7784.1082` → IC=+0.152 (n=2498)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7784.1082 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=27203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=33053)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=24610)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=8876)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6266.6285` → IC=+0.138 (n=3487)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 6266.6285 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=2232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=2733)

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
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=680)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.073)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.120 (n=2217)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.45 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=5625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.378 (n=1905)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.200 (n=2698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=3143)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.193)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=978)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.645` → IC=+0.236 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.645 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1207)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2043.1794` → IC=+0.138 (n=974)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2043.1794 (IC base=+0.135)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.144 (n=1486)
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
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.135 (n=1065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.254 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.127)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=27282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=17263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.220 (n=8725)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `8407.3041` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8407.3041 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=6221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.160 (n=3933)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.174 (n=5995)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=3842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=2570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.243 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.204)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=6055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.173 (n=5136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6192)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4771)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.252 (n=2322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1648)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=5917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=3762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1933)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=1037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=1033)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `14027.0561` → IC=+0.450 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14027.0561 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=473)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.405 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.403)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.410 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.403)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.418 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.403)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=35100)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.185 (n=5319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=11461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=16446)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=14877)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6310)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.189 (n=6102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=12610)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=5787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5745)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.258 (n=6096)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=13543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.251 (n=6395)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=5922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5926)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7338)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=12787)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=14030)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.29` → IC=+0.140 (n=11988)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.29 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6214)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6371)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=7934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.76` → IC=+0.141 (n=7839)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.76 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6573)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.135 (n=8464)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.89` → IC=+0.136 (n=7906)

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
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=95)

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
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=95)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5086` → IC=+0.140 (n=20432)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5086 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=20689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=14244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9737` → IC=+0.247 (n=6814)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9737 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8821` → IC=+0.293 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8821 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.462` → IC=+0.191 (n=10244)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.462 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6944` → IC=+0.269 (n=5588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6944 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3034` → IC=+0.257 (n=2114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3034 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7399` → IC=+0.235 (n=4938)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7399 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=9840)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4912.4282` → IC=+0.151 (n=6811)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4912.4282 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.122 (n=12956)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0066 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.5641` → IC=+0.146 (n=25868)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5641 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.6791` → IC=+0.193 (n=1770)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6791 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.1779` → IC=+0.196 (n=10569)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1779 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.8563` → IC=+0.198 (n=7198)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8563 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.230 (n=2620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.2829` → IC=+0.212 (n=8301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2829 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=18288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.088)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.304` → IC=+0.214 (n=3811)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.304 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=2098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2904)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9822` → IC=+0.274 (n=1964)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9822 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.433` → IC=+0.275 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.433 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.261 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4382` → IC=+0.213 (n=4161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4382 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2047.52` → IC=+0.216 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2047.52 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.220 (n=3585)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.246 (n=1792)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0966` → IC=+0.271 (n=1315)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0966 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1807)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0794` → IC=+0.278 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0794 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.961` → IC=+0.245 (n=4040)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.961 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0724` → IC=+0.242 (n=3408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0724 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.247 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.5533` → IC=+0.240 (n=1663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5533 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.8555` → IC=+0.242 (n=2519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8555 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=4336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.231 (n=1241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1152` → IC=+0.245 (n=1633)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1152 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.8906` → IC=+0.255 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8906 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.7571` → IC=+0.234 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7571 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.747` → IC=+0.260 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.747 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6962` → IC=+0.229 (n=3316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6962 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.267 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.4398` → IC=+0.247 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4398 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `15715.3297` → IC=+0.222 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15715.3297 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.159 (n=3594)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0835` → IC=+0.158 (n=1363)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0835 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7101` → IC=+0.172 (n=4080)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7101 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1554` → IC=+0.152 (n=3986)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1554 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.97` → IC=+0.142 (n=3759)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.97 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.157 (n=1361)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6279 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.160 (n=1478)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4451` → IC=+0.144 (n=3948)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4451 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=5299)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.188 (n=1300)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.213 (n=2086)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.886` → IC=+0.277 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.886 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.193 (n=4124)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.224 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7293` → IC=+0.211 (n=2037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7293 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5540)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2025.0984` → IC=+0.202 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2025.0984 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.226 (n=1901)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.3079` → IC=+0.229 (n=2880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3079 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=1965)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0526` → IC=+0.268 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0526 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.645` → IC=+0.266 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.645 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.255 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.152` → IC=+0.230 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.152 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1890.8984` → IC=+0.223 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1890.8984 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.222 (n=4194)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.171 (n=256)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5549)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.140 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.250 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.351 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.5966` → IC=+0.344 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5966 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.19` → IC=+0.217 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.19 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2486` → IC=+0.366 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2486 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1652` → IC=+0.349 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1652 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.357 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4179` → IC=+0.363 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4179 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.2782` → IC=+0.355 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2782 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.350 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0865` → IC=+0.189 (n=1452)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0865 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.3644` → IC=+0.157 (n=729)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3644 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1535` → IC=+0.159 (n=2717)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1535 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.8259` → IC=+0.163 (n=1908)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8259 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.190 (n=363)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.4311` → IC=+0.171 (n=919)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.4311 (IC base=+0.060)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.183 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=893)

- **FILTRO** `ibs_20min` > `0.1935` → IC=-0.126 (n=5443)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1935
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=2703)

- **FILTRO** `sigma_ewma_delta_pct` > `8.272` → IC=-0.232 (n=883)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.272
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=7263)

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

- **PATRÓN** `ibs_20min` < `0.1935` → IC=+0.161 (n=2703)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1935 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.8372` → IC=+0.294 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8372 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.3228` → IC=+0.293 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3228 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.304 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6932 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `1.0412` → IC=+0.294 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0412 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0782` → IC=+0.321 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0782 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.7983` → IC=+0.311 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7983 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5263` → IC=+0.299 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5263 (IC base=-0.031)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7982` → IC=-0.160 (n=4201)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7982
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=2165)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.179 (n=1309)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=5057)

- **FILTRO** `ibs_20min` > `0.7213` → IC=-0.190 (n=2195)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7213
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=6587)

- **PATRÓN** `ibs_20min` > `0.7982` → IC=+0.146 (n=2165)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7982 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.455` → IC=+0.342 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.455 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.319 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3081` → IC=+0.319 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3081 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5309` → IC=+0.320 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5309 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1054` → IC=+0.286 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1054 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.6364` → IC=+0.276 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6364 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.2131` → IC=+0.279 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2131 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2383` → IC=+0.279 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2383 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.4899` → IC=+0.263 (n=2491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4899 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.270 (n=2490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.187 (n=8941)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0112 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8659` → IC=+0.284 (n=12155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8659 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0076` → IC=+0.306 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0076 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.457` → IC=+0.167 (n=12067)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.457 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.280 (n=8911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.297 (n=2211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6441` → IC=+0.289 (n=5183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6441 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=15198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.154 (n=11832)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0093 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5161` → IC=+0.175 (n=22954)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.5161 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2053` → IC=+0.285 (n=8885)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2053 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.8575` → IC=+0.280 (n=5951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8575 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1877` → IC=+0.286 (n=2976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1877 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.322 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4529` → IC=+0.304 (n=4426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4529 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2708` → IC=+0.305 (n=6020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2708 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.313 (n=13289)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8155` → IC=-0.148 (n=4745)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8155
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2447)

- **FILTRO** `ibs_20min` > `0.7` → IC=-0.243 (n=1621)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=4878)

- **FILTRO** `sigma_ewma_delta_pct` > `4.057` → IC=-0.240 (n=1362)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.057
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5137)

- **PATRÓN** `ibs_20min` > `0.8155` → IC=+0.313 (n=2447)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8155 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.145` → IC=+0.175 (n=2676)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 2.145 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.332 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.293 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2229` → IC=+0.317 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2229 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.316 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1707` → IC=+0.174 (n=1625)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1707 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1546` → IC=+0.388 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1546 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6471` → IC=+0.395 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6471 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1826` → IC=+0.231 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1826 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.222 (n=2338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.245 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.230 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4611` → IC=+0.219 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4611 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `368.0` → IC=+0.234 (n=2591)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 368.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.5742` → IC=+0.259 (n=2339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5742 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.0184` → IC=+0.269 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0184 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.285 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.257 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1506` → IC=+0.263 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1506 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.275 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 196.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.320 (n=1661)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.574` → IC=+0.306 (n=2488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.574 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.13` → IC=+0.294 (n=3410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.13 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.1652` → IC=+0.297 (n=2378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1652 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2021.7` → IC=+0.299 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2021.7 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.302 (n=2277)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.335 (n=2282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.309)

- **PATRÓN** `drift_60min` |x|≤ `0.189` → IC=+0.328 (n=1508)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.189 (IC base=+0.309)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=1310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.309)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.313 (n=1549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.309)

- **PATRÓN** `ibs_20min` < `0.0306` → IC=+0.309 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0306 (IC base=+0.309)

- **PATRÓN** `ibs_20min` > `0.1562` → IC=+0.321 (n=2281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1562 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.983` → IC=+0.318 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.983 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` < `0.1987` → IC=+0.309 (n=3399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1987 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.317 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.309)

- **PATRÓN** `volumen_spike_ratio` > `2.7409` → IC=+0.327 (n=1503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7409 (IC base=+0.309)

- **PATRÓN** `libro_liquidez` > `2004.4248` → IC=+0.321 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.4248 (IC base=+0.309)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.314 (n=3292)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.309)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1598` → IC=+0.241 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1598 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.6407` → IC=+0.236 (n=2685)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6407 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.173` → IC=+0.238 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.173 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.5961` → IC=+0.236 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5961 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.238 (n=2572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1025` → IC=+0.242 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1025 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4071` → IC=+0.244 (n=2379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4071 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4958` → IC=+0.238 (n=2125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4958 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.254 (n=2430)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.152 (n=1692)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.092 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.3861` → IC=+0.262 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3861 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.173` → IC=+0.264 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.173 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6142` → IC=+0.261 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6142 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.266 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.1598` → IC=+0.279 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1598 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.7764` → IC=+0.284 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7764 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4143` → IC=+0.272 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4143 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.282 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.249 (n=2748)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.316 (n=2769)

- **FILTRO** `ibs_20min` > `0.6047` → IC=-0.236 (n=1298)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6047
  - _Potencial_: sin este filtro IC_bueno=+0.169 (n=3902)

- **FILTRO** `sigma_ewma_delta_pct` > `8.236` → IC=-0.261 (n=596)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.236
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=4604)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.316 (n=2769)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `1.1139` → IC=+0.356 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1139 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.448` → IC=+0.159 (n=2253)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.448 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.349 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6979` → IC=+0.337 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6979 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.0998` → IC=+0.339 (n=1912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0998 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.369 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7921` → IC=+0.357 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7921 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.354 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6047` → IC=+0.169 (n=3902)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6047 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.3259` → IC=+0.276 (n=2107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3259 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.727` → IC=+0.136 (n=4076)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.727 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6884` → IC=+0.288 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6884 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.301 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.1387` → IC=+0.281 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1387 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.293 (n=2031)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.351 (n=2580)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=2913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=3031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.651` → IC=+0.337 (n=2886)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.651 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2208` → IC=+0.336 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2208 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.777` → IC=+0.339 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.777 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.6286` → IC=+0.323 (n=2886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6286 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.344 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.324 (n=2790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `3005.6232` → IC=+0.323 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3005.6232 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.330 (n=3126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=3137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` < `0.39` → IC=+0.328 (n=3124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.39 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `1.3077` → IC=+0.323 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3077 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` < `0.2594` → IC=+0.317 (n=3075)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2594 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.07` → IC=+0.326 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.07 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` < `0.636` → IC=+0.319 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.636 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.2104` → IC=+0.339 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2104 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.362 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` < `1.4149` → IC=+0.325 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4149 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `2.1535` → IC=+0.319 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1535 (IC base=+0.314)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.221 (n=6526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1273` → IC=+0.193 (n=8617)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1273 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=20367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.229 (n=19584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5357 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.206 (n=7406)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.260 (n=3831)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1745` → IC=+0.152 (n=13061)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1745 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6205` → IC=+0.151 (n=13062)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6205 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.208 (n=2825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6011` → IC=+0.185 (n=6359)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6011 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.192 (n=18535)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.194 (n=8633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0062 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.187 (n=13081)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0859` → IC=+0.223 (n=6541)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0859 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=9408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5263` → IC=+0.238 (n=19607)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5263 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1978` → IC=+0.181 (n=14290)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1978 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.398` → IC=+0.191 (n=3079)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.398 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.489` → IC=+0.193 (n=17539)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.489 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1891` → IC=+0.167 (n=13875)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1891 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.217 (n=2936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.5637` → IC=+0.186 (n=8257)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.5637 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6358` → IC=+0.197 (n=6255)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6358 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=18588)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.265 (n=1076)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.0757` → IC=+0.267 (n=1073)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0757 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=2183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `0.9425` → IC=+0.292 (n=2141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9425 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.47` → IC=+0.328 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.47 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.283 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.8308` → IC=+0.227 (n=2051)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8308 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.229 (n=3075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.254 (n=2729)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.253 (n=1237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.1017` → IC=+0.308 (n=1202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1017 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=2813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=2486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.0054` → IC=+0.308 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0054 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.946` → IC=+0.259 (n=2699)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.946 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.256 (n=2411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.264 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.5501` → IC=+0.268 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5501 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.6782` → IC=+0.254 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6782 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.260 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1932.1926` → IC=+0.253 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1932.1926 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.190 (n=1005)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0033 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0677` → IC=+0.174 (n=1001)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0677 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2499` → IC=+0.201 (n=2998)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2499 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1973` → IC=+0.211 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1973 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.547` → IC=+0.203 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.547 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8524` → IC=+0.132 (n=1999)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8524 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.0477` → IC=+0.129 (n=1359)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.0477 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.172 (n=456)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.129 (n=1299)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.455` → IC=+0.141 (n=984)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.455 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `385.0` → IC=+0.131 (n=2920)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 385.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.182 (n=2859)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0061 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.258` → IC=+0.176 (n=2858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.258 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.6128` → IC=+0.212 (n=3247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6128 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.2218` → IC=+0.177 (n=3521)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2218 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.919` → IC=+0.177 (n=595)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.919 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.022` → IC=+0.158 (n=2863)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.022 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.165 (n=3247)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2065 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.0967` → IC=+0.156 (n=2853)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0967 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.144` → IC=+0.160 (n=2745)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.144 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `203.0` → IC=+0.197 (n=1352)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 203.0 (IC base=+0.155)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.231 (n=1500)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2576` → IC=+0.234 (n=2205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2576 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.285 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.987` → IC=+0.305 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.987 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.232 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7121` → IC=+0.224 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7121 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2019.6184` → IC=+0.222 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2019.6184 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.243 (n=3003)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.2556` → IC=+0.266 (n=2002)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2556 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.274 (n=1138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0438` → IC=+0.291 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0438 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.736` → IC=+0.283 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.736 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.286 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.240 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1795` → IC=+0.251 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1795 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1882.5784` → IC=+0.246 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.5784 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.237 (n=2915)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.195 (n=1082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.004 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0823` → IC=+0.173 (n=1077)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0823 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2441` → IC=+0.189 (n=3229)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2441 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1491` → IC=+0.189 (n=1830)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1491 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.182` → IC=+0.202 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.182 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8368` → IC=+0.140 (n=2154)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8368 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.178 (n=486)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5168` → IC=+0.126 (n=1392)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5168 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5003` → IC=+0.138 (n=1054)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5003 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6913.8034` → IC=+0.198 (n=1464)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6913.8034 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.129 (n=3166)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 123.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.174 (n=2312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0057 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4319` → IC=+0.150 (n=3464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4319 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6685` → IC=+0.190 (n=3464)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6685 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1728` → IC=+0.158 (n=3545)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1728 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.531` → IC=+0.144 (n=1183)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 6.531 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.851` → IC=+0.153 (n=2310)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.851 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2376` → IC=+0.163 (n=714)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2376 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.1869` → IC=+0.136 (n=2905)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1869 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4092` → IC=+0.136 (n=3301)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4092 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `6679.7564` → IC=+0.192 (n=1571)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6679.7564 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.139 (n=3288)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 121.0 (IC base=+0.134)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.177 (n=1201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0131 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.205 (n=3611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7992` → IC=+0.213 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7992 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.93` → IC=+0.284 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.93 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1668` → IC=+0.131 (n=3603)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1668 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6243` → IC=+0.125 (n=3603)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6243 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.124 (n=3680)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.129 (n=502)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.544` → IC=+0.128 (n=1540)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.544 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2718.2425` → IC=+0.200 (n=1634)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2718.2425 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.128 (n=2316)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.153 (n=3335)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0112 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.170 (n=1264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=3866)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.222 (n=3789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.149 (n=3754)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.148 (n=3359)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.18` → IC=+0.131 (n=3788)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.18 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.8584` → IC=+0.126 (n=2527)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8584 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1642` → IC=+0.127 (n=3752)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1642 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.148 (n=530)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.143 (n=1201)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4415 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4632` → IC=+0.136 (n=1201)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4632 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2614.875` → IC=+0.191 (n=1717)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2614.875 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.133 (n=3614)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 43.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.249 (n=2888)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1692` → IC=+0.239 (n=1422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1692 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=3365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.255 (n=3233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1879` → IC=+0.233 (n=1994)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1879 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8391` → IC=+0.227 (n=3333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8391 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.438` → IC=+0.271 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.438 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6183` → IC=+0.234 (n=3232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6183 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.267 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.4964` → IC=+0.227 (n=3157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4964 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4368` → IC=+0.228 (n=3156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4368 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=4189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2627.1049` → IC=+0.230 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2627.1049 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0162` → IC=+0.247 (n=2252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0162 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6212` → IC=+0.250 (n=3376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6212 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0381` → IC=+0.296 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0381 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `1.1922` → IC=+0.250 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1922 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.997` → IC=+0.270 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.997 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.8647` → IC=+0.245 (n=2251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8647 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `1.0478` → IC=+0.241 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0478 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.300 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `2.5421` → IC=+0.236 (n=3205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5421 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.5572` → IC=+0.239 (n=2863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5572 (IC base=+0.239)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.204 (n=1723)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.145` → IC=+0.169 (n=2274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.145 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=5401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.6563` → IC=+0.222 (n=3445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6563 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9192` → IC=+0.178 (n=787)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9192 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.547` → IC=+0.208 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.547 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.163 (n=3142)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8553 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1873` → IC=+0.158 (n=1572)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1873 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1554` → IC=+0.170 (n=1329)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1554 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5268` → IC=+0.158 (n=2220)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5268 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.4192` → IC=+0.154 (n=5046)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4192 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=5675)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7204.9187` → IC=+0.193 (n=2343)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7204.9187 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.5905` → IC=+0.154 (n=4985)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5905 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.121 (n=5518)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 136.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.206 (n=1246)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.237 (n=416)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.229 (n=1126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.6215` → IC=+0.258 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6215 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.6873` → IC=+0.241 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6873 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.984` → IC=+0.220 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.984 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8697` → IC=+0.217 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8697 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0897` → IC=+0.215 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0897 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.1509` → IC=+0.209 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1509 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.4022` → IC=+0.199 (n=1223)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4022 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `13762.5784` → IC=+0.207 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13762.5784 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.149 (n=688)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2189` → IC=+0.188 (n=687)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.2189 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.141 (n=1019)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 234.0 (IC base=+0.069)

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
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0072 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.137 (n=1399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5333` → IC=+0.185 (n=1249)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.5333 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0502` → IC=+0.149 (n=249)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 1.0502 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.863` → IC=+0.226 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.863 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.0426` → IC=+0.128 (n=1229)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0426 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.222` → IC=+0.140 (n=237)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.222 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4172` → IC=+0.150 (n=453)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4172 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3056.5696` → IC=+0.150 (n=466)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3056.5696 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.167 (n=1362)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.5588 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2764.626` → IC=+0.164 (n=701)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2764.626 (IC base=+0.087)

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
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.228 (n=8637)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=27066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9659` → IC=+0.300 (n=8632)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9659 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9558` → IC=+0.218 (n=3005)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9558 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.878` → IC=+0.260 (n=6331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.878 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.160 (n=17468)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2129 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.216 (n=3399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6262` → IC=+0.194 (n=8440)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6262 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=24534)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.209 (n=8042)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.155` → IC=+0.203 (n=10621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.155 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=8999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5938` → IC=+0.246 (n=24127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5938 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.1931` → IC=+0.183 (n=15375)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1931 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.503` → IC=+0.206 (n=22500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.503 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.0526` → IC=+0.177 (n=14224)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0526 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.255 (n=3315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.6241` → IC=+0.211 (n=7742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6241 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.215 (n=23037)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.200)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3823` → IC=+0.236 (n=4123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3823 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2776)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8608` → IC=+0.294 (n=2749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8608 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.031` → IC=+0.302 (n=2710)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.031 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.288 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2808` → IC=+0.243 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2808 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2047.52` → IC=+0.240 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2047.52 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.267 (n=3791)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.265)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.267 (n=1718)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1287` → IC=+0.291 (n=1668)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1287 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=3939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.269 (n=3421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.4698` → IC=+0.287 (n=3335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4698 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.267 (n=3839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2914` → IC=+0.286 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2914 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5624` → IC=+0.267 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5624 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6397` → IC=+0.271 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6397 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.270 (n=2550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1934.2652` → IC=+0.267 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.2652 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.271 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.172 (n=1429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0034 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0839` → IC=+0.147 (n=1422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0839 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.189` → IC=+0.187 (n=4265)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.189 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.211 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.267` → IC=+0.171 (n=878)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.267 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6329` → IC=+0.157 (n=1423)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6329 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0665` → IC=+0.142 (n=1933)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0665 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.190 (n=597)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.144 (n=3692)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5213` → IC=+0.145 (n=3748)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5213 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `353.0` → IC=+0.149 (n=3651)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 353.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.171 (n=3328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0061 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.084` → IC=+0.173 (n=1260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.084 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6821` → IC=+0.192 (n=3778)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6821 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1557` → IC=+0.163 (n=3702)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1557 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.001` → IC=+0.148 (n=1780)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.001 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.205` → IC=+0.151 (n=3856)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.205 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.042` → IC=+0.158 (n=3325)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.042 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2219` → IC=+0.198 (n=687)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2219 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.432` → IC=+0.152 (n=3665)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.432 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7717` → IC=+0.154 (n=2443)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7717 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=4905)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.182 (n=1210)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 212.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.243 (n=1953)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.932` → IC=+0.315 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.932 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2042` → IC=+0.233 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2042 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7573` → IC=+0.242 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7573 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1906.3268` → IC=+0.238 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1906.3268 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.247 (n=1840)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1862` → IC=+0.259 (n=1837)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1862 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.069` → IC=+0.297 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.069 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.89` → IC=+0.303 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.89 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.299 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.1664` → IC=+0.256 (n=2695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1664 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2004.4248` → IC=+0.251 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.4248 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.247 (n=3982)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.244)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.191 (n=1496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3565` → IC=+0.148 (n=3941)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3565 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.877` → IC=+0.266 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.877 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1503` → IC=+0.170 (n=2219)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1503 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.0` → IC=+0.164 (n=1949)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.0 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.155 (n=2986)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8567 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.200 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.156 (n=1927)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1501` → IC=+0.145 (n=1985)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1501 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `5876.4965` → IC=+0.233 (n=2030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5876.4965 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.144 (n=2912)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 85.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.170 (n=3794)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4625` → IC=+0.161 (n=3793)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4625 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5712` → IC=+0.214 (n=3337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5712 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.6408` → IC=+0.159 (n=4388)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6408 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.065` → IC=+0.158 (n=759)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.065 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.044` → IC=+0.155 (n=3301)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.044 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.0398` → IC=+0.160 (n=3338)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0398 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.205 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4833` → IC=+0.157 (n=3676)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4833 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5223` → IC=+0.159 (n=3284)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.5223 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `6740.2044` → IC=+0.216 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6740.2044 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.162 (n=3286)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 114.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.157 (n=1525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0132 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.6957` → IC=+0.256 (n=3044)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6957 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.8146` → IC=+0.196 (n=1020)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8146 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.192` → IC=+0.268 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.192 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2095` → IC=+0.126 (n=4564)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2095 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1013` → IC=+0.123 (n=4348)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1013 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.141 (n=571)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `2.5005` → IC=+0.125 (n=4458)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5005 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2477.3162` → IC=+0.225 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2477.3162 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.160 (n=3746)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0113 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1433` → IC=+0.152 (n=1419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1433 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=2008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5403` → IC=+0.247 (n=3745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5403 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2279` → IC=+0.154 (n=3911)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2279 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.018` → IC=+0.162 (n=4135)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.018 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1927` → IC=+0.144 (n=4255)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1927 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2796` → IC=+0.203 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2796 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4388` → IC=+0.164 (n=1356)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4388 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4888` → IC=+0.145 (n=1355)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4888 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2654.6046` → IC=+0.222 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2654.6046 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.152 (n=4104)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.255 (n=4166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=4359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.240 (n=2791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.987` → IC=+0.302 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.987 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.2049` → IC=+0.251 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2049 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.962` → IC=+0.296 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.962 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2164` → IC=+0.236 (n=4164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2164 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.242 (n=4164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.0796` → IC=+0.254 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0796 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.516` → IC=+0.256 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.516 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=5375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2644.9749` → IC=+0.240 (n=2776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2644.9749 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0247` → IC=+0.272 (n=1447)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0247 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.251 (n=4086)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.1398` → IC=+0.307 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1398 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.1946` → IC=+0.251 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1946 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2328` → IC=+0.250 (n=4173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2328 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.936` → IC=+0.281 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.936 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.7123` → IC=+0.249 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7123 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.265 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.310 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4331` → IC=+0.249 (n=4126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4331 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.245 (n=2822)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.241 (n=2472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.5385` → IC=+0.232 (n=7395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5385 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=7429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9282` → IC=+0.258 (n=2465)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9282 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.9629` → IC=+0.227 (n=6033)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9629 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.427` → IC=+0.233 (n=2463)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.427 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.7072` → IC=+0.228 (n=2303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7072 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.8813` → IC=+0.226 (n=3489)

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

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.212 (n=2397)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4161` → IC=+0.222 (n=4648)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4161 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.225 (n=2375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.6132` → IC=+0.215 (n=4648)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6132 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7151` → IC=+0.219 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7151 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2565` → IC=+0.204 (n=4634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2565 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.702` → IC=+0.225 (n=4794)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.702 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.0965` → IC=+0.213 (n=4213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0965 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.215 (n=4881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5326` → IC=+0.216 (n=2289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5326 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8167` → IC=+0.218 (n=3467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8167 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.236 (n=3481)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3879` → IC=+0.186 (n=1546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3879 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.177 (n=580)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 5.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.191 (n=681)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.3612` → IC=+0.175 (n=333)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3612 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.5553` → IC=+0.172 (n=1852)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.5553 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.329` → IC=+0.194 (n=1519)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.329 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.185 (n=1360)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.091 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.186 (n=473)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.4957` → IC=+0.178 (n=1537)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.4957 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.175 (n=697)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1732 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `14611.4186` → IC=+0.173 (n=701)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 14611.4186 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.188 (n=1502)

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

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.244 (n=548)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.5101` → IC=+0.221 (n=1642)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5101 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.0844` → IC=+0.213 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0844 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.7294` → IC=+0.223 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7294 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.255` → IC=+0.211 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.255 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.6375` → IC=+0.222 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6375 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.7185` → IC=+0.210 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7185 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.226 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1647` → IC=+0.208 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1647 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7743` → IC=+0.211 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7743 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `7946.6096` → IC=+0.215 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7946.6096 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.211 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.207)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.229 (n=864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.225 (n=431)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.299 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `1.1012` → IC=+0.244 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1012 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.269 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.246 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.219 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.238 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `2.4968` → IC=+0.225 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4968 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3372.142` → IC=+0.242 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3372.142 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.222 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0141` → IC=+0.247 (n=970)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0141 (IC base=+0.247)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.254 (n=648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.247)

- **PATRÓN** `drift_60min` |x|≤ `0.6907` → IC=+0.260 (n=970)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6907 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.268 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` < `0.6479` → IC=+0.273 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6479 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.988` → IC=+0.267 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.988 (IC base=+0.247)

- **PATRÓN** `volumen_regimen` < `0.7517` → IC=+0.262 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7517 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.259 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` > `1.8448` → IC=+0.263 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8448 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `4016.482` → IC=+0.270 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4016.482 (IC base=+0.247)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.277 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.247)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.144 (n=929)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0042 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.417` → IC=+0.132 (n=2685)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.417 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1587` → IC=+0.155 (n=1268)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1587 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.138 (n=580)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.5843` → IC=+0.178 (n=2108)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5843 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.544` → IC=+0.129 (n=930)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.544 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.184 (n=590)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.095)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5478` → IC=-0.121 (n=341)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5478
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=695)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.180 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0029 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.5478` → IC=+0.157 (n=695)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5478 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.166 (n=363)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.065)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.127 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0037 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.250 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.143 (n=315)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.056)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5264` → IC=-0.121 (n=354)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5264
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=720)

- **FILTRO** `ibs_20min` > `0.4948` → IC=-0.129 (n=265)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4948
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=515)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.154 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0043 (IC base=+0.062)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.120 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.5264` → IC=+0.157 (n=720)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.5264 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.135` → IC=+0.153 (n=387)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.135 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.957` → IC=+0.169 (n=176)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.957 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.281 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=+0.045)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.144 (n=610)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.72 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.7653` → IC=+0.158 (n=223)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.7653 (IC base=+0.036)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.177 (n=410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0103 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.196 (n=586)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` < `0.2242` → IC=+0.155 (n=578)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2242 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.904` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.904 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `1.1084` → IC=+0.180 (n=195)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.1084 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.188 (n=152)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `2.193` → IC=+0.128 (n=487)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.193 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `1.8607` → IC=+0.144 (n=369)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8607 (IC base=+0.101)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.377 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.2739` → IC=+0.328 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2739 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.6242` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6242 (IC base=+0.307)

- **PATRÓN** `dist_vwap_pct` > `0.4912` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4912 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.192` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.192 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` < `0.9978` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9978 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` > `0.6039` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6039 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.0555` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0555 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` < `2.5614` → IC=+0.355 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5614 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.307)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.389 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.340)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.338 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.382 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.340)

- **PATRÓN** `ibs_20min` < `0.1183` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1183 (IC base=+0.340)

- **PATRÓN** `ibs_20min` > `0.4562` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4562 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.59` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.59 (IC base=+0.340)

- **PATRÓN** `volumen_regimen` > `0.6112` → IC=+0.382 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6112 (IC base=+0.340)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.340)

- **PATRÓN** `volumen_spike_ratio` < `1.501` → IC=+0.382 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.501 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.378 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `46.39` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 46.39 (IC base=+0.340)

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
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1016)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.249 (n=397)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.205 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.8933` → IC=+0.308 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8933 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.629` → IC=+0.193 (n=382)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.629 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6243` → IC=+0.194 (n=289)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6243 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.1982` → IC=+0.173 (n=289)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1982 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` < `0.0673` → IC=+0.193 (n=662)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0673 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.202 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.166)

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

- **FILTRO** `dist_vwap_pct` > `0.1978` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1978
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=187)

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
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1537)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `liq_n` > 2.0 (IC base=+0.095)

- **PATRÓN** `liq_usd_total` > `110.72` → IC=+0.126 (n=177)

  - _Acción_: Kelly boost +0.63€ cuando `liq_usd_total` > 110.72 (IC base=+0.095)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.095)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.5 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.095)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4268)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1678)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1632)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=767)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=776)

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
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1574)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1574)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.130 (n=3652)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=9433)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.145 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=145)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=90)

- **FILTRO** `restante_min` < `3.99` → IC=-0.122 (n=72)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=74)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.163 (n=440)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1055)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.141 (n=349)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=946)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.143 (n=449)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.51 (IC base=-0.007)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.129 (n=203)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=470)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.122 (n=347)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=701)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=746)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=795)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.140 (n=365)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=790)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.129 (n=574)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=721)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=600)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=637)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.133 (n=651)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=756)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9282)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=28985)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=9653)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=29909)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4213)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3381)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4333)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=960)

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
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=58708)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20612)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=63999)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27815)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=56796)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.154 (n=28656)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=55955)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26208)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=79575)

- **FILTRO** `ibs_7min` > `0.2782` → IC=-0.183 (n=26442)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2782
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=79341)

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
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=10672)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3434)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10620)

- **FILTRO** `ibs_7min` < `0.7112` → IC=-0.214 (n=3510)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7112
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10544)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.205 (n=3502)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10552)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=3278)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=11109)

- **FILTRO** `ibs_7min` > `0.2635` → IC=-0.189 (n=3594)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2635
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10793)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.177 (n=3590)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10797)

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
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=9231)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=3126)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10605)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.202 (n=3430)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10301)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.199 (n=3408)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=10323)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=3323)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=10938)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.178 (n=3562)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=10699)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.171 (n=3511)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10750)

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

- **FILTRO** `py_entrada` > `0.545` → IC=-0.161 (n=184)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=682)

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
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=557)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.144 (n=774)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `458.564` → IC=+0.166 (n=570)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 458.564 (IC base=+0.124)

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
- **PATRÓN** `delta_ratio` |x|> `0.3984` → IC=+0.136 (n=358)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3984 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=436)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.118)

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
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4315 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.164 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `4782.684` → IC=+0.180 (n=195)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4782.684 (IC base=+0.131)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.129 (n=313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 13.0 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=218)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `4.4533` → IC=-0.202 (n=129)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4533
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=131)

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
- **FILTRO** `T_h` > `76.1623` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `T_h` > 76.1623
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

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
- **FILTRO** `T_h` < `130.5499` → IC=-0.254 (n=652)

  - _Acción_: SKIP cuando `T_h` < 130.5499
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=218)

- **FILTRO** `sigma_h` < `0.0081` → IC=-0.159 (n=414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=415)

- **FILTRO** `T_h` < `102.7869` → IC=-0.151 (n=414)

  - _Acción_: SKIP cuando `T_h` < 102.7869
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=415)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `49.2927` → IC=-0.239 (n=213)

  - _Acción_: SKIP cuando `T_h` > 49.2927
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=73)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1111)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1358)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5581)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3377)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.184 (n=2194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.2333` → IC=+0.158 (n=6583)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2333 (IC base=+0.131)

- **PATRÓN** `drift_15min` |x|≤ `1.124` → IC=+0.133 (n=6582)

  - _Acción_: Kelly boost +0.66€ cuando `drift_15min` |x|≤ 1.124 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.132 (n=6582)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.131)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0999` → IC=+0.143 (n=2075)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0999 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6093)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.5532` → IC=+0.207 (n=5879)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5532 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.99` → IC=+0.230 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.99 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3448)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4309.2693` → IC=+0.170 (n=2194)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4309.2693 (IC base=+0.131)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2540)

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
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.148 (n=1002)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0067 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.146 (n=759)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.137 (n=1017)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.4811` → IC=+0.217 (n=1138)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4811 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1241` → IC=+0.147 (n=715)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1241 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.133 (n=1291)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.945` → IC=+0.286 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.945 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6122.7931` → IC=+0.176 (n=516)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 6122.7931 (IC base=+0.133)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8333` → IC=+0.147 (n=695)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` > 0.8333 (IC base=+0.045)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.143 (n=1669)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0119 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2399` → IC=+0.174 (n=1669)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2399 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0582` → IC=+0.140 (n=1669)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0582 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.184 (n=523)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.142 (n=1525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.141 (n=1470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.6981` → IC=+0.232 (n=1113)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6981 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.215` → IC=+0.145 (n=764)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.215 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.9054` → IC=+0.140 (n=1924)

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

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.378 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7881` → IC=+0.394 (n=816)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7881 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2713` → IC=+0.383 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2713 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.84` → IC=+0.397 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.84 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=993)

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
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.362 (n=426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.377 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.367 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1258` → IC=+0.378 (n=284)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1258 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.105` → IC=+0.374 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.105 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.379 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.397 (n=426)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.377 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.6907` → IC=+0.363 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6907 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.857` → IC=+0.399 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.857 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2710)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3415)

- **FILTRO** `libro_liquidez` < `4391.961` → IC=-0.172 (n=4042)

  - _Acción_: SKIP cuando `libro_liquidez` < 4391.961
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=2083)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.278 (n=1345)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` > `0.117` → IC=+0.209 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.117 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` < `0.602` → IC=+0.198 (n=1424)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.602 (IC base=-0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.228` → IC=+0.267 (n=2012)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.228 (IC base=+0.002)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.282 (n=6039)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.7088` → IC=+0.264 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7088 (IC base=+0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0741` → IC=-0.238 (n=2016)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0741
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=2019)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.209 (n=1008)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3027)

- **FILTRO** `sigma_ewma_delta_pct` > `22.231` → IC=-0.239 (n=570)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.231
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=3465)

- **FILTRO** `libro_liquidez` < `10164.669` → IC=-0.193 (n=1331)

  - _Acción_: SKIP cuando `libro_liquidez` < 10164.669
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2704)

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
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=887)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.162 (n=679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0067 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.174 (n=299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2988` → IC=+0.184 (n=536)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2988 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5657` → IC=+0.241 (n=678)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5657 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6788` → IC=+0.181 (n=133)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6788 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.258 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=887)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5211.9622` → IC=+0.170 (n=452)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5211.9622 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.255 (n=1038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.4821` → IC=+0.242 (n=2359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4821 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `0.8255` → IC=+0.248 (n=2076)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8255 (IC base=+0.236)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1983` → IC=+0.256 (n=1070)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1983 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.239 (n=1613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.236)

- **PATRÓN** `ibs_15` < `0.3923` → IC=+0.268 (n=2359)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3923 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.2378` → IC=+0.245 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2378 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.514` → IC=+0.241 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.514 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.307` → IC=+0.239 (n=2481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.307 (IC base=+0.236)

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
- **FILTRO** `sigma_h` > `0.0143` → IC=-0.250 (n=1150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0143
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=567)

- **FILTRO** `drift_60min` |x|> `0.1231` → IC=-0.244 (n=583)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1231
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=1134)

- **FILTRO** `drift_15min` |x|> `1.2992` → IC=-0.284 (n=429)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2992
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=1288)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1696)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.283 (n=1250)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=-0.008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.287 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3297` → IC=+0.292 (n=1398)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3297 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.325 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=-0.008)

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

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2171` → IC=+0.288 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2171 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8361` → IC=+0.310 (n=1495)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8361 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2762` → IC=+0.316 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2762 (IC base=+0.284)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.324 (n=237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.293 (n=708)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.308 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.289 (n=354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8448` → IC=+0.314 (n=708)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8448 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.315 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2918 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.914` → IC=+0.381 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.914 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1089` → IC=-0.161 (n=234)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1089
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=116)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.145 (n=240)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=120)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.162 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=384)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.198 (n=124)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=127)

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
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0653` → IC=-0.257 (n=35)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0653
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=33)

- **FILTRO** `drift_15min` |x|> `0.5336` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5336
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=44)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5532 sube el IC de +0.131 a +0.207 en UPDOWN_GBM#15min (n=5879). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7031 sube el IC de +0.206 a +0.274 en UPDOWN_GBM#BTC#15min (n=888). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4811 sube el IC de +0.133 a +0.217 en UPDOWN_GBM#ETH#15min (n=1138). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.6981 sube el IC de +0.136 a +0.232 en UPDOWN_GBM#XRP#15min (n=1113). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6288 sube el IC de -0.088 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1345). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.002 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=6039). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.064 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=483). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.180 a +0.291 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5657 sube el IC de +0.147 a +0.241 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=678). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3923 sube el IC de +0.236 a +0.268 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2359). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.026 a +0.298 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=997). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3297 sube el IC de -0.008 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1398). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.081 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7 (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.081 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8361 sube el IC de +0.284 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1495). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8568 sube el IC de +0.279 a +0.307 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=702). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8448 sube el IC de +0.290 a +0.314 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=708). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7881 sube el IC de +0.363 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=816). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.362 a +0.383 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.363 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=426). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2358 | +0.084 | +256.34€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2358 | +0.084 | +256.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1946 | +0.085 | +216.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1946 | +0.085 | +216.85€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1492 | -0.028 | +54.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1492 | -0.028 | +54.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1168 | -0.040 | +42.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1168 | -0.040 | +42.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51514 | -0.087 | -6589.66€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3380 | +0.096 | -317.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48134 | -0.099 | -6272.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3380 | +0.096 | -317.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3380 | +0.096 | -317.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14345 | -0.044 | -1327.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14345 | -0.044 | -1327.71€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 57145 | -0.012 | +2616.57€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14741 | +0.003 | +1467.55€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 42404 | -0.017 | +1149.02€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 57145 | -0.012 | +2616.57€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14741 | +0.003 | +1467.55€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 42404 | -0.017 | +1149.02€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 212921 | +0.112 | -8693.01€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23449 | +0.179 | -745.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 995 | +0.021 | -79.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 176392 | +0.105 | -7471.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12085 | +0.095 | -395.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 29249 | +0.101 | -2101.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 87 | -0.197 | +9.66€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 29125 | +0.102 | -2120.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 39863 | +0.123 | -624.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5719 | +0.177 | -225.17€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 29200 | +0.119 | -217.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4902 | +0.081 | -158.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 29295 | +0.098 | -2054.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 106 | -0.102 | +22.72€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 29162 | +0.099 | -2071.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 12 | -0.043 | +5.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 45569 | +0.123 | -963.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11342 | +0.178 | -323.63€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 29669 | +0.106 | -547.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4546 | +0.103 | -83.81€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 39683 | +0.111 | -1671.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6095 | +0.200 | -242.31€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 898 | +0.044 | -25.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 30090 | +0.096 | -1220.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2600 | +0.108 | -182.15€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 29262 | +0.106 | -1278.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 100 | -0.137 | +13.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 29146 | +0.107 | -1293.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 34699 | +0.188 | -2636.10€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 34699 | +0.188 | -2636.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7867 | +0.160 | -946.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7867 | +0.160 | -946.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5216 | +0.194 | -224.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5216 | +0.194 | -224.78€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7669 | +0.171 | -715.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7669 | +0.171 | -715.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6351 | +0.252 | -219.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6351 | +0.252 | -219.20€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7517 | +0.182 | -543.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7517 | +0.182 | -543.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1338 | +0.425 | -49.83€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1338 | +0.425 | -49.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 571 | +0.439 | -5.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 571 | +0.439 | -5.35€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 225 | +0.403 | -16.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 225 | +0.403 | -16.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 122666 | +0.199 | -8992.20€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 122666 | +0.199 | -8992.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21269 | +0.175 | -2522.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21269 | +0.175 | -2522.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19764 | +0.223 | -659.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19764 | +0.223 | -659.95€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21037 | +0.180 | -2214.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21037 | +0.180 | -2214.78€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19947 | +0.217 | -784.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19947 | +0.217 | -784.49€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20231 | +0.205 | -1185.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20231 | +0.205 | -1185.88€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20418 | +0.196 | -1624.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20418 | +0.196 | -1624.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 47698 | +0.117 | +414.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 47698 | +0.117 | +414.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 23750 | +0.117 | +266.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 23750 | +0.117 | +266.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 23948 | +0.116 | +148.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 23948 | +0.116 | +148.28€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 97507 | +0.101 | -2044.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7914 | +0.097 | +191.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 89593 | +0.101 | -2235.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 53211 | +0.105 | -434.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7914 | +0.097 | +191.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 45297 | +0.106 | -625.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 20976 | +0.110 | -75.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 20976 | +0.110 | -75.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 23320 | +0.083 | -1534.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 23320 | +0.083 | -1534.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 920 | +0.185 | -105.50€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 920 | +0.185 | -105.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 920 | +0.185 | -105.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 920 | +0.185 | -105.50€ | 1 | 4 |
| ✅ GBM_LATE_15M | 66429 | +0.103 | +37528.04€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 66429 | +0.103 | +37528.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11031 | +0.225 | +9489.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11031 | +0.225 | +9489.97€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 10386 | +0.177 | +8414.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10386 | +0.177 | +8414.66€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 11883 | +0.207 | +9385.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11883 | +0.207 | +9385.35€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8780 | +0.063 | +3010.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8780 | +0.063 | +3010.85€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 9201 | -0.025 | +2385.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9201 | -0.025 | +2385.55€ | 3 | 15 |
| ✅ GBM_LATE_15M#XRP | 15148 | -0.019 | +4841.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15148 | -0.019 | +4841.66€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 70505 | +0.088 | +41329.59€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 70505 | +0.088 | +41329.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13691 | -0.002 | +7167.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13691 | -0.002 | +7167.17€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15163 | +0.007 | +4207.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15163 | +0.007 | +4207.34€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9442 | +0.296 | +10850.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9442 | +0.296 | +10850.98€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13481 | +0.019 | +4331.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13481 | +0.019 | +4331.89€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10717 | +0.051 | +5023.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10717 | +0.051 | +5023.41€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8011 | +0.313 | +9748.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8011 | +0.313 | +9748.81€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 52240 | +0.180 | +43564.62€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 52240 | +0.180 | +43564.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7919 | +0.240 | +7387.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7919 | +0.240 | +7387.73€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8326 | +0.141 | +6290.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8326 | +0.141 | +6290.80€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8409 | +0.224 | +7276.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8409 | +0.224 | +7276.33€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8923 | +0.131 | +7016.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8923 | +0.131 | +7016.56€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9853 | +0.124 | +7650.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9853 | +0.124 | +7650.05€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8810 | +0.232 | +7943.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8810 | +0.232 | +7943.14€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14441 | +0.127 | +7392.96€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14441 | +0.127 | +7392.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3740 | +0.126 | +2027.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3740 | +0.126 | +2027.20€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4236 | +0.127 | +2145.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4236 | +0.127 | +2145.57€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3923 | +0.102 | +1629.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3923 | +0.102 | +1629.38€ | 0 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1355 | +0.168 | +858.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1355 | +0.168 | +858.78€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 66695 | +0.190 | +55748.08€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 66695 | +0.190 | +55748.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10549 | +0.250 | +10179.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10549 | +0.250 | +10179.20€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10720 | +0.143 | +7847.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10720 | +0.143 | +7847.28€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11306 | +0.234 | +10194.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11306 | +0.234 | +10194.73€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11026 | +0.146 | +8367.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11026 | +0.146 | +8367.04€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11757 | +0.129 | +8628.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11757 | +0.129 | +8628.46€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11337 | +0.241 | +10531.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11337 | +0.241 | +10531.38€ | 0 | 23 |
| ✅ GBM_LATE_5M | 16900 | +0.219 | +14276.87€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 16900 | +0.219 | +14276.87€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3332 | +0.210 | +2853.06€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3332 | +0.210 | +2853.06€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1591 | +0.218 | +1323.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1591 | +0.218 | +1323.18€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4886 | +0.210 | +3851.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4886 | +0.210 | +3851.14€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 3015 | +0.230 | +2682.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3015 | +0.230 | +2682.39€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 2128 | +0.208 | +1668.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2128 | +0.208 | +1668.37€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6613 | +0.080 | +2275.33€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 6613 | +0.080 | +2275.33€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 184 | +0.269 | +201.17€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 184 | +0.269 | +201.17€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2069 | +0.061 | +621.85€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2069 | +0.061 | +621.85€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 178 | +0.322 | +222.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 178 | +0.322 | +222.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1924 | +0.055 | +592.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1924 | +0.055 | +592.02€ | 2 | 6 |
| ✅ GBM_LATE_60M#SOL | 2079 | +0.061 | +418.92€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2079 | +0.061 | +418.92€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 179 | +0.329 | +219.20€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 179 | +0.329 | +219.20€ | 0 | 22 |
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
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2521 | +0.089 | +668.75€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2521 | +0.089 | +668.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 927 | +0.070 | +237.53€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 927 | +0.070 | +237.53€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 23 | +0.180 | +14.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 23 | +0.180 | +14.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 832 | +0.053 | +160.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 832 | +0.053 | +160.11€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 672 | +0.151 | +239.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 672 | +0.151 | +239.06€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 67 | +0.123 | +18.04€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 67 | +0.123 | +18.04€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 425 | +0.306 | +505.51€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 425 | +0.306 | +505.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 425 | +0.306 | +505.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 425 | +0.306 | +505.51€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4976 | +0.095 | +1080.99€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4976 | +0.095 | +1080.99€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4976 | +0.095 | +1080.99€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4976 | +0.095 | +1080.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1865 | +0.021 | +110.14€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1865 | +0.021 | +110.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 236 | +0.092 | +48.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 236 | +0.092 | +48.42€ | 0 | 5 |
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
| ✅ LIQUIDACIONES_5M | 4628 | +0.019 | +211.25€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4628 | +0.019 | +211.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 867 | +0.015 | +49.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 867 | +0.015 | +49.10€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 352 | +0.073 | +99.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 352 | +0.073 | +99.32€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1730 | +0.023 | +37.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1730 | +0.023 | +37.76€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 817 | +0.015 | +6.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 817 | +0.015 | +6.44€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 621 | -0.006 | +24.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 621 | -0.006 | +24.80€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2836 | -0.035 | -10.98€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2836 | -0.035 | -10.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 862 | -0.039 | -18.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 862 | -0.039 | -18.92€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1025 | -0.015 | +19.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1025 | -0.015 | +19.40€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 924 | -0.055 | -11.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 924 | -0.055 | -11.31€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 20 | +0.045 | +0.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 20 | +0.045 | +0.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 21563 | -0.032 | -218.02€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10451 | -0.032 | -106.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11112 | -0.032 | -111.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 761 | -0.053 | -41.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 390 | -0.041 | -9.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 371 | -0.066 | -31.90€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5814 | -0.025 | -14.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2771 | -0.022 | +10.76€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3043 | -0.028 | -24.91€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1964 | -0.034 | -12.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1007 | -0.039 | -22.52€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 957 | -0.029 | +10.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4948 | -0.032 | -59.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2382 | -0.029 | -13.37€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2566 | -0.035 | -45.64€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4101 | -0.025 | +35.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2000 | -0.029 | +2.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2101 | -0.023 | +32.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3975 | -0.045 | -126.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1901 | -0.049 | -74.20€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2074 | -0.041 | -52.30€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 77829 | -0.000 | +4193.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 77829 | -0.000 | +4193.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10855 | -0.038 | -152.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10855 | -0.038 | -152.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10840 | -0.053 | -276.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10840 | -0.053 | -276.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7503 | -0.052 | -105.78€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7503 | -0.052 | -105.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2162 | -0.058 | -19.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2162 | -0.058 | -19.55€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 821 | -0.116 | -32.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 821 | -0.116 | -32.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2277 | -0.065 | -10.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2277 | -0.065 | -10.57€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 190394 | -0.078 | +2127.33€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 190394 | -0.078 | +2127.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 28441 | -0.102 | -1432.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 28441 | -0.102 | -1432.95€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 27992 | -0.101 | -998.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 27992 | -0.101 | -998.84€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9397 | -0.035 | -185.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9397 | -0.035 | -185.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1012 | -0.017 | -19.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1012 | -0.017 | -19.26€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2206 | -0.046 | -28.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2206 | -0.046 | -28.90€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2682 | -0.024 | -31.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2682 | -0.024 | -31.64€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1316 | -0.063 | -30.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1316 | -0.063 | -30.57€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1172 | -0.039 | -43.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1172 | -0.039 | -43.46€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2412 | +0.120 | +972.48€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2276 | +0.124 | +959.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 524 | +0.144 | +278.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 524 | +0.144 | +278.06€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 477 | +0.118 | +169.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 477 | +0.118 | +169.93€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 415 | +0.128 | +191.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 415 | +0.128 | +191.95€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 388 | +0.131 | +183.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 388 | +0.131 | +183.68€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 472 | +0.097 | +136.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 472 | +0.097 | +136.26€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2540 | -0.023 | -51.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2540 | -0.023 | -51.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 447 | +0.006 | +20.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 447 | +0.006 | +20.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 463 | -0.051 | -33.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 463 | -0.051 | -33.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 613 | -0.045 | -43.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 613 | -0.045 | -43.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 529 | -0.007 | -2.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 529 | -0.007 | -2.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 488 | -0.012 | +8.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 488 | -0.012 | +8.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1346 | -0.043 | +134.81€ | 1 | 1 |
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
| ✅ PRICE_TARGET_GBM_FADE | 1699 | -0.185 | -35.36€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 672 | -0.172 | -8.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 593 | -0.171 | -5.74€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 79 | -0.179 | -3.17€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 571 | -0.198 | -32.97€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 502 | -0.204 | -38.08€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 69 | -0.148 | +5.11€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 456 | -0.186 | +6.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 422 | -0.182 | +3.38€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 34 | -0.222 | +3.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1517 | -0.185 | -40.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 182 | -0.179 | +5.08€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 600 | +0.377 | +538.69€ | 0 | 10 |
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
| ✅ STREAK_FADE_5M | 3664 | -0.023 | -143.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3664 | -0.023 | -143.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1129 | -0.022 | -40.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1129 | -0.022 | -40.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 631 | -0.028 | -26.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 631 | -0.028 | -26.87€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 178 | -0.050 | -16.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 178 | -0.050 | -16.31€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1726 | -0.018 | -59.95€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1726 | -0.018 | -59.95€ | 1 | 0 |
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
| ✅ STREAK_MOM_5M | 11716 | +0.013 | +62.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11716 | +0.013 | +62.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3010 | +0.017 | +20.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3010 | +0.017 | +20.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3130 | +0.013 | +25.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3130 | +0.013 | +25.17€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2954 | +0.009 | -2.25€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2954 | +0.009 | -2.25€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2622 | +0.014 | +18.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2622 | +0.014 | +18.81€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13980 | +0.019 | +7.54€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13980 | +0.019 | +7.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5600 | +0.021 | +5.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5600 | +0.021 | +5.80€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4969 | +0.019 | +4.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4969 | +0.019 | +4.13€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3411 | +0.015 | -2.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3411 | +0.015 | -2.40€ | 1 | 0 |
| ✅ UPDOWN_GBM | 126335 | +0.060 | +12079.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 31569 | +0.077 | +6173.44€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3584 | -0.001 | +40.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 83245 | +0.062 | +5737.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7507 | -0.002 | +130.81€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11047 | +0.104 | +2048.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2093 | +0.165 | +981.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8864 | +0.090 | +1069.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 28557 | +0.057 | +2524.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4231 | +0.081 | +953.87€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1056 | +0.000 | +21.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19718 | +0.066 | +1461.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3398 | -0.004 | +83.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 154 | -0.064 | +4.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14142 | +0.074 | +1570.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11972 | +0.061 | +677.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 29597 | +0.049 | +2111.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7312 | +0.070 | +1144.07€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1020 | +0.005 | +15.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18336 | +0.052 | +909.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2785 | -0.002 | +40.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 144 | -0.096 | +2.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26108 | +0.041 | +1500.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8535 | +0.032 | +476.23€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 935 | -0.011 | +7.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15201 | +0.054 | +1017.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1307 | +0.003 | +7.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 130 | -0.136 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16882 | +0.073 | +2325.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7314 | +0.088 | +1724.59€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9154 | +0.064 | +602.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 17 | +0.022 | +0.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 428 | -0.098 | -0.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1087 | +0.363 | +414.35€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1087 | +0.363 | +414.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 520 | +0.362 | +186.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 520 | +0.362 | +186.53€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 567 | +0.363 | +227.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 567 | +0.363 | +227.82€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 29911 | -0.016 | +7543.08€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 29911 | -0.016 | +7543.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2352 | -0.044 | +634.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2352 | -0.044 | +634.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5513 | -0.115 | +335.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5513 | -0.115 | +335.77€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4049 | +0.216 | +2548.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4049 | +0.216 | +2548.24€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8396 | -0.057 | +1270.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8396 | -0.057 | +1270.63€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8307 | -0.052 | +1690.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8307 | -0.052 | +1690.66€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 377 | +0.059 | +31.96€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 377 | +0.059 | +31.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 377 | +0.059 | +31.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 377 | +0.059 | +31.96€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1991 | +0.284 | +1701.60€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1991 | +0.284 | +1701.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1047 | +0.279 | +846.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1047 | +0.279 | +846.28€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 944 | +0.290 | +855.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 944 | +0.290 | +855.32€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 904 | -0.120 | -94.81€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 904 | -0.120 | -94.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 290 | -0.086 | -23.04€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 290 | -0.086 | -23.04€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 126 | -0.195 | -7.59€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 126 | -0.195 | -7.59€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5424 | +0.291 | +2360.42€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2122 | +0.247 | +323.50€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2098 | +0.284 | +868.54€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1204 | +0.381 | +1168.38€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.034) — sin ventaja clara. oversold(IBS<0.3): IC=+0.072 n=44533 | neutral: IC=+0.063 n=47246 | overbought(IBS>0.7): IC=+0.097 n=42548
  - _Datos_: n=139560 IC=+0.078 PNL=+21227.63€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 855 celda(s) pasan gate riguroso completo de 3082 evaluadas (n>=40) y 4193 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=8535 IC=+0.032 PNL=+476.23€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=2098/15 IC=+0.284 PNL=+868.54€ | BTC: n=2122/15 IC=+0.247 PNL=+323.50€ | SOL: n=1204/15 IC=+0.381 PNL=+1168.38€

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
  - _Estado_: 126273 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.137 n=1175/60 | contraria IC=+0.184 n=1240 | gap=-0.047 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=656, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 388 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2785/40 IC=-0.002 PNL=+40.39€ | BTC#60min: n=3398/40 IC=-0.004 PNL=+83.12€ | SOL#60min: n=1307/40 IC=+0.003 PNL=+7.02€ | XRP#60min: n=17/40 IC=+0.022 PNL=+0.29€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=842300 | tras_1loss IC=+0.103 n=636964 | tras_2loss IC=+0.074 n=252853/40 | gap=-0.030 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.039 n=18861 | contrario_BTC IC=+0.058 n=16625/40 | gap=+0.018 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=1297 PNL=+733.40€
  - _Datos_: n=1297 IC=+0.150 PNL=+733.40€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.08 con n=1522 PNL=+674.27€
  - _Datos_: n=1522 IC=+0.123 PNL=+674.27€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=93 PNL=+33.51€
  - _Datos_: n=93 IC=+0.111 PNL=+33.51€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.331 > 0.1 con n=4445 PNL=+2503.50€
  - _Datos_: n=4445 IC=+0.331 PNL=+2503.50€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1268 IC=+0.065 PNL=+127.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1268 IC=+0.065 PNL=+127.85€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=121 IC=+0.159 PNL=+69.74€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=121 IC=+0.159 PNL=+69.74€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=122265 IC=+0.060 PNL=+11778.40€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=122265 IC=+0.060 PNL=+11778.40€

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
  - _Estado_: n=4913 IC=-0.009 PNL=-63.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4913 IC=-0.009 PNL=-63.84€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2594 IC=+0.011 PNL=+194.65€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2594 IC=+0.011 PNL=+194.65€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1534 IC=+0.025 PNL=+73.13€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1534 IC=+0.025 PNL=+73.13€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.1 con n=8774 PNL=+4135.19€
  - _Datos_: n=8774 IC=+0.131 PNL=+4135.19€

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
  - _Estado_: n=4231 IC=+0.081 PNL=+953.87€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=4231 IC=+0.081 PNL=+953.87€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.092 > 0.08 con n=18219 PNL=+4481.45€
  - _Datos_: n=18219 IC=+0.092 PNL=+4481.45€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=875 IC=-0.188 PNL=+55.72€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=875 IC=-0.188 PNL=+55.72€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=835 IC=-0.008 PNL=+3.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=835 IC=-0.008 PNL=+3.81€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=1722 IC=+0.042 PNL=+140.19€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1722 IC=+0.042 PNL=+140.19€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=214 IC=-0.023 PNL=-5.78€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=214 IC=-0.023 PNL=-5.78€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=14899 IC=+0.046 PNL=+851.47€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=14899 IC=+0.046 PNL=+851.47€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.306 n=425) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=425 IC=+0.306 PNL=+505.51€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=21025 IC=+0.057 PNL=+1900.42€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=21025 IC=+0.057 PNL=+1900.42€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=8385 IC=+0.057 PNL=+1153.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8385 IC=+0.057 PNL=+1153.13€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=852 PNL=+285.31€
  - _Datos_: n=852 IC=+0.111 PNL=+285.31€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.08 con n=2295 PNL=+534.49€
  - _Datos_: n=2295 IC=+0.106 PNL=+534.49€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=1852 PNL=+694.15€
  - _Datos_: n=1852 IC=+0.083 PNL=+694.15€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=109944 IC=+0.129 PNL=+46296.55€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=109944 IC=+0.129 PNL=+46296.55€

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
  - _Estado_: n=19945 IC=+0.062 PNL=+2063.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=19945 IC=+0.062 PNL=+2063.51€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=1409 PNL=+562.21€
  - _Datos_: n=1409 IC=+0.117 PNL=+562.21€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.444 > 0.1 con n=2382 PNL=+2131.36€
  - _Datos_: n=2382 IC=+0.444 PNL=+2131.36€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=51940 IC=+0.069 PNL=+6956.13€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=51940 IC=+0.069 PNL=+6956.13€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.197 > 0.1 con n=10167 PNL=+5862.85€
  - _Datos_: n=10167 IC=+0.197 PNL=+5862.85€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.121 < -0.1 con n=861 PNL=+150.00€
  - _Datos_: n=861 IC=-0.121 PNL=+150.00€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=5089 IC=+0.067 PNL=+601.33€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=5089 IC=+0.067 PNL=+601.33€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=218 IC=-0.096 PNL=+1.67€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=218 IC=-0.096 PNL=+1.67€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1363 IC=+0.099 PNL=+328.59€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1363 IC=+0.099 PNL=+328.59€

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
  - _Estado_: n=50396 IC=-0.137 PNL=+3195.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=50396 IC=-0.137 PNL=+3195.35€

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
  - _Estado_: n=5438 IC=+0.136 PNL=+3855.03€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5438 IC=+0.136 PNL=+3855.03€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=6184 PNL=+4346.60€
  - _Datos_: n=6184 IC=+0.191 PNL=+4346.60€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=13181 IC=+0.057 PNL=+1151.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13181 IC=+0.057 PNL=+1151.35€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=5481 PNL=+3116.80€
  - _Datos_: n=5481 IC=+0.103 PNL=+3116.80€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.08 con n=1181 PNL=+693.68€
  - _Datos_: n=1181 IC=+0.206 PNL=+693.68€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=5511 PNL=-442.08€
  - _Datos_: n=5511 IC=-0.220 PNL=-442.08€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.223 > 0.2 con n=13849 PNL=+11498.58€
  - _Datos_: n=13849 IC=+0.223 PNL=+11498.58€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.08 con n=179 PNL=+70.00€
  - _Datos_: n=179 IC=+0.108 PNL=+70.00€

**🟡 H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.101 > 0.08 con n=4722 PNL=+1944.36€
  - _Datos_: n=4722 IC=+0.101 PNL=+1944.36€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=4757 PNL=+3832.67€
  - _Datos_: n=4757 IC=+0.175 PNL=+3832.67€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=7904 IC=-0.018 PNL=+2400.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7904 IC=-0.018 PNL=+2400.52€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.241 > 0.08 con n=6223 PNL=-480.80€
  - _Datos_: n=6223 IC=+0.241 PNL=-480.80€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=2543) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2543 IC=+0.097 PNL=+504.26€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.310 > 0.08 con n=752 PNL=+199.39€
  - _Datos_: n=752 IC=+0.310 PNL=+199.39€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=697) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=697 IC=+0.411 PNL=+1014.68€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=21268 IC=+0.175 PNL=-2521.13€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=21268 IC=+0.175 PNL=-2521.13€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.231 > 0.1 con n=351 PNL=+244.09€
  - _Datos_: n=351 IC=+0.231 PNL=+244.09€
