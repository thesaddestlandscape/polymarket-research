# Hipótesis automáticas — 2026-11-24 18:04 UTC
_Generado por shadow_postmortem.py sobre 1480854 resoluciones (PNL=+209967.28€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=725)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1113)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `60.0` → IC=+0.172 (n=361)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 60.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8117` → IC=+0.268 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8117 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.232` → IC=+0.196 (n=350)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.232 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1142)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4620.7315` → IC=+0.128 (n=476)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 4620.7315 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=555)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=976)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.181 (n=308)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 63.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8112` → IC=+0.263 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8112 (IC base=+0.125)

- **PATRÓN** `banda_z` > `8.315` → IC=+0.193 (n=307)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.315 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.137 (n=830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=1042)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

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
- **FILTRO** `restante_s_al_confirmar` < `130.43` → IC=-0.220 (n=12881)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.43
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=38643)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.84` → IC=-0.160 (n=3587)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.84
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=10765)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=30727)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7776.5412` → IC=+0.152 (n=2499)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7776.5412 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=27239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=33053)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=24632)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=8880)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6266.6285` → IC=+0.138 (n=3490)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1948)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2790)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16036.8816` → IC=+0.186 (n=720)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16036.8816 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=680)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.073)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.121 (n=2219)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.45 (IC base=+0.090)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=5632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.200 (n=2701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=3145)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.193)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=978)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.645` → IC=+0.236 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.645 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1207)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2042.9185` → IC=+0.139 (n=975)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2042.9185 (IC base=+0.135)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1487)
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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=25882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=17263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.220 (n=8733)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `8407.3041` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8407.3041 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=6228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.160 (n=3933)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.175 (n=6000)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=3848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=2570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.244 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.204)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=6063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.173 (n=5138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6198)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4778)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1650)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=5924)
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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=35583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=35121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=6189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=11461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=16465)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=14894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.189 (n=6109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=12620)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=5795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5745)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.258 (n=6099)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=13562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.251 (n=6398)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=5930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5926)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7341)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=12799)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=14048)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.138 (n=15798)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.33 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6220)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=6379)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=7934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.76` → IC=+0.141 (n=7849)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.76 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6579)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.135 (n=8474)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.89` → IC=+0.136 (n=7916)

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
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=98)

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
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=98)

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
- **PATRÓN** `drift_60min` |x|≤ `0.509` → IC=+0.140 (n=20454)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.509 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=20717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=14244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9736` → IC=+0.247 (n=6822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9736 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8836` → IC=+0.293 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8836 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.463` → IC=+0.191 (n=10254)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.463 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6945` → IC=+0.268 (n=5595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6945 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.256 (n=2116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7395` → IC=+0.235 (n=4944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7395 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=9850)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4916.3756` → IC=+0.151 (n=6818)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4916.3756 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.122 (n=12957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0066 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.5641` → IC=+0.145 (n=25892)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5641 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.6796` → IC=+0.193 (n=1768)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6796 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.1781` → IC=+0.196 (n=10582)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1781 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.8562` → IC=+0.197 (n=7203)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8562 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.230 (n=2621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.2829` → IC=+0.212 (n=8308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2829 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.228 (n=18302)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.088)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.304` → IC=+0.214 (n=3815)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.304 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=2104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2904)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9814` → IC=+0.274 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9814 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.434` → IC=+0.275 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.434 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.261 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4382` → IC=+0.213 (n=4166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4382 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2048.3196` → IC=+0.215 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.3196 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.219 (n=3507)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.247 (n=1316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.271 (n=1317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=4110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1807)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0793` → IC=+0.277 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0793 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.242 (n=3411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.247 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.5533` → IC=+0.239 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5533 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.8556` → IC=+0.242 (n=2521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8556 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=4336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.231 (n=1241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1155` → IC=+0.245 (n=1635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1155 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.8903` → IC=+0.254 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8903 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.7578` → IC=+0.235 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7578 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.747` → IC=+0.260 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.747 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6265` → IC=+0.227 (n=3716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6265 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.267 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.4383` → IC=+0.246 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4383 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.159 (n=3595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0835` → IC=+0.158 (n=1363)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0835 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7098` → IC=+0.172 (n=4082)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7098 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1554` → IC=+0.152 (n=3990)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1554 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.97` → IC=+0.142 (n=3762)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.97 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.157 (n=1361)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6279 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.159 (n=1479)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4451` → IC=+0.144 (n=3951)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4451 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5303)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.188 (n=1301)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.212 (n=2091)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.887` → IC=+0.278 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.887 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.193 (n=4129)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.224 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7293` → IC=+0.211 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7293 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5540)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2024.8196` → IC=+0.202 (n=1533)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.8196 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.227 (n=1906)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3081` → IC=+0.229 (n=2882)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3081 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=1965)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0526` → IC=+0.268 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0526 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.645` → IC=+0.266 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.645 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.254 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.152` → IC=+0.230 (n=2786)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.152 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1889.7284` → IC=+0.223 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1889.7284 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.222 (n=4198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.171 (n=256)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5556)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.140 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.250 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.351 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.6014` → IC=+0.344 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6014 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.197` → IC=+0.218 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.197 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.8706` → IC=+0.345 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8706 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2478` → IC=+0.363 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2478 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1649` → IC=+0.349 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1649 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.3009` → IC=+0.357 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3009 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.363 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.2749` → IC=+0.355 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2749 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.351 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.189 (n=1454)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0867 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.3652` → IC=+0.157 (n=729)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3652 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1538` → IC=+0.158 (n=2724)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1538 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8256` → IC=+0.163 (n=1911)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8256 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.191 (n=364)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.4299` → IC=+0.172 (n=921)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.4299 (IC base=+0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.183 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=895)

- **FILTRO** `ibs_20min` > `0.1935` → IC=-0.126 (n=5449)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1935
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=2704)

- **FILTRO** `sigma_ewma_delta_pct` > `8.272` → IC=-0.233 (n=884)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.272
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=7269)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.174 (n=363)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.75 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.270 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `1.3529` → IC=+0.269 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.3529 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.674` → IC=+0.176 (n=168)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 6.674 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.0067` → IC=+0.321 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0067 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1591` → IC=+0.274 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1591 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.1724` → IC=+0.280 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1724 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.264 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.1935` → IC=+0.161 (n=2704)

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
- **FILTRO** `ibs_20min` < `0.7988` → IC=-0.160 (n=4203)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7988
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=2166)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.179 (n=1310)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=5059)

- **FILTRO** `ibs_20min` > `0.7213` → IC=-0.190 (n=2196)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7213
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=6595)

- **PATRÓN** `ibs_20min` > `0.7988` → IC=+0.146 (n=2166)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7988 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.4559` → IC=+0.342 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4559 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.319 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3075` → IC=+0.319 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3075 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5282` → IC=+0.318 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5282 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1071` → IC=+0.286 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1071 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.6364` → IC=+0.275 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6364 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.2131` → IC=+0.279 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2131 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2384` → IC=+0.278 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2384 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.269 (n=2492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.187 (n=8951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0113 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8659` → IC=+0.284 (n=12173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8659 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.01` → IC=+0.306 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.01 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.457` → IC=+0.167 (n=12084)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.457 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6927` → IC=+0.280 (n=8929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6927 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.297 (n=2212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6446` → IC=+0.289 (n=5191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6446 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=15225)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.154 (n=11856)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0093 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5161` → IC=+0.175 (n=22974)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.5161 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2057` → IC=+0.284 (n=8894)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2057 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.8573` → IC=+0.280 (n=5955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8573 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.286 (n=2977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.322 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4529` → IC=+0.303 (n=4431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4529 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2715` → IC=+0.305 (n=6025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2715 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.313 (n=13299)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8162` → IC=-0.148 (n=4751)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8162
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2448)

- **FILTRO** `ibs_20min` > `0.6998` → IC=-0.243 (n=1626)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6998
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4881)

