# Hipótesis automáticas — 2026-11-26 01:26 UTC
_Generado por shadow_postmortem.py sobre 1497002 resoluciones (PNL=+212268.04€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=735)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1120)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `60.0` → IC=+0.173 (n=362)

  - _Acción_: Kelly boost +0.87€ cuando `n_total_lado` > 60.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8116` → IC=+0.266 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8116 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.202` → IC=+0.193 (n=353)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.202 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=1068)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1149)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.124)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=565)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=983)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.184 (n=315)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 62.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.817` → IC=+0.280 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.817 (IC base=+0.126)

- **PATRÓN** `banda_z` > `8.273` → IC=+0.196 (n=310)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.273 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.138 (n=838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1049)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `5101.7817` → IC=+0.130 (n=420)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 5101.7817 (IC base=+0.126)

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
- **FILTRO** `restante_s_al_confirmar` < `130.53` → IC=-0.219 (n=12922)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.53
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=38770)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.15` → IC=-0.159 (n=3624)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.15
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=10877)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=31060)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7720.8875` → IC=+0.151 (n=2524)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7720.8875 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=27727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=33412)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=24930)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=8958)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `6245.3024` → IC=+0.135 (n=3525)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 6245.3024 (IC base=+0.123)

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
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=688)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.121 (n=2241)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.45 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=5709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.378 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=2739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.328 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=3182)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.192)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=1312)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.243 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1215)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2036.7604` → IC=+0.139 (n=987)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2036.7604 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.230 (n=2049)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.428 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.164 (n=489)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.051)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.137 (n=1075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.254 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=26241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=23317)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.220 (n=8797)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `8407.3041` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8407.3041 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=6306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.174 (n=6086)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=3918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=2604)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.243 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.203)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=5823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=5190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.174 (n=6293)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4832)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=4857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.251 (n=2346)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1673)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=5996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=5069)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1939)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=1046)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=1038)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `14011.0969` → IC=+0.450 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14011.0969 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `15264.989` → IC=+0.445 (n=287)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.406 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.421 (n=162)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=31103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=35500)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.184 (n=5421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=11584)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=16687)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=15084)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6362)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=5334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=12771)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=5071)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5806)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=6155)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.218 (n=5127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.252 (n=6472)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.204 (n=5180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5990)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7430)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=12952)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=14290)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.28` → IC=+0.141 (n=12122)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.28 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6296)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6500)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.73` → IC=+0.142 (n=7954)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.73 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6656)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.135 (n=8600)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.87` → IC=+0.135 (n=8016)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.87 (IC base=+0.116)

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
- **FILTRO** `py_entrada` > `0.73` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.73
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=103)

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
- **FILTRO** `py_entrada` > `0.73` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.73
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=103)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5113` → IC=+0.140 (n=20748)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5113 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=21030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=14410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.973` → IC=+0.246 (n=6918)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.973 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8903` → IC=+0.289 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8903 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.463` → IC=+0.190 (n=10405)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.463 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6937` → IC=+0.267 (n=5677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6937 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3029` → IC=+0.255 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3029 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.739` → IC=+0.233 (n=5018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.739 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=9961)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4940.7614` → IC=+0.150 (n=6916)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4940.7614 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.122 (n=13148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0067 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5643` → IC=+0.144 (n=26251)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5643 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6856` → IC=+0.192 (n=1792)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6856 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.18` → IC=+0.194 (n=10773)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.18 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.6923` → IC=+0.199 (n=4829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6923 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2962` → IC=+0.230 (n=2656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2962 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.2839` → IC=+0.212 (n=8435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2839 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.227 (n=18588)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3053` → IC=+0.213 (n=3873)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3053 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=4636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.273 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.981 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.433` → IC=+0.273 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.433 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.259 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.212 (n=4231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2056.0274` → IC=+0.213 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2056.0274 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.245 (n=1820)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.268 (n=1336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1833)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0816` → IC=+0.275 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0816 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.955` → IC=+0.243 (n=4108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.955 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0962` → IC=+0.240 (n=3650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0962 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.248 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.5555` → IC=+0.237 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5555 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.8571` → IC=+0.243 (n=2559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8571 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=4343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.232 (n=1264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.116` → IC=+0.245 (n=1662)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.116 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=3969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.220 (n=2690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8901` → IC=+0.249 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8901 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.2069` → IC=+0.227 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2069 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.583` → IC=+0.220 (n=4167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.583 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.702` → IC=+0.259 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.702 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6959` → IC=+0.227 (n=3374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6959 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2768` → IC=+0.261 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2768 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.4328` → IC=+0.244 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4328 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `15670.8457` → IC=+0.220 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15670.8457 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.157 (n=3650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0062 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.286` → IC=+0.146 (n=3647)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.286 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=1561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5915` → IC=+0.180 (n=3646)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5915 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.781` → IC=+0.142 (n=5005)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.781 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.586` → IC=+0.137 (n=648)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 10.586 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.968` → IC=+0.142 (n=3819)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.968 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6277` → IC=+0.158 (n=1381)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6277 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0982` → IC=+0.159 (n=1503)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0982 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4453` → IC=+0.143 (n=4012)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4453 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5381)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.186 (n=1327)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.210 (n=2117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=1798)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.886` → IC=+0.277 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.886 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.193 (n=4187)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.224 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.209 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5542)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1903.7172` → IC=+0.201 (n=2116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.7172 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.227 (n=1932)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.221 (n=1987)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1833` → IC=+0.232 (n=1928)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1833 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1661)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.225 (n=1992)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0542` → IC=+0.268 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0542 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.615` → IC=+0.267 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.615 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.346` → IC=+0.250 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.346 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7569` → IC=+0.218 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7569 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.230 (n=2824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1884.35` → IC=+0.223 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1884.35 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.220 (n=4195)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.168 (n=260)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5633)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.139 (n=755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.248 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1608` → IC=+0.348 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1608 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.3807` → IC=+0.341 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3807 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.226` → IC=+0.216 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.226 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.8694` → IC=+0.341 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8694 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2469` → IC=+0.359 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2469 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1649` → IC=+0.346 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1649 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2994` → IC=+0.357 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2994 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4157` → IC=+0.366 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4157 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.2709` → IC=+0.348 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2709 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.348 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0865` → IC=+0.187 (n=1474)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0865 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.3689` → IC=+0.157 (n=733)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3689 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1563` → IC=+0.154 (n=2778)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1563 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8257` → IC=+0.161 (n=1941)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8257 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2779` → IC=+0.193 (n=369)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2779 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.4276` → IC=+0.170 (n=936)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.4276 (IC base=+0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=913)

- **FILTRO** `ibs_20min` < `0.275` → IC=-0.183 (n=269)

  - _Acción_: SKIP cuando `ibs_20min` < 0.275
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=808)

- **FILTRO** `ibs_20min` > `0.1923` → IC=-0.125 (n=5533)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1923
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=2730)

- **FILTRO** `sigma_ewma_delta_pct` > `8.313` → IC=-0.230 (n=894)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.313
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=7369)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.179 (n=369)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.993` → IC=+0.279 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.993 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `1.3876` → IC=+0.266 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.3876 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.289` → IC=+0.144 (n=363)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 2.289 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.0067` → IC=+0.323 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0067 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0778` → IC=+0.280 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0778 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.1712` → IC=+0.279 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1712 (IC base=+0.022)

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.160 (n=2730)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1923 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.8451` → IC=+0.296 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8451 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2407` → IC=+0.293 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2407 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.6941` → IC=+0.307 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6941 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `1.0428` → IC=+0.293 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0428 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.318 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.7994` → IC=+0.310 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7994 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5251` → IC=+0.301 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5251 (IC base=-0.031)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7955` → IC=-0.161 (n=4250)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7955
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=2191)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.178 (n=1348)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=5093)

- **FILTRO** `ibs_20min` > `0.7204` → IC=-0.190 (n=2227)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7204
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=6684)

- **PATRÓN** `ibs_20min` > `0.7955` → IC=+0.146 (n=2191)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7955 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.455` → IC=+0.343 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.455 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.318 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3083` → IC=+0.315 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3083 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.531` → IC=+0.317 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.531 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1179` → IC=+0.296 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1179 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.636` → IC=+0.275 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.636 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.213` → IC=+0.279 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.213 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.281 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.268 (n=2533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4444 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.185 (n=9080)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0113 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8661` → IC=+0.283 (n=12340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8661 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0168` → IC=+0.305 (n=1883)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0168 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.456` → IC=+0.168 (n=12268)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.456 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.279 (n=9079)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.296 (n=2246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6453` → IC=+0.288 (n=5271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6453 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.308 (n=15472)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.160 (n=8841)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0109 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5158` → IC=+0.174 (n=23311)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5158 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2867` → IC=+0.282 (n=9407)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2867 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.6926` → IC=+0.280 (n=3993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6926 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1872` → IC=+0.286 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1872 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.322 (n=1997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4542` → IC=+0.302 (n=4504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4542 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.275` → IC=+0.305 (n=6125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.275 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.311 (n=13496)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8174` → IC=-0.148 (n=4816)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8174
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2482)

- **FILTRO** `ibs_20min` > `0.6978` → IC=-0.241 (n=1653)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6978
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4960)

- **FILTRO** `sigma_ewma_delta_pct` > `4.051` → IC=-0.239 (n=1387)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.051
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5226)

- **PATRÓN** `ibs_20min` > `0.8174` → IC=+0.312 (n=2482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8174 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.159` → IC=+0.176 (n=2717)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 2.159 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.332 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.295 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2236` → IC=+0.317 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2236 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.318 (n=2012)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.172 (n=1654)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1702 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.1556` → IC=+0.384 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1556 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6507` → IC=+0.388 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6507 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1845` → IC=+0.228 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1845 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.5308` → IC=+0.214 (n=2949)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5308 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.214 (n=2659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1952 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.6941` → IC=+0.222 (n=2376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6941 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2729` → IC=+0.242 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2729 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4147` → IC=+0.229 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4147 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.4465` → IC=+0.221 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4465 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `367.0` → IC=+0.232 (n=2632)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 367.0 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.7559` → IC=+0.260 (n=2434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7559 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.0184` → IC=+0.269 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0184 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.283 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.259 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.261 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.275 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 196.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.317 (n=1686)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=3737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.571` → IC=+0.306 (n=2529)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.571 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1304` → IC=+0.293 (n=3455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1304 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.1656` → IC=+0.295 (n=2413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1656 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2015.955` → IC=+0.298 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2015.955 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.300 (n=2347)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.343 (n=1156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.189` → IC=+0.328 (n=1528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.189 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.322 (n=1335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.311 (n=1567)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.0312` → IC=+0.308 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0312 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.157` → IC=+0.321 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.157 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.966` → IC=+0.320 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.966 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1983` → IC=+0.308 (n=3449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1983 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3448` → IC=+0.312 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3448 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7414` → IC=+0.325 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7414 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1577.7336` → IC=+0.313 (n=3099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1577.7336 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.309 (n=2972)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1625` → IC=+0.238 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1625 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.6476` → IC=+0.233 (n=2748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6476 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.1746` → IC=+0.235 (n=2500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1746 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.5982` → IC=+0.233 (n=2499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5982 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.237 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4031` → IC=+0.240 (n=2428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4031 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.251 (n=2482)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.151 (n=1719)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.092 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.3942` → IC=+0.261 (n=2031)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3942 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.176` → IC=+0.262 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.176 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6137` → IC=+0.258 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6137 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.264 (n=1724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.284 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.7734` → IC=+0.281 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7734 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4173` → IC=+0.269 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4173 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.284 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.249 (n=2777)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=2812)

- **FILTRO** `ibs_20min` > `0.6038` → IC=-0.236 (n=1319)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6038
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=3970)

- **FILTRO** `sigma_ewma_delta_pct` > `8.259` → IC=-0.264 (n=607)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.259
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=4682)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.317 (n=2812)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `1.1327` → IC=+0.353 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1327 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.448` → IC=+0.161 (n=2288)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.448 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8439` → IC=+0.352 (n=1372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8439 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.337 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6975 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1` → IC=+0.338 (n=1939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.372 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7937` → IC=+0.356 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7937 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.357 (n=1776)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.6038` → IC=+0.168 (n=3970)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6038 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.3303` → IC=+0.275 (n=2159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3303 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.727` → IC=+0.135 (n=4148)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.727 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.287 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6872 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.298 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.8068` → IC=+0.282 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8068 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.291 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.067)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.350 (n=2631)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.314 (n=2977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.314 (n=3087)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.336 (n=2946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2225` → IC=+0.336 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2225 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.743` → IC=+0.342 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.743 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.7017` → IC=+0.327 (n=2631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7017 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.344 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.323 (n=2848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `3000.4288` → IC=+0.321 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3000.4288 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.329 (n=3173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.39` → IC=+0.327 (n=3175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.39 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.318` → IC=+0.323 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.318 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.262` → IC=+0.315 (n=3133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.262 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.689` → IC=+0.328 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.689 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.6352` → IC=+0.317 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6352 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2104` → IC=+0.340 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2104 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.359 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.323 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1624` → IC=+0.319 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1624 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.219 (n=6635)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1283` → IC=+0.193 (n=8751)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1283 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=20712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5345` → IC=+0.228 (n=19882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5345 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1728` → IC=+0.205 (n=7461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1728 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.708` → IC=+0.260 (n=3899)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.708 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1739` → IC=+0.152 (n=13264)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1739 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6202` → IC=+0.151 (n=13264)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6202 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.206 (n=2862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6045` → IC=+0.185 (n=6460)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6045 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=18844)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.193 (n=8779)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0062 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.186 (n=13269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0083 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0867` → IC=+0.223 (n=6640)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0867 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=9565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5283` → IC=+0.237 (n=19902)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5283 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.2001` → IC=+0.179 (n=14553)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2001 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.391` → IC=+0.190 (n=3122)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.391 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.488` → IC=+0.191 (n=17803)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.488 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.6995` → IC=+0.174 (n=6199)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6995 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.217 (n=2982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6401` → IC=+0.196 (n=6349)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6401 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.199 (n=18867)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 89.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.266 (n=1088)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=2206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.291 (n=2175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.476` → IC=+0.326 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.476 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.284 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8299` → IC=+0.226 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8299 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4341` → IC=+0.227 (n=3123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4341 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.254 (n=2770)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.251)

- **PATRÓN** `drift_60min` |x|≤ `0.1025` → IC=+0.308 (n=1219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1025 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=2851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=2518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` < `0.0069` → IC=+0.309 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0069 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.95` → IC=+0.256 (n=2740)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.95 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0741` → IC=+0.254 (n=2308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0741 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.266 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `1.5544` → IC=+0.263 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5544 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.6903` → IC=+0.255 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6903 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.189 (n=1020)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0034 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.167 (n=1342)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2429` → IC=+0.201 (n=3051)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2429 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.210 (n=1473)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.538` → IC=+0.202 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.538 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8519` → IC=+0.135 (n=2034)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8519 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.1917` → IC=+0.128 (n=1017)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.1917 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.167 (n=463)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.128 (n=1322)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4541` → IC=+0.138 (n=1002)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4541 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.138 (n=1311)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 206.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.181 (n=2915)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0061 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2622` → IC=+0.175 (n=2913)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2622 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.176 (n=1586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.617` → IC=+0.210 (n=3310)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.617 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2262` → IC=+0.176 (n=3593)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2262 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.877` → IC=+0.178 (n=609)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.877 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.021` → IC=+0.156 (n=2914)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.021 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.163 (n=3310)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2053 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.155 (n=2913)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1481` → IC=+0.158 (n=2800)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1481 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `203.0` → IC=+0.196 (n=1380)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 203.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.231 (n=1523)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2593` → IC=+0.234 (n=2239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2593 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.987` → IC=+0.306 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.987 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.237 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.1669` → IC=+0.219 (n=2190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1669 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3993)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2014.7184` → IC=+0.223 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.7184 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.242 (n=3049)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1419` → IC=+0.275 (n=1340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1419 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=1150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0445` → IC=+0.289 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0445 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.72` → IC=+0.281 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.72 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3531` → IC=+0.280 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3531 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7638` → IC=+0.243 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7638 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.248 (n=1969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1880.06` → IC=+0.248 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.06 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.235 (n=2936)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.191 (n=1095)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.004 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.171 (n=1096)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2434` → IC=+0.187 (n=3282)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.2434 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1517` → IC=+0.188 (n=1844)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1517 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.175` → IC=+0.196 (n=558)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.175 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8362` → IC=+0.138 (n=2190)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8362 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.175 (n=494)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5149` → IC=+0.125 (n=1415)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5149 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4972` → IC=+0.136 (n=1072)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4972 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6913.8034` → IC=+0.196 (n=1488)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6913.8034 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.127 (n=3226)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 123.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.173 (n=2350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4369` → IC=+0.149 (n=3516)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4369 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6697` → IC=+0.187 (n=3516)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6697 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1748` → IC=+0.156 (n=3606)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1748 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.5` → IC=+0.141 (n=1199)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.5 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.151 (n=2344)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.852 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.166 (n=531)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1878` → IC=+0.134 (n=2951)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1878 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.407` → IC=+0.135 (n=3352)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.407 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6678.0732` → IC=+0.191 (n=1594)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6678.0732 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.155 (n=1132)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.176 (n=1218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0132 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.205 (n=3653)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8091` → IC=+0.215 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8091 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.901` → IC=+0.284 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.901 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1682` → IC=+0.131 (n=3653)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1682 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6239` → IC=+0.125 (n=3653)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6239 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.124 (n=3729)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.132 (n=509)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5437` → IC=+0.127 (n=1562)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5437 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2715.618` → IC=+0.200 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2715.618 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.128 (n=2383)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.153 (n=3383)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0113 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1197` → IC=+0.172 (n=1283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1197 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.222 (n=3843)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.2316` → IC=+0.147 (n=3820)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2316 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.147 (n=3405)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.182` → IC=+0.131 (n=3842)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.182 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8584` → IC=+0.126 (n=2561)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8584 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.148 (n=538)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.442` → IC=+0.142 (n=1219)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.442 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4659` → IC=+0.139 (n=1218)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.4659 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2611.4528` → IC=+0.192 (n=1742)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2611.4528 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.133 (n=3638)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 42.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.248 (n=2930)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.4651` → IC=+0.232 (n=2887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4651 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=3418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2954)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.254 (n=3281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1892` → IC=+0.234 (n=2010)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1892 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8482` → IC=+0.227 (n=3395)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8482 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.446` → IC=+0.273 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.446 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6171` → IC=+0.233 (n=3281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6171 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2362` → IC=+0.266 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2362 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.5004` → IC=+0.226 (n=3204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5004 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4372` → IC=+0.228 (n=3204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4372 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=4213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2620.9731` → IC=+0.229 (n=2187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.9731 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.016` → IC=+0.248 (n=2280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.016 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6225` → IC=+0.248 (n=3420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6225 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.298 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.3319` → IC=+0.251 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3319 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.994` → IC=+0.272 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.994 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.245 (n=2280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0478` → IC=+0.240 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0478 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.302 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.856` → IC=+0.236 (n=2164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.856 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5579` → IC=+0.239 (n=2899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5579 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.204 (n=1744)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1457` → IC=+0.169 (n=2303)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1457 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=5477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.2964` → IC=+0.190 (n=5229)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2964 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9262` → IC=+0.179 (n=792)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9262 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.210 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8539` → IC=+0.163 (n=3183)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8539 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.186` → IC=+0.160 (n=1591)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.186 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1553` → IC=+0.172 (n=1344)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1553 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5256` → IC=+0.159 (n=2247)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5256 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.8055` → IC=+0.156 (n=3404)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8055 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=5753)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7284.1957` → IC=+0.192 (n=2371)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7284.1957 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.1974` → IC=+0.203 (n=2531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1974 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.141 (n=2534)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 22.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.211 (n=853)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.237 (n=427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.226 (n=1161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.6075` → IC=+0.252 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6075 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.699` → IC=+0.241 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.699 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.858` → IC=+0.230 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.858 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.8658` → IC=+0.212 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8658 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.0881` → IC=+0.214 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0881 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `2.1509` → IC=+0.206 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1509 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `1.4016` → IC=+0.196 (n=1256)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4016 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `11292.6265` → IC=+0.200 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11292.6265 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.152 (n=536)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0032 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2185` → IC=+0.186 (n=709)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.2185 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.167 (n=698)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 165.0 (IC base=+0.071)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.241 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.157 (n=710)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.258 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1582` → IC=+0.167 (n=763)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1582 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.04` → IC=+0.187 (n=228)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 10.04 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8292` → IC=+0.154 (n=1073)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8292 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7708` → IC=+0.159 (n=1058)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7708 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `7831.4295` → IC=+0.174 (n=729)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7831.4295 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.143 (n=530)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 30.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.122 (n=1607)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0082 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.1818` → IC=+0.207 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1818 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6744` → IC=+0.136 (n=707)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6744 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.129 (n=273)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `7746.672` → IC=+0.161 (n=729)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7746.672 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.145 (n=689)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 40.0 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.150 (n=470)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0073 (IC base=+0.121)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.134 (n=471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0129 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.140 (n=1411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.5338` → IC=+0.190 (n=1257)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5338 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `1.0635` → IC=+0.149 (n=249)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 1.0635 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.856` → IC=+0.225 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.856 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.0426` → IC=+0.130 (n=1238)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0426 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.7012` → IC=+0.126 (n=1257)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.7012 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2222` → IC=+0.146 (n=241)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2222 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4182` → IC=+0.148 (n=456)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4182 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=1424)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3054.254` → IC=+0.150 (n=469)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3054.254 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.130 (n=466)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 10.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.5676` → IC=+0.164 (n=1378)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.5676 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `2755.7226` → IC=+0.166 (n=710)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2755.7226 (IC base=+0.081)

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
- **PATRÓN** `sigma_h` > `0.013` → IC=+0.226 (n=8778)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=27524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9655` → IC=+0.298 (n=8778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9655 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.9678` → IC=+0.216 (n=3036)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9678 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.866` → IC=+0.259 (n=6436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.866 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8663` → IC=+0.163 (n=11827)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8663 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2924` → IC=+0.216 (n=3446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2924 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6283` → IC=+0.193 (n=8577)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6283 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1766.1026` → IC=+0.181 (n=26308)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1766.1026 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.199 (n=24931)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.208 (n=8183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1143` → IC=+0.203 (n=8171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1143 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=9185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4894` → IC=+0.251 (n=21573)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4894 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1954` → IC=+0.182 (n=15678)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1954 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.497` → IC=+0.205 (n=22859)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.497 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6264` → IC=+0.181 (n=5475)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6264 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.254 (n=3367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6273` → IC=+0.211 (n=7867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6273 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.220 (n=20662)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3091` → IC=+0.235 (n=3689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3091 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2811)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.315 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.034` → IC=+0.298 (n=2758)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.034 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.289 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2808` → IC=+0.241 (n=1841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2808 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2057.3966` → IC=+0.235 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2057.3966 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.268 (n=1284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.264)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.264 (n=1751)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.1299` → IC=+0.289 (n=1694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1299 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.265 (n=4000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.264)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.266 (n=3468)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` < `0.4699` → IC=+0.285 (n=3388)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4699 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.266 (n=3513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.287 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.265 (n=1634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` > `2.6442` → IC=+0.273 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6442 (IC base=+0.264)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=4178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.264)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.268 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.264)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.173 (n=1444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0844` → IC=+0.147 (n=1445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0844 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.1869` → IC=+0.186 (n=4331)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.1869 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.7467` → IC=+0.210 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7467 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.005` → IC=+0.174 (n=679)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.005 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6328` → IC=+0.155 (n=1445)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6328 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.0636` → IC=+0.140 (n=1964)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0636 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.189 (n=602)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1654` → IC=+0.143 (n=3751)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1654 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5193` → IC=+0.145 (n=3807)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5193 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `351.0` → IC=+0.147 (n=3710)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 351.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.169 (n=3375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0062 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0847` → IC=+0.173 (n=1278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0847 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=1420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6828` → IC=+0.191 (n=3832)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6828 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1581` → IC=+0.163 (n=3766)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1581 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.0` → IC=+0.147 (n=1805)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.188` → IC=+0.151 (n=3914)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.188 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0404` → IC=+0.157 (n=3372)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0404 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2219` → IC=+0.198 (n=701)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2219 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.151 (n=3721)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7756` → IC=+0.152 (n=2480)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7756 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=4976)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.180 (n=1232)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 212.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.241 (n=1991)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=4604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.902` → IC=+0.314 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.902 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2044` → IC=+0.234 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2044 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.768` → IC=+0.231 (n=3833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.768 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1901.2255` → IC=+0.237 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1901.2255 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.249 (n=1864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1865` → IC=+0.259 (n=1864)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1865 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=1934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0698` → IC=+0.294 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0698 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.871` → IC=+0.305 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.871 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.296 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1676` → IC=+0.255 (n=2735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1676 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1997.0984` → IC=+0.252 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1997.0984 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.246 (n=4062)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.189 (n=1517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3601` → IC=+0.148 (n=4001)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3601 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8748` → IC=+0.262 (n=1516)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8748 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1533` → IC=+0.169 (n=2235)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1533 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.968` → IC=+0.162 (n=1983)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.968 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.154 (n=3032)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8567 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.197 (n=801)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5159` → IC=+0.154 (n=1957)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5159 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1486` → IC=+0.142 (n=2016)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1486 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5902.6946` → IC=+0.230 (n=2062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5902.6946 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.142 (n=2964)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.169 (n=3861)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4669` → IC=+0.161 (n=3858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4669 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5731` → IC=+0.212 (n=3396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5731 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.6524` → IC=+0.156 (n=4467)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.6524 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.044` → IC=+0.155 (n=770)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.044 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.029` → IC=+0.153 (n=3362)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.029 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8499` → IC=+0.161 (n=2572)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8499 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.207 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4806` → IC=+0.155 (n=3742)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4806 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5217` → IC=+0.157 (n=3342)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5217 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6722.1308` → IC=+0.213 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6722.1308 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.171 (n=1278)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.157 (n=1546)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0133 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=3287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.6957` → IC=+0.255 (n=3089)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6957 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8244` → IC=+0.196 (n=1022)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8244 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.195` → IC=+0.269 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.195 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8713` → IC=+0.133 (n=3089)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8713 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.124 (n=4413)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2794` → IC=+0.145 (n=582)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2794 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.8243` → IC=+0.131 (n=3018)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8243 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2470.3906` → IC=+0.224 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2470.3906 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.159 (n=3811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0114 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.144` → IC=+0.150 (n=1445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.144 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=2055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.246 (n=3813)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5417 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.2304` → IC=+0.152 (n=3997)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2304 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.019` → IC=+0.161 (n=4206)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.019 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1927` → IC=+0.143 (n=4330)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1927 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.201 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.162 (n=1380)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4901` → IC=+0.146 (n=1379)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4901 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2649.7268` → IC=+0.224 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2649.7268 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.150 (n=4144)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 47.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.255 (n=4231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.239 (n=2824)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.302 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.2063` → IC=+0.250 (n=2140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2063 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.931` → IC=+0.298 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.931 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `1.2165` → IC=+0.236 (n=4231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2165 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.6403` → IC=+0.242 (n=4230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6403 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.258 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.522` → IC=+0.254 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.522 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=5415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2643.9324` → IC=+0.238 (n=2820)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2643.9324 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0246` → IC=+0.271 (n=1471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0246 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.251 (n=4146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.14` → IC=+0.304 (n=1946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.14 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.2084` → IC=+0.249 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2084 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2341` → IC=+0.249 (n=4245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2341 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.928` → IC=+0.280 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.928 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.6362` → IC=+0.248 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6362 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.266 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.312 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4357` → IC=+0.249 (n=4187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4357 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.245 (n=3641)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.233 (n=6573)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.5407` → IC=+0.234 (n=7469)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5407 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=7497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.928` → IC=+0.259 (n=2490)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.928 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.9779` → IC=+0.228 (n=6125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9779 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.434` → IC=+0.236 (n=2492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.434 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.232 (n=2337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.8778` → IC=+0.228 (n=3538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8778 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.1638` → IC=+0.236 (n=2092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1638 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.4488` → IC=+0.236 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4488 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.230 (n=5340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `3759.3` → IC=+0.234 (n=4979)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3759.3 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.229 (n=1795)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4191` → IC=+0.222 (n=4702)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4191 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=2414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.6134` → IC=+0.216 (n=4702)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6134 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7213` → IC=+0.217 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7213 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.681` → IC=+0.225 (n=4855)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.681 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2534` → IC=+0.211 (n=4849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2534 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.214 (n=4942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.216 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8177` → IC=+0.218 (n=3508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8177 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.236 (n=3530)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.212)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.280 (n=639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.273)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.304 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.282 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.273)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.273 (n=961)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.4706` → IC=+0.287 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4706 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` < `0.3337` → IC=+0.284 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3337 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.278 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `0.8784` → IC=+0.292 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8784 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `2.4917` → IC=+0.281 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4917 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `12917.6999` → IC=+0.284 (n=638)

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
- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.224 (n=1819)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.4747` → IC=+0.221 (n=2064)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4747 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.4688` → IC=+0.232 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4688 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.8315` → IC=+0.217 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8315 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.4305` → IC=+0.227 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4305 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.936` → IC=+0.223 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.936 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.218 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.2299` → IC=+0.220 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2299 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.217 (n=1916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.1586` → IC=+0.218 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1586 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.3999` → IC=+0.233 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3999 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4929` → IC=+0.217 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4929 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.246 (n=560)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.5119` → IC=+0.220 (n=1673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5119 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.214 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0847 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.7326` → IC=+0.221 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7326 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.22` → IC=+0.211 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.22 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.1036` → IC=+0.214 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1036 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.7189` → IC=+0.210 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7189 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.229 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1602` → IC=+0.210 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1602 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7691` → IC=+0.210 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7691 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.211 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.207)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.230 (n=869)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.219)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.228 (n=436)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=1166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.301 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `1.1079` → IC=+0.248 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1079 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.998` → IC=+0.271 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.998 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `0.6422` → IC=+0.248 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6422 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` < `0.1058` → IC=+0.221 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1058 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.241 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `2.4925` → IC=+0.227 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4925 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.227 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `3369.0196` → IC=+0.244 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.0196 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0141` → IC=+0.246 (n=977)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0141 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.253 (n=651)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.246)

- **PATRÓN** `drift_60min` |x|≤ `0.6921` → IC=+0.259 (n=976)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6921 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.266 (n=677)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.272 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.5875` → IC=+0.246 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5875 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` < `0.332` → IC=+0.256 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.332 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.991` → IC=+0.266 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.991 (IC base=+0.246)

- **PATRÓN** `volumen_regimen` < `0.7541` → IC=+0.264 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7541 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.258 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.267 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `4016.542` → IC=+0.269 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4016.542 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.276 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.246)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.147 (n=955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0043 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.4182` → IC=+0.137 (n=2762)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.4182 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1612` → IC=+0.157 (n=1285)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1612 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.308` → IC=+0.145 (n=598)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.308 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5784` → IC=+0.178 (n=2198)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5784 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.545` → IC=+0.133 (n=977)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.545 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.184 (n=622)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.096)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5521` → IC=-0.121 (n=344)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5521
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=700)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.120 (n=717)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0057 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5521` → IC=+0.158 (n=700)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5521 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.129` → IC=+0.165 (n=365)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.129 (IC base=+0.066)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.120 (n=335)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0037 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.245 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.141 (n=324)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.056)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.4861` → IC=-0.125 (n=270)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4861
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=525)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.158 (n=372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0043 (IC base=+0.064)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.124 (n=426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.53` → IC=+0.158 (n=728)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.53 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.155 (n=389)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.996` → IC=+0.169 (n=179)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.996 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.0943` → IC=+0.277 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0943 (IC base=+0.045)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.193 (n=311)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.981 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.778` → IC=+0.159 (n=224)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.778 (IC base=+0.038)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.180 (n=423)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0103 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.195 (n=605)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` < `0.2333` → IC=+0.152 (n=602)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2333 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.159` → IC=+0.242 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.159 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `1.1167` → IC=+0.190 (n=201)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.1167 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `2.193` → IC=+0.128 (n=503)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.193 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `1.8607` → IC=+0.142 (n=381)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8607 (IC base=+0.101)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.384 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.2821` → IC=+0.329 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2821 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.371 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` > `0.5815` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5815 (IC base=+0.302)

- **PATRÓN** `dist_vwap_pct` > `0.5771` → IC=+0.386 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5771 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.192` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.192 (IC base=+0.302)

- **PATRÓN** `volumen_regimen` > `1.1852` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1852 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `2.6162` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6162 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.302)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.406 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.368 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.333)

- **PATRÓN** `ibs_20min` < `0.118` → IC=+0.378 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.118 (IC base=+0.333)

- **PATRÓN** `ibs_20min` > `0.4562` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4562 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.6346` → IC=+0.374 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6346 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.683` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.683 (IC base=+0.333)

- **PATRÓN** `volumen_regimen` > `0.5619` → IC=+0.368 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5619 (IC base=+0.333)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.333)

- **PATRÓN** `volumen_spike_ratio` < `1.5212` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5212 (IC base=+0.333)

- **PATRÓN** `volumen_spike_ratio` > `3.0999` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0999 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.359 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `40.2` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 40.2 (IC base=+0.333)

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
- **FILTRO** `ibs_20min` > `0.2471` → IC=-0.153 (n=350)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2471
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1053)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.260 (n=306)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.204 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.6875` → IC=+0.200 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6875 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.9045` → IC=+0.312 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9045 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.365` → IC=+0.188 (n=219)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 10.365 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.191 (n=299)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6242 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `1.1982` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1982 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.187 (n=701)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.4082` → IC=+0.206 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4082 (IC base=+0.165)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.292 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.303 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` > `0.7967` → IC=+0.405 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7967 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` < `0.8033` → IC=+0.302 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8033 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` < `0.2102` → IC=+0.298 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2102 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2694` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2694 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.324 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `2.0543` → IC=+0.314 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0543 (IC base=+0.273)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.274 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.273)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=209)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.325)

- **PATRÓN** `elapsed_s` > `209.4` → IC=+0.373 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.4 (IC base=+0.325)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.325)

- **PATRÓN** `drift_60min` |x|≤ `0.6894` → IC=+0.391 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6894 (IC base=+0.325)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.380 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.325)

- **PATRÓN** `ballena_activa_n` < `1039.0` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1039.0 (IC base=+0.325)

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

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.325)

- **PATRÓN** `elapsed_s` > `209.4` → IC=+0.373 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.4 (IC base=+0.325)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.325)

- **PATRÓN** `drift_60min` |x|≤ `0.6894` → IC=+0.391 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6894 (IC base=+0.325)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.380 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.325)

- **PATRÓN** `ballena_activa_n` < `1039.0` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1039.0 (IC base=+0.325)

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
- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=239)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=294)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=1626)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `liq_n` > 2.0 (IC base=+0.102)

- **PATRÓN** `liq_usd_total` > `100.7` → IC=+0.137 (n=191)

  - _Acción_: Kelly boost +0.69€ cuando `liq_usd_total` > 100.7 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.204 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.102)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.144 (n=102)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` > 0.5 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.121 (n=167)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 15.0 (IC base=+0.102)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=132)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.132 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 10.0 (IC base=+0.084)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4299)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=267)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=224)

- **FILTRO** `ballena_activa_n` > `39.0` → IC=-0.178 (n=85)

  - _Acción_: SKIP cuando `ballena_activa_n` > 39.0
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=169)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.184 (n=169)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 39.0 (IC base=+0.028)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.133 (n=298)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.188)

- **PATRÓN** `liq_usd_total` > `750.26` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 750.26 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.209 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.231 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.201 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.188)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1699)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1653)

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
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=1189)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=1189)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1607)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1607)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=374)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=374)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.144 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=304)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=422)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=471)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=346)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=454)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=454)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=442)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=3791)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=9711)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.164 (n=459)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1095)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.141 (n=357)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=978)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.135 (n=461)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.51 (IC base=-0.010)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.126 (n=209)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=483)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.121 (n=167)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=532)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=765)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=822)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.137 (n=384)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=810)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.130 (n=590)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=743)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=625)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=650)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.133 (n=674)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=773)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9341)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=29067)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9681)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=30073)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4281)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7645` → IC=-0.148 (n=1308)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7645
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3927)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.181 (n=1426)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4334)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3431)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4383)

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
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

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

- **FILTRO** `ibs_20min` > `0.8636` → IC=-0.127 (n=644)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8636
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=645)

- **FILTRO** `ballena_activa_n` > `22.0` → IC=-0.177 (n=422)

  - _Acción_: SKIP cuando `ballena_activa_n` > 22.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=858)

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

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.175 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=100)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.138 (n=26003)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=58980)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20697)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=64286)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27922)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=57061)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.154 (n=27833)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=57150)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26299)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=79888)

- **FILTRO** `ibs_7min` > `0.2781` → IC=-0.182 (n=26545)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2781
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=79642)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.129 (n=3421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=10813)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.268 (n=3484)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10750)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.213 (n=3558)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10676)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.205 (n=3541)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10693)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=3325)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=11269)

- **FILTRO** `ibs_7min` > `0.2639` → IC=-0.187 (n=3648)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2639
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10946)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.177 (n=3648)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10946)

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
- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=3176)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10747)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.201 (n=3480)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10443)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.197 (n=3419)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=10504)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3367)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=11091)

