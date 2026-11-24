# Hipótesis automáticas — 2026-11-24 04:32 UTC
_Generado por shadow_postmortem.py sobre 1473937 resoluciones (PNL=+208725.14€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=721)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=1108)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8114` → IC=+0.268 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8114 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.259` → IC=+0.194 (n=348)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.259 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=1053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=1135)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4605.9198` → IC=+0.128 (n=474)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 4605.9198 (IC base=+0.124)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=551)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=971)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.180 (n=307)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 63.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.8109` → IC=+0.267 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8109 (IC base=+0.126)

- **PATRÓN** `banda_z` > `8.32` → IC=+0.193 (n=304)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.32 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.139 (n=823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=1035)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `8588.5981` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 8588.5981 (IC base=+0.018)

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
- **FILTRO** `restante_s_al_confirmar` < `130.38` → IC=-0.220 (n=12865)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.38
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=38599)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.68` → IC=-0.161 (n=3574)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.68
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=10724)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=30613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7807.7255` → IC=+0.152 (n=2491)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7807.7255 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=27203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=32882)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=24490)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=8859)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6293.6472` → IC=+0.139 (n=3477)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 6293.6472 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=2228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=2729)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `16202.3525` → IC=+0.182 (n=709)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16202.3525 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1946)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2787)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16036.8816` → IC=+0.186 (n=720)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16036.8816 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=677)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.154 (n=1586)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.44 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=5597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2741)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.378 (n=1893)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.200 (n=2686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=3131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.140 (n=973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.645` → IC=+0.235 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.645 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1206)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2043.3255` → IC=+0.137 (n=971)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2043.3255 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.231 (n=2040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.428 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.144 (n=1484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=760)
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

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.135 (n=1058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.255 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=27122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=22893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.221 (n=8663)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `8407.3041` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8407.3041 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=6182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.175 (n=5978)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=3815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=2546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.244 (n=1833)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.204)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=6021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=5099)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=6168)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=4745)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.258 (n=4755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1638)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=5887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.190 (n=3739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1925)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.184)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=1031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=1027)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `14027.0561` → IC=+0.449 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14027.0561 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.437 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=442)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `15243.1529` → IC=+0.444 (n=284)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.408 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.417 (n=154)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=30520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=34976)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.185 (n=5319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=11385)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=16366)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=14796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=5237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=12563)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=4978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=6078)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.216 (n=5032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.251 (n=6375)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=5922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5904)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.240 (n=7299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=12733)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=13951)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.29` → IC=+0.140 (n=11925)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.29 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6188)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=6332)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=7898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.77` → IC=+0.142 (n=7807)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.77 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6545)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.135 (n=8420)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.9` → IC=+0.136 (n=7872)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.9 (IC base=+0.116)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5078` → IC=+0.140 (n=20340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5078 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=20585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=14150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9738` → IC=+0.247 (n=6781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9738 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8836` → IC=+0.293 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8836 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.456` → IC=+0.191 (n=10196)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.456 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.269 (n=5562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6953 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.256 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7403` → IC=+0.235 (n=4914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7403 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=9803)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4884.9028` → IC=+0.152 (n=6780)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4884.9028 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.122 (n=12883)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0066 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5641` → IC=+0.145 (n=25740)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5641 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6775` → IC=+0.193 (n=1774)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6775 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1775` → IC=+0.196 (n=10502)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1775 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.197 (n=7162)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8561 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.230 (n=2605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4558` → IC=+0.209 (n=18212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4558 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=18187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3036` → IC=+0.215 (n=3795)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3036 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=2098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9823` → IC=+0.273 (n=1955)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9823 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.799` → IC=+0.291 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.799 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2342` → IC=+0.259 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2342 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.213 (n=4142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2047.52` → IC=+0.216 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2047.52 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.220 (n=3559)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.245 (n=1780)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0965` → IC=+0.270 (n=1308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0965 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1798)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0792` → IC=+0.276 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0792 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0726` → IC=+0.242 (n=3388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0726 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.246 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `2.254` → IC=+0.239 (n=3307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.254 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.8558` → IC=+0.243 (n=2505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8558 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=4335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.231 (n=1241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.115` → IC=+0.246 (n=1626)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.115 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.891` → IC=+0.256 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.891 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.7572` → IC=+0.234 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7572 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.733` → IC=+0.263 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.733 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.697` → IC=+0.229 (n=3296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.697 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.267 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.246 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.158 (n=3575)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0835` → IC=+0.157 (n=1358)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0835 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7097` → IC=+0.172 (n=4063)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7097 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1552` → IC=+0.152 (n=3965)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1552 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.969` → IC=+0.143 (n=3745)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.969 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6277` → IC=+0.157 (n=1355)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6277 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.159 (n=1471)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4459` → IC=+0.143 (n=3931)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4459 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5277)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.189 (n=1298)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.212 (n=2074)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.877` → IC=+0.279 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.877 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.194 (n=4103)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3497` → IC=+0.223 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3497 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7279` → IC=+0.210 (n=2027)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7279 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5540)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1910.4284` → IC=+0.201 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.4284 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.227 (n=1894)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.4676` → IC=+0.226 (n=3780)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4676 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=1956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0526` → IC=+0.267 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0526 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.654` → IC=+0.269 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.654 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3455` → IC=+0.254 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3455 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1531` → IC=+0.231 (n=2767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1531 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1893.3248` → IC=+0.223 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1893.3248 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.223 (n=4162)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=253)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5524)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.141 (n=742)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0041 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.251 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1604` → IC=+0.351 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1604 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.222` → IC=+0.216 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.222 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `1.251` → IC=+0.366 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.251 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.1652` → IC=+0.348 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1652 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.357 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.4179` → IC=+0.362 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4179 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `2.2799` → IC=+0.354 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2799 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.350 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.0866` → IC=+0.190 (n=1445)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0866 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.3644` → IC=+0.157 (n=729)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3644 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1535` → IC=+0.159 (n=2695)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1535 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.8255` → IC=+0.164 (n=1897)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8255 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.192 (n=361)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.431` → IC=+0.172 (n=914)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.431 (IC base=+0.060)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.183 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=893)

- **FILTRO** `ibs_20min` > `0.1935` → IC=-0.127 (n=5419)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1935
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=2682)

- **FILTRO** `sigma_ewma_delta_pct` > `8.253` → IC=-0.232 (n=878)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.253
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=7223)

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

- **PATRÓN** `ibs_20min` < `0.1935` → IC=+0.160 (n=2682)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1935 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.5432` → IC=+0.291 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5432 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.3228` → IC=+0.292 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3228 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.303 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6932 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` > `1.041` → IC=+0.294 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.041 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0781` → IC=+0.320 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0781 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4353` → IC=+0.304 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4353 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5251` → IC=+0.298 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5251 (IC base=-0.032)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7996` → IC=-0.159 (n=4185)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7996
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=2156)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.179 (n=1294)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=5047)

- **FILTRO** `ibs_20min` > `0.722` → IC=-0.190 (n=2184)

  - _Acción_: SKIP cuando `ibs_20min` > 0.722
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=6555)

- **PATRÓN** `ibs_20min` > `0.7996` → IC=+0.146 (n=2156)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7996 (IC base=-0.055)

- **PATRÓN** `dist_vwap_pct` > `0.4523` → IC=+0.344 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4523 (IC base=-0.055)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.320 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.324 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=-0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.5275` → IC=+0.317 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5275 (IC base=-0.055)

- **PATRÓN** `dist_vwap_pct` > `1.1009` → IC=+0.289 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1009 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` < `0.2342` → IC=+0.263 (n=2590)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2342 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.6372` → IC=+0.276 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6372 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.214` → IC=+0.278 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.214 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.280 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.270 (n=2478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.188 (n=8902)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0112 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8659` → IC=+0.284 (n=12098)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8659 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0085` → IC=+0.307 (n=1858)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0085 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.453` → IC=+0.167 (n=12010)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.453 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.280 (n=8864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6932 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2924` → IC=+0.297 (n=2194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2924 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6421` → IC=+0.289 (n=5157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6421 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.310 (n=15125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.154 (n=11781)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0093 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5158` → IC=+0.175 (n=22819)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.5158 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2049` → IC=+0.284 (n=8816)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2049 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.8573` → IC=+0.279 (n=5915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8573 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1872` → IC=+0.286 (n=2957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1872 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.322 (n=1955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4537` → IC=+0.303 (n=4398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4537 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2717` → IC=+0.305 (n=5981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2717 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.313 (n=13197)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.815` → IC=-0.147 (n=4726)

  - _Acción_: SKIP cuando `ibs_20min` < 0.815
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2435)

- **FILTRO** `ibs_20min` > `0.7` → IC=-0.242 (n=1612)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=4845)

- **FILTRO** `sigma_ewma_delta_pct` > `4.051` → IC=-0.240 (n=1354)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.051
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5103)

- **PATRÓN** `ibs_20min` > `0.815` → IC=+0.312 (n=2435)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.815 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.145` → IC=+0.174 (n=2666)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 2.145 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.331 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.292 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2229` → IC=+0.316 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2229 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.315 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1707` → IC=+0.174 (n=1616)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1707 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1562` → IC=+0.388 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1562 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6507` → IC=+0.394 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6507 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1828` → IC=+0.231 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1828 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.222 (n=2324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.246 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.230 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4611` → IC=+0.218 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4611 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `368.0` → IC=+0.233 (n=2573)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 368.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.575` → IC=+0.258 (n=2327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.575 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.018` → IC=+0.269 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.018 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.288 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.255 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.264 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.274 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 196.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.318 (n=1655)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=3664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1983)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.571` → IC=+0.306 (n=2477)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.571 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.13` → IC=+0.294 (n=3397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.13 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `3.2535` → IC=+0.301 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2535 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2023.617` → IC=+0.300 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2023.617 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.303 (n=2258)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.335 (n=2269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.328 (n=1498)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=1310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.312 (n=1542)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` < `0.0306` → IC=+0.309 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0306 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.1562` → IC=+0.320 (n=2269)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1562 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.986` → IC=+0.317 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.986 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.1986` → IC=+0.309 (n=3383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1986 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3445` → IC=+0.316 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3445 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.7404` → IC=+0.326 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7404 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `2006.8969` → IC=+0.320 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.8969 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.314 (n=3268)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1598` → IC=+0.240 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1598 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.6449` → IC=+0.235 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6449 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.173` → IC=+0.237 (n=2433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.173 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.5957` → IC=+0.235 (n=2433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5957 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.238 (n=2555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1025` → IC=+0.242 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1025 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4059` → IC=+0.244 (n=2363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4059 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4951` → IC=+0.237 (n=2111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4951 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.254 (n=2407)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.0915` → IC=+0.152 (n=1683)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0915 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.385` → IC=+0.261 (n=1983)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.385 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `1.1729` → IC=+0.263 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1729 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` > `0.6137` → IC=+0.260 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6137 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.265 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.282 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.783` → IC=+0.283 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.783 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.4173` → IC=+0.272 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4173 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.282 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.013)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.248 (n=2739)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=2755)

- **FILTRO** `ibs_20min` > `0.6053` → IC=-0.237 (n=1288)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6053
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=3882)

- **FILTRO** `sigma_ewma_delta_pct` > `8.222` → IC=-0.263 (n=592)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.222
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=4578)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.317 (n=2755)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `1.114` → IC=+0.356 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.114 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.445` → IC=+0.159 (n=2240)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.445 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.350 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.337 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6986 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.339 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.370 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7895` → IC=+0.356 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7895 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.355 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6053` → IC=+0.168 (n=3882)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6053 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.3274` → IC=+0.275 (n=2088)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3274 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.725` → IC=+0.135 (n=4053)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.725 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.6886` → IC=+0.286 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6886 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.301 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.8036` → IC=+0.286 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8036 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.293 (n=2011)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.067)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.352 (n=2567)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=3014)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` > `0.6508` → IC=+0.338 (n=2874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6508 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `0.2202` → IC=+0.337 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2202 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.768` → IC=+0.338 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.768 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `0.6288` → IC=+0.324 (n=2874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6288 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2846` → IC=+0.346 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2846 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `1.5345` → IC=+0.326 (n=2482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5345 (IC base=+0.314)

- **PATRÓN** `libro_liquidez` > `3006.6404` → IC=+0.323 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3006.6404 (IC base=+0.314)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.330 (n=3105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.319 (n=1579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.313 (n=3109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.39` → IC=+0.328 (n=3104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.39 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.296` → IC=+0.324 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.296 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2586` → IC=+0.317 (n=3050)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2586 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.088` → IC=+0.327 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.088 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.6364` → IC=+0.319 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6364 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2103` → IC=+0.338 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2103 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.361 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4149` → IC=+0.323 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4149 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1532` → IC=+0.318 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1532 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.221 (n=6501)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.127` → IC=+0.194 (n=8581)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.127 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=20277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5361` → IC=+0.229 (n=19500)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5361 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.206 (n=7386)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.716` → IC=+0.261 (n=3814)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.716 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1747` → IC=+0.152 (n=13009)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1747 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.152 (n=13009)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6206 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.208 (n=2813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6002` → IC=+0.186 (n=6334)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6002 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.192 (n=18458)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.194 (n=8591)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0062 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.187 (n=13015)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.223 (n=6505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=9396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5263` → IC=+0.238 (n=19502)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5263 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1974` → IC=+0.180 (n=14200)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1974 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.403` → IC=+0.191 (n=3067)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.403 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.489` → IC=+0.193 (n=17434)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.489 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.6995` → IC=+0.175 (n=6076)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6995 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.218 (n=2918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6335` → IC=+0.197 (n=6219)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6335 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=18478)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.265 (n=1067)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.267 (n=1067)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9421` → IC=+0.292 (n=2134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9421 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.458` → IC=+0.328 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.458 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2317` → IC=+0.283 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2317 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.8304` → IC=+0.227 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8304 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.229 (n=3063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.255 (n=2713)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.1014` → IC=+0.307 (n=1193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1014 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=2790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=2463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.0054` → IC=+0.307 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0054 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.938` → IC=+0.258 (n=2679)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.938 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.074` → IC=+0.256 (n=2260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.074 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.263 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.5521` → IC=+0.267 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5521 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.6805` → IC=+0.253 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6805 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.260 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1930.337` → IC=+0.255 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.337 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.191 (n=999)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0033 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.173 (n=996)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=3115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2499` → IC=+0.201 (n=2985)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2499 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1973` → IC=+0.211 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1973 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.546` → IC=+0.202 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.546 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.853` → IC=+0.131 (n=1991)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.853 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.0479` → IC=+0.130 (n=1354)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.0479 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.172 (n=455)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.129 (n=1294)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4558` → IC=+0.141 (n=980)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.4558 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `386.0` → IC=+0.131 (n=2911)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 386.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.183 (n=2846)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.006 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2577` → IC=+0.176 (n=2844)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2577 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.211 (n=3232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6119 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.2208` → IC=+0.177 (n=3501)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2208 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.918` → IC=+0.176 (n=593)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.918 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.013` → IC=+0.158 (n=2845)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.013 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.164 (n=3232)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2053 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0716` → IC=+0.156 (n=2707)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0716 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.144` → IC=+0.160 (n=2732)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.144 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `203.0` → IC=+0.196 (n=1344)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 203.0 (IC base=+0.154)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.231 (n=1493)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2571` → IC=+0.234 (n=2196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2571 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.285 (n=1748)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.987` → IC=+0.306 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.987 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0987` → IC=+0.209 (n=2875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0987 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.231 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7115` → IC=+0.224 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7115 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2020.5034` → IC=+0.223 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2020.5034 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.245 (n=2628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.2545` → IC=+0.266 (n=1990)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2545 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.274 (n=1138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0436` → IC=+0.292 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0436 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.76` → IC=+0.284 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.76 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.285 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.7653` → IC=+0.240 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7653 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1795` → IC=+0.251 (n=1929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1795 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1884.62` → IC=+0.247 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1884.62 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.238 (n=2890)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.195 (n=1073)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.004 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0819` → IC=+0.173 (n=1073)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0819 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2437` → IC=+0.189 (n=3214)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2437 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1492` → IC=+0.189 (n=1822)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1492 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.182` → IC=+0.203 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.182 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8368` → IC=+0.138 (n=2144)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8368 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.1749` → IC=+0.129 (n=1073)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.1749 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.179 (n=484)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5166` → IC=+0.127 (n=1385)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5166 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5007` → IC=+0.138 (n=1049)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5007 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6908.9474` → IC=+0.198 (n=1457)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6908.9474 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.128 (n=3152)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 123.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.174 (n=2301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0057 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4312` → IC=+0.150 (n=3451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4312 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6685` → IC=+0.190 (n=3451)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6685 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1727` → IC=+0.158 (n=3527)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1727 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.531` → IC=+0.143 (n=1177)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.531 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.152 (n=2301)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8509 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2914` → IC=+0.167 (n=520)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2914 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.1869` → IC=+0.136 (n=2893)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1869 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4087` → IC=+0.137 (n=3288)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4087 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `6679.7564` → IC=+0.193 (n=1564)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6679.7564 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.139 (n=3274)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 121.0 (IC base=+0.134)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.177 (n=1198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0131 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.206 (n=3599)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8001` → IC=+0.213 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8001 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.93` → IC=+0.283 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.93 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1665` → IC=+0.132 (n=3589)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1665 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.125 (n=3589)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6248 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.125 (n=3666)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2798` → IC=+0.125 (n=499)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.2798 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5435` → IC=+0.129 (n=1534)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5435 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2718.7721` → IC=+0.200 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2718.7721 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.128 (n=2298)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.152 (n=3319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0112 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.170 (n=1257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=3841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.222 (n=3770)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.148 (n=3730)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.23` → IC=+0.147 (n=3341)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.23 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.131 (n=3769)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1777 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8579` → IC=+0.125 (n=2513)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8579 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1633` → IC=+0.128 (n=3733)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1633 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.144 (n=524)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4406` → IC=+0.142 (n=1195)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4406 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4588` → IC=+0.134 (n=1194)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4588 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2614.875` → IC=+0.190 (n=1709)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2614.875 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.132 (n=3589)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 43.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.246 (n=3222)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1691` → IC=+0.241 (n=1418)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1691 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=3352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.255 (n=3224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.233 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.834` → IC=+0.228 (n=3319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.834 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.438` → IC=+0.272 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.438 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6172` → IC=+0.234 (n=3222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6172 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.266 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4865` → IC=+0.228 (n=3145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4865 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4365` → IC=+0.229 (n=3145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4365 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2628.6921` → IC=+0.232 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2628.6921 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0245` → IC=+0.252 (n=1120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0245 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6185` → IC=+0.249 (n=3356)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6185 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.297 (n=1478)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `1.1799` → IC=+0.250 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1799 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.011` → IC=+0.271 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.011 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.8647` → IC=+0.245 (n=2238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8647 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `1.0469` → IC=+0.241 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0469 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.300 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.5559` → IC=+0.240 (n=2845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5559 (IC base=+0.239)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.204 (n=1723)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1445` → IC=+0.170 (n=2258)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1445 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=5361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.658` → IC=+0.222 (n=3421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.658 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9256` → IC=+0.178 (n=783)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9256 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.206 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.162 (n=3118)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8554 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1881` → IC=+0.158 (n=1559)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1881 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1553` → IC=+0.170 (n=1321)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1553 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5265` → IC=+0.158 (n=2205)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5265 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.8055` → IC=+0.155 (n=3340)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8055 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=5636)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7159.933` → IC=+0.194 (n=2326)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7159.933 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.5895` → IC=+0.154 (n=4956)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5895 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.121 (n=5482)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 136.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.206 (n=1231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1061` → IC=+0.235 (n=541)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1061 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.229 (n=1114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.6242` → IC=+0.260 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6242 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.6873` → IC=+0.241 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6873 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.957` → IC=+0.225 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.957 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8664` → IC=+0.216 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8664 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.09` → IC=+0.214 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.09 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.210 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.4033` → IC=+0.199 (n=1207)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4033 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `13741.2485` → IC=+0.207 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13741.2485 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.149 (n=685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.2189` → IC=+0.187 (n=682)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.2189 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `170.0` → IC=+0.163 (n=672)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 170.0 (IC base=+0.067)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.239 (n=530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1325` → IC=+0.159 (n=695)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1325 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.765` → IC=+0.258 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.765 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.166 (n=755)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.954` → IC=+0.179 (n=222)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.954 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8308` → IC=+0.154 (n=1053)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8308 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2173` → IC=+0.187 (n=276)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2173 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7708` → IC=+0.158 (n=1038)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7708 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `7845.8544` → IC=+0.177 (n=716)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7845.8544 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.147 (n=522)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 30.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.123 (n=1577)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0081 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.4065` → IC=+0.183 (n=1051)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.4065 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6748` → IC=+0.144 (n=695)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6748 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.140 (n=270)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4003` → IC=+0.142 (n=512)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4003 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `5539.9883` → IC=+0.150 (n=1050)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5539.9883 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.149 (n=681)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 40.0 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.152 (n=466)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0072 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.137 (n=1397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5333` → IC=+0.184 (n=1245)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5333 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.0502` → IC=+0.149 (n=249)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 1.0502 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.867` → IC=+0.225 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.867 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.0438` → IC=+0.127 (n=1227)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0438 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2215` → IC=+0.139 (n=236)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2215 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4156` → IC=+0.152 (n=452)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4156 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `3057.0712` → IC=+0.151 (n=465)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3057.0712 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5574` → IC=+0.167 (n=1357)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.5574 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `2767.3523` → IC=+0.166 (n=699)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2767.3523 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0147` → IC=+0.234 (n=317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0147 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.31` → IC=+0.174 (n=317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.31 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.223 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.8476` → IC=+0.176 (n=418)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.8476 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.3816` → IC=+0.185 (n=475)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.3816 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.2422` → IC=+0.189 (n=226)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2422 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.534` → IC=+0.190 (n=476)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 5.534 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `1.0467` → IC=+0.243 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0467 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` < `0.2439` → IC=+0.192 (n=511)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.2439 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.193 (n=174)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.4387` → IC=+0.191 (n=445)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.4387 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.191 (n=484)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.03 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `2681.708` → IC=+0.205 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2681.708 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.176 (n=532)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0105 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.3554` → IC=+0.170 (n=355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3554 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.174 (n=468)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.186` → IC=+0.169 (n=475)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.186 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `1.2367` → IC=+0.297 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2367 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.863` → IC=+0.163 (n=574)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 4.863 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.247` → IC=+0.182 (n=532)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.247 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.1147` → IC=+0.179 (n=497)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1147 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.4975` → IC=+0.211 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4975 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `2.6497` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6497 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2230.097` → IC=+0.165 (n=475)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2230.097 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.176 (n=511)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 19.0 (IC base=+0.162)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.228 (n=8593)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=26910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9661` → IC=+0.300 (n=8596)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9661 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9558` → IC=+0.218 (n=3005)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9558 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.877` → IC=+0.260 (n=6302)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.877 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8671` → IC=+0.163 (n=11588)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8671 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.292` → IC=+0.216 (n=3380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.292 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6245` → IC=+0.194 (n=8398)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6245 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=24406)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.208 (n=8010)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1132` → IC=+0.203 (n=8003)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1132 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=8999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4883` → IC=+0.253 (n=21121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4883 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1927` → IC=+0.183 (n=15276)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1927 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.502` → IC=+0.206 (n=22377)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.502 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0517` → IC=+0.177 (n=14151)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0517 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.254 (n=3297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6241` → IC=+0.211 (n=7700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6241 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.215 (n=22903)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.275 (n=1371)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.3816` → IC=+0.236 (n=4105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3816 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8614` → IC=+0.293 (n=2737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8614 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.025` → IC=+0.301 (n=2696)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.025 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2325` → IC=+0.288 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2325 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2817` → IC=+0.243 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2817 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2047.52` → IC=+0.240 (n=1368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2047.52 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.267 (n=3771)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1286` → IC=+0.291 (n=1659)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1286 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=3913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.268 (n=3394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.4697` → IC=+0.287 (n=3318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4697 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.268 (n=3436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.292` → IC=+0.285 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.292 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5651` → IC=+0.266 (n=1599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5651 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.644` → IC=+0.271 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.644 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.270 (n=2550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.270 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.173 (n=1416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0836` → IC=+0.146 (n=1415)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0836 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.189` → IC=+0.187 (n=4243)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.189 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.741` → IC=+0.211 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.741 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.252` → IC=+0.170 (n=874)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.252 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6335` → IC=+0.155 (n=1415)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6335 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.0665` → IC=+0.143 (n=1924)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0665 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.189 (n=592)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1695` → IC=+0.144 (n=3673)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1695 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5213` → IC=+0.144 (n=3728)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5213 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `353.0` → IC=+0.148 (n=3625)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 353.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.171 (n=3315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0061 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.084` → IC=+0.172 (n=1255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.084 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6815` → IC=+0.192 (n=3760)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6815 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1555` → IC=+0.163 (n=3680)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1555 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.199` → IC=+0.151 (n=3842)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.199 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0413` → IC=+0.157 (n=3309)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0413 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.222` → IC=+0.196 (n=683)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.222 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.434` → IC=+0.151 (n=3649)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.434 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7747` → IC=+0.153 (n=2432)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7747 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=4883)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.182 (n=1206)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 212.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.240 (n=1947)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.932` → IC=+0.315 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.932 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2043` → IC=+0.232 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2043 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7568` → IC=+0.241 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7568 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1907.76` → IC=+0.237 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1907.76 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.248 (n=1837)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1859` → IC=+0.259 (n=1827)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1859 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.069` → IC=+0.297 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.069 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.906` → IC=+0.302 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.906 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.3458` → IC=+0.299 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3458 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.17` → IC=+0.256 (n=2680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.17 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2006.8969` → IC=+0.251 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.8969 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.247 (n=3953)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.244)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.190 (n=1485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.356` → IC=+0.148 (n=3920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.356 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.877` → IC=+0.267 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.877 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.151` → IC=+0.170 (n=2210)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.151 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.028` → IC=+0.165 (n=1734)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.028 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.154 (n=2970)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8567 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.201 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5173` → IC=+0.157 (n=1917)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5173 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1502` → IC=+0.146 (n=1975)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1502 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `5855.9048` → IC=+0.234 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5855.9048 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.143 (n=2895)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 85.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.170 (n=3776)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4626` → IC=+0.161 (n=3774)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4626 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5691` → IC=+0.214 (n=3321)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5691 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.6408` → IC=+0.158 (n=4363)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6408 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.065` → IC=+0.157 (n=755)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.065 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.031` → IC=+0.155 (n=3284)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.031 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.0394` → IC=+0.160 (n=3322)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0394 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2901` → IC=+0.204 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2901 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1935` → IC=+0.157 (n=3219)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1935 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5224` → IC=+0.159 (n=3268)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5224 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `6746.1912` → IC=+0.217 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6746.1912 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.172 (n=1255)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.156 (n=1514)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0132 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.6966` → IC=+0.257 (n=3028)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6966 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.8146` → IC=+0.196 (n=1020)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8146 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.192` → IC=+0.269 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.192 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2091` → IC=+0.127 (n=4542)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2091 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.123 (n=4329)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.140 (n=570)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `2.4946` → IC=+0.126 (n=4436)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.4946 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2477.4482` → IC=+0.225 (n=2059)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2477.4482 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.160 (n=3726)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0113 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1431` → IC=+0.152 (n=1411)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1431 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=2006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6607` → IC=+0.228 (n=4232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6607 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2278` → IC=+0.153 (n=3882)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2278 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.018` → IC=+0.161 (n=4111)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.018 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1918` → IC=+0.143 (n=4232)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1918 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2309` → IC=+0.200 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2309 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.163 (n=1349)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4837` → IC=+0.145 (n=1347)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4837 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2656.9872` → IC=+0.223 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2656.9872 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.152 (n=4073)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.256 (n=4146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=4336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=3712)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.304 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.2045` → IC=+0.251 (n=2118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2045 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.972` → IC=+0.295 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.972 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2159` → IC=+0.237 (n=4145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2159 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6415` → IC=+0.242 (n=4145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6415 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.255 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5127` → IC=+0.258 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5127 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=5365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2645.2136` → IC=+0.242 (n=2763)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.2136 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0248` → IC=+0.271 (n=1440)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0248 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.251 (n=4060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.1391` → IC=+0.307 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1391 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.1868` → IC=+0.250 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1868 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2319` → IC=+0.250 (n=4144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2319 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.941` → IC=+0.281 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.941 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.7123` → IC=+0.248 (n=1900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7123 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.265 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2876` → IC=+0.310 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2876 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4331` → IC=+0.249 (n=4102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4331 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.244 (n=2790)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.242 (n=2464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.5383` → IC=+0.232 (n=7389)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5383 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=7423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9283` → IC=+0.258 (n=2463)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9283 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.9629` → IC=+0.227 (n=6025)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9629 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.424` → IC=+0.233 (n=2462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.424 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.707` → IC=+0.228 (n=2300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.707 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.8813` → IC=+0.226 (n=3485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8813 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.234 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4502` → IC=+0.234 (n=2423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4502 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.229 (n=5279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3756.0694` → IC=+0.232 (n=4926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3756.0694 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.231 (n=1765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.213 (n=2391)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4157` → IC=+0.223 (n=4641)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4157 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.225 (n=2369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.7292` → IC=+0.218 (n=5275)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7292 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7156` → IC=+0.220 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7156 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2565` → IC=+0.204 (n=4628)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2565 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.715` → IC=+0.226 (n=4788)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.715 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.25` → IC=+0.211 (n=4780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.25 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.216 (n=4872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5326` → IC=+0.217 (n=2285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5326 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8167` → IC=+0.218 (n=3462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8167 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.237 (n=3473)

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

- **PATRÓN** `dist_vwap_pct` < `0.5307` → IC=+0.281 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5307 (IC base=+0.272)

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
- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.221 (n=2023)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.4737` → IC=+0.219 (n=2024)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4737 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.225 (n=1810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.472` → IC=+0.225 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.472 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.8348` → IC=+0.216 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8348 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.4248` → IC=+0.224 (n=2014)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4248 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.908` → IC=+0.223 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.908 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.216 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.218 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.215 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.1597` → IC=+0.215 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1597 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4052` → IC=+0.227 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4052 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.4955` → IC=+0.215 (n=1763)

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

- **PATRÓN** `volumen_regimen` < `1.2492` → IC=+0.213 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2492 (IC base=+0.207)

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
- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.229 (n=860)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.225 (n=430)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.299 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.535` → IC=+0.238 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.535 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.98` → IC=+0.268 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.98 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.245 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.219 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.237 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `2.4925` → IC=+0.224 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4925 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `4231.908` → IC=+0.251 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4231.908 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.255 (n=646)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.247)

- **PATRÓN** `drift_60min` |x|≤ `0.6907` → IC=+0.261 (n=968)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6907 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.267 (n=668)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` < `0.7357` → IC=+0.271 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7357 (IC base=+0.247)

- **PATRÓN** `dist_vwap_pct` < `0.332` → IC=+0.258 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.332 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.99` → IC=+0.267 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.99 (IC base=+0.247)

- **PATRÓN** `volumen_regimen` < `0.7522` → IC=+0.262 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7522 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.260 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` > `1.8448` → IC=+0.263 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8448 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.247 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `4624.342` → IC=+0.279 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4624.342 (IC base=+0.247)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.278 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.247)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.145 (n=916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0042 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.4159` → IC=+0.133 (n=2656)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.4159 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1586` → IC=+0.154 (n=1264)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1586 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.361` → IC=+0.140 (n=573)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.361 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.585` → IC=+0.175 (n=2077)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.585 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.548` → IC=+0.124 (n=915)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.548 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.183 (n=578)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.092)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.178 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0029 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.5464` → IC=+0.161 (n=689)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5464 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.166 (n=363)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.069)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.127 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0037 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0653` → IC=+0.251 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0653 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2123` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2123 (IC base=+0.055)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5205` → IC=-0.120 (n=351)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5205
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=715)

- **FILTRO** `ibs_20min` > `0.5013` → IC=-0.126 (n=263)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5013
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=511)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.152 (n=366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0043 (IC base=+0.065)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.120 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.5205` → IC=+0.160 (n=715)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5205 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1909` → IC=+0.159 (n=347)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1909 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.939` → IC=+0.167 (n=175)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.939 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.0953` → IC=+0.283 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0953 (IC base=+0.044)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.144 (n=607)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.72 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.7657` → IC=+0.158 (n=223)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.7657 (IC base=+0.035)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.176 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0102 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.195 (n=582)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.2223` → IC=+0.154 (n=571)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2223 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.907` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.907 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.1082` → IC=+0.187 (n=193)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1082 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.193 (n=151)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `1.4591` → IC=+0.139 (n=547)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4591 (IC base=+0.100)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.387 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.2953` → IC=+0.321 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2953 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.320 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.6242` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6242 (IC base=+0.308)

- **PATRÓN** `dist_vwap_pct` > `0.4912` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4912 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.192` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.192 (IC base=+0.308)

- **PATRÓN** `volumen_regimen` < `0.9596` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9596 (IC base=+0.308)

- **PATRÓN** `volumen_regimen` > `0.6039` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6039 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.0521` → IC=+0.349 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0521 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` < `2.5568` → IC=+0.345 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5568 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.0841` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0841 (IC base=+0.308)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.308)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.354 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0122 (IC base=+0.328)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.325 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.328)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.398 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.328)

- **PATRÓN** `ibs_20min` < `0.1481` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1481 (IC base=+0.328)

- **PATRÓN** `ibs_20min` > `0.3556` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3556 (IC base=+0.328)

- **PATRÓN** `dist_vwap_pct` < `0.6346` → IC=+0.359 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6346 (IC base=+0.328)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.709` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.709 (IC base=+0.328)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.373 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6258 (IC base=+0.328)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.382 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.328)

- **PATRÓN** `volumen_spike_ratio` < `1.501` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.501 (IC base=+0.328)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `40.2712` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 40.2712 (IC base=+0.328)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0062` → IC=-0.249 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=210)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=321)

- **FILTRO** `dist_vwap_pct` > `0.2613` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2613
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=400)

- **FILTRO** `volumen_regimen` < `0.8729` → IC=-0.304 (n=136)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8729
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
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=99)

- **FILTRO** `ibs_20min` < `0.018` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.018
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=97)

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

- **FILTRO** `libro_spread` > `0.05` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.05
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=50)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2727` → IC=-0.161 (n=334)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=1004)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.231 (n=578)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.6871` → IC=+0.204 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6871 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.8858` → IC=+0.309 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8858 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.61` → IC=+0.188 (n=376)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.61 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6243` → IC=+0.192 (n=287)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6243 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.1982` → IC=+0.171 (n=287)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1982 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` < `0.0674` → IC=+0.192 (n=653)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0674 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.206 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.166)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.151 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0066 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.7986` → IC=+0.153 (n=217)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.7986 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.7218` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7218 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2693` → IC=+0.131 (n=448)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2693 (IC base=+0.069)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.287 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.297 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.268)

- **PATRÓN** `dist_vwap_pct` > `0.7916` → IC=+0.404 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7916 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.268)

- **PATRÓN** `volumen_regimen` < `0.8033` → IC=+0.296 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8033 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.311 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.318 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.3612` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3612 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.274 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.268)

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
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=290)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=235)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=290)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1513)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `liq_n` > 2.0 (IC base=+0.092)

- **PATRÓN** `liq_usd_total` > `153.37` → IC=+0.124 (n=155)

  - _Acción_: Kelly boost +0.62€ cuando `liq_usd_total` > 153.37 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.092)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.5 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.092)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.150 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=84)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=107)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.186 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 8.0 (IC base=+0.081)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4254)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=249)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=206)

- **FILTRO** `ballena_activa_n` > `59.0` → IC=-0.195 (n=80)

  - _Acción_: SKIP cuando `ballena_activa_n` > 59.0
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=156)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.177 (n=156)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 59.0 (IC base=+0.015)

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
- **PATRÓN** `liq_n` > `3.0` → IC=+0.320 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.184)

- **PATRÓN** `liq_usd_total` > `211.68` → IC=+0.238 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 211.68 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.206 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.218 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.184)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1670)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=1624)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=761)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=770)

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
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=1158)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=1158)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1566)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1566)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=366)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=366)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.144 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=296)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=413)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=462)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=338)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=439)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=439)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=435)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.130 (n=3607)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=9314)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.145 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=143)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.163 (n=434)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1043)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.143 (n=345)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=934)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.145 (n=446)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.51 (IC base=-0.006)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.136 (n=201)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=462)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.122 (n=503)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=528)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=738)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=783)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.139 (n=364)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=778)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.126 (n=346)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=934)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.126 (n=589)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=629)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.131 (n=640)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=749)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.179 (n=9265)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=28947)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=9643)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=29864)

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
- **FILTRO** `py_entrada` > `0.575` → IC=-0.176 (n=1365)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4189)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.179 (n=1392)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4262)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3362)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4314)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=953)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=25861)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=58622)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20579)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=63904)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27786)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=56697)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.155 (n=28535)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=55948)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26185)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=79463)