- **FILTRO** `sigma_ewma_delta_pct` > `4.057` → IC=-0.240 (n=1364)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.057
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5143)

- **PATRÓN** `ibs_20min` > `0.8162` → IC=+0.312 (n=2448)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8162 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.149` → IC=+0.175 (n=2679)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 2.149 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.332 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4467` → IC=+0.293 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4467 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2236` → IC=+0.317 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2236 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.316 (n=2037)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1705` → IC=+0.174 (n=1627)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1705 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1552` → IC=+0.388 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1552 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6493` → IC=+0.395 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6493 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1828` → IC=+0.231 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1828 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `1.1976` → IC=+0.214 (n=2620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1976 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.222 (n=2340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6953 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2739` → IC=+0.246 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2739 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.231 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4593` → IC=+0.219 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4593 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `367.0` → IC=+0.233 (n=2587)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 367.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.575` → IC=+0.258 (n=2341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.575 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.0184` → IC=+0.269 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0184 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.285 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.257 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.263 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.275 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 196.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.319 (n=1665)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=1989)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.572` → IC=+0.305 (n=2491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.572 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.1302` → IC=+0.293 (n=3414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1302 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.1663` → IC=+0.296 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1663 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2020.7156` → IC=+0.299 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2020.7156 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.301 (n=2284)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.335 (n=2285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.189` → IC=+0.328 (n=1508)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.189 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=1311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.313 (n=1549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` < `0.0306` → IC=+0.309 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0306 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.1562` → IC=+0.320 (n=2283)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1562 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.977` → IC=+0.318 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.977 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.1987` → IC=+0.309 (n=3402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1987 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3445` → IC=+0.317 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3445 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.7409` → IC=+0.327 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7409 (IC base=+0.308)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `2004.3184` → IC=+0.321 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.3184 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.313 (n=3295)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1604` → IC=+0.241 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1604 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.6437` → IC=+0.236 (n=2693)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6437 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.1723` → IC=+0.238 (n=2453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1723 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.5964` → IC=+0.236 (n=2453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5964 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.239 (n=2576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1025` → IC=+0.242 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1025 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4056` → IC=+0.244 (n=2383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4056 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4957` → IC=+0.238 (n=2129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4957 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.254 (n=2434)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.152 (n=1692)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.092 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.3871` → IC=+0.262 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3871 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.173` → IC=+0.264 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.173 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6147` → IC=+0.261 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6147 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.266 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.16` → IC=+0.279 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.16 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.7764` → IC=+0.284 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7764 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4143` → IC=+0.272 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4143 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.282 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.249 (n=2749)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=2775)

- **FILTRO** `ibs_20min` > `0.6047` → IC=-0.236 (n=1299)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6047
  - _Potencial_: sin este filtro IC_bueno=+0.169 (n=3907)

- **FILTRO** `sigma_ewma_delta_pct` > `8.222` → IC=-0.262 (n=598)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.222
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=4608)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.317 (n=2775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `1.1199` → IC=+0.355 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1199 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.454` → IC=+0.160 (n=2259)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.454 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8446` → IC=+0.351 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8446 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6972` → IC=+0.337 (n=1814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6972 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.0999` → IC=+0.339 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0999 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.369 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7937` → IC=+0.358 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7937 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.355 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6047` → IC=+0.169 (n=3907)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6047 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.3265` → IC=+0.276 (n=2110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3265 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.728` → IC=+0.136 (n=4081)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.728 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6876` → IC=+0.289 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6876 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0721` → IC=+0.301 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0721 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.1387` → IC=+0.281 (n=1751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1387 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.294 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.351 (n=2586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=2920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=3038)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.336 (n=2896)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2211` → IC=+0.336 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2211 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.777` → IC=+0.339 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.777 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.7029` → IC=+0.326 (n=2584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7029 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.344 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.323 (n=2795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `3005.3016` → IC=+0.322 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3005.3016 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.330 (n=3128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=3140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` < `0.39` → IC=+0.328 (n=3125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.39 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `1.3088` → IC=+0.322 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3088 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` < `0.2595` → IC=+0.317 (n=3079)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2595 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.07` → IC=+0.326 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.07 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` < `0.636` → IC=+0.318 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.636 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.2103` → IC=+0.339 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2103 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.361 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` < `1.4152` → IC=+0.325 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4152 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `2.1571` → IC=+0.318 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1571 (IC base=+0.314)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.220 (n=6535)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1273` → IC=+0.193 (n=8624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1273 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=20391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.229 (n=19602)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5357 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.206 (n=7406)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.72` → IC=+0.260 (n=3837)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.72 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1739` → IC=+0.152 (n=13073)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1739 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6204` → IC=+0.151 (n=13073)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6204 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.208 (n=2827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6009` → IC=+0.185 (n=6365)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6009 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.192 (n=18553)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.194 (n=8634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0062 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.187 (n=13101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0859` → IC=+0.223 (n=6543)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0859 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=9432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5265` → IC=+0.238 (n=19622)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5265 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.198` → IC=+0.180 (n=14310)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.198 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.397` → IC=+0.191 (n=3080)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.397 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.489` → IC=+0.193 (n=17559)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.489 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.6996` → IC=+0.175 (n=6111)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6996 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.217 (n=2937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.5635` → IC=+0.186 (n=8263)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.5635 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6369` → IC=+0.197 (n=6260)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6369 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=18606)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.266 (n=1073)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.0756` → IC=+0.266 (n=1072)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0756 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=2183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `0.9426` → IC=+0.292 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9426 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.469` → IC=+0.328 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.469 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.286 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.8308` → IC=+0.227 (n=2052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8308 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.229 (n=3078)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.254 (n=2736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.253 (n=1240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.1017` → IC=+0.308 (n=1203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1017 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=2817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=2486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.0054` → IC=+0.308 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0054 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.946` → IC=+0.259 (n=2703)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.946 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.256 (n=2415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.264 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.5501` → IC=+0.267 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5501 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.679` → IC=+0.254 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.679 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.260 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1932.2548` → IC=+0.253 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1932.2548 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.190 (n=1005)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0033 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0677` → IC=+0.174 (n=1001)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0677 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2499` → IC=+0.202 (n=3000)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2499 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1973` → IC=+0.211 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1973 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.556` → IC=+0.203 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.556 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8528` → IC=+0.132 (n=2001)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8528 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.0475` → IC=+0.129 (n=1360)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.0475 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.172 (n=456)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5081` → IC=+0.129 (n=1300)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5081 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4541` → IC=+0.141 (n=985)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4541 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `385.0` → IC=+0.131 (n=2922)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 385.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.182 (n=2860)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0061 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2585` → IC=+0.176 (n=2860)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2585 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.6128` → IC=+0.212 (n=3250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6128 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.222` → IC=+0.177 (n=3525)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.222 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.918` → IC=+0.177 (n=595)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.918 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.021` → IC=+0.158 (n=2864)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.021 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.164 (n=3250)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2053 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.156 (n=2855)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.144` → IC=+0.160 (n=2748)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.144 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `203.0` → IC=+0.197 (n=1352)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 203.0 (IC base=+0.154)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.232 (n=1500)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2576` → IC=+0.233 (n=2207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2576 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.285 (n=1755)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.988` → IC=+0.305 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.988 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.232 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7121` → IC=+0.224 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7121 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2019.42` → IC=+0.221 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2019.42 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.243 (n=3008)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1413` → IC=+0.275 (n=1322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1413 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.274 (n=1138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0438` → IC=+0.291 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0438 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.736` → IC=+0.283 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.736 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.284 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.239 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1795` → IC=+0.251 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1795 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1882.4784` → IC=+0.246 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.4784 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.236 (n=2918)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.195 (n=1082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.004 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0823` → IC=+0.173 (n=1078)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0823 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2441` → IC=+0.190 (n=3232)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2441 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1491` → IC=+0.189 (n=1830)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1491 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.182` → IC=+0.202 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.182 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8362` → IC=+0.140 (n=2156)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8362 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.178 (n=486)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5166` → IC=+0.127 (n=1393)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5166 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4985` → IC=+0.139 (n=1055)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4985 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6908.9474` → IC=+0.198 (n=1466)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6908.9474 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.129 (n=3170)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 123.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.174 (n=2312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0057 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4323` → IC=+0.150 (n=3468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4323 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6686` → IC=+0.190 (n=3468)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6686 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1728` → IC=+0.158 (n=3550)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1728 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.508` → IC=+0.143 (n=1185)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.508 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.152 (n=2312)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8509 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.291` → IC=+0.165 (n=523)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.291 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.1861` → IC=+0.136 (n=2908)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1861 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4077` → IC=+0.137 (n=3305)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4077 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `6679.82` → IC=+0.191 (n=1572)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6679.82 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.139 (n=3291)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 121.0 (IC base=+0.134)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.178 (n=1203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0131 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.206 (n=3614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.801` → IC=+0.213 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.801 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.921` → IC=+0.284 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.921 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1668` → IC=+0.132 (n=3607)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1668 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6239` → IC=+0.125 (n=3606)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6239 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.124 (n=3682)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.128 (n=503)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.544` → IC=+0.129 (n=1541)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.544 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2718.2425` → IC=+0.200 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2718.2425 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.128 (n=2320)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.153 (n=3337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0112 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.169 (n=1265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=3870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.222 (n=3791)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.2291` → IC=+0.148 (n=3759)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2291 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.148 (n=3362)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1798` → IC=+0.131 (n=3791)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1798 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8584` → IC=+0.126 (n=2527)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8584 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1643` → IC=+0.127 (n=3760)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1643 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.148 (n=530)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.143 (n=1202)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4415 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4634` → IC=+0.136 (n=1202)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4634 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2614.3455` → IC=+0.191 (n=1719)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2614.3455 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.133 (n=3618)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 43.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.248 (n=2892)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1691` → IC=+0.240 (n=1424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1691 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=3370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.254 (n=3237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.188` → IC=+0.233 (n=1992)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.188 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8399` → IC=+0.227 (n=3341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8399 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.439` → IC=+0.271 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.439 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6172` → IC=+0.233 (n=3237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6172 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.267 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.1694` → IC=+0.227 (n=2780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1694 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4371` → IC=+0.228 (n=3159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4371 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=4190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2627.0905` → IC=+0.230 (n=2157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2627.0905 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0162` → IC=+0.247 (n=2253)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0162 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6212` → IC=+0.249 (n=3379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6212 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.297 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `1.1945` → IC=+0.250 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1945 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.997` → IC=+0.270 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.997 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.245 (n=2253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `1.0472` → IC=+0.240 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0472 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.300 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.8538` → IC=+0.237 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8538 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.5572` → IC=+0.239 (n=2866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5572 (IC base=+0.239)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.204 (n=1730)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1451` → IC=+0.170 (n=2277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1451 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=5410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.6563` → IC=+0.222 (n=3449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6563 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9216` → IC=+0.178 (n=784)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9216 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.546` → IC=+0.208 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.546 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8557` → IC=+0.163 (n=3148)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8557 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1873` → IC=+0.159 (n=1574)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1873 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1554` → IC=+0.170 (n=1329)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1554 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5268` → IC=+0.158 (n=2223)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5268 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.8068` → IC=+0.155 (n=3368)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8068 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=5684)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7211.3919` → IC=+0.192 (n=2346)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7211.3919 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.5908` → IC=+0.154 (n=4993)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5908 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.121 (n=5525)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 136.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.204 (n=1249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.237 (n=417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.228 (n=1131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.6198` → IC=+0.258 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6198 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.689` → IC=+0.240 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.689 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.969` → IC=+0.221 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.969 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8703` → IC=+0.216 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8703 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0897` → IC=+0.215 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0897 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.209 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.4021` → IC=+0.198 (n=1227)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4021 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `13767.6452` → IC=+0.205 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13767.6452 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.147 (n=692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0037 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2186` → IC=+0.187 (n=689)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.2186 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.141 (n=1024)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 234.0 (IC base=+0.069)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.239 (n=534)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1344` → IC=+0.157 (n=701)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1344 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=1654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.7633` → IC=+0.257 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7633 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1568` → IC=+0.166 (n=761)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1568 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.976` → IC=+0.181 (n=224)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.976 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8293` → IC=+0.153 (n=1062)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8293 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2176` → IC=+0.186 (n=278)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2176 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.771` → IC=+0.157 (n=1047)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.771 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `7846.5169` → IC=+0.174 (n=722)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7846.5169 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.142 (n=529)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 30.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.124 (n=1590)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0081 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.4078` → IC=+0.183 (n=1060)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.4078 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6746` → IC=+0.142 (n=699)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6746 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.137 (n=271)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.141 (n=516)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `5566.218` → IC=+0.148 (n=1059)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5566.218 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.148 (n=686)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 40.0 (IC base=+0.110)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.151 (n=468)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0072 (IC base=+0.119)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.130 (n=466)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0129 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.138 (n=1401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5333` → IC=+0.186 (n=1251)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.5333 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.5064` → IC=+0.145 (n=446)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.5064 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.867` → IC=+0.226 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.867 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.0438` → IC=+0.129 (n=1231)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0438 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.222` → IC=+0.140 (n=237)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.222 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4172` → IC=+0.150 (n=453)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4172 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.120 (n=1415)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3056.5696` → IC=+0.150 (n=466)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3056.5696 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.167 (n=1363)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.5588 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2762.9059` → IC=+0.165 (n=702)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2762.9059 (IC base=+0.087)

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
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.228 (n=8651)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=27107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9658` → IC=+0.300 (n=8644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9658 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9583` → IC=+0.218 (n=2998)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9583 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.88` → IC=+0.260 (n=6338)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.88 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.867` → IC=+0.163 (n=11660)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.867 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2404` → IC=+0.215 (n=4625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2404 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6262` → IC=+0.194 (n=8452)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6262 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=24566)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.208 (n=8056)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.155` → IC=+0.203 (n=10625)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.155 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=9004)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.594` → IC=+0.246 (n=24143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.594 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.1931` → IC=+0.183 (n=15392)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1931 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.503` → IC=+0.206 (n=22518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.503 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.0523` → IC=+0.177 (n=14235)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0523 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.255 (n=3315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.6243` → IC=+0.211 (n=7747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6243 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.215 (n=23055)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.200)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3826` → IC=+0.236 (n=4128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3826 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2776)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8607` → IC=+0.293 (n=2752)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8607 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.034` → IC=+0.301 (n=2714)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.034 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.289 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.245 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2048.3196` → IC=+0.239 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.3196 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.267 (n=3792)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.268 (n=1720)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1288` → IC=+0.291 (n=1669)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1288 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.267 (n=3942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.269 (n=3421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.4698` → IC=+0.288 (n=3337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4698 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.267 (n=3842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.292` → IC=+0.285 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.292 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5629` → IC=+0.267 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5629 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.271 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.270 (n=2550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1934.4056` → IC=+0.267 (n=1719)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.4056 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.272 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.172 (n=1429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.084` → IC=+0.147 (n=1424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.084 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.189` → IC=+0.187 (n=4270)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.189 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.7429` → IC=+0.212 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7429 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.264` → IC=+0.171 (n=879)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.264 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6331` → IC=+0.156 (n=1424)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6331 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.0665` → IC=+0.142 (n=1936)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0665 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.190 (n=597)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.144 (n=3697)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5213` → IC=+0.145 (n=3752)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5213 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `352.0` → IC=+0.148 (n=3648)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 352.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.171 (n=3328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0061 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.084` → IC=+0.173 (n=1260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.084 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.682` → IC=+0.192 (n=3778)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.682 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1558` → IC=+0.163 (n=3704)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1558 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.001` → IC=+0.148 (n=1780)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.001 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.205` → IC=+0.151 (n=3858)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.205 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0418` → IC=+0.157 (n=3325)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0418 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2219` → IC=+0.198 (n=687)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2219 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.152 (n=3667)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7717` → IC=+0.154 (n=2444)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7717 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=4907)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.182 (n=1210)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 212.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.242 (n=1955)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.935` → IC=+0.314 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.935 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3482` → IC=+0.234 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3482 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7573` → IC=+0.241 (n=1916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7573 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1905.7248` → IC=+0.238 (n=1955)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1905.7248 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.245 (n=3676)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1863` → IC=+0.258 (n=1839)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1863 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.069` → IC=+0.297 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.069 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.89` → IC=+0.303 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.89 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.299 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.1664` → IC=+0.256 (n=2696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1664 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2004.4248` → IC=+0.251 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.4248 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.246 (n=3985)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.244)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.191 (n=1496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3568` → IC=+0.149 (n=3945)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3568 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.8768` → IC=+0.265 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8768 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1505` → IC=+0.170 (n=2218)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1505 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.031` → IC=+0.165 (n=1745)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.031 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8566` → IC=+0.155 (n=2989)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8566 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.200 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5173` → IC=+0.157 (n=1930)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5173 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1479` → IC=+0.145 (n=1988)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1479 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `5876.7125` → IC=+0.233 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5876.7125 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.144 (n=2916)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 85.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.170 (n=3802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4626` → IC=+0.162 (n=3797)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4626 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5718` → IC=+0.215 (n=3341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5718 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.6411` → IC=+0.159 (n=4393)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6411 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.058` → IC=+0.158 (n=759)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.058 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.043` → IC=+0.154 (n=3306)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.043 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.0398` → IC=+0.160 (n=3342)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0398 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.205 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4824` → IC=+0.157 (n=3680)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4824 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5218` → IC=+0.159 (n=3288)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.5218 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `6737.5602` → IC=+0.215 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6737.5602 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.162 (n=3289)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 114.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.156 (n=1523)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0132 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.6957` → IC=+0.256 (n=3046)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6957 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.8159` → IC=+0.195 (n=1018)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8159 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.195` → IC=+0.268 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.195 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2095` → IC=+0.127 (n=4570)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2095 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1013` → IC=+0.123 (n=4352)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1013 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.141 (n=571)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `2.5015` → IC=+0.125 (n=4463)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5015 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2477.4137` → IC=+0.225 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2477.4137 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.160 (n=3756)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0113 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1433` → IC=+0.151 (n=1421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1433 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=2014)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5403` → IC=+0.247 (n=3749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5403 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.228` → IC=+0.154 (n=3917)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.228 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.019` → IC=+0.162 (n=4140)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.019 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1923` → IC=+0.144 (n=4260)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1923 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.203 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4388` → IC=+0.164 (n=1358)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4388 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4896` → IC=+0.145 (n=1356)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4896 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2654.0431` → IC=+0.222 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2654.0431 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.152 (n=4110)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.255 (n=4171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.240 (n=2791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.987` → IC=+0.302 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.987 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.2053` → IC=+0.251 (n=2119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2053 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.962` → IC=+0.296 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.962 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2164` → IC=+0.236 (n=4169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2164 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6407` → IC=+0.241 (n=4169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6407 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.254 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.517` → IC=+0.256 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.517 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=5377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2644.9749` → IC=+0.240 (n=2779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2644.9749 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0247` → IC=+0.272 (n=1450)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0247 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.251 (n=4090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.1398` → IC=+0.307 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1398 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.1969` → IC=+0.250 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1969 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2331` → IC=+0.250 (n=4177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2331 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.936` → IC=+0.281 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.936 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.7122` → IC=+0.249 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7122 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.265 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.310 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4335` → IC=+0.249 (n=4128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4335 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.245 (n=2826)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.241 (n=2472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.5388` → IC=+0.232 (n=7402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5388 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=7438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.259 (n=2469)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.9649` → IC=+0.227 (n=6044)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9649 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.428` → IC=+0.234 (n=2467)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.428 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.229 (n=2306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.8793` → IC=+0.227 (n=3493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8793 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.234 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4503` → IC=+0.235 (n=2428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4503 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.229 (n=5285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3755.0982` → IC=+0.232 (n=4934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3755.0982 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.231 (n=1765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.213 (n=2402)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4161` → IC=+0.222 (n=4651)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4161 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.225 (n=2375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.6139` → IC=+0.216 (n=4651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6139 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7161` → IC=+0.219 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7161 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2566` → IC=+0.204 (n=4639)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2566 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.702` → IC=+0.225 (n=4798)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.702 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2512` → IC=+0.211 (n=4791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2512 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.215 (n=4884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5326` → IC=+0.216 (n=2290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5326 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8164` → IC=+0.218 (n=3471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8164 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.236 (n=3485)

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
- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.220 (n=2026)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.4737` → IC=+0.219 (n=2026)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4737 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.225 (n=1812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.4724` → IC=+0.226 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4724 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.8348` → IC=+0.216 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8348 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.4248` → IC=+0.224 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4248 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.911` → IC=+0.222 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.911 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.8664` → IC=+0.216 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8664 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.218 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0989` → IC=+0.215 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0989 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.1597` → IC=+0.215 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1597 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4052` → IC=+0.228 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4052 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.4954` → IC=+0.215 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4954 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.244 (n=548)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.5091` → IC=+0.221 (n=1642)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5091 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.217 (n=619)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.0844` → IC=+0.213 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0844 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.7294` → IC=+0.223 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7294 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.241` → IC=+0.211 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.241 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.6375` → IC=+0.222 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6375 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.7185` → IC=+0.211 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7185 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.226 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1637` → IC=+0.208 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1637 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7743` → IC=+0.211 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7743 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `7946.1767` → IC=+0.216 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7946.1767 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.211 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.207)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.229 (n=864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.226 (n=432)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.299 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `1.1022` → IC=+0.246 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1022 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.269 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `0.6422` → IC=+0.246 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6422 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.219 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.240 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `2.4968` → IC=+0.225 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4968 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `3372.142` → IC=+0.243 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3372.142 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.223 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.217)

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

- **PATRÓN** `dist_vwap_pct` < `0.332` → IC=+0.257 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.332 (IC base=+0.247)

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
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0042 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.417` → IC=+0.131 (n=2688)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.417 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.155 (n=1267)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.308` → IC=+0.138 (n=580)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.308 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.5837` → IC=+0.179 (n=2116)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5837 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.539` → IC=+0.131 (n=935)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.539 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.185 (n=591)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.1389` → IC=+0.122 (n=1788)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.1389 (IC base=+0.096)

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

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.121 (n=333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0037 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0653` → IC=+0.253 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0653 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.145 (n=316)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.057)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5264` → IC=-0.121 (n=354)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5264
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=721)

- **FILTRO** `ibs_20min` > `0.4948` → IC=-0.129 (n=265)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4948
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=517)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.155 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0043 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.5264` → IC=+0.156 (n=721)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.5264 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.135` → IC=+0.153 (n=387)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.135 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.957` → IC=+0.169 (n=176)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.957 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.282 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=+0.046)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.196 (n=307)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 1.0 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.7657` → IC=+0.158 (n=223)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.7657 (IC base=+0.036)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.176 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0103 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.195 (n=588)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.2242` → IC=+0.155 (n=580)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2242 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.01` → IC=+0.258 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.01 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.1084` → IC=+0.180 (n=195)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.1084 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.188 (n=152)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `2.1906` → IC=+0.129 (n=488)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.1906 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `1.8578` → IC=+0.145 (n=370)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8578 (IC base=+0.100)

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

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.368 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0122 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.341 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.386 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.343)

- **PATRÓN** `ibs_20min` < `0.1183` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1183 (IC base=+0.343)

- **PATRÓN** `ibs_20min` > `0.3512` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3512 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.526` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.526 (IC base=+0.343)

- **PATRÓN** `volumen_regimen` > `0.6174` → IC=+0.384 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6174 (IC base=+0.343)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.343)

- **PATRÓN** `volumen_spike_ratio` < `1.5039` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5039 (IC base=+0.343)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `47.3155` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 47.3155 (IC base=+0.343)

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

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.256 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=76)

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
- **FILTRO** `ibs_20min` > `0.2609` → IC=-0.160 (n=339)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1019)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.248 (n=399)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.205 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.8971` → IC=+0.305 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8971 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.66` → IC=+0.193 (n=382)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.66 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.192 (n=290)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6242 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.175 (n=290)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1967 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` < `0.0673` → IC=+0.191 (n=664)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0673 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.203 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.166)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.155 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0066 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.7315` → IC=+0.142 (n=244)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.7315 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.7249` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7249 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2613` → IC=+0.133 (n=453)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2613 (IC base=+0.072)

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

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.321 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.288 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.299 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.7916` → IC=+0.404 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7916 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.006` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.006 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `0.7978` → IC=+0.298 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7978 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.0893` → IC=+0.313 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0893 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.320 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.3741` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3741 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.276 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.269)

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
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1538)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `liq_n` > 2.0 (IC base=+0.097)

- **PATRÓN** `liq_usd_total` > `153.37` → IC=+0.134 (n=159)

  - _Acción_: Kelly boost +0.67€ cuando `liq_usd_total` > 153.37 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.097)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.5 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.097)

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
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=255)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=212)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.199 (n=81)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=161)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=151)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.193 (n=161)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 50.0 (IC base=+0.025)

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

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.196)

- **PATRÓN** `liq_usd_total` > `862.23` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 862.23 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.220 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.230 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `3278.591` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3278.591 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `3.0` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 3.0 (IC base=+0.196)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.130 (n=3663)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=9465)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.164 (n=442)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1059)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.141 (n=349)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=950)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.143 (n=449)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.51 (IC base=-0.007)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.126 (n=204)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=472)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.123 (n=348)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=703)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=749)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=797)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.140 (n=367)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=792)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.127 (n=577)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=722)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=601)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=640)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.132 (n=653)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=757)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9284)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=28990)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=9656)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=29920)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4221)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3383)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4335)

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
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=961)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=231)

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
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=58731)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20616)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=64018)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27825)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=56809)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.154 (n=28679)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=55955)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26214)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=79599)

- **FILTRO** `ibs_7min` > `0.2782` → IC=-0.183 (n=26453)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2782
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=79360)

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
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=10683)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3437)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10628)