- **FILTRO** `ibs_7min` > `0.2716` → IC=-0.177 (n=3613)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2716
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=10845)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.174 (n=3495)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10963)

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
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1037)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1326)

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
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=561)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.142 (n=781)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.131 (n=629)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.165 (n=574)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 459.6089 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3675.377` → IC=+0.131 (n=781)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3675.377 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.182 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `381.605` → IC=+0.164 (n=349)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 381.605 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.147 (n=358)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.04 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.135 (n=362)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.118)

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
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.213 (n=134)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `4819.793` → IC=+0.178 (n=197)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4819.793 (IC base=+0.133)

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
- **FILTRO** `sigma_h` > `0.0151` → IC=-0.206 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0151
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=149)

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

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.303 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `sigma_h` < `0.0097` → IC=-0.255 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=143)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=498)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=534)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.137 (n=166)

  - _Acción_: Kelly boost +0.68€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.022)

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
- **PATRÓN** `streak_estiramiento` < `0.3805` → IC=+0.132 (n=131)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.3805 (IC base=+0.041)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.211 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 35.0 (IC base=+0.085)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5658)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3410)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.183 (n=2220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0059 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2338` → IC=+0.158 (n=6656)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2338 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1275` → IC=+0.133 (n=6656)

  - _Acción_: Kelly boost +0.66€ cuando `drift_15min` |x|≤ 1.1275 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0643` → IC=+0.132 (n=6656)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0643 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0994` → IC=+0.143 (n=2099)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0994 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.551` → IC=+0.207 (n=5947)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.551 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.974` → IC=+0.228 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.974 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3485)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4314.4132` → IC=+0.171 (n=2219)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4314.4132 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2596)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.249 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.249 (n=396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.207)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2667` → IC=+0.232 (n=300)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2667 (IC base=+0.207)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2244` → IC=+0.218 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2244 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_15` > `0.7031` → IC=+0.276 (n=899)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7031 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.4048` → IC=+0.232 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4048 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.5565` → IC=+0.210 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5565 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.047` → IC=+0.301 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.047 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `11859.4037` → IC=+0.221 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11859.4037 (IC base=+0.207)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.147 (n=1018)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0068 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.146 (n=772)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0834` → IC=+0.137 (n=1033)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0834 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.144 (n=824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.4797` → IC=+0.217 (n=1156)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4797 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.146 (n=719)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.6818` → IC=+0.132 (n=1312)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6818 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.9` → IC=+0.282 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.9 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6114.254` → IC=+0.175 (n=524)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6114.254 (IC base=+0.133)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8333` → IC=+0.144 (n=701)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.72€ cuando `ibs_15` > 0.8333 (IC base=+0.045)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.143 (n=1681)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0119 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.24` → IC=+0.175 (n=1683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.24 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0583` → IC=+0.139 (n=1681)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0583 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0928` → IC=+0.186 (n=526)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0928 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=1539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=1555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6959` → IC=+0.232 (n=1121)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6959 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2152` → IC=+0.142 (n=766)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2152 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.9158` → IC=+0.141 (n=1943)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.9158 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.978` → IC=+0.183 (n=389)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 16.978 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2943.2931` → IC=+0.179 (n=762)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2943.2931 (IC base=+0.137)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1089` → IC=+0.364 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1089 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.378 (n=549)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.102` → IC=+0.379 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.102 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.380 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.394 (n=827)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.2727` → IC=+0.383 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2727 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.787` → IC=+0.394 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.787 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.378 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9610.6074 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1523` → IC=+0.365 (n=347)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1523 (IC base=+0.363)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.364 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2167` → IC=+0.379 (n=179)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2167 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.399 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.363 (n=400)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.384 (n=394)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.394 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.667` → IC=+0.384 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.667 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `15150.2605` → IC=+0.390 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15150.2605 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.385 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 409.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.363 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.374 (n=196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.366 (n=289)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1264` → IC=+0.379 (n=287)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1264 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0998` → IC=+0.382 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0998 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.381 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.396 (n=431)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.379 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.6907` → IC=+0.362 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6907 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.854` → IC=+0.400 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.854 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.587` → IC=+0.365 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.587 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `3715.9445` → IC=+0.368 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3715.9445 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.204 (n=3083)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=3085)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2731)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3437)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1392` → IC=+0.217 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1392 (IC base=-0.087)

- **PATRÓN** `ibs_15` > `0.6296` → IC=+0.279 (n=1357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6296 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` > `0.117` → IC=+0.208 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.117 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` < `0.6021` → IC=+0.200 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6021 (IC base=-0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2273` → IC=+0.267 (n=2039)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2273 (IC base=+0.002)

