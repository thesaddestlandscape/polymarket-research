# Hipótesis automáticas — 2026-11-28 03:47 UTC
_Generado por shadow_postmortem.py sobre 1522942 resoluciones (PNL=+216756.52€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=738)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1125)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `60.0` → IC=+0.170 (n=365)

  - _Acción_: Kelly boost +0.85€ cuando `n_total_lado` > 60.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8114` → IC=+0.263 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8114 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.173` → IC=+0.195 (n=355)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.173 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=1073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1154)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=568)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=988)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.181 (n=318)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 62.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8108` → IC=+0.264 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8108 (IC base=+0.125)

- **PATRÓN** `banda_z` > `8.262` → IC=+0.197 (n=311)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.262 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.137 (n=843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 8.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1054)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `5103.2759` → IC=+0.133 (n=423)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 5103.2759 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8583.6708` → IC=+0.126 (n=252)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 8583.6708 (IC base=+0.017)

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
- **FILTRO** `restante_s_al_confirmar` < `130.32` → IC=-0.218 (n=13024)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=39074)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#BTC#15min
- **PATRÓN** `restante_s_al_confirmar` < `641.82` → IC=+0.131 (n=2598)

  - _Acción_: Kelly boost +0.66€ cuando `restante_s_al_confirmar` < 641.82 (IC base=+0.089)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.65` → IC=-0.161 (n=3711)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.65
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=11135)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=31497)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7621.7477` → IC=+0.150 (n=2558)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7621.7477 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.126 (n=28239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=34077)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=25433)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=9072)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=2247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=2753)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `16172.9987` → IC=+0.182 (n=715)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16172.9987 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.184 (n=1968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.179 (n=2205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2817)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `15969.7518` → IC=+0.184 (n=728)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 15969.7518 (IC base=+0.176)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.173 (n=656)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.615 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.123 (n=2275)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.45 (IC base=+0.087)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=5808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=2793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.330 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=3239)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.192)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.143 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.142 (n=1007)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.243 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=1227)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.252 (n=1005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.231 (n=2054)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.428 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.143)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=499)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.165 (n=499)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.053)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.141 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.136 (n=1091)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.256 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=28220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=23792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.219 (n=8994)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.336 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `5024.6381` → IC=+0.335 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5024.6381 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=6425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.173 (n=6169)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.159)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.209 (n=4019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=2677)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.245 (n=1897)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.203)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=6254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.173 (n=5289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6397)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4935)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=4939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.251 (n=2395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1696)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=6100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=3876)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1966)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.184)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=1064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.424 (n=1058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `13981.3978` → IC=+0.451 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13981.3978 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=455)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `15188.1532` → IC=+0.446 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15188.1532 (IC base=+0.437)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.399)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.398 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.399)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.419 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.399)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=31685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=36101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.184 (n=5522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.175 (n=11818)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=17030)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=15366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.277 (n=6456)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=6333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=13015)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=5163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.258 (n=6248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.218 (n=5218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.253 (n=6559)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.204 (n=5279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=6137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7573)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=13201)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=14565)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.31` → IC=+0.138 (n=16274)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.31 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6411)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6622)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.73` → IC=+0.142 (n=8109)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.73 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6790)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.135 (n=8773)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.95 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.86` → IC=+0.135 (n=8166)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.300 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=138)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.259 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=85)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.300 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=138)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.259 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=85)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5106` → IC=+0.140 (n=21192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5106 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=21462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=14735)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9728` → IC=+0.247 (n=7064)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9728 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8881` → IC=+0.288 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8881 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.459` → IC=+0.190 (n=10629)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.459 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.266 (n=5807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3029` → IC=+0.255 (n=2185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3029 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7442` → IC=+0.234 (n=5131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7442 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=10133)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `5031.3688` → IC=+0.150 (n=7064)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5031.3688 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.123 (n=13409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0067 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.144 (n=26829)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5652 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.684` → IC=+0.192 (n=1818)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.684 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1799` → IC=+0.194 (n=11030)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1799 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8552` → IC=+0.197 (n=7475)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8552 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2963` → IC=+0.232 (n=2721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2963 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.284` → IC=+0.213 (n=8622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.284 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.227 (n=18995)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.240 (n=1501)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3061` → IC=+0.212 (n=3959)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3061 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=2195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=3007)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9814` → IC=+0.272 (n=2039)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9814 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.782` → IC=+0.286 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.782 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.261 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4385` → IC=+0.213 (n=4326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4385 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2066.52` → IC=+0.215 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2066.52 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.242 (n=1857)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0974` → IC=+0.267 (n=1365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0974 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=4260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0833` → IC=+0.273 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0833 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0727` → IC=+0.239 (n=3548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0727 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.248 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `1.8557` → IC=+0.241 (n=2617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8557 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=4351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.230 (n=1705)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1167` → IC=+0.244 (n=1705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1167 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=4061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.220 (n=2761)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8868` → IC=+0.245 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8868 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.2062` → IC=+0.227 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2062 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.5797` → IC=+0.220 (n=4279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5797 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.669` → IC=+0.260 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.669 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.227 (n=3456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6953 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2768` → IC=+0.261 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2768 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.4383` → IC=+0.243 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4383 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.152 (n=4237)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0071 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.364` → IC=+0.145 (n=4234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.364 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=1591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.3633` → IC=+0.199 (n=2823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3633 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.7783` → IC=+0.141 (n=5125)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.7783 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.569` → IC=+0.141 (n=663)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.569 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.967` → IC=+0.142 (n=3901)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.967 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6265` → IC=+0.159 (n=1412)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6265 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0975` → IC=+0.159 (n=1537)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0975 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4465` → IC=+0.142 (n=4102)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4465 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.183 (n=1369)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.212 (n=2162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=5022)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.872` → IC=+0.277 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.872 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.194 (n=4277)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3497` → IC=+0.224 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3497 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.7343` → IC=+0.210 (n=2116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7343 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5545)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2012.6284` → IC=+0.202 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2012.6284 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.227 (n=1971)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3091` → IC=+0.229 (n=2982)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3091 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=2034)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.269 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.601` → IC=+0.267 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.601 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.254 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.231 (n=2881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1880.1748` → IC=+0.224 (n=2026)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.1748 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.219 (n=3816)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.174 (n=271)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=5751)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.139 (n=776)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0041 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.94` → IC=+0.247 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.94 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1609` → IC=+0.348 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1609 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.377` → IC=+0.343 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.377 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.218` → IC=+0.218 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.218 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `0.8651` → IC=+0.344 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8651 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.0915` → IC=+0.358 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0915 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` < `0.1652` → IC=+0.347 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1652 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.355 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.363 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `2.2749` → IC=+0.345 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2749 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.351 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.0871` → IC=+0.186 (n=1506)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0871 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.3688` → IC=+0.159 (n=736)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3688 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1571` → IC=+0.156 (n=2848)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1571 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.8228` → IC=+0.162 (n=1982)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8228 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `0.667` → IC=+0.154 (n=2656)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.667 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.200 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.1353` → IC=+0.172 (n=1300)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1353 (IC base=+0.060)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.175 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=935)

- **FILTRO** `ibs_20min` > `0.1923` → IC=-0.125 (n=5642)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1923
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2793)

- **FILTRO** `sigma_ewma_delta_pct` > `8.329` → IC=-0.225 (n=913)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.329
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=7522)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.180 (n=376)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.9803` → IC=+0.283 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9803 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `1.3395` → IC=+0.264 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.3395 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.217` → IC=+0.141 (n=374)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 2.217 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `1.0024` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0024 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.272 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.7847` → IC=+0.280 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7847 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.159 (n=2793)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1923 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.8349` → IC=+0.299 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8349 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.3269` → IC=+0.293 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3269 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.6936` → IC=+0.309 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6936 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0787` → IC=+0.322 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0787 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4676` → IC=+0.306 (n=1212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4676 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5251` → IC=+0.302 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5251 (IC base=-0.031)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7949` → IC=-0.161 (n=4318)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7949
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=2227)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.178 (n=1399)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=5146)

- **FILTRO** `ibs_20min` > `0.72` → IC=-0.192 (n=2267)

  - _Acción_: SKIP cuando `ibs_20min` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=6840)

- **PATRÓN** `ibs_20min` > `0.7949` → IC=+0.147 (n=2227)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7949 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.4559` → IC=+0.339 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4559 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.316 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3087` → IC=+0.320 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3087 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.542` → IC=+0.315 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.542 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1147` → IC=+0.294 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1147 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.6353` → IC=+0.275 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6353 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.2109` → IC=+0.276 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2109 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.1083` → IC=+0.275 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1083 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.5579` → IC=+0.266 (n=2314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5579 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.187 (n=9282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0113 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.284 (n=12631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0133` → IC=+0.304 (n=1912)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0133 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.448` → IC=+0.168 (n=12545)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.448 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6914` → IC=+0.279 (n=9315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6914 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.295 (n=2301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6559` → IC=+0.290 (n=5401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6559 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=15860)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.137 (n=18047)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0073 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5158` → IC=+0.174 (n=23815)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5158 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2844` → IC=+0.282 (n=9649)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2844 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.6911` → IC=+0.279 (n=4092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6911 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1871` → IC=+0.285 (n=3099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1871 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.323 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4556` → IC=+0.302 (n=4613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4556 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2768` → IC=+0.305 (n=6274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2768 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.312 (n=13822)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8218` → IC=-0.150 (n=4913)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8218
  - _Potencial_: sin este filtro IC_bueno=+0.318 (n=2531)

- **FILTRO** `ibs_20min` > `0.6978` → IC=-0.241 (n=1692)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6978
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=5079)

- **FILTRO** `sigma_ewma_delta_pct` > `4.043` → IC=-0.240 (n=1419)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.043
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5352)

- **PATRÓN** `ibs_20min` > `0.8218` → IC=+0.318 (n=2531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8218 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.142` → IC=+0.176 (n=2772)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 2.142 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.333 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4476` → IC=+0.294 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4476 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2336` → IC=+0.319 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2336 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.326 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1697` → IC=+0.170 (n=1693)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1697 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.386 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6481` → IC=+0.388 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6481 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1843` → IC=+0.228 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1843 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.529` → IC=+0.214 (n=3020)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.529 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.214 (n=2719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1952 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.222 (n=2429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.240 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4151` → IC=+0.232 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4151 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4502` → IC=+0.223 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4502 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `366.0` → IC=+0.232 (n=2691)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 366.0 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.5804` → IC=+0.256 (n=2433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5804 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `0.8314` → IC=+0.263 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8314 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.281 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5313` → IC=+0.256 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5313 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1523` → IC=+0.263 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1523 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.273 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 196.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.319 (n=1722)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.286 (n=3359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.541` → IC=+0.305 (n=2583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.541 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` < `0.1306` → IC=+0.294 (n=3528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1306 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `1.6` → IC=+0.291 (n=3694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4391)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `2009.8728` → IC=+0.300 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.8728 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.302 (n=2447)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.332 (n=2356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.189` → IC=+0.328 (n=1556)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.189 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=1356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.313 (n=1595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.1593` → IC=+0.321 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1593 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.945` → IC=+0.322 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.945 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.199` → IC=+0.308 (n=3511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.199 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3445` → IC=+0.316 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3445 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.7483` → IC=+0.326 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7483 (IC base=+0.308)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `1575.1356` → IC=+0.314 (n=3154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1575.1356 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.307 (n=2361)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1625` → IC=+0.237 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1625 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.6458` → IC=+0.230 (n=2846)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6458 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.1733` → IC=+0.234 (n=2579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1733 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.5938` → IC=+0.230 (n=2580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5938 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.234 (n=2712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.0763` → IC=+0.236 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0763 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4161` → IC=+0.236 (n=2508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4161 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.4974` → IC=+0.233 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4974 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.248 (n=2559)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 116.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.0918` → IC=+0.150 (n=1758)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.0918 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.3945` → IC=+0.261 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3945 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `1.173` → IC=+0.261 (n=1888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.173 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` > `0.6123` → IC=+0.259 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6123 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.264 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.284 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `1.7831` → IC=+0.282 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7831 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `2.426` → IC=+0.269 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.426 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.285 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7536` → IC=-0.247 (n=2860)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7536
  - _Potencial_: sin este filtro IC_bueno=+0.319 (n=2860)

- **FILTRO** `ibs_20min` > `0.6` → IC=-0.233 (n=1343)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=4054)

- **FILTRO** `sigma_ewma_delta_pct` > `8.222` → IC=-0.257 (n=619)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.222
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=4778)

- **PATRÓN** `ibs_20min` > `0.7536` → IC=+0.319 (n=2860)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7536 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `1.1141` → IC=+0.353 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1141 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.448` → IC=+0.161 (n=2346)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.448 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8418` → IC=+0.352 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8418 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.695` → IC=+0.338 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.695 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.369 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7961` → IC=+0.357 (n=1372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7961 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.356 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.168 (n=4054)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.3265` → IC=+0.274 (n=2215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3265 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.71` → IC=+0.136 (n=4230)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.71 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6857` → IC=+0.285 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6857 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.299 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.282 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8106 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.290 (n=2134)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.350 (n=2695)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=3040)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=3168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.6511` → IC=+0.335 (n=3017)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6511 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2224` → IC=+0.336 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2224 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.714` → IC=+0.342 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.714 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.7017` → IC=+0.328 (n=2696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7017 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.345 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.5417` → IC=+0.326 (n=2607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5417 (IC base=+0.313)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.314 (n=3799)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `2999.8754` → IC=+0.324 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2999.8754 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.330 (n=3243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=3255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.326 (n=3242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3902 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `1.3142` → IC=+0.322 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3142 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` < `0.2606` → IC=+0.316 (n=3199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2606 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.618` → IC=+0.331 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.618 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` < `0.6348` → IC=+0.319 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6348 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `1.2104` → IC=+0.339 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2104 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.357 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.326 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `2.1633` → IC=+0.316 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1633 (IC base=+0.312)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.219 (n=6790)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1287` → IC=+0.193 (n=8962)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1287 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=21144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5344` → IC=+0.228 (n=20355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5344 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1719` → IC=+0.205 (n=7631)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1719 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.663` → IC=+0.259 (n=3983)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.663 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1729` → IC=+0.152 (n=13574)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1729 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6189` → IC=+0.151 (n=13573)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6189 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.207 (n=2925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6086` → IC=+0.186 (n=6615)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6086 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.192 (n=19322)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.193 (n=8929)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0063 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.185 (n=13528)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0083 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.223 (n=6769)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.205 (n=9742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5294` → IC=+0.236 (n=20296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5294 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.1999` → IC=+0.178 (n=14862)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1999 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.36` → IC=+0.191 (n=3193)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.36 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.484` → IC=+0.190 (n=18153)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.484 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.165 (n=14372)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1913 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.218 (n=3057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5653` → IC=+0.184 (n=8553)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5653 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6401` → IC=+0.196 (n=6479)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6401 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.198 (n=19272)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 90.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.252 (n=1516)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.0762` → IC=+0.265 (n=1116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0762 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=2265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.290 (n=2229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.453` → IC=+0.325 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.453 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.286 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.8304` → IC=+0.226 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8304 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4341` → IC=+0.229 (n=3205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4341 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.253 (n=2828)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.1018` → IC=+0.306 (n=1244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1018 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=2916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.254 (n=2580)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.0081` → IC=+0.306 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0081 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.952` → IC=+0.255 (n=2805)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.952 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.253 (n=2506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.264 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.5528` → IC=+0.263 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5528 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.6727` → IC=+0.256 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6727 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=3031)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.191 (n=1047)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0684` → IC=+0.173 (n=1042)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0684 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2429` → IC=+0.201 (n=3121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2429 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.211 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.483` → IC=+0.201 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.483 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8507` → IC=+0.135 (n=2081)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8507 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.129 (n=1042)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.1915 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.168 (n=477)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5093` → IC=+0.129 (n=1353)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5093 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4553` → IC=+0.139 (n=1025)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4553 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.131 (n=3044)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 381.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.180 (n=2982)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0062 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2618` → IC=+0.175 (n=2979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2618 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.174 (n=1622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.6184` → IC=+0.208 (n=3386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6184 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.2269` → IC=+0.174 (n=3686)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.2269 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.846` → IC=+0.179 (n=625)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.846 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.022` → IC=+0.155 (n=2976)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.022 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2077` → IC=+0.162 (n=3385)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2077 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.153 (n=2978)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4845` → IC=+0.156 (n=3257)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4845 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.195 (n=1406)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 201.0 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.232 (n=1559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2614` → IC=+0.233 (n=2292)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2614 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.97` → IC=+0.304 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.97 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.234 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.1704` → IC=+0.218 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1704 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2007.0492` → IC=+0.224 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.0492 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.242 (n=3097)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.2562` → IC=+0.266 (n=2064)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2562 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.272 (n=1169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0462` → IC=+0.290 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0462 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.678` → IC=+0.281 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.678 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.279 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7638` → IC=+0.240 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7638 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `3.3154` → IC=+0.256 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3154 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1877.4416` → IC=+0.247 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1877.4416 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.234 (n=2622)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.189 (n=1126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.004 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0826` → IC=+0.170 (n=1119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0826 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2404` → IC=+0.187 (n=3356)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2404 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1514` → IC=+0.189 (n=1880)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1514 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.177` → IC=+0.199 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.177 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8337` → IC=+0.138 (n=2238)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8337 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.173 (n=503)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5028` → IC=+0.137 (n=1096)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.5028 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6919.7421` → IC=+0.196 (n=1522)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6919.7421 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.127 (n=3301)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 124.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.172 (n=2395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4378` → IC=+0.150 (n=3590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4378 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.67` → IC=+0.188 (n=3590)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.67 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1751` → IC=+0.157 (n=3691)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1751 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.172` → IC=+0.145 (n=850)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.172 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.150 (n=2395)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8509 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.169 (n=545)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.7916` → IC=+0.135 (n=2283)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7916 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.5144` → IC=+0.136 (n=3058)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.5144 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6670.9737` → IC=+0.193 (n=1628)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6670.9737 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.156 (n=1137)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.159 (n=2495)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.207 (n=3739)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4737 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7992` → IC=+0.212 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7992 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.862` → IC=+0.280 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.862 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1682` → IC=+0.132 (n=3739)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1682 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6228` → IC=+0.126 (n=3741)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6228 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1637` → IC=+0.125 (n=3819)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1637 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.135 (n=518)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5459` → IC=+0.130 (n=1599)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5459 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2710.4123` → IC=+0.198 (n=1695)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2710.4123 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.130 (n=2404)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 26.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.151 (n=3456)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0113 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1196` → IC=+0.171 (n=1308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1196 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=4000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6489` → IC=+0.220 (n=3920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6489 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.23` → IC=+0.145 (n=3891)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.23 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.229` → IC=+0.145 (n=3473)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.229 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1831` → IC=+0.129 (n=3920)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1831 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.7028` → IC=+0.124 (n=3502)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7028 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.154 (n=556)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.140 (n=1244)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.479` → IC=+0.136 (n=1244)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.479 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2603.8733` → IC=+0.193 (n=1777)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2603.8733 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.131 (n=3742)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.245 (n=3359)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.4636` → IC=+0.232 (n=2956)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4636 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=3490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.253 (n=3359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1878` → IC=+0.232 (n=2062)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1878 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.8515` → IC=+0.227 (n=3479)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8515 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.492` → IC=+0.263 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.492 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6164` → IC=+0.233 (n=3358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6164 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.266 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.5063` → IC=+0.231 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5063 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=4263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2632.626` → IC=+0.229 (n=2239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2632.626 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0211` → IC=+0.249 (n=1577)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0211 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6212` → IC=+0.248 (n=3478)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6212 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0388` → IC=+0.296 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0388 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `1.2084` → IC=+0.251 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2084 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.969` → IC=+0.274 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.969 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.243 (n=2320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8653 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `1.0483` → IC=+0.237 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0483 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.299 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8565` → IC=+0.237 (n=2203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8565 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.5616` → IC=+0.238 (n=2952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5616 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=4391)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.199 (n=1769)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1457` → IC=+0.168 (n=2329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1457 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=5530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.2959` → IC=+0.189 (n=5292)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2959 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9192` → IC=+0.180 (n=797)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.9192 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.479` → IC=+0.208 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.479 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8529` → IC=+0.162 (n=3225)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8529 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.186` → IC=+0.159 (n=1613)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.186 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1553` → IC=+0.170 (n=1362)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1553 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.5256` → IC=+0.156 (n=2275)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5256 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.8073` → IC=+0.155 (n=3447)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8073 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.154 (n=5824)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7304.2068` → IC=+0.188 (n=2400)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7304.2068 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.7101` → IC=+0.141 (n=5834)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.7101 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.137 (n=2571)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 22.0 (IC base=+0.100)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.200 (n=1152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.225 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.222 (n=1183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.2136` → IC=+0.223 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2136 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.6958` → IC=+0.237 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6958 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.825` → IC=+0.226 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.825 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.6238` → IC=+0.215 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6238 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.0887` → IC=+0.209 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0887 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.1439` → IC=+0.201 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1439 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.3995` → IC=+0.193 (n=1284)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.3995 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `15567.5377` → IC=+0.203 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15567.5377 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.150 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0033 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.2134` → IC=+0.192 (n=722)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.2134 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.165 (n=712)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 166.0 (IC base=+0.074)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.238 (n=543)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.155 (n=717)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=1690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.7593` → IC=+0.257 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7593 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1587` → IC=+0.163 (n=769)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1587 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.976` → IC=+0.181 (n=230)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.976 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8289` → IC=+0.151 (n=1085)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8289 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.183 (n=219)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.7716` → IC=+0.155 (n=1071)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7716 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7789.4103` → IC=+0.173 (n=738)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7789.4103 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.143 (n=530)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 30.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.125 (n=1630)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0082 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1814` → IC=+0.210 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1814 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6736` → IC=+0.136 (n=717)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6736 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.128 (n=280)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `4074.8497` → IC=+0.138 (n=1455)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 4074.8497 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.145 (n=714)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 41.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.153 (n=476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0073 (IC base=+0.123)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.135 (n=475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0129 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=1003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.7273` → IC=+0.225 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7273 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.2199` → IC=+0.144 (n=677)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.2199 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.862` → IC=+0.232 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.862 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.0405` → IC=+0.132 (n=1253)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0405 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.7005` → IC=+0.128 (n=1271)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.7005 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4192` → IC=+0.152 (n=461)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4192 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=1436)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3046.3244` → IC=+0.150 (n=475)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3046.3244 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.139 (n=452)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 9.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6923` → IC=+0.144 (n=1592)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6923 (IC base=+0.078)

- **PATRÓN** `libro_liquidez` > `2737.6784` → IC=+0.162 (n=722)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2737.6784 (IC base=+0.078)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0146` → IC=+0.237 (n=321)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0146 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.312` → IC=+0.178 (n=321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.312 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.8462` → IC=+0.174 (n=424)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.8462 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.3805` → IC=+0.187 (n=481)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.3805 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.2422` → IC=+0.188 (n=229)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2422 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.53` → IC=+0.189 (n=483)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 5.53 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `1.1939` → IC=+0.248 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1939 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` < `0.2469` → IC=+0.192 (n=517)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.2469 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `2.5077` → IC=+0.193 (n=451)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.5077 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.190 (n=485)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2676.4564` → IC=+0.200 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2676.4564 (IC base=+0.173)

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
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.226 (n=8976)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=28123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9655` → IC=+0.299 (n=8982)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9655 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9631` → IC=+0.215 (n=3081)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9631 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.851` → IC=+0.260 (n=6585)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.851 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8642` → IC=+0.163 (n=12104)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8642 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.217 (n=3519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6383` → IC=+0.194 (n=8778)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6383 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1768.047` → IC=+0.181 (n=26914)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1768.047 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=25561)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.199 (n=8353)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0056 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.206 (n=8354)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1144` → IC=+0.204 (n=8345)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1144 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=9364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.596` → IC=+0.244 (n=25027)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.596 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.1953` → IC=+0.182 (n=16034)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1953 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.49` → IC=+0.204 (n=23355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.49 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.6251` → IC=+0.182 (n=5596)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6251 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.256 (n=3445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6299` → IC=+0.211 (n=8039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6299 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.213 (n=23943)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.262 (n=1949)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3103` → IC=+0.235 (n=3771)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3103 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2875)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.315 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.034` → IC=+0.298 (n=2815)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.034 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2318` → IC=+0.287 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2318 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6262` → IC=+0.242 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6262 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2066.615` → IC=+0.238 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2066.615 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.269 (n=1312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.263 (n=1783)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1298` → IC=+0.289 (n=1731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1298 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.264 (n=4085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.264 (n=3548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.4727` → IC=+0.283 (n=3462)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4727 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0998` → IC=+0.264 (n=3605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0998 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.286 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5656` → IC=+0.263 (n=1670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5656 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6384` → IC=+0.271 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6384 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=4185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.263 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.169 (n=1960)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.146 (n=1479)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2913` → IC=+0.200 (n=3961)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2913 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.7453` → IC=+0.211 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7453 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.003` → IC=+0.173 (n=690)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.003 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6316` → IC=+0.157 (n=1478)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6316 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.2201` → IC=+0.143 (n=1478)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.2201 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.186 (n=616)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.272 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1711` → IC=+0.144 (n=3840)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1711 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5201` → IC=+0.144 (n=3899)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5201 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `287.0` → IC=+0.152 (n=2883)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 287.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.169 (n=3450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0062 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.177 (n=1306)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=1448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.3224` → IC=+0.231 (n=2611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3224 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.7696` → IC=+0.152 (n=4743)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.7696 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.002` → IC=+0.147 (n=1846)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.002 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.188` → IC=+0.150 (n=4001)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.188 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0392` → IC=+0.157 (n=3447)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0392 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.222` → IC=+0.202 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.222 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4364` → IC=+0.150 (n=3804)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4364 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7756` → IC=+0.153 (n=2536)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7756 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=5082)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.182 (n=1250)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 211.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.242 (n=2032)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=4704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=3989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.865` → IC=+0.311 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.865 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2033` → IC=+0.233 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2033 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.6122` → IC=+0.230 (n=4387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6122 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=5188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2011.3382` → IC=+0.238 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2011.3382 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.249 (n=1899)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1864` → IC=+0.260 (n=1900)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1864 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.071` → IC=+0.295 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.071 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.851` → IC=+0.305 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.851 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.3456` → IC=+0.300 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3456 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1714` → IC=+0.255 (n=2789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1714 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1991.42` → IC=+0.254 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1991.42 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.248 (n=2797)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.188 (n=1552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3607` → IC=+0.147 (n=4096)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3607 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8746` → IC=+0.262 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8746 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.169 (n=2274)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.973` → IC=+0.161 (n=2033)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.973 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8538` → IC=+0.154 (n=3104)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8538 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.198 (n=614)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.152 (n=2004)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1549` → IC=+0.144 (n=2065)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1549 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5906.3056` → IC=+0.228 (n=2111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5906.3056 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.144 (n=3059)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 86.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.169 (n=3957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4658` → IC=+0.163 (n=3952)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4658 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.7057` → IC=+0.201 (n=3952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7057 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.6524` → IC=+0.158 (n=4588)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6524 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.033` → IC=+0.162 (n=793)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.033 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.028` → IC=+0.155 (n=3443)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.028 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6812` → IC=+0.163 (n=1739)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6812 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.211 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.8043` → IC=+0.156 (n=2557)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.8043 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5243` → IC=+0.159 (n=3424)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5243 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `6737.5602` → IC=+0.219 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6737.5602 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.172 (n=1337)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 58.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.145 (n=3161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0101 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=3356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.257 (n=3161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8157` → IC=+0.195 (n=1047)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.8157 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.192` → IC=+0.271 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.192 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2098` → IC=+0.128 (n=4740)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2098 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1019` → IC=+0.124 (n=4516)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1019 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.147 (n=593)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.8275` → IC=+0.132 (n=3088)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8275 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2771.0345` → IC=+0.239 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2771.0345 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.158 (n=3897)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0114 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1438` → IC=+0.151 (n=1476)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1438 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=4557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.224 (n=4454)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.151 (n=4083)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.023` → IC=+0.161 (n=4301)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.023 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1941` → IC=+0.143 (n=4427)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1941 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.198 (n=779)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.165 (n=1411)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.5023` → IC=+0.145 (n=1411)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.5023 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2645.2912` → IC=+0.225 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.2912 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.149 (n=4273)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 47.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.254 (n=4332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.240 (n=2897)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.988` → IC=+0.301 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.988 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.2047` → IC=+0.250 (n=2195)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2047 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.906` → IC=+0.300 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.906 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.6388` → IC=+0.242 (n=4330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6388 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.262 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.5313` → IC=+0.257 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5313 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=5473)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2647.7632` → IC=+0.240 (n=2886)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2647.7632 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0244` → IC=+0.270 (n=1499)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0244 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.250 (n=4227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.1402` → IC=+0.304 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1402 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.2084` → IC=+0.250 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2084 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2333` → IC=+0.249 (n=4322)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2333 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.841` → IC=+0.283 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.841 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.6361` → IC=+0.250 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6361 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.264 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.314 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.5504` → IC=+0.248 (n=3814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5504 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.245 (n=3752)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.234 (n=6652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.5404` → IC=+0.235 (n=7552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5404 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=7576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.260 (n=2521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` < `0.973` → IC=+0.230 (n=6220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.973 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.427` → IC=+0.237 (n=2522)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.427 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `0.7046` → IC=+0.232 (n=2373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7046 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.8771` → IC=+0.229 (n=3593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8771 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.1639` → IC=+0.237 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1639 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4493` → IC=+0.238 (n=2477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4493 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.231 (n=5390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `3771.3096` → IC=+0.235 (n=5035)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3771.3096 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.229 (n=1806)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.211 (n=3612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.4189` → IC=+0.221 (n=4764)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4189 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=1815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=2458)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.7286` → IC=+0.216 (n=5414)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7286 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.7166` → IC=+0.219 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7166 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.681` → IC=+0.223 (n=4931)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.681 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2537` → IC=+0.210 (n=4920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2537 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.7288` → IC=+0.203 (n=4395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7288 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.212 (n=5007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.5361` → IC=+0.215 (n=2346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5361 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8221` → IC=+0.218 (n=3555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8221 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.235 (n=3578)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.211)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.279 (n=849)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.306 (n=322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` < `0.8328` → IC=+0.282 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8328 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` < `0.3337` → IC=+0.285 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3337 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.096` → IC=+0.300 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.096 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.280 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` > `0.8759` → IC=+0.289 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8759 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.336 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` < `1.8048` → IC=+0.277 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8048 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `1.4175` → IC=+0.275 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4175 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `12950.5411` → IC=+0.288 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12950.5411 (IC base=+0.274)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.260 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3904` → IC=+0.185 (n=1554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3904 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.173 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.191 (n=684)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1382 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.3617` → IC=+0.173 (n=334)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3617 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.5601` → IC=+0.170 (n=1861)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.5601 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.338` → IC=+0.190 (n=1527)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 6.338 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.0935` → IC=+0.185 (n=1368)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.0935 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1521` → IC=+0.185 (n=474)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1521 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.496` → IC=+0.175 (n=1545)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.496 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `1.8093` → IC=+0.172 (n=1030)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8093 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `14629.5629` → IC=+0.170 (n=704)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14629.5629 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `702.0` → IC=+0.185 (n=1507)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 702.0 (IC base=+0.169)

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

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.222 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.343 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.312 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.6336` → IC=+0.316 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6336 (IC base=+0.288)

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

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 5.0 (IC base=+0.288)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.224 (n=1839)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.474` → IC=+0.222 (n=2089)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.474 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.4666` → IC=+0.231 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4666 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.8315` → IC=+0.216 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8315 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.4293` → IC=+0.226 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4293 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.248` → IC=+0.221 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.248 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.217 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8615 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.229` → IC=+0.221 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.229 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.217 (n=1940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.1582` → IC=+0.217 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1582 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4004` → IC=+0.235 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4004 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4929` → IC=+0.216 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4929 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.247 (n=563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.5101` → IC=+0.219 (n=1687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5101 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.215 (n=626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=1131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.213 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0847 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.7294` → IC=+0.221 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7294 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.201` → IC=+0.209 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.201 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2534` → IC=+0.212 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2534 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.7178` → IC=+0.210 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7178 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.227 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.4742` → IC=+0.207 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4742 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.7691` → IC=+0.210 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7691 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.210 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 95.0 (IC base=+0.205)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.233 (n=889)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.232 (n=446)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.253 (n=1198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.222 (n=1219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.9877` → IC=+0.303 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9877 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `1.094` → IC=+0.244 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.094 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.023` → IC=+0.274 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.023 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `0.6422` → IC=+0.252 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6422 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `1.2446` → IC=+0.225 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2446 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.225 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.250 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.5096` → IC=+0.231 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5096 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `3376.162` → IC=+0.246 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3376.162 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0141` → IC=+0.246 (n=1011)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0141 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.254 (n=906)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.246)

- **PATRÓN** `drift_60min` |x|≤ `0.549` → IC=+0.254 (n=891)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.549 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.266 (n=700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` < `0.6463` → IC=+0.270 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6463 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.5652` → IC=+0.246 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5652 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` < `0.2463` → IC=+0.254 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2463 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.048` → IC=+0.264 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.048 (IC base=+0.246)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.259 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.256 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `1.8587` → IC=+0.266 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8587 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.250 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `4038.9632` → IC=+0.268 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4038.9632 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.274 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.246)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.145 (n=996)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0044 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.4233` → IC=+0.142 (n=2897)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.4233 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1615` → IC=+0.161 (n=1330)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1615 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.289` → IC=+0.149 (n=630)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.289 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.5781` → IC=+0.182 (n=2316)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5781 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.522` → IC=+0.139 (n=1033)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 2.522 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` > `1.0986` → IC=+0.143 (n=703)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0986 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.152` → IC=+0.191 (n=655)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.152 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.1652` → IC=+0.126 (n=1965)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.1652 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` > `2.5283` → IC=+0.127 (n=744)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.5283 (IC base=+0.103)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5656` → IC=-0.120 (n=351)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5656
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=714)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.122 (n=730)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0057 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5656` → IC=+0.158 (n=714)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5656 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.165 (n=368)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.0612` → IC=+0.247 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0612 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.2132` → IC=+0.162 (n=155)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2132 (IC base=+0.058)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.161 (n=381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0044 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.135 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5264` → IC=+0.163 (n=745)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5264 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.158 (n=396)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.057` → IC=+0.181 (n=183)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 12.057 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.3108` → IC=+0.225 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3108 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2624` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2624 (IC base=+0.051)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9778` → IC=+0.189 (n=320)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.9778 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7698` → IC=+0.162 (n=232)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.7698 (IC base=+0.041)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.178 (n=439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0103 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.120 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.195 (n=625)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.2242` → IC=+0.151 (n=620)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2242 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.015` → IC=+0.250 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.015 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.1136` → IC=+0.186 (n=208)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1136 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.1626` → IC=+0.187 (n=161)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1626 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.5364` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.5364 (IC base=+0.100)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.399 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.326 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.9191` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9191 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.5696` → IC=+0.333 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5696 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.4847` → IC=+0.381 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4847 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.738` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.738 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.112` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.112 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` < `0.8086` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8086 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` > `1.1852` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1852 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.193` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.193 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `2.819` → IC=+0.332 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.819 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.327 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1576.2726` → IC=+0.354 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1576.2726 (IC base=+0.293)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.372 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.366 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.329)

- **PATRÓN** `ibs_20min` < `0.0457` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0457 (IC base=+0.329)

- **PATRÓN** `ibs_20min` > `0.4868` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4868 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.557` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.557 (IC base=+0.329)

- **PATRÓN** `volumen_regimen` > `0.5915` → IC=+0.379 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5915 (IC base=+0.329)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.419 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.329)

- **PATRÓN** `volumen_spike_ratio` < `1.5421` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5421 (IC base=+0.329)

- **PATRÓN** `volumen_spike_ratio` > `3.0959` → IC=+0.368 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0959 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.343 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `38.0` → IC=+0.330 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 38.0 (IC base=+0.329)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.248 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=214)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=328)

- **FILTRO** `volumen_regimen` < `0.8808` → IC=-0.307 (n=138)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8808
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=284)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.292 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=284)

- **FILTRO** `dist_vwap_pct` > `0.4617` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4617
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=366)

- **FILTRO** `sigma_ewma_delta_pct` > `9.288` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.288
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=372)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=277)

- **FILTRO** `volumen_spike_ratio` > `2.2757` → IC=-0.269 (n=76)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2757
  - _Potencial_: sin este filtro IC_bueno=-0.251 (n=231)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.007` → IC=-0.255 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=104)

- **FILTRO** `ibs_20min` < `0.0328` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0328
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=101)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.281 (n=117)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=42)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.329 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=120)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.003` → IC=-0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.003
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=104)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.472 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=104)

- **FILTRO** `volumen_regimen` > `1.0898` → IC=-0.188 (n=46)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0898
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=92)

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
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.346 (n=37)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=112)

- **FILTRO** `volumen_spike_ratio` < `1.5734` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5734
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=93)

- **FILTRO** `dist_vwap_pct` > `0.2836` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2836
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=61)

- **FILTRO** `volumen_regimen` < `0.9756` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9756
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=53)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.200 (n=434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.201 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9091` → IC=+0.311 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9091 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.194` → IC=+0.184 (n=226)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 10.194 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.6198` → IC=+0.187 (n=311)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6198 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `1.1943` → IC=+0.184 (n=311)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1943 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` < `0.2118` → IC=+0.185 (n=952)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2118 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.419` → IC=+0.205 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.419 (IC base=+0.169)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.126 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` > 0.0044 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.7306` → IC=+0.135 (n=253)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7306 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.3355` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3355 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.2563` → IC=+0.134 (n=468)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2563 (IC base=+0.074)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.151 (n=270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0029 (IC base=+0.133)

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

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.357 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.291 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` > `0.6111` → IC=+0.296 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6111 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.7834` → IC=+0.397 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7834 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.276)

- **PATRÓN** `volumen_regimen` < `0.811` → IC=+0.297 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.811 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` < `0.2102` → IC=+0.302 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2102 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.312 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` < `1.4956` → IC=+0.332 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4956 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` > `2.4024` → IC=+0.320 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4024 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.276 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.276)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=217)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.322)

- **PATRÓN** `elapsed_s` > `209.5` → IC=+0.374 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.5 (IC base=+0.322)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.322)

- **PATRÓN** `drift_60min` |x|≤ `0.6903` → IC=+0.392 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6903 (IC base=+0.322)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.376 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.322)

- **PATRÓN** `ballena_activa_n` < `1043.0` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1043.0 (IC base=+0.322)

- **PATRÓN** `drift_ventana_pct` |x|> `0.445` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.445 (IC base=+0.280)

- **PATRÓN** `elapsed_s` > `232.5` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.5 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `2.3682` → IC=+0.309 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3682 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.7195` → IC=+0.308 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7195 (IC base=+0.280)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.313 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `1283.0` → IC=+0.358 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1283.0 (IC base=+0.280)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=217)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.322)

- **PATRÓN** `elapsed_s` > `209.5` → IC=+0.374 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.5 (IC base=+0.322)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.322)

- **PATRÓN** `drift_60min` |x|≤ `0.6903` → IC=+0.392 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6903 (IC base=+0.322)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.376 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.322)

- **PATRÓN** `ballena_activa_n` < `1043.0` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1043.0 (IC base=+0.322)

- **PATRÓN** `drift_ventana_pct` |x|> `0.445` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.445 (IC base=+0.280)

- **PATRÓN** `elapsed_s` > `232.5` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 232.5 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `2.3682` → IC=+0.309 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3682 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.7195` → IC=+0.308 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7195 (IC base=+0.280)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.313 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `1283.0` → IC=+0.358 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1283.0 (IC base=+0.280)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=297)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=298)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1771)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.173 (n=99)

  - _Acción_: Kelly boost +0.87€ cuando `liq_n` > 2.0 (IC base=+0.079)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.171 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.079)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11682.4811` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 11682.4811
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=129)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=165)

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
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=289)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=4355)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=277)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=234)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.159 (n=89)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=175)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.155 (n=175)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 33.0 (IC base=+0.017)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=306)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.026)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.159)

- **PATRÓN** `liq_usd_total` > `2564.96` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2564.96 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.201 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.04 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3293.399` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3293.399 (IC base=+0.159)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1736)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1690)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=778)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=787)

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
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1215)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1215)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1662)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1662)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=381)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=381)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.156 (n=123)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=273)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=434)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=484)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=354)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=465)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=465)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=453)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=3893)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=9971)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.153 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=153)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.164 (n=468)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1133)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.148 (n=370)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=1002)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.139 (n=471)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.51 (IC base=-0.009)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.121 (n=323)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=382)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.124 (n=171)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=541)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.156 (n=257)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1383)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.129 (n=375)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.51 (IC base=-0.019)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.137 (n=395)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=832)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.132 (n=599)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=759)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=640)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=663)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.137 (n=686)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=789)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9423)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=29204)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9717)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=30313)

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
- **FILTRO** `py_entrada` > `0.57` → IC=-0.175 (n=1422)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4437)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.179 (n=1458)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=4414)

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
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3496)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4448)

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
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=51)

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

- **FILTRO** `ibs_20min` > `0.8571` → IC=-0.127 (n=654)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8571
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=666)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.175 (n=438)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=873)

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
- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=20837)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=64758)

- **FILTRO** `ibs_7min` < `0.2105` → IC=-0.237 (n=21394)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2105
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=64201)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.153 (n=28396)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=57199)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26426)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=80309)

- **FILTRO** `ibs_7min` > `0.278` → IC=-0.182 (n=26676)

  - _Acción_: SKIP cuando `ibs_7min` > 0.278
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=80059)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.126 (n=3515)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=11023)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=3563)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=10975)

- **FILTRO** `ibs_7min` < `0.7103` → IC=-0.210 (n=3634)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7103
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10904)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.203 (n=3631)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=10907)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.257 (n=3716)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11154)

- **FILTRO** `ibs_7min` > `0.2637` → IC=-0.186 (n=3717)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2637
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=11153)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.177 (n=3709)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=11161)

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
- **FILTRO** `py_entrada` < `0.33` → IC=-0.275 (n=3259)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10972)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.201 (n=3556)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10675)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.196 (n=3460)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10771)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=3434)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=11296)

- **FILTRO** `ibs_7min` > `0.2716` → IC=-0.178 (n=3676)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2716
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=11054)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.171 (n=3628)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=11102)

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
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1043)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1332)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.154 (n=189)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=698)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=939)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=600)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=255)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=509)

- **FILTRO** `libro_liquidez` < `3309.2037` → IC=-0.140 (n=198)

  - _Acción_: SKIP cuando `libro_liquidez` < 3309.2037
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=594)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=565)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.143 (n=793)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.130 (n=893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.163 (n=583)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 459.6089 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4209.805` → IC=+0.130 (n=582)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4209.805 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.175 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 14.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `287.798` → IC=+0.170 (n=268)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 287.798 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.143 (n=362)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.04 (IC base=+0.139)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.135 (n=365)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=341)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.122 (n=442)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4156` → IC=+0.162 (n=211)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `706.5888` → IC=+0.175 (n=278)

  - _Acción_: Kelly boost +0.88€ cuando `total_vol_5m` < 706.5888 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 59.0 (IC base=+0.129)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4315` → IC=+0.210 (n=136)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4315 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.133 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.161 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `4782.684` → IC=+0.183 (n=200)

  - _Acción_: Kelly boost +0.92€ cuando `total_vol_5m` < 4782.684 (IC base=+0.133)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.121 (n=249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 10.0 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=223)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.092)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `4.4525` → IC=-0.197 (n=130)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4525
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=132)

- **FILTRO** `sigma_h` > `0.0061` → IC=-0.124 (n=536)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=538)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.166 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0044 (IC base=-0.029)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.179 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=216)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.274 (n=82)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.006)

- **PATRÓN** `pct_vs_K` |x|≤ `2.0617` → IC=+0.218 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 2.0617 (IC base=+0.006)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `7.5593` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.5593
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=72)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0157` → IC=-0.217 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0157
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=154)

- **FILTRO** `T_h` < `63.9936` → IC=-0.179 (n=51)

  - _Acción_: SKIP cuando `T_h` < 63.9936
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=154)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0173` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0173
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.268 (n=611)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=301)

- **FILTRO** `sigma_h` < `0.0066` → IC=-0.175 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=585)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.01` → IC=-0.236 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=77)

- **FILTRO** `T_h` > `49.268` → IC=-0.254 (n=226)

  - _Acción_: SKIP cuando `T_h` > 49.268
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=76)

- **FILTRO** `T_h` < `92.8103` → IC=-0.179 (n=107)

  - _Acción_: SKIP cuando `T_h` < 92.8103
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=218)

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
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=135)

- **FILTRO** `T_h` > `135.7558` → IC=-0.336 (n=65)

  - _Acción_: SKIP cuando `T_h` > 135.7558
  - _Potencial_: sin este filtro IC_bueno=-0.299 (n=202)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.142 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=198)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9843` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `pct_vs_K` |x|≤ 1.9843 (IC base=-0.092)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0147` → IC=-0.234 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0147
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=187)

- **FILTRO** `T_h` > `61.9454` → IC=-0.234 (n=186)

  - _Acción_: SKIP cuando `T_h` > 61.9454
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=63)

- **FILTRO** `sigma_h` > `0.014` → IC=-0.306 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.014
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=129)

- **FILTRO** `T_h` > `49.2646` → IC=-0.141 (n=129)

  - _Acción_: SKIP cuando `T_h` > 49.2646
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=65)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.106` → IC=+0.452 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.106 (IC base=+0.330)

- **PATRÓN** `sigma_h` < `0.0151` → IC=+0.349 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0151 (IC base=+0.330)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.344 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.330)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.330)

- **PATRÓN** `dist_50` > `0.4594` → IC=+0.485 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4594 (IC base=+0.330)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.347 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.330)

- **PATRÓN** `edge` > `0.099` → IC=+0.423 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.099 (IC base=+0.392)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.413 (n=205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.392)

- **PATRÓN** `T_h` < `0.7285` → IC=+0.420 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7285 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.368` → IC=+0.439 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.368 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.392)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.0972` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0972 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.284 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.208)

- **PATRÓN** `T_h` < `0.7026` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7026 (IC base=+0.208)

- **PATRÓN** `T_h` > `1.4764` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4764 (IC base=+0.208)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1295` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1295 (IC base=+0.280)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.340 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.280)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.280)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.280)

- **PATRÓN** `edge` > `0.0997` → IC=+0.468 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.439 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.417)

- **PATRÓN** `T_h` < `1.178` → IC=+0.444 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.178 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.4134` → IC=+0.484 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4134 (IC base=+0.417)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.407 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1324` → IC=+0.488 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1324 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.472 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.418)

- **PATRÓN** `T_h` > `1.268` → IC=+0.466 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.268 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.4467` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4467 (IC base=+0.418)

- **PATRÓN** `edge` > `0.177` → IC=+0.473 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.177 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.476 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.492 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=505)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=546)

- **PATRÓN** `streak_estiramiento` < `0.3805` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.3805 (IC base=+0.021)

- **PATRÓN** `streak_estiramiento` < `0.8333` → IC=+0.125 (n=379)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.8333 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.137 (n=188)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 18.0 (IC base=+0.062)

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
- **PATRÓN** `streak_estiramiento` < `0.2738` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.2738 (IC base=+0.038)

- **PATRÓN** `streak_estiramiento` < `0.3856` → IC=+0.207 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3856 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.140 (n=209)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 34.0 (IC base=+0.082)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=106)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=60)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=71)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=860)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=40)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.515 (IC base=+0.025)

- **PATRÓN** `streak_estiramiento` < `0.5336` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.5336 (IC base=+0.000)

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

- **PATRÓN** `streak_estiramiento` < `0.6279` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6279 (IC base=+0.030)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1126)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1366)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1337)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5776)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3434)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.184 (n=2261)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0059 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2336` → IC=+0.159 (n=6781)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2336 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1241` → IC=+0.133 (n=6781)

  - _Acción_: Kelly boost +0.67€ cuando `drift_15min` |x|≤ 1.1241 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.133 (n=6781)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0991` → IC=+0.144 (n=2140)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0991 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.5517` → IC=+0.207 (n=6058)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5517 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.956` → IC=+0.226 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.956 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3543)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4334.8506` → IC=+0.173 (n=2261)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4334.8506 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2661)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.225 (n=812)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0773` → IC=+0.247 (n=406)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0773 (IC base=+0.208)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2654` → IC=+0.229 (n=308)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2654 (IC base=+0.208)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2221` → IC=+0.222 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2221 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_15` > `0.702` → IC=+0.275 (n=923)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.702 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.4005` → IC=+0.237 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4005 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.559` → IC=+0.210 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.559 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.939` → IC=+0.297 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.939 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `11835.8417` → IC=+0.221 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11835.8417 (IC base=+0.208)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.147 (n=1041)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0068 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0663` → IC=+0.152 (n=521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0663 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.083` → IC=+0.136 (n=1057)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.083 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.142 (n=839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.477` → IC=+0.216 (n=1183)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.477 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.143 (n=732)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.132 (n=1344)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.945` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.945 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6126.0702` → IC=+0.175 (n=537)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 6126.0702 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8333` → IC=+0.147 (n=706)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` > 0.8333 (IC base=+0.047)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.143 (n=1700)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0118 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2398` → IC=+0.176 (n=1700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2398 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0586` → IC=+0.139 (n=1700)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0586 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.184 (n=533)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=1551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.142 (n=1499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6944` → IC=+0.232 (n=1133)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6944 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2138` → IC=+0.143 (n=782)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2138 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.9137` → IC=+0.142 (n=1964)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.9137 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.874` → IC=+0.184 (n=394)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 16.874 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2939.0564` → IC=+0.179 (n=771)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2939.0564 (IC base=+0.137)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.381 (n=385)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.15` → IC=+0.362 (n=747)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.15 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.375 (n=566)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1007` → IC=+0.382 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1007 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.373 (n=895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.7872` → IC=+0.391 (n=849)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7872 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2713` → IC=+0.387 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2713 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.716` → IC=+0.387 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.716 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `9875.3038` → IC=+0.373 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9875.3038 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.361 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.1527` → IC=+0.364 (n=359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1527 (IC base=+0.361)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.368 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2167` → IC=+0.372 (n=185)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2167 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.397 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.361)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.361 (n=414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.8042` → IC=+0.378 (n=408)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8042 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.397 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.422` → IC=+0.377 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.422 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `15112.1783` → IC=+0.388 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15112.1783 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `401.0` → IC=+0.384 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 401.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.367 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.371 (n=200)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.366 (n=296)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1257` → IC=+0.378 (n=294)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1257 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0998` → IC=+0.385 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0998 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.369 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.370 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7604` → IC=+0.396 (n=441)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7604 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.382 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.6628` → IC=+0.363 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6628 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.854` → IC=+0.393 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.854 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.532` → IC=+0.365 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.532 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.362 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `4411.1912` → IC=+0.371 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4411.1912 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.203 (n=3136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=3138)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2786)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3488)

- **FILTRO** `libro_liquidez` < `4436.7034` → IC=-0.172 (n=4140)

  - _Acción_: SKIP cuando `libro_liquidez` < 4436.7034
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2134)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.277 (n=1385)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.208 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1169 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` < `0.6018` → IC=+0.201 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6018 (IC base=-0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2278` → IC=+0.269 (n=2073)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2278 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.3781` → IC=+0.282 (n=6216)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3781 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.7129` → IC=+0.262 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7129 (IC base=+0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.046` → IC=-0.226 (n=2818)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=1388)

- **FILTRO** `sigma_h` < `0.0041` → IC=-0.207 (n=1051)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=3155)

- **FILTRO** `sigma_ewma_delta_pct` > `22.129` → IC=-0.232 (n=592)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.129
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=3614)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1422` → IC=+0.290 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1422 (IC base=+0.067)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.312 (n=503)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1068` → IC=+0.285 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1068 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.5528` → IC=+0.285 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5528 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.613` → IC=+0.140 (n=251)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 21.613 (IC base=+0.067)

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
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=912)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.160 (n=697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0067 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.151 (n=465)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0053 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.162 (n=614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.184 (n=552)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5639` → IC=+0.240 (n=697)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5639 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6666` → IC=+0.169 (n=137)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6666 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.149 (n=534)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.357` → IC=+0.244 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.357 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=912)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5223.3427` → IC=+0.172 (n=465)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5223.3427 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.254 (n=1649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.4861` → IC=+0.243 (n=2471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4861 (IC base=+0.235)

- **PATRÓN** `drift_15min` |x|≤ `0.8375` → IC=+0.249 (n=2175)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8375 (IC base=+0.235)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1962` → IC=+0.257 (n=1121)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1962 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.242 (n=1091)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.235)

- **PATRÓN** `ibs_15` < `0.1944` → IC=+0.294 (n=1648)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1944 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.242` → IC=+0.249 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.242 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.511` → IC=+0.241 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.511 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.254` → IC=+0.239 (n=2596)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.254 (IC base=+0.235)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2006` → IC=-0.302 (n=376)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2006
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1130)

- **FILTRO** `drift_60min` |x|> `0.173` → IC=-0.281 (n=510)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.173
  - _Potencial_: sin este filtro IC_bueno=-0.166 (n=996)

- **FILTRO** `drift_15min` |x|> `1.0228` → IC=-0.302 (n=376)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0228
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1130)

- **FILTRO** `sigma_ewma_delta_pct` > `6.094` → IC=-0.211 (n=327)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.094
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=1179)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.206)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.206)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.206)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2132` → IC=+0.246 (n=341)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2132 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.295 (n=1025)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2882` → IC=+0.257 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2882 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1214` → IC=-0.273 (n=870)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1214
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=873)

- **FILTRO** `drift_15min` |x|> `1.2903` → IC=-0.283 (n=435)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2903
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1308)

- **FILTRO** `sigma_ewma_delta_pct` > `7.243` → IC=-0.227 (n=521)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.243
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=1222)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1720)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.282 (n=1274)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=-0.008)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0937` → IC=+0.286 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0937 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=1433)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.323 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=-0.008)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.172 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.160 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.7471` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.7471 (IC base=+0.100)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2338` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2338 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.312 (n=30)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.341` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.341 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 52.0 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.136 (n=97)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.049)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.172 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.160 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.7471` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.7471 (IC base=+0.100)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2338` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2338 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.312 (n=30)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.341` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.341 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 52.0 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.136 (n=97)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.049)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.299 (n=515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.291 (n=515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0715` → IC=+0.306 (n=683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0715 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.067` → IC=+0.288 (n=1544)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.067 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2158` → IC=+0.290 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2158 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=1607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.309 (n=1545)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2757` → IC=+0.318 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2757 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.54` → IC=+0.382 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.54 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `13023.4511` → IC=+0.301 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13023.4511 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.309 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.284 (n=271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.298 (n=359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `0.3894` → IC=+0.280 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3894 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.280 (n=812)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2257` → IC=+0.293 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2257 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.303 (n=750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.8545` → IC=+0.305 (n=726)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8545 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2612` → IC=+0.313 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2612 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.371` → IC=+0.385 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.371 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `14356.961` → IC=+0.311 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14356.961 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.303 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.298 (n=488)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.323 (n=246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0634` → IC=+0.294 (n=732)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0634 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.309 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.298 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8447` → IC=+0.316 (n=732)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8447 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.316 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2918 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.767` → IC=+0.372 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.767 (IC base=+0.290)

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
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=392)

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

- **FILTRO** `drift_15min` |x|> `0.3104` → IC=-0.260 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3104
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `drift_60min` |x|> `0.0858` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0858
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1667` → IC=-0.167 (n=22)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1667
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

- **FILTRO** `drift_15min` |x|> `0.2372` → IC=-0.352 (n=25)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2372
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1635` → IC=-0.283 (n=21)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1635
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=43)

- **FILTRO** `sigma_h` > `0.0115` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0115
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=49)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1457` → IC=-0.308 (n=24)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1457
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=47)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0549` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9866` → IC=+0.252 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9866 (IC base=+0.122)

- **PATRÓN** `T_h` > `117.4221` → IC=+0.351 (n=3441)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 117.4221 (IC base=+0.330)

- **PATRÓN** `ratio` > `1.0158` → IC=+0.389 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0158 (IC base=+0.330)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9756` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `ratio` < 0.9756 (IC base=+0.064)

- **PATRÓN** `T_h` > `111.7856` → IC=+0.320 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.7856 (IC base=+0.301)

- **PATRÓN** `ratio` > `1.0003` → IC=+0.302 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0003 (IC base=+0.301)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9775` → IC=+0.361 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.185)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.346 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.313)

- **PATRÓN** `ratio` > `1.0221` → IC=+0.408 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0221 (IC base=+0.313)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.409 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5517 sube el IC de +0.132 a +0.207 en UPDOWN_GBM#15min (n=6058). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.702 sube el IC de +0.208 a +0.275 en UPDOWN_GBM#BTC#15min (n=923). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.477 sube el IC de +0.131 a +0.216 en UPDOWN_GBM#ETH#15min (n=1183). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.6944 sube el IC de +0.137 a +0.232 en UPDOWN_GBM#XRP#15min (n=1133). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.086 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=1385). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3781 sube el IC de +0.001 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=6216). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.067 a +0.312 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=503). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.180 a +0.295 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=86). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5639 sube el IC de +0.149 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=697). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1944 sube el IC de +0.235 a +0.294 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1648). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.206 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.026 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=1025). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.008 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1433). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.100 a +0.312 en UPDOWN_GBM_ETH_15M_HORA7 (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.100 a +0.312 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.285 a +0.309 en UPDOWN_GBM_IBS_ALTO (n=1545). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8545 sube el IC de +0.280 a +0.305 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=726). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8447 sube el IC de +0.290 a +0.316 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=732). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7872 sube el IC de +0.362 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=849). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8042 sube el IC de +0.361 a +0.378 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=408). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7604 sube el IC de +0.363 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=441). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2393 | +0.084 | +266.17€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2393 | +0.084 | +266.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1981 | +0.085 | +226.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1981 | +0.085 | +226.68€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1529 | -0.028 | +50.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1529 | -0.028 | +50.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1205 | -0.040 | +37.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1205 | -0.040 | +37.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 52098 | -0.086 | -6675.57€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3463 | +0.089 | -330.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48635 | -0.098 | -6345.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3463 | +0.089 | -330.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3463 | +0.089 | -330.19€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14846 | -0.042 | -1400.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14846 | -0.042 | -1400.66€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 59301 | -0.012 | +2490.26€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 15281 | +0.003 | +1457.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 44020 | -0.017 | +1032.28€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 59301 | -0.012 | +2490.26€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 15281 | +0.003 | +1457.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 44020 | -0.017 | +1032.28€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 219628 | +0.112 | -9094.89€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#15min | 23940 | +0.178 | -778.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 1029 | +0.024 | -80.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 182210 | +0.104 | -7812.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12449 | +0.095 | -423.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 30209 | +0.101 | -2195.94€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#15min | 92 | -0.202 | +7.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 30080 | +0.102 | -2212.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 41024 | +0.121 | -723.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5769 | +0.175 | -245.99€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 30160 | +0.118 | -276.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 5053 | +0.080 | -178.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 30262 | +0.098 | -2103.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 117 | -0.105 | +19.63€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 30117 | +0.099 | -2116.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 13 | -0.065 | +4.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 47065 | +0.123 | -1032.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11715 | +0.176 | -344.00€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 30655 | +0.105 | -593.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4683 | +0.103 | -86.32€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 40850 | +0.111 | -1699.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6146 | +0.199 | -233.16€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 932 | +0.047 | -26.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 31097 | +0.095 | -1253.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2675 | +0.108 | -186.60€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 30218 | +0.106 | -1340.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 101 | -0.131 | +17.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 30101 | +0.107 | -1360.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 35898 | +0.188 | -2758.11€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 35898 | +0.188 | -2758.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 8129 | +0.159 | -997.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 8129 | +0.159 | -997.70€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5453 | +0.193 | -244.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5453 | +0.193 | -244.08€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7921 | +0.171 | -740.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7921 | +0.171 | -740.67€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6564 | +0.251 | -240.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6564 | +0.251 | -240.18€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7752 | +0.183 | -549.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7752 | +0.183 | -549.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1374 | +0.424 | -56.37€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1374 | +0.424 | -56.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 586 | +0.437 | -7.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 586 | +0.437 | -7.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 246 | +0.399 | -20.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 246 | +0.399 | -20.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 126740 | +0.199 | -9273.62€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 126740 | +0.199 | -9273.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 21977 | +0.175 | -2616.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 21977 | +0.175 | -2616.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 20423 | +0.223 | -685.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 20423 | +0.223 | -685.75€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21740 | +0.180 | -2279.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21740 | +0.180 | -2279.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 20600 | +0.217 | -807.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 20600 | +0.217 | -807.20€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20897 | +0.205 | -1217.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20897 | +0.205 | -1217.87€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 21103 | +0.196 | -1666.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 21103 | +0.196 | -1666.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 49288 | +0.116 | +394.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 49288 | +0.116 | +394.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 24544 | +0.117 | +260.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 24544 | +0.117 | +260.08€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 24744 | +0.115 | +134.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 24744 | +0.115 | +134.22€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2084 | +0.064 | -107.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1359 | +0.073 | -43.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1650 | +0.070 | -62.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1359 | +0.073 | -43.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 101076 | +0.100 | -2142.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 8206 | +0.096 | +178.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 92870 | +0.101 | -2321.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 55138 | +0.105 | -485.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 8206 | +0.096 | +178.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 46932 | +0.106 | -664.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 21793 | +0.109 | -91.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 21793 | +0.109 | -91.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 24145 | +0.083 | -1566.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 24145 | +0.083 | -1566.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 947 | +0.172 | -108.93€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 947 | +0.172 | -108.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 947 | +0.172 | -108.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 947 | +0.172 | -108.93€ | 2 | 4 |
| ✅ GBM_LATE_15M | 68876 | +0.102 | +38802.20€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 68876 | +0.102 | +38802.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11455 | +0.223 | +9763.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11455 | +0.223 | +9763.42€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 10803 | +0.176 | +8726.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10803 | +0.176 | +8726.98€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 12312 | +0.207 | +9720.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 12312 | +0.207 | +9720.53€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 9117 | +0.064 | +3144.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 9117 | +0.064 | +3144.94€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 9537 | -0.025 | +2477.28€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9537 | -0.025 | +2477.28€ | 3 | 14 |
| ✅ GBM_LATE_15M#XRP | 15652 | -0.019 | +4969.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15652 | -0.019 | +4969.04€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 73185 | +0.088 | +42978.00€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 73185 | +0.088 | +42978.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 14215 | -0.002 | +7498.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 14215 | -0.002 | +7498.62€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15722 | +0.008 | +4372.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15722 | +0.008 | +4372.92€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9759 | +0.296 | +11213.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9759 | +0.296 | +11213.90€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 14028 | +0.021 | +4532.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 14028 | +0.021 | +4532.75€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 11117 | +0.052 | +5228.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 11117 | +0.052 | +5228.47€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8344 | +0.313 | +10131.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8344 | +0.313 | +10131.34€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 54193 | +0.179 | +45014.21€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 54193 | +0.179 | +45014.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 8226 | +0.238 | +7603.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 8226 | +0.238 | +7603.64€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8673 | +0.140 | +6537.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8673 | +0.140 | +6537.41€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8709 | +0.224 | +7535.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8709 | +0.224 | +7535.89€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 9260 | +0.130 | +7261.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 9260 | +0.130 | +7261.83€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 10211 | +0.123 | +7895.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 10211 | +0.123 | +7895.47€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 9114 | +0.231 | +8179.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 9114 | +0.231 | +8179.98€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14834 | +0.125 | +7547.99€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14834 | +0.125 | +7547.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3930 | +0.125 | +2095.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3930 | +0.125 | +2095.05€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 510 | +0.154 | +284.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 510 | +0.154 | +284.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4339 | +0.125 | +2197.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4339 | +0.125 | +2197.49€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 4018 | +0.100 | +1658.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 4018 | +0.100 | +1658.46€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1357 | +0.168 | +868.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1357 | +0.168 | +868.50€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 69254 | +0.189 | +57679.50€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 69254 | +0.189 | +57679.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10957 | +0.248 | +10475.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10957 | +0.248 | +10475.35€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 11132 | +0.143 | +8140.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 11132 | +0.143 | +8140.33€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11719 | +0.234 | +10542.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11719 | +0.234 | +10542.71€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11474 | +0.145 | +8664.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11474 | +0.145 | +8664.75€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 12219 | +0.129 | +8961.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 12219 | +0.129 | +8961.07€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11753 | +0.240 | +10895.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11753 | +0.240 | +10895.29€ | 0 | 22 |
| ✅ GBM_LATE_5M | 17287 | +0.220 | +14643.12€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 17287 | +0.220 | +14643.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3355 | +0.209 | +2852.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3355 | +0.209 | +2852.55€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1592 | +0.218 | +1323.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1592 | +0.218 | +1323.49€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 5033 | +0.211 | +3968.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 5033 | +0.211 | +3968.52€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3124 | +0.233 | +2808.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3124 | +0.233 | +2808.55€ | 0 | 29 |
| ✅ GBM_LATE_5M#XRP | 2235 | +0.213 | +1791.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2235 | +0.213 | +1791.28€ | 0 | 0 |
| ✅ GBM_LATE_60M | 7172 | +0.090 | +2684.46€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 7172 | +0.090 | +2684.46€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 280 | +0.280 | +313.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 280 | +0.280 | +313.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2150 | +0.062 | +647.68€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2150 | +0.062 | +647.68€ | 1 | 5 |
| ✅ GBM_LATE_60M#DOGE | 272 | +0.307 | +322.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 272 | +0.307 | +322.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 2003 | +0.061 | +637.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 2003 | +0.061 | +637.00€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 2190 | +0.064 | +436.15€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2190 | +0.064 | +436.15€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 277 | +0.314 | +327.69€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 277 | +0.314 | +327.69€ | 0 | 24 |
| 🚫 GBM_LATE_60M_FADE | 828 | -0.246 | -36.30€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 828 | -0.246 | -36.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 293 | -0.256 | -19.27€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 293 | -0.256 | -19.27€ | 5 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 281 | -0.246 | -9.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 281 | -0.246 | -9.46€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 229 | -0.245 | -11.34€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 229 | -0.245 | -11.34€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2711 | +0.093 | +743.18€ | 0 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2711 | +0.093 | +743.18€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 959 | +0.071 | +257.69€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 959 | +0.071 | +257.69€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 59 | +0.205 | +35.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 59 | +0.205 | +35.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 834 | +0.054 | +160.87€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 834 | +0.054 | +160.87€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 706 | +0.155 | +246.24€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 706 | +0.155 | +246.24€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 153 | +0.113 | +42.74€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 153 | +0.113 | +42.74€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 451 | +0.301 | +532.61€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 451 | +0.301 | +532.61€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 451 | +0.301 | +532.61€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 451 | +0.301 | +532.61€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 5205 | +0.095 | +1125.46€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 5205 | +0.095 | +1125.46€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 5205 | +0.095 | +1125.46€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 5205 | +0.095 | +1125.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 2106 | +0.013 | +86.86€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 2106 | +0.013 | +86.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 272 | +0.077 | +41.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 272 | +0.077 | +41.89€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M#BTC | 381 | -0.017 | +6.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 381 | -0.017 | +6.06€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 190 | +0.026 | +16.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 190 | +0.026 | +16.19€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 453 | +0.023 | +22.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 453 | +0.023 | +22.25€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 363 | -0.026 | -1.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 363 | -0.026 | -1.44€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 447 | +0.015 | +1.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 447 | +0.015 | +1.90€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4738 | +0.020 | +216.21€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4738 | +0.020 | +216.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 884 | +0.019 | +57.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 884 | +0.019 | +57.59€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 374 | +0.064 | +90.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 374 | +0.064 | +90.56€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1788 | +0.025 | +42.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1788 | +0.025 | +42.71€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 828 | +0.012 | +3.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 828 | +0.012 | +3.93€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 623 | -0.004 | +27.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 623 | -0.004 | +27.57€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2972 | -0.037 | -16.72€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2972 | -0.037 | -16.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 895 | -0.040 | -19.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 895 | -0.040 | -19.93€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1083 | -0.023 | +12.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1083 | -0.023 | +12.09€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 963 | -0.052 | -8.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 963 | -0.052 | -8.73€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 25 | +0.018 | -0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 25 | +0.018 | -0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 22850 | -0.032 | -219.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 11122 | -0.031 | -62.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11728 | -0.034 | -157.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 789 | -0.054 | -41.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 405 | -0.038 | -4.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 384 | -0.070 | -36.52€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 6207 | -0.026 | -23.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2963 | -0.022 | +13.80€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3244 | -0.029 | -37.63€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 2061 | -0.034 | -16.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1063 | -0.037 | -18.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 998 | -0.031 | +2.62€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 5267 | -0.029 | -19.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2553 | -0.026 | +9.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2714 | -0.032 | -29.06€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4335 | -0.027 | +23.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2128 | -0.028 | +8.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2207 | -0.026 | +14.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 4191 | -0.046 | -142.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 2010 | -0.048 | -70.53€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2181 | -0.045 | -71.81€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 78657 | -0.001 | +4149.61€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 78657 | -0.001 | +4149.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 11304 | -0.038 | -155.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 11304 | -0.038 | -155.06€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 11219 | -0.054 | -316.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 11219 | -0.054 | -316.90€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7618 | -0.053 | -112.96€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7618 | -0.053 | -112.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2210 | -0.058 | -19.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2210 | -0.058 | -19.83€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 106 | -0.028 | -1.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 106 | -0.028 | -1.20€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 828 | -0.118 | -35.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 828 | -0.118 | -35.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2327 | -0.065 | -12.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2327 | -0.065 | -12.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 876 | -0.021 | -29.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 876 | -0.021 | -29.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 4059 | +0.002 | -9.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 4059 | +0.002 | -9.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 871 | -0.003 | -12.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 871 | -0.003 | -12.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1327 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1327 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 192330 | -0.078 | +2147.58€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 192330 | -0.078 | +2147.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 29408 | -0.101 | -1376.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 29408 | -0.101 | -1376.07€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 28961 | -0.101 | -1035.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 28961 | -0.101 | -1035.48€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9456 | -0.035 | -178.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9456 | -0.035 | -178.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1014 | -0.017 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1014 | -0.017 | -18.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2234 | -0.046 | -28.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2234 | -0.046 | -28.97€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1012 | -0.021 | -30.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1012 | -0.021 | -30.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2690 | -0.023 | -30.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2690 | -0.023 | -30.13€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1322 | -0.062 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1322 | -0.062 | -29.21€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1184 | -0.038 | -41.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1184 | -0.038 | -41.56€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2464 | +0.119 | +980.21€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2328 | +0.122 | +967.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 535 | +0.139 | +271.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 535 | +0.139 | +271.62€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 486 | +0.119 | +175.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 486 | +0.119 | +175.33€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 421 | +0.129 | +195.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 421 | +0.129 | +195.89€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 398 | +0.133 | +191.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 398 | +0.133 | +191.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 488 | +0.092 | +132.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 488 | +0.092 | +132.91€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2634 | -0.022 | -54.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2634 | -0.022 | -54.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 454 | +0.002 | +16.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 454 | +0.002 | +16.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 471 | -0.054 | -37.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 471 | -0.054 | -37.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 637 | -0.043 | -44.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 637 | -0.043 | -44.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 551 | -0.010 | -8.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 551 | -0.010 | -8.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 521 | -0.001 | +19.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 521 | -0.001 | +19.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1403 | -0.042 | +141.67€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 648 | -0.068 | +28.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 508 | -0.065 | +53.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 140 | -0.077 | -25.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 494 | -0.006 | +76.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 360 | +0.011 | +86.66€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 134 | -0.051 | -9.98€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 261 | -0.048 | +36.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 223 | -0.047 | +32.49€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 38 | -0.050 | +4.42€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1091 | -0.036 | +172.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 312 | -0.064 | -30.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1784 | -0.186 | -36.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 707 | -0.174 | -8.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 627 | -0.172 | -4.72€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 80 | -0.183 | -3.68€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 600 | -0.198 | -32.58€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 530 | -0.203 | -37.18€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 70 | -0.153 | +4.60€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 477 | -0.187 | +4.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 443 | -0.183 | +1.34€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 34 | -0.222 | +3.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1600 | -0.186 | -40.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 184 | -0.183 | +4.06€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 626 | +0.374 | +557.54€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 147 | +0.185 | +120.72€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 147 | +0.185 | +120.72€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 143 | +0.376 | +109.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 143 | +0.376 | +109.53€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#SOL | 336 | +0.453 | +327.29€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 336 | +0.453 | +327.29€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#sniper | 626 | +0.374 | +557.54€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1089 | +0.043 | +96.05€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1089 | +0.043 | +96.05€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 361 | +0.018 | +4.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 361 | +0.018 | +4.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 83 | +0.029 | +3.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 83 | +0.029 | +3.15€ | 1 | 3 |
| ✅ STREAK_FADE_15M#SOL | 87 | +0.039 | +10.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 87 | +0.039 | +10.03€ | 2 | 3 |
| ✅ STREAK_FADE_15M#XRP | 558 | +0.061 | +78.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 558 | +0.061 | +78.13€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3699 | -0.021 | -138.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3699 | -0.021 | -138.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 636 | -0.025 | -25.19€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 636 | -0.025 | -25.19€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 191 | -0.039 | -14.67€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 191 | -0.039 | -14.67€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1742 | -0.018 | -58.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1742 | -0.018 | -58.81€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 175 | +0.009 | -2.88€ | 1 | 2 |
| ✅ STREAK_FADE_60M#60min | 175 | +0.009 | -2.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB | 13 | +0.108 | +6.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB#60min | 13 | +0.108 | +6.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#DOGE | 9 | -0.021 | -2.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#DOGE#60min | 9 | -0.021 | -2.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 52 | -0.018 | -1.12€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 52 | -0.018 | -1.12€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 92 | +0.000 | -5.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 92 | +0.000 | -5.57€ | 1 | 1 |
| ✅ STREAK_FADE_60M#XRP | 9 | +0.021 | -0.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#XRP#60min | 9 | +0.021 | -0.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 11798 | +0.013 | +64.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11798 | +0.013 | +64.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3035 | +0.017 | +21.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3035 | +0.017 | +21.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3162 | +0.013 | +25.54€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3162 | +0.013 | +25.54€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2978 | +0.008 | -1.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2978 | +0.008 | -1.90€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2623 | +0.014 | +19.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2623 | +0.014 | +19.34€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 14439 | +0.019 | +5.14€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 14439 | +0.019 | +5.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5795 | +0.021 | +6.52€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5795 | +0.021 | +6.52€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5176 | +0.019 | +3.36€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5176 | +0.019 | +3.36€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3468 | +0.014 | -4.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3468 | +0.014 | -4.74€ | 1 | 0 |
| ✅ UPDOWN_GBM | 130515 | +0.060 | +12495.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 32543 | +0.078 | +6363.41€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3706 | -0.000 | +41.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 85949 | +0.062 | +5955.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7868 | -0.001 | +139.80€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11457 | +0.104 | +2138.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2186 | +0.164 | +1021.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 9181 | +0.091 | +1119.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 29714 | +0.056 | +2598.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4441 | +0.081 | +996.20€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1098 | +0.000 | +22.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 20464 | +0.065 | +1490.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3550 | -0.004 | +85.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 161 | -0.064 | +4.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14537 | +0.074 | +1598.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 12367 | +0.061 | +705.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 30757 | +0.049 | +2191.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7612 | +0.070 | +1174.03€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1060 | +0.006 | +15.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 19033 | +0.052 | +957.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2902 | -0.001 | +43.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 150 | -0.099 | +1.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26768 | +0.041 | +1567.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8749 | +0.034 | +507.38€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 975 | -0.011 | +7.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15541 | +0.054 | +1050.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1367 | +0.005 | +10.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 136 | -0.138 | -8.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 17280 | +0.074 | +2402.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7471 | +0.089 | +1770.86€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9363 | +0.065 | +631.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 49 | +0.010 | +1.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 447 | -0.099 | -2.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1131 | +0.362 | +431.69€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1131 | +0.362 | +431.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 543 | +0.361 | +192.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 543 | +0.361 | +192.93€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 588 | +0.363 | +238.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 588 | +0.363 | +238.76€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 30913 | -0.017 | +7762.70€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 30913 | -0.017 | +7762.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2481 | -0.046 | +649.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2481 | -0.046 | +649.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5732 | -0.114 | +348.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5732 | -0.114 | +348.57€ | 3 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4223 | +0.216 | +2651.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4223 | +0.216 | +2651.99€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8652 | -0.058 | +1308.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8652 | -0.058 | +1308.57€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8531 | -0.052 | +1740.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8531 | -0.052 | +1740.63€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 392 | +0.061 | +40.65€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 392 | +0.061 | +40.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 392 | +0.061 | +40.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 392 | +0.061 | +40.65€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 2059 | +0.285 | +1765.69€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 2059 | +0.285 | +1765.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1083 | +0.280 | +874.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1083 | +0.280 | +874.37€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 976 | +0.290 | +891.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 976 | +0.290 | +891.32€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 920 | -0.123 | -97.94€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 920 | -0.123 | -97.94€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 312 | -0.080 | -36.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 312 | -0.080 | -36.02€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 296 | -0.087 | -24.08€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 296 | -0.087 | -24.08€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 135 | -0.201 | -9.16€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 135 | -0.201 | -9.16€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5611 | +0.291 | +2421.24€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2199 | +0.246 | +347.31€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2172 | +0.283 | +884.97€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1240 | +0.382 | +1188.96€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.027 n=1592 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1592 IC=+0.027 PNL=+80.99€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 859 celda(s) pasan gate riguroso completo de 3105 evaluadas (n>=40) y 4230 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=8746 IC=+0.034 PNL=+506.86€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=2172/15 IC=+0.283 PNL=+884.97€ | BTC: n=2199/15 IC=+0.246 PNL=+347.31€ | SOL: n=1240/15 IC=+0.382 PNL=+1188.96€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=1217/60 | contraria IC=+0.187 n=1282 | gap=-0.045 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=669, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2900/40 IC=-0.001 PNL=+42.74€ | BTC#60min: n=3548/40 IC=-0.004 PNL=+85.17€ | SOL#60min: n=1366/40 IC=+0.005 PNL=+10.62€ | XRP#60min: n=49/40 IC=+0.010 PNL=+1.35€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=867350 | tras_1loss IC=+0.104 n=654808 | tras_2loss IC=+0.075 n=259439/40 | gap=-0.030 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.149 > 0.08 con n=1336 PNL=+747.97€
  - _Datos_: n=1336 IC=+0.149 PNL=+747.97€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.08 con n=1570 PNL=+712.07€
  - _Datos_: n=1570 IC=+0.127 PNL=+712.07€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.328 > 0.1 con n=4631 PNL=+2566.35€
  - _Datos_: n=4631 IC=+0.328 PNL=+2566.35€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1326 IC=+0.059 PNL=+124.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1326 IC=+0.059 PNL=+124.58€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=122 IC=+0.153 PNL=+67.70€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=122 IC=+0.153 PNL=+67.70€

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
  - _Estado_: 3/20 ops en el filtro definido (IC actual=-0.015 PNL=-2.12€)
  - _Datos_: n=3 IC=-0.015 PNL=-2.12€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=5150 IC=-0.008 PNL=-63.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5150 IC=-0.008 PNL=-63.32€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2713 IC=+0.012 PNL=+203.20€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2713 IC=+0.012 PNL=+203.20€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1592 IC=+0.027 PNL=+80.99€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1592 IC=+0.027 PNL=+80.99€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.1 con n=9041 PNL=+4270.67€
  - _Datos_: n=9041 IC=+0.132 PNL=+4270.67€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=4441 IC=+0.081 PNL=+996.20€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=4441 IC=+0.081 PNL=+996.20€

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
  - _Estado_: n=1787 IC=+0.044 PNL=+151.46€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1787 IC=+0.044 PNL=+151.46€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=224 IC=-0.022 PNL=-5.88€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=224 IC=-0.022 PNL=-5.88€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.301 n=451) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=451 IC=+0.301 PNL=+532.61€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.02 con n=1439 PNL=+568.68€
  - _Datos_: n=1439 IC=+0.115 PNL=+568.68€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=291 IC=-0.125 PNL=+1.65€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=291 IC=-0.125 PNL=+1.65€

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
  - _Estado_: n=53843 IC=+0.069 PNL=+7227.57€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=53843 IC=+0.069 PNL=+7227.57€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.118 < -0.1 con n=905 PNL=+159.56€
  - _Datos_: n=905 IC=-0.118 PNL=+159.56€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=5204 IC=+0.068 PNL=+619.58€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=5204 IC=+0.068 PNL=+619.58€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=228 IC=-0.087 PNL=+2.79€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=228 IC=-0.087 PNL=+2.79€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1441 IC=+0.098 PNL=+344.58€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1441 IC=+0.098 PNL=+344.58€

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
  - _Estado_: n=51700 IC=-0.137 PNL=+3405.00€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=51700 IC=-0.137 PNL=+3405.00€

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
  - _Estado_: n=5643 IC=+0.136 PNL=+3997.33€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5643 IC=+0.136 PNL=+3997.33€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=13563 IC=+0.057 PNL=+1175.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13563 IC=+0.057 PNL=+1175.81€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=5679 PNL=+3239.27€
  - _Datos_: n=5679 IC=+0.103 PNL=+3239.27€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.217 < -0.1 con n=5723 PNL=-412.08€
  - _Datos_: n=5723 IC=-0.217 PNL=-412.08€

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
  - _Estado_: n=139 IC=+0.067 PNL=+22.16€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=139 IC=+0.067 PNL=+22.16€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.095 n=2659) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2659 IC=+0.095 PNL=+515.84€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=21970 IC=+0.174 PNL=-2614.80€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=21970 IC=+0.174 PNL=-2614.80€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.232 > 0.1 con n=364 PNL=+255.83€
  - _Datos_: n=364 IC=+0.232 PNL=+255.83€