- **FILTRO** `ibs_7min` < `0.7112` → IC=-0.214 (n=3515)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7112
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10550)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.204 (n=3506)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10559)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=3282)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=11121)

- **FILTRO** `ibs_7min` > `0.2638` → IC=-0.189 (n=3600)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2638
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10803)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.177 (n=3592)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10811)

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
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=9243)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=3129)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10614)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.202 (n=3433)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10310)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.198 (n=3418)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=10325)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.257 (n=3325)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=10950)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.178 (n=3566)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=10709)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.171 (n=3523)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10752)

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
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=683)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=932)

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
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=558)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.143 (n=775)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `458.564` → IC=+0.166 (n=570)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 458.564 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3675.377` → IC=+0.129 (n=775)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3675.377 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.180 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 14.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.144 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 5.0 (IC base=+0.143)

- **PATRÓN** `total_vol_5m` < `381.982` → IC=+0.168 (n=347)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 381.982 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.146 (n=357)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.04 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.156 (n=277)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 9.0 (IC base=+0.143)

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
- **PATRÓN** `delta_ratio` |x|> `0.4312` → IC=+0.206 (n=134)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4312 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.164 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 5.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `4782.684` → IC=+0.180 (n=195)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4782.684 (IC base=+0.132)

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

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.152 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0047 (IC base=-0.029)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.252 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.003)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9196` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.9196 (IC base=+0.003)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` > `76.1623` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `T_h` > 76.1623
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `75.359` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `T_h` < 75.359
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=132)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0147` → IC=-0.167 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0147
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `130.5499` → IC=-0.256 (n=659)

  - _Acción_: SKIP cuando `T_h` < 130.5499
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=220)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.178 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=630)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.371 (n=208)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=631)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `49.2927` → IC=-0.243 (n=216)

  - _Acción_: SKIP cuando `T_h` > 49.2927
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `sigma_h` < `0.0068` → IC=-0.175 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=156)