- **PATRÓN** `ibs_15` < `0.3765` → IC=+0.282 (n=6111)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3765 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.7153` → IC=+0.264 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7153 (IC base=+0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` < `0.0041` → IC=-0.208 (n=1025)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=3080)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.185 (n=1909)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2196)

- **FILTRO** `sigma_ewma_delta_pct` > `22.211` → IC=-0.235 (n=580)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.211
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3525)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.180 (n=95)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=4010)

- **FILTRO** `libro_liquidez` < `10169.1496` → IC=-0.192 (n=1354)

  - _Acción_: SKIP cuando `libro_liquidez` < 10169.1496
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2751)

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
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=897)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.161 (n=686)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0067 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.178 (n=302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2988` → IC=+0.186 (n=543)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2988 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.5656` → IC=+0.241 (n=686)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5656 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6788` → IC=+0.179 (n=135)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6788 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.151 (n=525)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.241` → IC=+0.254 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.241 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=897)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `5213.5522` → IC=+0.171 (n=457)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5213.5522 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.249 (n=1605)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4846` → IC=+0.241 (n=2407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4846 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.8321` → IC=+0.248 (n=2118)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8321 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1966` → IC=+0.255 (n=1092)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1966 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.239 (n=1643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.1931` → IC=+0.294 (n=1607)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1931 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.2399` → IC=+0.245 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2399 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.522` → IC=+0.240 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.522 (IC base=+0.234)

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

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.294 (n=1010)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2882` → IC=+0.256 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2882 (IC base=-0.025)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0142` → IC=-0.250 (n=1155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=569)