- **FILTRO** `ibs_7min` > `0.2783` → IC=-0.183 (n=26405)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2783
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=79243)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=3369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=10620)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3417)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10572)

- **FILTRO** `ibs_7min` < `0.7112` → IC=-0.215 (n=3497)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7112
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10492)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.204 (n=3486)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10503)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=3268)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=11053)

- **FILTRO** `ibs_7min` > `0.2637` → IC=-0.189 (n=3580)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2637
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10741)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.178 (n=3573)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10748)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.121 (n=4479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=9189)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=3108)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10560)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.202 (n=3415)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10253)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.200 (n=3366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=10302)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=3310)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=10882)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.177 (n=3546)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=10646)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.172 (n=3470)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10722)

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
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=680)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=931)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=356)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=473)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=594)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=255)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=503)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=555)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.143 (n=772)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1540)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.168 (n=567)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 453.526 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3672.897` → IC=+0.130 (n=771)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3672.897 (IC base=+0.124)

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
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.134 (n=356)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=330)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.116)

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
- **PATRÓN** `delta_ratio` |x|> `0.4315` → IC=+0.207 (n=131)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4315 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.153 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.180 (n=192)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4761.643 (IC base=+0.131)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.131 (n=312)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=218)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.1729` → IC=-0.222 (n=88)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.1729
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=171)

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
- **FILTRO** `sigma_h` < `0.0164` → IC=-0.192 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0164
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `130.5499` → IC=-0.255 (n=651)

  - _Acción_: SKIP cuando `T_h` < 130.5499
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=218)

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