- **FILTRO** `pct_vs_K` |x|> `2.3701` → IC=-0.322 (n=105)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3701
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=206)

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
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.323 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=129)

- **FILTRO** `T_h` < `69.3519` → IC=-0.314 (n=84)

  - _Acción_: SKIP cuando `T_h` < 69.3519
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=173)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=189)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9843` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `pct_vs_K` |x|≤ 1.9843 (IC base=-0.097)

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
- **FILTRO** `sigma_h` < `0.0129` → IC=-0.225 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=82)

- **FILTRO** `T_h` > `113.6692` → IC=-0.235 (n=81)

  - _Acción_: SKIP cuando `T_h` > 113.6692
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=159)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.300 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=124)

- **FILTRO** `sigma_h` < `0.0097` → IC=-0.250 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=141)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1072` → IC=+0.449 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.326)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.341 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.326)

- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.336 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.326)

- **PATRÓN** `T_h` < `0.3491` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3491 (IC base=+0.326)

- **PATRÓN** `T_h` > `0.4307` → IC=+0.339 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4307 (IC base=+0.326)

- **PATRÓN** `dist_50` > `0.4566` → IC=+0.484 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4566 (IC base=+0.326)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.344 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.326)

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
- **PATRÓN** `edge` > `0.15` → IC=+0.487 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.15 (IC base=+0.422)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.471 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.422)