- **FILTRO** `drift_60min` |x|> `0.1231` → IC=-0.244 (n=585)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1231
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=1139)

- **FILTRO** `drift_15min` |x|> `1.2906` → IC=-0.285 (n=430)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2906
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1294)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1703)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.283 (n=1259)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=-0.007)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.288 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.007)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=1421)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.327 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=-0.007)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.294 (n=504)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.310 (n=665)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.288 (n=1007)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2178` → IC=+0.290 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2178 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.301 (n=1376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8361` → IC=+0.311 (n=1511)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8361 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2764` → IC=+0.316 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2764 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.592` → IC=+0.387 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.592 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `13060.5836` → IC=+0.300 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13060.5836 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.309 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.302 (n=351)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.283 (n=265)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2292` → IC=+0.289 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2292 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.304 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.8555` → IC=+0.309 (n=709)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8555 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2614` → IC=+0.310 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2614 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.41` → IC=+0.393 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.41 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.282 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `14467.1785` → IC=+0.309 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14467.1785 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.302 (n=316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.292 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.326 (n=240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.295 (n=717)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.311 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.305 (n=244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.292 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8452` → IC=+0.316 (n=717)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8452 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.316 (n=313)

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
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=386)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.197 (n=186)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=67)

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

- **FILTRO** `sigma_h` > `0.0115` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0115
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=51)

- **FILTRO** `drift_15min` |x|> `0.639` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.639
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=52)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0549` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=51)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.551 sube el IC de +0.132 a +0.207 en UPDOWN_GBM#15min (n=5947). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7031 sube el IC de +0.207 a +0.276 en UPDOWN_GBM#BTC#15min (n=899). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4797 sube el IC de +0.133 a +0.217 en UPDOWN_GBM#ETH#15min (n=1156). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.6959 sube el IC de +0.137 a +0.232 en UPDOWN_GBM#XRP#15min (n=1121). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6296 sube el IC de -0.087 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3765 sube el IC de +0.002 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=6111). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.065 a +0.318 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=487). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.180 a +0.291 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5656 sube el IC de +0.150 a +0.241 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=686). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1931 sube el IC de +0.234 a +0.294 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1607). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.025 a +0.294 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=1010). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.007 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1421). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8692 sube el IC de +0.086 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8692 sube el IC de +0.086 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8361 sube el IC de +0.286 a +0.311 en UPDOWN_GBM_IBS_ALTO (n=1511). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8555 sube el IC de +0.280 a +0.309 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=709). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8452 sube el IC de +0.291 a +0.316 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=717). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.364 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=827). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.363 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=394). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.363 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=431). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2381 | +0.085 | +263.88€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2381 | +0.085 | +263.88€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1969 | +0.086 | +224.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1969 | +0.086 | +224.39€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1512 | -0.028 | +49.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1512 | -0.028 | +49.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1188 | -0.040 | +36.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1188 | -0.040 | +36.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 51692 | -0.086 | -6588.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3402 | +0.095 | -324.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48290 | -0.099 | -6264.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3402 | +0.095 | -324.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3402 | +0.095 | -324.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14501 | -0.043 | -1320.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14501 | -0.043 | -1320.09€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 58004 | -0.012 | +2574.23€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14955 | +0.004 | +1481.83€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 43049 | -0.017 | +1092.40€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 58004 | -0.012 | +2574.23€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14955 | +0.004 | +1481.83€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 43049 | -0.017 | +1092.40€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 215630 | +0.112 | -8904.60€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23656 | +0.178 | -762.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 1009 | +0.022 | -81.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 178732 | +0.104 | -7652.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12233 | +0.095 | -408.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 29636 | +0.101 | -2134.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 90 | -0.196 | +9.57€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 29509 | +0.102 | -2153.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 40330 | +0.122 | -659.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5739 | +0.176 | -237.80€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 29586 | +0.119 | -231.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4963 | +0.081 | -167.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 29685 | +0.098 | -2103.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 112 | -0.105 | +20.53€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 29545 | +0.099 | -2116.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 13 | -0.065 | +4.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 46180 | +0.123 | -1000.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11499 | +0.177 | -336.01€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 30066 | +0.106 | -570.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4603 | +0.103 | -84.62€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 40154 | +0.111 | -1702.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6116 | +0.200 | -231.88€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 912 | +0.046 | -27.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 30497 | +0.095 | -1259.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2629 | +0.108 | -184.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 29645 | +0.106 | -1305.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 100 | -0.137 | +13.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 29529 | +0.107 | -1321.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 35190 | +0.188 | -2705.47€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 35190 | +0.188 | -2705.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7969 | +0.159 | -966.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7969 | +0.159 | -966.35€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5311 | +0.193 | -237.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5311 | +0.193 | -237.61€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7774 | +0.171 | -731.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7774 | +0.171 | -731.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6445 | +0.251 | -233.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6445 | +0.251 | -233.80€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7612 | +0.182 | -549.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7612 | +0.182 | -549.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1349 | +0.425 | -50.68€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1349 | +0.425 | -50.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 574 | +0.439 | -5.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 574 | +0.439 | -5.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 233 | +0.402 | -18.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 233 | +0.402 | -18.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 124304 | +0.199 | -9093.32€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 124304 | +0.199 | -9093.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21559 | +0.175 | -2566.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21559 | +0.175 | -2566.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 20026 | +0.223 | -664.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 20026 | +0.223 | -664.67€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21314 | +0.180 | -2245.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21314 | +0.180 | -2245.93€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 20211 | +0.218 | -784.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 20211 | +0.218 | -784.00€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20502 | +0.206 | -1196.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20502 | +0.206 | -1196.65€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 20692 | +0.196 | -1636.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 20692 | +0.196 | -1636.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 48355 | +0.116 | +405.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 48355 | +0.116 | +405.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 24083 | +0.117 | +266.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 24083 | +0.117 | +266.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 24272 | +0.116 | +138.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 24272 | +0.116 | +138.81€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2070 | +0.063 | -108.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1345 | +0.072 | -44.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1636 | +0.069 | -63.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1345 | +0.072 | -44.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 98954 | +0.101 | -2086.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 8031 | +0.097 | +196.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 90923 | +0.101 | -2283.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 53983 | +0.105 | -441.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 8031 | +0.097 | +196.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 45952 | +0.106 | -638.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 21310 | +0.109 | -95.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 21310 | +0.109 | -95.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 23661 | +0.083 | -1549.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 23661 | +0.083 | -1549.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 937 | +0.175 | -110.91€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 937 | +0.175 | -110.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 937 | +0.175 | -110.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 937 | +0.175 | -110.91€ | 1 | 4 |
| ✅ GBM_LATE_15M | 67434 | +0.102 | +37961.72€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 67434 | +0.102 | +37961.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11208 | +0.223 | +9568.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11208 | +0.223 | +9568.98€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 10558 | +0.176 | +8535.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10558 | +0.176 | +8535.87€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 12064 | +0.206 | +9497.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 12064 | +0.206 | +9497.38€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 8912 | +0.063 | +3035.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8912 | +0.063 | +3035.81€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 9340 | -0.025 | +2422.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9340 | -0.025 | +2422.73€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 15352 | -0.019 | +4900.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15352 | -0.019 | +4900.96€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 71610 | +0.088 | +42024.32€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 71610 | +0.088 | +42024.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13911 | -0.001 | +7358.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13911 | -0.001 | +7358.83€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15384 | +0.007 | +4287.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15384 | +0.007 | +4287.00€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9577 | +0.295 | +10968.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9577 | +0.295 | +10968.23€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13705 | +0.020 | +4421.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13705 | +0.020 | +4421.93€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10878 | +0.051 | +5101.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10878 | +0.051 | +5101.49€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8155 | +0.312 | +9886.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8155 | +0.312 | +9886.84€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 53036 | +0.179 | +44101.34€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 53036 | +0.179 | +44101.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 8036 | +0.238 | +7429.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 8036 | +0.238 | +7429.32€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8478 | +0.140 | +6412.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8478 | +0.140 | +6412.65€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8535 | +0.223 | +7372.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8535 | +0.223 | +7372.74€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 9063 | +0.130 | +7102.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 9063 | +0.130 | +7102.90€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9992 | +0.124 | +7744.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9992 | +0.124 | +7744.34€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8932 | +0.232 | +8039.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8932 | +0.232 | +8039.40€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14639 | +0.125 | +7431.20€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14639 | +0.125 | +7431.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3848 | +0.126 | +2064.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3848 | +0.126 | +2064.86€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4286 | +0.126 | +2167.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4286 | +0.126 | +2167.66€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3961 | +0.100 | +1609.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3961 | +0.100 | +1609.36€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1355 | +0.168 | +858.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1355 | +0.168 | +858.78€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 67750 | +0.189 | +56414.78€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 67750 | +0.189 | +56414.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10721 | +0.248 | +10266.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10721 | +0.248 | +10266.43€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10883 | +0.143 | +7957.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10883 | +0.143 | +7957.93€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11481 | +0.233 | +10311.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11481 | +0.233 | +10311.00€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11205 | +0.145 | +8462.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11205 | +0.145 | +8462.98€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11949 | +0.129 | +8753.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11949 | +0.129 | +8753.53€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11511 | +0.240 | +10662.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11511 | +0.240 | +10662.91€ | 0 | 23 |
| ✅ GBM_LATE_5M | 17081 | +0.220 | +14477.23€ | 0 | 24 |
| ✅ GBM_LATE_5M#5min | 17081 | +0.220 | +14477.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3339 | +0.210 | +2861.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3339 | +0.210 | +2861.73€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1591 | +0.218 | +1323.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1591 | +0.218 | +1323.18€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4980 | +0.212 | +3956.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4980 | +0.212 | +3956.29€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3038 | +0.231 | +2700.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3038 | +0.231 | +2700.73€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 2185 | +0.211 | +1736.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2185 | +0.211 | +1736.58€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6835 | +0.083 | +2378.98€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 6835 | +0.083 | +2378.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 223 | +0.269 | +241.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 223 | +0.269 | +241.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2098 | +0.061 | +614.32€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2098 | +0.061 | +614.32€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 218 | +0.300 | +252.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 218 | +0.300 | +252.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1951 | +0.056 | +593.90€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1951 | +0.056 | +593.90€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 2128 | +0.063 | +414.69€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2128 | +0.063 | +414.69€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 217 | +0.322 | +261.82€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 217 | +0.322 | +261.82€ | 0 | 22 |
| 🚫 GBM_LATE_60M_FADE | 810 | -0.245 | -34.72€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 810 | -0.245 | -34.72€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 284 | -0.255 | -20.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 284 | -0.255 | -20.31€ | 5 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 279 | -0.244 | -8.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 279 | -0.244 | -8.44€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 222 | -0.245 | -9.74€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 222 | -0.245 | -9.74€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2627 | +0.090 | +699.02€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2627 | +0.090 | +699.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 949 | +0.071 | +241.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 949 | +0.071 | +241.77€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 56 | +0.190 | +31.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 56 | +0.190 | +31.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 832 | +0.053 | +160.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 832 | +0.053 | +160.11€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 684 | +0.153 | +243.61€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 684 | +0.153 | +243.61€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 106 | +0.093 | +22.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 106 | +0.093 | +22.51€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 441 | +0.304 | +524.47€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 441 | +0.304 | +524.47€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 441 | +0.304 | +524.47€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 441 | +0.304 | +524.47€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 5067 | +0.095 | +1097.92€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 5067 | +0.095 | +1097.92€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 5067 | +0.095 | +1097.92€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 5067 | +0.095 | +1097.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1957 | +0.021 | +117.33€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1957 | +0.021 | +117.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 255 | +0.099 | +58.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 255 | +0.099 | +58.77€ | 0 | 6 |
| ✅ LIQUIDACIONES_15M#BTC | 365 | -0.015 | +6.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 365 | -0.015 | +6.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 157 | +0.053 | +24.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 157 | +0.053 | +24.33€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 425 | +0.022 | +21.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 425 | +0.022 | +21.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 360 | -0.022 | +0.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 360 | -0.022 | +0.09€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 395 | +0.026 | +6.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 395 | +0.026 | +6.53€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4672 | +0.020 | +221.14€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4672 | +0.020 | +221.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 870 | +0.016 | +50.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 870 | +0.016 | +50.32€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 365 | +0.075 | +104.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 365 | +0.075 | +104.92€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1751 | +0.025 | +41.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1751 | +0.025 | +41.53€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 823 | +0.013 | +4.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 823 | +0.013 | +4.42€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 622 | -0.005 | +26.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 622 | -0.005 | +26.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2891 | -0.037 | -17.59€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2891 | -0.037 | -17.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 875 | -0.042 | -21.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 875 | -0.042 | -21.29€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1048 | -0.020 | +14.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1048 | -0.020 | +14.39€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 941 | -0.054 | -9.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 941 | -0.054 | -9.52€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 22 | +0.000 | -0.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 22 | +0.000 | -0.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 22222 | -0.033 | -231.10€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 10799 | -0.031 | -66.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11423 | -0.034 | -164.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 776 | -0.051 | -37.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 400 | -0.037 | -5.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 376 | -0.066 | -32.37€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 6015 | -0.025 | -14.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2871 | -0.020 | +23.16€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3144 | -0.030 | -37.40€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 2008 | -0.036 | -20.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1033 | -0.038 | -20.71€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 975 | -0.033 | +0.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 5117 | -0.031 | -43.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2478 | -0.025 | +10.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2639 | -0.036 | -53.41€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4224 | -0.027 | +18.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2064 | -0.028 | +5.14€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2160 | -0.027 | +13.06€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 4082 | -0.045 | -133.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1953 | -0.050 | -79.20€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2129 | -0.042 | -54.75€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 78162 | -0.000 | +4167.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 78162 | -0.000 | +4167.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 11033 | -0.038 | -151.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 11033 | -0.038 | -151.09€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10995 | -0.054 | -303.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10995 | -0.054 | -303.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7553 | -0.052 | -105.89€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7553 | -0.052 | -105.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2184 | -0.057 | -17.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2184 | -0.057 | -17.59€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 103 | -0.024 | -0.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 103 | -0.024 | -0.73€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 825 | -0.117 | -33.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 825 | -0.117 | -33.69€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2296 | -0.065 | -10.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2296 | -0.065 | -10.29€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 874 | -0.019 | -28.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 874 | -0.019 | -28.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3467 | +0.003 | -1.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3467 | +0.003 | -1.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 279 | +0.002 | -4.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 279 | +0.002 | -4.51€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1327 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1327 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 191170 | -0.078 | +2104.48€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 191170 | -0.078 | +2104.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 28828 | -0.102 | -1449.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 28828 | -0.102 | -1449.49€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 28381 | -0.101 | -1005.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 28381 | -0.101 | -1005.16€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9416 | -0.035 | -181.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9416 | -0.035 | -181.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1014 | -0.017 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1014 | -0.017 | -18.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2213 | -0.046 | -28.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2213 | -0.046 | -28.95€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1011 | -0.020 | -29.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1011 | -0.020 | -29.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2684 | -0.023 | -30.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2684 | -0.023 | -30.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1317 | -0.062 | -29.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1317 | -0.062 | -29.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1177 | -0.039 | -43.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1177 | -0.039 | -43.89€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2431 | +0.120 | +976.79€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2295 | +0.124 | +964.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 528 | +0.141 | +273.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 528 | +0.141 | +273.90€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 482 | +0.118 | +171.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 482 | +0.118 | +171.62€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 416 | +0.129 | +193.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 416 | +0.129 | +193.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 393 | +0.133 | +189.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 393 | +0.133 | +189.50€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 476 | +0.096 | +135.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 476 | +0.096 | +135.31€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2578 | -0.022 | -51.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2578 | -0.022 | -51.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 450 | +0.007 | +21.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 450 | +0.007 | +21.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 469 | -0.052 | -35.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 469 | -0.052 | -35.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 618 | -0.045 | -45.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 618 | -0.045 | -45.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 533 | -0.010 | -7.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 533 | -0.010 | -7.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 508 | -0.006 | +15.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 508 | -0.006 | +15.49€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 1070 | +0.043 | +94.40€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1070 | +0.043 | +94.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 360 | +0.017 | +3.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 360 | +0.017 | +3.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 83 | +0.029 | +3.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 83 | +0.029 | +3.15€ | 1 | 3 |
| ✅ STREAK_FADE_15M#SOL | 86 | +0.034 | +8.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 86 | +0.034 | +8.76€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 541 | +0.064 | +78.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 541 | +0.064 | +78.88€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3677 | -0.022 | -139.51€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3677 | -0.022 | -139.51€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 634 | -0.027 | -26.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 634 | -0.027 | -26.29€ | 1 | 0 |
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
| ✅ STREAK_MOM_5M | 11751 | +0.013 | +64.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11751 | +0.013 | +64.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3013 | +0.017 | +21.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3013 | +0.017 | +21.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3148 | +0.013 | +25.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3148 | +0.013 | +25.37€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2968 | +0.009 | -1.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2968 | +0.009 | -1.00€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2622 | +0.014 | +18.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2622 | +0.014 | +18.81€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 14168 | +0.019 | +11.88€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 14168 | +0.019 | +11.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5677 | +0.022 | +10.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5677 | +0.022 | +10.75€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5047 | +0.019 | +2.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5047 | +0.019 | +2.54€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3444 | +0.015 | -1.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3444 | +0.015 | -1.41€ | 1 | 0 |
| ✅ UPDOWN_GBM | 127844 | +0.059 | +12178.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 31971 | +0.077 | +6254.99€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3637 | -0.000 | +40.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 84114 | +0.062 | +5757.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7682 | -0.002 | +129.11€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11185 | +0.103 | +2063.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2124 | +0.165 | +998.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8971 | +0.089 | +1067.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 28966 | +0.056 | +2546.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4322 | +0.081 | +974.32€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1074 | +0.000 | +21.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19949 | +0.065 | +1462.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3463 | -0.004 | +82.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 158 | -0.062 | +4.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14258 | +0.074 | +1574.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 12088 | +0.060 | +681.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 30003 | +0.049 | +2135.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7438 | +0.070 | +1158.95€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1038 | +0.005 | +14.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 18548 | +0.051 | +920.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2832 | -0.003 | +38.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 147 | -0.097 | +2.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26366 | +0.041 | +1511.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8622 | +0.033 | +485.12€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 952 | -0.011 | +7.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15321 | +0.053 | +1020.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1338 | +0.002 | +6.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 133 | -0.137 | -7.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 17064 | +0.073 | +2349.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7381 | +0.088 | +1745.07€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9237 | +0.064 | +604.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 49 | +0.010 | +1.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 438 | -0.098 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1099 | +0.364 | +420.77€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1099 | +0.364 | +420.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 525 | +0.363 | +189.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 525 | +0.363 | +189.87€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 574 | +0.363 | +230.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 574 | +0.363 | +230.90€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 30314 | -0.016 | +7632.53€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 30314 | -0.016 | +7632.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2399 | -0.044 | +644.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2399 | -0.044 | +644.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5594 | -0.115 | +340.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5594 | -0.115 | +340.87€ | 5 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4123 | +0.215 | +2587.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4123 | +0.215 | +2587.65€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8507 | -0.057 | +1277.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8507 | -0.057 | +1277.77€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8397 | -0.051 | +1719.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8397 | -0.051 | +1719.16€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 383 | +0.058 | +34.37€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 383 | +0.058 | +34.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 383 | +0.058 | +34.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 383 | +0.058 | +34.37€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 2014 | +0.286 | +1736.67€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 2014 | +0.286 | +1736.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1058 | +0.280 | +860.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1058 | +0.280 | +860.62€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 956 | +0.291 | +876.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 956 | +0.291 | +876.05€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 910 | -0.123 | -97.87€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 910 | -0.123 | -97.87€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 312 | -0.080 | -36.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 312 | -0.080 | -36.02€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 292 | -0.088 | -24.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 292 | -0.088 | -24.06€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 129 | -0.202 | -9.12€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 129 | -0.202 | -9.12€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5520 | +0.291 | +2401.59€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2159 | +0.247 | +346.57€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2139 | +0.283 | +875.85€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1222 | +0.382 | +1179.17€ | 0 | 1 |