- **PATRÓN** `edge` > `0.0995` → IC=+0.427 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0995 (IC base=+0.391)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.405 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.391)

- **PATRÓN** `dist_50` > `0.3717` → IC=+0.440 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3717 (IC base=+0.391)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.391)

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

- **PATRÓN** `edge` > `0.1954` → IC=+0.472 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1954 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.475 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.4192` → IC=+0.481 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4192 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=489)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=523)

- **PATRÓN** `streak_estiramiento` < `0.3778` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `streak_estiramiento` < 0.3778 (IC base=+0.020)

- **PATRÓN** `streak_estiramiento` < `0.829` → IC=+0.124 (n=362)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.829 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.121 (n=275)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 29.0 (IC base=+0.058)

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
- **PATRÓN** `streak_estiramiento` < `0.3762` → IC=+0.125 (n=126)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.3762 (IC base=+0.037)

- **PATRÓN** `streak_estiramiento` < `0.5965` → IC=+0.156 (n=184)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.5965 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.138 (n=197)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 35.0 (IC base=+0.083)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=101)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=121)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=57)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=42)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

- **FILTRO** `streak_estiramiento` > `0.6393` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6393
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=30)

- **PATRÓN** `streak_estiramiento` < `0.6393` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6393 (IC base=+0.010)

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
- **PATRÓN** `streak_estiramiento` < `0.6279` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6279 (IC base=+0.032)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1107)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1355)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5555)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3368)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.185 (n=2187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2329` → IC=+0.158 (n=6559)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2329 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1235` → IC=+0.133 (n=6559)

  - _Acción_: Kelly boost +0.67€ cuando `drift_15min` |x|≤ 1.1235 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.132 (n=6560)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1` → IC=+0.145 (n=2068)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=6069)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.5542` → IC=+0.208 (n=5860)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5542 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.996` → IC=+0.232 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.996 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3438)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4305.62` → IC=+0.171 (n=2187)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4305.62 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2525)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.252 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.247 (n=390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.227 (n=295)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.206)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2257` → IC=+0.217 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2257 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.275 (n=885)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.3997` → IC=+0.232 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3997 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5531` → IC=+0.208 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5531 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.238` → IC=+0.298 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.238 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `11836.5406` → IC=+0.223 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11836.5406 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.148 (n=998)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0067 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.148 (n=756)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0836` → IC=+0.137 (n=1013)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.0836 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.4799` → IC=+0.218 (n=1134)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4799 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1241` → IC=+0.146 (n=713)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1241 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.6745` → IC=+0.133 (n=1285)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.6745 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.949` → IC=+0.286 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.949 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6114.254` → IC=+0.174 (n=514)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6114.254 (IC base=+0.133)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8346` → IC=+0.149 (n=674)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` > 0.8346 (IC base=+0.046)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.143 (n=1665)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0119 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2395` → IC=+0.174 (n=1666)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2395 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0581` → IC=+0.141 (n=1665)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0581 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.186 (n=521)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=1521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=1541)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6981` → IC=+0.232 (n=1110)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6981 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2145` → IC=+0.146 (n=763)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.2145 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.9054` → IC=+0.141 (n=1918)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.9054 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.0` → IC=+0.189 (n=384)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 17.0 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2945.7354` → IC=+0.182 (n=755)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2945.7354 (IC base=+0.137)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.387 (n=369)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1089` → IC=+0.364 (n=543)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1089 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.377 (n=542)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1057` → IC=+0.377 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1057 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7881` → IC=+0.395 (n=813)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7881 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.2719` → IC=+0.383 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2719 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.84` → IC=+0.397 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.84 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.376 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9610.6074 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.364 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.364 (n=343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.362 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2167` → IC=+0.377 (n=177)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2167 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.398 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.362 (n=396)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.383 (n=390)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.394 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.679` → IC=+0.383 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.679 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `16412.1684` → IC=+0.386 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16412.1684 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.384 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 409.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.364 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.377 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.367 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1264` → IC=+0.377 (n=283)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1264 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2929` → IC=+0.371 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2929 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.369 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.399 (n=424)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.377 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.6907` → IC=+0.364 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6907 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.857` → IC=+0.399 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.857 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.587` → IC=+0.365 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.587 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `4309.2693` → IC=+0.377 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4309.2693 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2702)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3405)