- **PATRÓN** `T_h` < `1.0409` → IC=+0.426 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0409 (IC base=+0.422)

- **PATRÓN** `T_h` > `0.5804` → IC=+0.427 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5804 (IC base=+0.422)

- **PATRÓN** `dist_50` > `0.325` → IC=+0.474 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.325 (IC base=+0.422)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=494)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=524)

- **PATRÓN** `streak_estiramiento` < `0.3783` → IC=+0.133 (n=164)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.3783 (IC base=+0.019)

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
- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.126 (n=129)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.034)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5584)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3378)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.184 (n=2197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2333` → IC=+0.158 (n=6590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2333 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.124` → IC=+0.133 (n=6589)

  - _Acción_: Kelly boost +0.66€ cuando `drift_15min` |x|≤ 1.124 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0645` → IC=+0.132 (n=6589)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0645 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0999` → IC=+0.143 (n=2078)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0999 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.5517` → IC=+0.207 (n=5889)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5517 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.230 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3452)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4305.62` → IC=+0.171 (n=2197)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4305.62 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2543)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.253 (n=297)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.247 (n=393)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.228 (n=296)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.206)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2251` → IC=+0.218 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2251 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7031` → IC=+0.274 (n=889)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7031 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.4005` → IC=+0.231 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4005 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5531` → IC=+0.209 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5531 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.166` → IC=+0.298 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.166 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.223 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.206)

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
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.143 (n=1671)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0119 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2399` → IC=+0.175 (n=1671)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2399 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0582` → IC=+0.140 (n=1671)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0582 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0929` → IC=+0.185 (n=522)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0929 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=1527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.141 (n=1470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.697` → IC=+0.231 (n=1115)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.697 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.215` → IC=+0.145 (n=764)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.215 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.9085` → IC=+0.140 (n=1928)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.9085 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.989` → IC=+0.186 (n=386)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 16.989 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2944.984` → IC=+0.183 (n=758)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2944.984 (IC base=+0.137)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.363 (n=547)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.377 (n=544)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.378 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=864)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7881` → IC=+0.394 (n=816)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7881 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2719` → IC=+0.383 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2719 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.84` → IC=+0.397 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.84 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9641.0136` → IC=+0.376 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9641.0136 (IC base=+0.363)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.362 (n=398)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.383 (n=391)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.394 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.679` → IC=+0.383 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.679 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `16402.4254` → IC=+0.387 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16402.4254 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.384 (n=231)

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
- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2711)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3417)

- **FILTRO** `libro_liquidez` < `4391.961` → IC=-0.172 (n=4044)

  - _Acción_: SKIP cuando `libro_liquidez` < 4391.961
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=2084)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.278 (n=1346)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` > `0.117` → IC=+0.209 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.117 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` < `0.6021` → IC=+0.198 (n=1426)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.6021 (IC base=-0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2279` → IC=+0.268 (n=2015)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2279 (IC base=+0.002)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.282 (n=6043)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.7099` → IC=+0.264 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7099 (IC base=+0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` < `0.004` → IC=-0.209 (n=1010)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=3032)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.185 (n=1882)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2160)

- **FILTRO** `sigma_ewma_delta_pct` > `22.231` → IC=-0.239 (n=572)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.231
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=3470)

- **FILTRO** `libro_liquidez` < `10168.4909` → IC=-0.192 (n=1333)

  - _Acción_: SKIP cuando `libro_liquidez` < 10168.4909
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2709)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.145 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0033 (IC base=+0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.279 (n=161)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.065)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.281 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.065)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.317 (n=483)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1068` → IC=+0.286 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1068 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.5501` → IC=+0.285 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5501 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.793` → IC=+0.142 (n=241)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 21.793 (IC base=+0.065)

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

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.255 (n=1040)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.4822` → IC=+0.241 (n=2362)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4822 (IC base=+0.235)

- **PATRÓN** `drift_15min` |x|≤ `0.8283` → IC=+0.248 (n=2079)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8283 (IC base=+0.235)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1979` → IC=+0.256 (n=1071)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1979 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.239 (n=1613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.235)

- **PATRÓN** `ibs_15` < `0.3923` → IC=+0.267 (n=2362)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3923 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.1669` → IC=+0.245 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1669 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.522` → IC=+0.241 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.522 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.323` → IC=+0.239 (n=2485)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.323 (IC base=+0.235)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2012` → IC=-0.296 (n=366)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2012
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=1106)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.282 (n=499)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=973)

- **FILTRO** `drift_15min` |x|> `1.0228` → IC=-0.305 (n=367)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0228
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=1105)

- **FILTRO** `sigma_ewma_delta_pct` > `5.969` → IC=-0.214 (n=323)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.969
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1149)

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

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.296 (n=1002)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2881` → IC=+0.255 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2881 (IC base=-0.026)

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

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.293 (n=1410)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.008)

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
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.301 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.292 (n=498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0715` → IC=+0.307 (n=660)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0715 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1495` → IC=+0.286 (n=996)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1495 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2171` → IC=+0.288 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2171 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8361` → IC=+0.310 (n=1495)
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

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2292` → IC=+0.287 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2292 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.302 (n=725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.9653` → IC=+0.336 (n=357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9653 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2614` → IC=+0.309 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2614 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.592` → IC=+0.391 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.592 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `14493.8191` → IC=+0.308 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14493.8191 (IC base=+0.279)

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
- **FILTRO** `sigma_h` < `0.0081` → IC=-0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.103` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.103
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=27)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=33)

- **FILTRO** `drift_15min` |x|> `0.5336` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5336
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=44)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9866` → IC=+0.252 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9866 (IC base=+0.122)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.355 (n=3367)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.332)

- **PATRÓN** `ratio` > `1.0158` → IC=+0.385 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0158 (IC base=+0.332)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9756` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `ratio` < 0.9756 (IC base=+0.064)

- **PATRÓN** `T_h` > `109.838` → IC=+0.327 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.838 (IC base=+0.303)

- **PATRÓN** `ratio` > `1.0005` → IC=+0.294 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0005 (IC base=+0.303)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `103.6521` → IC=+0.239 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 103.6521 (IC base=+0.185)

- **PATRÓN** `ratio` < `0.9775` → IC=+0.361 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.185)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.350 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.315)