- **FILTRO** `libro_liquidez` < `4383.3565` → IC=-0.172 (n=4030)

  - _Acción_: SKIP cuando `libro_liquidez` < 4383.3565
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=2077)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1398` → IC=+0.215 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1398 (IC base=-0.088)

- **PATRÓN** `ibs_15` > `0.6285` → IC=+0.279 (n=1341)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6285 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.208 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1169 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` < `0.6021` → IC=+0.197 (n=1419)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.6021 (IC base=-0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2282` → IC=+0.268 (n=2005)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2282 (IC base=+0.002)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.282 (n=6023)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.7093` → IC=+0.264 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7093 (IC base=+0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.074` → IC=-0.240 (n=2001)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=2006)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.209 (n=1001)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=3006)

- **FILTRO** `sigma_ewma_delta_pct` > `22.231` → IC=-0.243 (n=566)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.231
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3441)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.181 (n=89)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=3918)

- **FILTRO** `libro_liquidez` < `10151.808` → IC=-0.194 (n=1322)

  - _Acción_: SKIP cuando `libro_liquidez` < 10151.808
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2685)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.144 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0033 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.273 (n=161)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.285 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.064)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.318 (n=481)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1067` → IC=+0.286 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1067 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.5498` → IC=+0.284 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5498 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.8` → IC=+0.142 (n=241)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 21.8 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.223 (n=81)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.181)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0902` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0902 (IC base=-0.181)

- **PATRÓN** `ibs_15` < `0.6283` → IC=+0.286 (n=82)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6283 (IC base=-0.181)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.276 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.181)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.309 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.181)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=883)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.162 (n=676)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0066 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.173 (n=298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.187 (n=534)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5656` → IC=+0.241 (n=675)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5656 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6818` → IC=+0.187 (n=132)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6818 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.588` → IC=+0.258 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.588 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=883)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5210.4456` → IC=+0.168 (n=450)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5210.4456 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.257 (n=1032)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.483` → IC=+0.242 (n=2345)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.483 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `0.8255` → IC=+0.248 (n=2064)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8255 (IC base=+0.236)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1989` → IC=+0.257 (n=1063)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1989 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.239 (n=1601)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.236)

- **PATRÓN** `ibs_15` < `0.3913` → IC=+0.268 (n=2345)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3913 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.2392` → IC=+0.246 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2392 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.514` → IC=+0.243 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.514 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.361` → IC=+0.238 (n=2467)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.361 (IC base=+0.236)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2006` → IC=-0.299 (n=366)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2006
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1101)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.282 (n=498)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=969)

- **FILTRO** `drift_15min` |x|> `1.0221` → IC=-0.304 (n=366)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0221
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=1101)

- **FILTRO** `sigma_ewma_delta_pct` > `5.969` → IC=-0.213 (n=322)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.969
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1145)

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

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.297 (n=995)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2022` → IC=+0.257 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2022 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0143` → IC=-0.250 (n=1147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0143
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=565)

- **FILTRO** `drift_60min` |x|> `0.1226` → IC=-0.243 (n=582)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=1130)

- **FILTRO** `drift_15min` |x|> `1.3055` → IC=-0.283 (n=427)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.3055
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=1285)

- **FILTRO** `sigma_ewma_delta_pct` > `7.243` → IC=-0.225 (n=518)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.243
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=1194)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=1691)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.283 (n=1247)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=-0.008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.288 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3297` → IC=+0.292 (n=1395)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3297 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.786` → IC=+0.325 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.786 (IC base=-0.008)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.146 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0068 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.159 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.306 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1952` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.1952 (IC base=+0.050)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.146 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0068 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.159 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.306 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1952` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.1952 (IC base=+0.050)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.302 (n=497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.294 (n=497)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.310 (n=497)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0688` → IC=+0.285 (n=1488)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0688 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.218` → IC=+0.289 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.218 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=1549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8361` → IC=+0.310 (n=1491)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8361 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2762` → IC=+0.316 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2762 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.742` → IC=+0.386 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.742 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `13081.1746` → IC=+0.300 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13081.1746 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.307 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.280 (n=262)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.298 (n=345)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.278)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.280 (n=262)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.286 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.301 (n=723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.9658` → IC=+0.335 (n=356)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9658 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2612` → IC=+0.310 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2612 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.592` → IC=+0.391 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.592 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `14498.4435` → IC=+0.307 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14498.4435 (IC base=+0.278)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.299 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.324 (n=236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.065` → IC=+0.293 (n=705)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.065 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.312 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8447` → IC=+0.316 (n=705)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8447 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.315 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2918 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.381 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.291)

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
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=383)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.209 (n=84)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=165)

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

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.235 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=32)

- **FILTRO** `drift_15min` |x|> `0.5336` → IC=-0.239 (n=21)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5336
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=43)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5542 sube el IC de +0.132 a +0.208 en UPDOWN_GBM#15min (n=5860). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.206 a +0.275 en UPDOWN_GBM#BTC#15min (n=885). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4799 sube el IC de +0.133 a +0.218 en UPDOWN_GBM#ETH#15min (n=1134). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.6981 sube el IC de +0.137 a +0.232 en UPDOWN_GBM#XRP#15min (n=1110). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6285 sube el IC de -0.088 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1341). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.002 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=6023). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.064 a +0.318 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=481). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.181 a +0.286 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=82). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5656 sube el IC de +0.147 a +0.241 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=675). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3913 sube el IC de +0.236 a +0.268 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2345). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.026 a +0.297 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=995). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3297 sube el IC de -0.008 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1395). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.088 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7 (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.088 a +0.306 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8361 sube el IC de +0.285 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1491). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9658 sube el IC de +0.278 a +0.335 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=356). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8447 sube el IC de +0.291 a +0.316 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=705). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7881 sube el IC de +0.364 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=813). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.362 a +0.383 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.364 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=424). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2349 | +0.085 | +259.69€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2349 | +0.085 | +259.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1937 | +0.086 | +220.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1937 | +0.086 | +220.20€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1482 | -0.030 | +54.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1482 | -0.030 | +54.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1158 | -0.042 | +41.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1158 | -0.042 | +41.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51464 | -0.087 | -6598.91€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3377 | +0.095 | -317.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48087 | -0.099 | -6281.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3377 | +0.095 | -317.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3377 | +0.095 | -317.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14298 | -0.044 | -1336.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14298 | -0.044 | -1336.99€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 56870 | -0.012 | +2608.39€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14666 | +0.003 | +1453.15€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 42204 | -0.017 | +1155.24€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 56870 | -0.012 | +2608.39€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14666 | +0.003 | +1453.15€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 42204 | -0.017 | +1155.24€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 212028 | +0.112 | -8592.08€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23387 | +0.179 | -741.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 990 | +0.020 | -80.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 175611 | +0.105 | -7367.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12040 | +0.095 | -402.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 29120 | +0.101 | -2081.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 87 | -0.197 | +9.66€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 28996 | +0.102 | -2101.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 39707 | +0.123 | -603.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5713 | +0.177 | -227.19€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 29070 | +0.120 | -192.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4882 | +0.081 | -161.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 29165 | +0.098 | -2039.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 105 | -0.098 | +23.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 29033 | +0.099 | -2056.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 12 | -0.043 | +5.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 45372 | +0.124 | -937.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11294 | +0.178 | -314.95€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 29537 | +0.106 | -527.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4529 | +0.102 | -86.09€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 39532 | +0.111 | -1683.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6088 | +0.200 | -245.22€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 893 | +0.044 | -26.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 29959 | +0.096 | -1227.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2592 | +0.107 | -184.38€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 29132 | +0.106 | -1247.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 100 | -0.137 | +13.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 29016 | +0.107 | -1262.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 34525 | +0.189 | -2593.08€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 34525 | +0.189 | -2593.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7825 | +0.161 | -932.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7825 | +0.161 | -932.08€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5183 | +0.194 | -222.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5183 | +0.194 | -222.03€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7632 | +0.172 | -705.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7632 | +0.172 | -705.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6322 | +0.252 | -216.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6322 | +0.252 | -216.87€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7484 | +0.183 | -530.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7484 | +0.183 | -530.29€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1332 | +0.425 | -50.57€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1332 | +0.425 | -50.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 568 | +0.439 | -5.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 568 | +0.439 | -5.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 222 | +0.402 | -17.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 222 | +0.402 | -17.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 122095 | +0.199 | -8920.89€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 122095 | +0.199 | -8920.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21169 | +0.175 | -2508.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21169 | +0.175 | -2508.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19670 | +0.224 | -650.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19670 | +0.224 | -650.19€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 20943 | +0.180 | -2202.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 20943 | +0.180 | -2202.62€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19850 | +0.217 | -784.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19850 | +0.217 | -784.46€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20137 | +0.206 | -1172.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20137 | +0.206 | -1172.22€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20326 | +0.197 | -1602.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20326 | +0.197 | -1602.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 47472 | +0.116 | +396.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 47472 | +0.116 | +396.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 23638 | +0.117 | +262.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 23638 | +0.117 | +262.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 23834 | +0.116 | +133.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 23834 | +0.116 | +133.85€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2052 | +0.063 | -107.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1327 | +0.073 | -43.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1618 | +0.069 | -62.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1327 | +0.073 | -43.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 97011 | +0.101 | -2002.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7873 | +0.098 | +193.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 89138 | +0.101 | -2196.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 52945 | +0.105 | -426.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7873 | +0.098 | +193.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 45072 | +0.107 | -619.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 20859 | +0.110 | -56.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 20859 | +0.110 | -56.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 23207 | +0.083 | -1520.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 23207 | +0.083 | -1520.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ GBM_LATE_15M | 66106 | +0.102 | +37272.81€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 66106 | +0.102 | +37272.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10976 | +0.225 | +9434.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10976 | +0.225 | +9434.03€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 10335 | +0.177 | +8344.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10335 | +0.177 | +8344.72€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 11821 | +0.207 | +9343.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11821 | +0.207 | +9343.42€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8738 | +0.063 | +2978.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8738 | +0.063 | +2978.38€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 9156 | -0.026 | +2364.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9156 | -0.026 | +2364.33€ | 3 | 15 |
| ✅ GBM_LATE_15M#XRP | 15080 | -0.019 | +4807.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15080 | -0.019 | +4807.93€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 70146 | +0.088 | +41110.73€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 70146 | +0.088 | +41110.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13618 | -0.002 | +7142.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13618 | -0.002 | +7142.37€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15087 | +0.007 | +4181.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15087 | +0.007 | +4181.50€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9399 | +0.296 | +10802.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9399 | +0.296 | +10802.17€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13412 | +0.019 | +4297.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13412 | +0.019 | +4297.35€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10664 | +0.051 | +4988.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10664 | +0.051 | +4988.32€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7966 | +0.314 | +9699.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7966 | +0.314 | +9699.01€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 52000 | +0.180 | +43349.34€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 52000 | +0.180 | +43349.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7880 | +0.240 | +7347.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7880 | +0.240 | +7347.20€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8289 | +0.141 | +6247.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8289 | +0.141 | +6247.14€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8368 | +0.224 | +7247.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8368 | +0.224 | +7247.89€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8885 | +0.131 | +6982.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8885 | +0.131 | +6982.50€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9810 | +0.124 | +7601.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9810 | +0.124 | +7601.46€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8768 | +0.233 | +7923.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8768 | +0.233 | +7923.14€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14350 | +0.126 | +7348.37€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14350 | +0.126 | +7348.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 678 | +0.162 | +445.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3704 | +0.125 | +1999.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3704 | +0.125 | +1999.62€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4205 | +0.128 | +2141.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4205 | +0.128 | +2141.01€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3913 | +0.102 | +1625.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3913 | +0.102 | +1625.34€ | 0 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1341 | +0.168 | +850.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1341 | +0.168 | +850.38€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 66360 | +0.190 | +55422.12€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 66360 | +0.190 | +55422.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10497 | +0.249 | +10117.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10497 | +0.249 | +10117.15€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10669 | +0.143 | +7781.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10669 | +0.143 | +7781.72€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11248 | +0.234 | +10144.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11248 | +0.234 | +10144.64€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10969 | +0.146 | +8300.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10969 | +0.146 | +8300.46€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11697 | +0.129 | +8587.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11697 | +0.129 | +8587.86€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11280 | +0.241 | +10490.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11280 | +0.241 | +10490.30€ | 0 | 23 |
| ✅ GBM_LATE_5M | 16882 | +0.219 | +14260.63€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 16882 | +0.219 | +14260.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3331 | +0.210 | +2855.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3331 | +0.210 | +2855.10€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1591 | +0.218 | +1323.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1591 | +0.218 | +1323.18€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4883 | +0.210 | +3844.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4883 | +0.210 | +3844.36€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3008 | +0.230 | +2671.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3008 | +0.230 | +2671.51€ | 0 | 24 |
| ✅ GBM_LATE_5M#XRP | 2121 | +0.209 | +1667.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2121 | +0.209 | +1667.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6533 | +0.079 | +2240.08€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 6533 | +0.079 | +2240.08€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 171 | +0.263 | +183.72€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 171 | +0.263 | +183.72€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2055 | +0.062 | +630.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2055 | +0.062 | +630.40€ | 0 | 6 |
| ✅ GBM_LATE_60M#DOGE | 166 | +0.321 | +206.85€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 166 | +0.321 | +206.85€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1910 | +0.056 | +600.14€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1910 | +0.056 | +600.14€ | 2 | 6 |
| ✅ GBM_LATE_60M#SOL | 2064 | +0.061 | +419.32€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2064 | +0.061 | +419.32€ | 0 | 9 |
| ✅ GBM_LATE_60M#XRP | 167 | +0.323 | +199.64€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 167 | +0.323 | +199.64€ | 0 | 24 |
| 🚫 GBM_LATE_60M_FADE | 802 | -0.244 | -31.62€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 802 | -0.244 | -31.62€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 281 | -0.253 | -18.78€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 281 | -0.253 | -18.78€ | 4 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 277 | -0.242 | -7.42€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 277 | -0.242 | -7.42€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 219 | -0.247 | -9.19€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 219 | -0.247 | -9.19€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2492 | +0.087 | +648.25€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2492 | +0.087 | +648.25€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 920 | +0.069 | +233.46€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 920 | +0.069 | +233.46€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 15 | +0.066 | +5.23€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 15 | +0.066 | +5.23€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 832 | +0.053 | +160.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 832 | +0.053 | +160.11€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 670 | +0.150 | +237.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 670 | +0.150 | +237.75€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 55 | +0.114 | +11.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 55 | +0.114 | +11.70€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 425 | +0.306 | +505.51€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 425 | +0.306 | +505.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 425 | +0.306 | +505.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 425 | +0.306 | +505.51€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4948 | +0.095 | +1077.67€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4948 | +0.095 | +1077.67€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4948 | +0.095 | +1077.67€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4948 | +0.095 | +1077.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1840 | +0.021 | +107.51€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1840 | +0.021 | +107.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 232 | +0.090 | +45.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 232 | +0.090 | +45.38€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M#BTC | 350 | -0.006 | +9.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 350 | -0.006 | +9.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 132 | +0.045 | +22.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 132 | +0.045 | +22.40€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 409 | +0.025 | +22.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 409 | +0.025 | +22.02€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 356 | -0.020 | +0.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 356 | -0.020 | +0.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 361 | +0.029 | +6.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 361 | +0.029 | +6.85€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4609 | +0.018 | +200.58€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4609 | +0.018 | +200.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 867 | +0.015 | +49.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 867 | +0.015 | +49.10€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 347 | +0.067 | +89.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 347 | +0.067 | +89.56€ | 0 | 4 |
| ✅ LIQUIDACIONES_5M#ETH | 1722 | +0.022 | +35.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1722 | +0.022 | +35.81€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 811 | +0.017 | +7.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 811 | +0.017 | +7.48€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 621 | -0.006 | +24.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 621 | -0.006 | +24.80€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2819 | -0.035 | -8.74€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2819 | -0.035 | -8.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 858 | -0.038 | -17.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 858 | -0.038 | -17.93€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1018 | -0.016 | +18.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1018 | -0.016 | +18.62€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 919 | -0.054 | -9.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 919 | -0.054 | -9.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 19 | +0.068 | +1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 19 | +0.068 | +1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 21298 | -0.032 | -209.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10324 | -0.033 | -122.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 10974 | -0.031 | -86.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 753 | -0.054 | -42.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 385 | -0.040 | -8.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 368 | -0.068 | -33.81€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5743 | -0.026 | -23.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2738 | -0.023 | +5.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3005 | -0.028 | -28.48€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1943 | -0.033 | -8.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 996 | -0.040 | -24.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 947 | -0.026 | +15.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4879 | -0.033 | -67.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2350 | -0.030 | -18.81€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2529 | -0.035 | -48.86€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4052 | -0.024 | +50.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1979 | -0.029 | +1.50€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2073 | -0.019 | +49.26€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3928 | -0.044 | -119.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1876 | -0.050 | -78.17€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2052 | -0.038 | -41.00€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 77719 | -0.000 | +4190.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 77719 | -0.000 | +4190.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10799 | -0.038 | -149.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10799 | -0.038 | -149.81€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10786 | -0.053 | -281.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10786 | -0.053 | -281.01€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7484 | -0.052 | -106.06€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7484 | -0.052 | -106.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2150 | -0.058 | -17.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2150 | -0.058 | -17.93€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 821 | -0.116 | -32.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 821 | -0.116 | -32.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2270 | -0.066 | -12.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2270 | -0.066 | -12.47€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 190131 | -0.078 | +2121.65€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 190131 | -0.078 | +2121.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 28310 | -0.102 | -1437.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 28310 | -0.102 | -1437.94€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 27860 | -0.101 | -999.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 27860 | -0.101 | -999.54€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9384 | -0.035 | -185.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9384 | -0.035 | -185.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1012 | -0.017 | -19.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1012 | -0.017 | -19.26€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2203 | -0.046 | -28.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2203 | -0.046 | -28.64€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2682 | -0.024 | -31.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2682 | -0.024 | -31.64€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1309 | -0.063 | -30.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1309 | -0.063 | -30.43€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1169 | -0.040 | -44.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1169 | -0.040 | -44.03€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2403 | +0.120 | +967.73€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2267 | +0.124 | +955.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 524 | +0.144 | +278.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 524 | +0.144 | +278.06€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 474 | +0.116 | +164.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 474 | +0.116 | +164.52€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 415 | +0.128 | +191.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 415 | +0.128 | +191.95€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 383 | +0.131 | +182.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 383 | +0.131 | +182.69€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 471 | +0.098 | +137.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 471 | +0.098 | +137.92€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2530 | -0.022 | -50.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2530 | -0.022 | -50.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 447 | +0.006 | +20.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 447 | +0.006 | +20.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 461 | -0.049 | -31.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 461 | -0.049 | -31.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 612 | -0.044 | -42.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 612 | -0.044 | -42.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 527 | -0.007 | -3.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 527 | -0.007 | -3.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 483 | -0.013 | +7.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 483 | -0.013 | +7.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1345 | -0.043 | +132.29€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 622 | -0.069 | +24.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 484 | -0.066 | +49.83€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 138 | -0.079 | -24.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 474 | -0.011 | +72.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 343 | +0.007 | +82.02€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 131 | -0.056 | -9.68€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 249 | -0.042 | +34.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 212 | -0.037 | +33.09€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 37 | -0.064 | +1.90€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1039 | -0.036 | +164.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 306 | -0.068 | -32.65€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1698 | -0.185 | -37.88€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 672 | -0.172 | -8.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 593 | -0.171 | -5.74€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 79 | -0.179 | -3.17€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 571 | -0.198 | -32.97€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 502 | -0.204 | -38.08€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 69 | -0.148 | +5.11€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 455 | -0.187 | +4.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 422 | -0.182 | +3.38€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 33 | -0.243 | +0.62€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1517 | -0.185 | -40.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 181 | -0.183 | +2.56€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 599 | +0.377 | +537.87€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 137 | +0.176 | +100.99€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 137 | +0.176 | +100.99€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 138 | +0.371 | +107.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 138 | +0.371 | +107.96€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 324 | +0.460 | +328.92€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 324 | +0.460 | +328.92€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#sniper | 599 | +0.377 | +537.87€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1050 | +0.040 | +85.68€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1050 | +0.040 | +85.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 80 | +0.024 | +1.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 80 | +0.024 | +1.80€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 526 | +0.061 | +73.93€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 526 | +0.061 | +73.93€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3659 | -0.023 | -143.88€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3659 | -0.023 | -143.88€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1129 | -0.022 | -40.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1129 | -0.022 | -40.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 630 | -0.029 | -27.42€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 630 | -0.029 | -27.42€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 177 | -0.048 | -15.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 177 | -0.048 | -15.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1723 | -0.019 | -60.49€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1723 | -0.019 | -60.49€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 152 | +0.006 | -1.21€ | 2 | 1 |
| ✅ STREAK_FADE_60M#60min | 152 | +0.006 | -1.21€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB | 7 | +0.097 | +7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB#60min | 7 | +0.097 | +7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 51 | -0.028 | -2.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 51 | -0.028 | -2.40€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 86 | -0.011 | -7.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 86 | -0.011 | -7.31€ | 0 | 1 |
| ✅ STREAK_FADE_60M#XRP | 5 | +0.018 | -0.23€ | 0 | 0 |
| ✅ STREAK_FADE_60M#XRP#60min | 5 | +0.018 | -0.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 11704 | +0.013 | +62.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11704 | +0.013 | +62.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3009 | +0.017 | +21.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3009 | +0.017 | +21.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3122 | +0.012 | +23.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3122 | +0.012 | +23.02€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2951 | +0.009 | -0.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2951 | +0.009 | -0.72€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2622 | +0.014 | +18.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2622 | +0.014 | +18.81€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13923 | +0.019 | +8.15€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13923 | +0.019 | +8.15€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5574 | +0.021 | +8.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5574 | +0.021 | +8.21€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4947 | +0.019 | +4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4947 | +0.019 | +4.68€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3402 | +0.014 | -4.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3402 | +0.014 | -4.74€ | 1 | 0 |
| ✅ UPDOWN_GBM | 125872 | +0.060 | +12058.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 31442 | +0.077 | +6164.23€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3570 | -0.001 | +39.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 82974 | +0.062 | +5724.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7456 | -0.002 | +131.93€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10989 | +0.104 | +2043.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2089 | +0.165 | +977.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8810 | +0.091 | +1067.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 28427 | +0.057 | +2512.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4201 | +0.081 | +946.16€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1050 | +0.000 | +21.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19644 | +0.066 | +1457.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3378 | -0.004 | +83.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 154 | -0.064 | +4.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14124 | +0.074 | +1570.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11954 | +0.061 | +677.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 29478 | +0.049 | +2112.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7276 | +0.071 | +1143.99€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1016 | +0.005 | +15.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18269 | +0.052 | +909.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2773 | -0.002 | +41.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 144 | -0.096 | +2.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26028 | +0.041 | +1501.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8503 | +0.032 | +482.31€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 931 | -0.011 | +7.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15163 | +0.054 | +1011.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1301 | +0.003 | +7.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 130 | -0.136 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16824 | +0.073 | +2319.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7289 | +0.088 | +1720.42€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9134 | +0.064 | +601.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 428 | -0.098 | -0.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1084 | +0.364 | +413.61€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1084 | +0.364 | +413.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 519 | +0.362 | +185.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 519 | +0.362 | +185.56€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 565 | +0.364 | +228.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 565 | +0.364 | +228.05€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 29775 | -0.017 | +7474.73€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 29775 | -0.017 | +7474.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2345 | -0.044 | +633.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2345 | -0.044 | +633.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5479 | -0.115 | +310.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5479 | -0.115 | +310.47€ | 5 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4026 | +0.216 | +2538.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4026 | +0.216 | +2538.13€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8360 | -0.058 | +1261.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8360 | -0.058 | +1261.89€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8271 | -0.052 | +1668.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8271 | -0.052 | +1668.00€ | 5 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 372 | +0.059 | +32.67€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 372 | +0.059 | +32.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 372 | +0.059 | +32.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 372 | +0.059 | +32.67€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1985 | +0.285 | +1699.05€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1985 | +0.285 | +1699.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1045 | +0.278 | +843.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1045 | +0.278 | +843.08€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 940 | +0.291 | +855.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 940 | +0.291 | +855.96€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 902 | -0.121 | -96.29€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 902 | -0.121 | -96.29€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 290 | -0.086 | -23.04€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 290 | -0.086 | -23.04€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 124 | -0.198 | -9.07€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 124 | -0.198 | -9.07€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5424 | +0.291 | +2360.42€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2122 | +0.247 | +323.50€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2098 | +0.284 | +868.54€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1204 | +0.381 | +1168.38€ | 0 | 1 |