- **PATRÓN** `ratio` > `1.0227` → IC=+0.405 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0227 (IC base=+0.315)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0386` → IC=+0.411 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0386 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5517 sube el IC de +0.132 a +0.207 en UPDOWN_GBM#15min (n=5889). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7031 sube el IC de +0.206 a +0.274 en UPDOWN_GBM#BTC#15min (n=889). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4811 sube el IC de +0.133 a +0.217 en UPDOWN_GBM#ETH#15min (n=1138). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.697 sube el IC de +0.137 a +0.231 en UPDOWN_GBM#XRP#15min (n=1115). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6288 sube el IC de -0.088 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1346). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.002 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=6043). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.065 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=483). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.180 a +0.291 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5657 sube el IC de +0.147 a +0.241 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=678). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3923 sube el IC de +0.235 a +0.267 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2362). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.026 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=1002). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.008 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1410). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.081 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7 (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.081 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8361 sube el IC de +0.284 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1495). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9653 sube el IC de +0.279 a +0.336 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8448 sube el IC de +0.290 a +0.314 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=708). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7881 sube el IC de +0.363 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=816). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.362 a +0.383 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=391). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.363 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=426). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2360 | +0.084 | +255.10€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2360 | +0.084 | +255.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1948 | +0.085 | +215.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1948 | +0.085 | +215.61€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1493 | -0.028 | +53.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1493 | -0.028 | +53.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1169 | -0.041 | +41.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1169 | -0.041 | +41.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51524 | -0.087 | -6583.18€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3383 | +0.096 | -316.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48141 | -0.099 | -6266.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3383 | +0.096 | -316.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3383 | +0.096 | -316.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14352 | -0.044 | -1321.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14352 | -0.044 | -1321.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 57204 | -0.012 | +2620.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14754 | +0.004 | +1470.36€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 42450 | -0.017 | +1150.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 57204 | -0.012 | +2620.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14754 | +0.004 | +1470.36€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 42450 | -0.017 | +1150.11€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 213100 | +0.112 | -8686.27€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23462 | +0.179 | -740.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 996 | +0.021 | -79.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 176549 | +0.105 | -7469.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12093 | +0.095 | -395.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 29275 | +0.101 | -2100.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 87 | -0.197 | +9.66€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 29151 | +0.102 | -2119.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 39893 | +0.123 | -617.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5720 | +0.177 | -223.73€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 29226 | +0.119 | -212.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4905 | +0.081 | -158.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 29322 | +0.098 | -2058.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 107 | -0.105 | +22.21€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 29188 | +0.099 | -2074.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 12 | -0.043 | +5.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 45608 | +0.123 | -962.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11352 | +0.178 | -321.17€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 29695 | +0.106 | -548.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4549 | +0.103 | -84.21€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 39714 | +0.111 | -1671.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6096 | +0.200 | -240.90€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 899 | +0.045 | -25.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 30117 | +0.096 | -1222.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2602 | +0.107 | -182.66€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 29288 | +0.106 | -1277.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 100 | -0.137 | +13.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 29172 | +0.107 | -1292.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 34734 | +0.189 | -2636.94€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 34734 | +0.189 | -2636.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7874 | +0.160 | -948.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7874 | +0.160 | -948.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5222 | +0.194 | -225.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5222 | +0.194 | -225.25€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7677 | +0.171 | -714.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7677 | +0.171 | -714.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6358 | +0.252 | -218.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6358 | +0.252 | -218.14€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7524 | +0.182 | -544.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7524 | +0.182 | -544.01€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 122778 | +0.199 | -9002.89€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 122778 | +0.199 | -9002.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21289 | +0.175 | -2530.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21289 | +0.175 | -2530.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19781 | +0.223 | -659.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19781 | +0.223 | -659.15€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21056 | +0.180 | -2217.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21056 | +0.180 | -2217.56€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19965 | +0.217 | -784.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19965 | +0.217 | -784.90€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20250 | +0.205 | -1188.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20250 | +0.205 | -1188.77€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20437 | +0.196 | -1622.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20437 | +0.196 | -1622.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 47746 | +0.117 | +410.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 47746 | +0.117 | +410.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 23774 | +0.117 | +267.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 23774 | +0.117 | +267.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 23972 | +0.116 | +143.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 23972 | +0.116 | +143.48€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2058 | +0.063 | -110.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1333 | +0.071 | -46.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1624 | +0.068 | -65.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1333 | +0.071 | -46.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 97600 | +0.101 | -2042.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7922 | +0.097 | +191.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 89678 | +0.101 | -2233.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 53261 | +0.105 | -430.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7922 | +0.097 | +191.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 45339 | +0.106 | -622.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 20998 | +0.110 | -75.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 20998 | +0.110 | -75.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 23341 | +0.083 | -1535.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 23341 | +0.083 | -1535.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 923 | +0.183 | -107.03€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 923 | +0.183 | -107.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 923 | +0.183 | -107.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 923 | +0.183 | -107.03€ | 1 | 4 |
| ✅ GBM_LATE_15M | 66492 | +0.103 | +37548.62€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 66492 | +0.103 | +37548.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11041 | +0.225 | +9497.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11041 | +0.225 | +9497.57€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 10396 | +0.177 | +8421.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10396 | +0.177 | +8421.78€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 11895 | +0.207 | +9385.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11895 | +0.207 | +9385.57€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8790 | +0.063 | +3012.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8790 | +0.063 | +3012.32€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 9210 | -0.025 | +2384.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9210 | -0.025 | +2384.18€ | 3 | 16 |
| ✅ GBM_LATE_15M#XRP | 15160 | -0.019 | +4847.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15160 | -0.019 | +4847.20€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 70582 | +0.088 | +41371.55€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 70582 | +0.088 | +41371.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13706 | -0.002 | +7183.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13706 | -0.002 | +7183.28€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15178 | +0.007 | +4215.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15178 | +0.007 | +4215.86€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9452 | +0.296 | +10851.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9452 | +0.296 | +10851.28€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13495 | +0.019 | +4338.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13495 | +0.019 | +4338.98€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10730 | +0.051 | +5029.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10730 | +0.051 | +5029.75€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8021 | +0.313 | +9752.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8021 | +0.313 | +9752.41€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 52288 | +0.180 | +43593.05€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 52288 | +0.180 | +43593.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7927 | +0.240 | +7395.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7927 | +0.240 | +7395.42€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8333 | +0.141 | +6289.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8333 | +0.141 | +6289.22€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8416 | +0.223 | +7278.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8416 | +0.223 | +7278.75€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8932 | +0.131 | +7025.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8932 | +0.131 | +7025.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9861 | +0.124 | +7655.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9861 | +0.124 | +7655.18€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8819 | +0.232 | +7948.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8819 | +0.232 | +7948.82€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14461 | +0.126 | +7395.26€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14461 | +0.126 | +7395.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3751 | +0.126 | +2032.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3751 | +0.126 | +2032.60€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4241 | +0.127 | +2144.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4241 | +0.127 | +2144.76€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3927 | +0.102 | +1627.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3927 | +0.102 | +1627.10€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1355 | +0.168 | +858.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1355 | +0.168 | +858.78€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 66759 | +0.190 | +55785.22€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 66759 | +0.190 | +55785.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10558 | +0.250 | +10188.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10558 | +0.250 | +10188.84€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10729 | +0.143 | +7851.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10729 | +0.143 | +7851.36€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11316 | +0.234 | +10195.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11316 | +0.234 | +10195.03€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11038 | +0.146 | +8380.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11038 | +0.146 | +8380.70€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11770 | +0.129 | +8632.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11770 | +0.129 | +8632.36€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11348 | +0.241 | +10536.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11348 | +0.241 | +10536.94€ | 0 | 23 |
| ✅ GBM_LATE_5M | 16914 | +0.219 | +14294.42€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 16914 | +0.219 | +14294.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3332 | +0.210 | +2853.06€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3332 | +0.210 | +2853.06€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1591 | +0.218 | +1323.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1591 | +0.218 | +1323.18€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4889 | +0.210 | +3858.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4889 | +0.210 | +3858.43€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 3017 | +0.230 | +2683.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3017 | +0.230 | +2683.11€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 2137 | +0.209 | +1677.91€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2137 | +0.209 | +1677.91€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6628 | +0.080 | +2284.39€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 6628 | +0.080 | +2284.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 187 | +0.267 | +203.05€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 187 | +0.267 | +203.05€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2071 | +0.061 | +622.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2071 | +0.061 | +622.43€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 180 | +0.324 | +226.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 180 | +0.324 | +226.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1927 | +0.055 | +591.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1927 | +0.055 | +591.18€ | 2 | 5 |
| ✅ GBM_LATE_60M#SOL | 2082 | +0.061 | +418.36€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2082 | +0.061 | +418.36€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 181 | +0.331 | +223.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 181 | +0.331 | +223.16€ | 0 | 22 |
| 🚫 GBM_LATE_60M_FADE | 803 | -0.244 | -32.13€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 803 | -0.244 | -32.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 282 | -0.254 | -19.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 282 | -0.254 | -19.29€ | 5 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 277 | -0.242 | -7.42€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 277 | -0.242 | -7.42€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 219 | -0.247 | -9.19€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 219 | -0.247 | -9.19€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2528 | +0.089 | +672.05€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2528 | +0.089 | +672.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 928 | +0.071 | +238.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 928 | +0.071 | +238.90€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 24 | +0.192 | +14.50€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 24 | +0.192 | +14.50€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 832 | +0.053 | +160.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 832 | +0.053 | +160.11€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 673 | +0.152 | +239.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 673 | +0.152 | +239.65€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 71 | +0.116 | +18.88€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 71 | +0.116 | +18.88€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 425 | +0.306 | +505.51€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 425 | +0.306 | +505.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 425 | +0.306 | +505.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 425 | +0.306 | +505.51€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4982 | +0.095 | +1082.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4982 | +0.095 | +1082.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4982 | +0.095 | +1082.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4982 | +0.095 | +1082.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1866 | +0.021 | +111.65€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1866 | +0.021 | +111.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 237 | +0.094 | +49.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 237 | +0.094 | +49.94€ | 0 | 5 |
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
| ✅ LIQUIDACIONES_5M | 4629 | +0.019 | +213.21€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#5min | 4629 | +0.019 | +213.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 867 | +0.015 | +49.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 867 | +0.015 | +49.10€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 353 | +0.075 | +101.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 353 | +0.075 | +101.28€ | 0 | 6 |
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
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 21624 | -0.032 | -209.41€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10484 | -0.032 | -99.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11140 | -0.032 | -109.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 761 | -0.053 | -41.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 390 | -0.041 | -9.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 371 | -0.066 | -31.90€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5834 | -0.025 | -14.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2781 | -0.022 | +11.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3053 | -0.028 | -26.09€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1969 | -0.033 | -7.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1010 | -0.037 | -18.90€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 959 | -0.029 | +11.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4963 | -0.032 | -57.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2391 | -0.028 | -10.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2572 | -0.035 | -47.30€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4113 | -0.026 | +34.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2006 | -0.029 | +0.30€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2107 | -0.022 | +34.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3984 | -0.044 | -122.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1906 | -0.048 | -72.79€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2078 | -0.040 | -49.28€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 77850 | -0.000 | +4187.99€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 77850 | -0.000 | +4187.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10866 | -0.038 | -152.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10866 | -0.038 | -152.61€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10850 | -0.053 | -280.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10850 | -0.053 | -280.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7505 | -0.052 | -105.75€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7505 | -0.052 | -105.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2162 | -0.058 | -19.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2162 | -0.058 | -19.55€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 821 | -0.116 | -32.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 821 | -0.116 | -32.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2278 | -0.065 | -11.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2278 | -0.065 | -11.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 872 | -0.018 | -27.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 872 | -0.018 | -27.81€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 190447 | -0.078 | +2118.82€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 190447 | -0.078 | +2118.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 28468 | -0.102 | -1438.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 28468 | -0.102 | -1438.88€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 28018 | -0.101 | -1001.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 28018 | -0.101 | -1001.43€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9400 | -0.035 | -185.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9400 | -0.035 | -185.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1012 | -0.017 | -19.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1012 | -0.017 | -19.26€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2207 | -0.046 | -29.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2207 | -0.046 | -29.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2683 | -0.023 | -31.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2683 | -0.023 | -31.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1316 | -0.063 | -30.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1316 | -0.063 | -30.57€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1173 | -0.039 | -42.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1173 | -0.039 | -42.91€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2414 | +0.120 | +972.16€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2278 | +0.124 | +959.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 525 | +0.143 | +276.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 525 | +0.143 | +276.02€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 477 | +0.118 | +169.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 477 | +0.118 | +169.93€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 415 | +0.128 | +191.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 415 | +0.128 | +191.95€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 389 | +0.132 | +185.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 389 | +0.132 | +185.41€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 472 | +0.097 | +136.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 472 | +0.097 | +136.26€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2542 | -0.023 | -53.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2542 | -0.023 | -53.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 447 | +0.006 | +20.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 447 | +0.006 | +20.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 463 | -0.051 | -33.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 463 | -0.051 | -33.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 614 | -0.045 | -45.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 614 | -0.045 | -45.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 530 | -0.007 | -4.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 530 | -0.007 | -4.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 488 | -0.012 | +8.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 488 | -0.012 | +8.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1357 | -0.042 | +140.17€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 628 | -0.068 | +27.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 490 | -0.065 | +52.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 138 | -0.079 | -24.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 477 | -0.009 | +74.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 346 | +0.009 | +84.45€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 131 | -0.056 | -9.68€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 252 | -0.039 | +38.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 214 | -0.037 | +33.77€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 38 | -0.050 | +4.42€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1050 | -0.035 | +170.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 307 | -0.066 | -30.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1718 | -0.185 | -33.10€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 680 | -0.173 | -7.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 601 | -0.172 | -4.30€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 79 | -0.179 | -3.17€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 577 | -0.198 | -32.47€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 508 | -0.204 | -37.58€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 69 | -0.148 | +5.11€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 461 | -0.185 | +6.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 427 | -0.181 | +3.70€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 34 | -0.222 | +3.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1536 | -0.185 | -38.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 182 | -0.179 | +5.08€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 606 | +0.373 | +534.00€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 141 | +0.178 | +100.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 141 | +0.178 | +100.38€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 138 | +0.371 | +107.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 138 | +0.371 | +107.96€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 327 | +0.454 | +325.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 327 | +0.454 | +325.67€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 606 | +0.373 | +534.00€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1056 | +0.039 | +83.58€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1056 | +0.039 | +83.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 80 | +0.024 | +1.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 80 | +0.024 | +1.80€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 532 | +0.058 | +71.83€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 532 | +0.058 | +71.83€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3666 | -0.023 | -144.32€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3666 | -0.023 | -144.32€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1129 | -0.022 | -40.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1129 | -0.022 | -40.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 631 | -0.028 | -26.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 631 | -0.028 | -26.87€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 178 | -0.050 | -16.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 178 | -0.050 | -16.31€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1728 | -0.019 | -60.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1728 | -0.019 | -60.97€ | 1 | 0 |
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
| ✅ STREAK_MOM_5M | 11717 | +0.013 | +62.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11717 | +0.013 | +62.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3010 | +0.017 | +20.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3010 | +0.017 | +20.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3131 | +0.013 | +24.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3131 | +0.013 | +24.66€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2954 | +0.009 | -2.25€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2954 | +0.009 | -2.25€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2622 | +0.014 | +18.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2622 | +0.014 | +18.81€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13985 | +0.019 | +5.98€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13985 | +0.019 | +5.98€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5603 | +0.021 | +5.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5603 | +0.021 | +5.26€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4970 | +0.019 | +3.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4970 | +0.019 | +3.62€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3412 | +0.014 | -2.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3412 | +0.014 | -2.91€ | 1 | 0 |
| ✅ UPDOWN_GBM | 126445 | +0.060 | +12079.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 31607 | +0.077 | +6182.56€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3590 | -0.001 | +40.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 83297 | +0.062 | +5732.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7517 | -0.002 | +128.79€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11064 | +0.104 | +2049.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2099 | +0.165 | +984.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8875 | +0.090 | +1066.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 28583 | +0.057 | +2527.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4240 | +0.081 | +957.10€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1058 | +0.000 | +22.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19727 | +0.066 | +1460.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3402 | -0.004 | +83.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 156 | -0.063 | +4.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14151 | +0.074 | +1569.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11981 | +0.061 | +676.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 29618 | +0.049 | +2109.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7320 | +0.070 | +1142.99€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1022 | +0.005 | +15.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18344 | +0.052 | +910.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2787 | -0.002 | +39.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 145 | -0.099 | +2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26132 | +0.041 | +1500.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8545 | +0.032 | +477.53€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 937 | -0.011 | +7.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15211 | +0.054 | +1017.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1308 | +0.002 | +6.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 131 | -0.139 | -8.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16895 | +0.073 | +2325.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7319 | +0.088 | +1726.59€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9159 | +0.064 | +600.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 20 | +0.000 | -0.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 432 | -0.099 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1088 | +0.363 | +415.23€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1088 | +0.363 | +415.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 521 | +0.362 | +187.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 521 | +0.362 | +187.41€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 567 | +0.363 | +227.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 567 | +0.363 | +227.82€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 29947 | -0.016 | +7570.54€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 29947 | -0.016 | +7570.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2358 | -0.044 | +646.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2358 | -0.044 | +646.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5521 | -0.115 | +342.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5521 | -0.115 | +342.15€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4053 | +0.216 | +2547.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4053 | +0.216 | +2547.04€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8407 | -0.057 | +1268.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8407 | -0.057 | +1268.38€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8314 | -0.052 | +1703.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8314 | -0.052 | +1703.09€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 377 | +0.059 | +31.96€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 377 | +0.059 | +31.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 377 | +0.059 | +31.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 377 | +0.059 | +31.96€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1992 | +0.284 | +1702.48€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1992 | +0.284 | +1702.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1048 | +0.279 | +847.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1048 | +0.279 | +847.16€ | 0 | 10 |
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
| ✅ UPDOWN_OU_5M#SOL#5min | 126 | -0.195 | -7.59€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5471 | +0.291 | +2387.06€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2139 | +0.247 | +336.00€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2119 | +0.284 | +876.69€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 1213 | +0.382 | +1174.37€ | 0 | 1 |