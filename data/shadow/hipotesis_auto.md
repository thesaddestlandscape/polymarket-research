# Hipótesis automáticas — 2026-11-28 10:34 UTC
_Generado por shadow_postmortem.py sobre 1526400 resoluciones (PNL=+217288.96€)_

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
- **FILTRO** `restante_s_al_confirmar` < `130.32` → IC=-0.217 (n=13037)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=39114)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#BTC#15min
- **PATRÓN** `restante_s_al_confirmar` < `641.37` → IC=+0.129 (n=2610)

  - _Acción_: Kelly boost +0.65€ cuando `restante_s_al_confirmar` < 641.37 (IC base=+0.087)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.66` → IC=-0.160 (n=3719)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.66
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=11164)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=31560)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7610.3719` → IC=+0.150 (n=2562)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7610.3719 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.126 (n=28239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=34269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=25495)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=9086)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=2248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=2754)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `16172.4857` → IC=+0.182 (n=716)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16172.4857 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.184 (n=1968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.179 (n=2206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2818)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `15969.7518` → IC=+0.184 (n=728)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 15969.7518 (IC base=+0.176)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.173 (n=656)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.615 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.123 (n=2282)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.45 (IC base=+0.087)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=5818)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.176 (n=2851)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=2798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.330 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=3248)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.191)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.143 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.142 (n=1010)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.243 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=1227)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.252 (n=1005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.230 (n=2056)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.229)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.428 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=771)
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

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.136 (n=1097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.255 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=28292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=17910)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.218 (n=9020)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.336 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `5024.6381` → IC=+0.335 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5024.6381 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=6445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.158)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.173 (n=6179)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.158)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=4030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=2695)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.246 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.203)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=6267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=5306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6412)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4946)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.251 (n=2410)
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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=6114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=3895)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1969)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.184)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=1064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=1059)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `13981.3978` → IC=+0.451 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13981.3978 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=456)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `15178.7462` → IC=+0.446 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15178.7462 (IC base=+0.437)

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

- **FILTRO** `libro_liquidez` < `6428.7632` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `libro_liquidez` < 6428.7632
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=36911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.237 (n=36193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.184 (n=5522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.175 (n=11879)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=17084)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=15403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.277 (n=6469)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=6333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.196 (n=13045)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=5163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5960)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.258 (n=6258)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=6088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.252 (n=6575)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=6158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=6166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7591)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=13232)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=14616)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.28` → IC=+0.141 (n=12381)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.28 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6426)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6644)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.73` → IC=+0.142 (n=8135)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.73 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=6806)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.135 (n=8803)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.95 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.86` → IC=+0.135 (n=8196)

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
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=145)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.259 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=92)

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
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=145)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.259 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=92)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5101` → IC=+0.140 (n=21240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5101 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=21503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=14799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9725` → IC=+0.247 (n=7085)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9725 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8853` → IC=+0.288 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8853 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.456` → IC=+0.190 (n=10658)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.456 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.267 (n=5820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.254 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7466` → IC=+0.234 (n=5142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7466 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=10151)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `5048.2462` → IC=+0.150 (n=7080)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5048.2462 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.123 (n=13455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0067 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5651` → IC=+0.144 (n=26895)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5651 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6833` → IC=+0.192 (n=1819)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6833 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1803` → IC=+0.194 (n=11082)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1803 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8549` → IC=+0.197 (n=7498)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8549 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.233 (n=2727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.2861` → IC=+0.213 (n=8650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2861 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.228 (n=19056)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.240 (n=1505)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3057` → IC=+0.213 (n=3970)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3057 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=2195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=3024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9814` → IC=+0.271 (n=2045)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9814 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.779` → IC=+0.286 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.779 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.260 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4395` → IC=+0.213 (n=4338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4395 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2066.5` → IC=+0.216 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2066.5 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.243 (n=1867)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0975` → IC=+0.268 (n=1371)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0975 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=4275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.241 (n=1889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0844` → IC=+0.273 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0844 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0727` → IC=+0.238 (n=3560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0727 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.249 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `1.8567` → IC=+0.241 (n=2626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8567 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=4352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.230 (n=1707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1167` → IC=+0.244 (n=1707)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1167 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=4070)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.221 (n=2772)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8864` → IC=+0.246 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8864 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.2062` → IC=+0.227 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2062 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.579` → IC=+0.220 (n=4288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.579 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.669` → IC=+0.260 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.669 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.227 (n=3465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6953 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.262 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.4415` → IC=+0.244 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4415 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.152 (n=4251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0071 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3631` → IC=+0.145 (n=4249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3631 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=1591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.3637` → IC=+0.200 (n=2833)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3637 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1571` → IC=+0.151 (n=4184)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1571 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.571` → IC=+0.141 (n=664)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.571 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.969` → IC=+0.142 (n=3915)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.969 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.626` → IC=+0.159 (n=1417)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.626 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.160 (n=1540)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4504` → IC=+0.142 (n=4117)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4504 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.183 (n=1375)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.212 (n=2170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=5030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=1850)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.865` → IC=+0.276 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.865 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.195 (n=4286)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.224 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.7343` → IC=+0.210 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7343 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5545)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2012.2756` → IC=+0.201 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2012.2756 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.228 (n=1976)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.3088` → IC=+0.230 (n=2988)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3088 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.227 (n=2045)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0547` → IC=+0.269 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0547 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.578` → IC=+0.268 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.578 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3453` → IC=+0.255 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3453 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.7599` → IC=+0.236 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7599 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1879.4952` → IC=+0.225 (n=2032)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1879.4952 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.220 (n=3834)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.176 (n=273)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=5769)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.139 (n=779)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0041 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.9396` → IC=+0.246 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9396 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1615` → IC=+0.348 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1615 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.3787` → IC=+0.344 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3787 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.222` → IC=+0.217 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.222 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `0.8651` → IC=+0.345 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8651 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.2462` → IC=+0.361 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2462 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` < `0.165` → IC=+0.347 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.165 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2994` → IC=+0.357 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2994 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.364 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `2.275` → IC=+0.346 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.275 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.352 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.0866` → IC=+0.187 (n=1511)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0866 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.3697` → IC=+0.158 (n=735)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3697 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1574` → IC=+0.156 (n=2862)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1574 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.8231` → IC=+0.162 (n=1989)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8231 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `0.6679` → IC=+0.154 (n=2664)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6679 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.201 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.1366` → IC=+0.172 (n=1304)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1366 (IC base=+0.060)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.175 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=935)

- **FILTRO** `ibs_20min` > `0.1919` → IC=-0.124 (n=5667)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1919
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2792)

- **FILTRO** `sigma_ewma_delta_pct` > `8.314` → IC=-0.226 (n=916)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.314
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=7543)

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

- **PATRÓN** `ibs_20min` < `0.1919` → IC=+0.159 (n=2792)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1919 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.8349` → IC=+0.299 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8349 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.3277` → IC=+0.293 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3277 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.310 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6932 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0787` → IC=+0.322 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0787 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4676` → IC=+0.306 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4676 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5251` → IC=+0.302 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5251 (IC base=-0.031)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.03` → IC=-0.179 (n=1408)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=5148)

- **FILTRO** `ibs_20min` > `0.72` → IC=-0.191 (n=2271)

  - _Acción_: SKIP cuando `ibs_20min` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=6863)

- **PATRÓN** `ibs_20min` > `0.794` → IC=+0.147 (n=2230)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.794 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `0.4566` → IC=+0.339 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4566 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.316 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.3085` → IC=+0.320 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3085 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.5382` → IC=+0.315 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5382 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.1135` → IC=+0.292 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1135 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.6352` → IC=+0.274 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6352 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.2104` → IC=+0.277 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2104 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1082` → IC=+0.275 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1082 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.5575` → IC=+0.266 (n=2321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5575 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.187 (n=9314)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0113 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.284 (n=12658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0121` → IC=+0.304 (n=1918)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0121 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.447` → IC=+0.168 (n=12581)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.447 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.280 (n=9342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6912 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.296 (n=2308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.659` → IC=+0.290 (n=5416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.659 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=15903)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.137 (n=18099)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0073 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5158` → IC=+0.174 (n=23893)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5158 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.286` → IC=+0.281 (n=9712)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.286 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.6906` → IC=+0.279 (n=4111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6906 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1862` → IC=+0.284 (n=3114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1862 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.322 (n=2048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.302 (n=4634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2778` → IC=+0.305 (n=6300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2778 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.312 (n=13921)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.822` → IC=-0.151 (n=4924)

  - _Acción_: SKIP cuando `ibs_20min` < 0.822
  - _Potencial_: sin este filtro IC_bueno=+0.318 (n=2538)

- **FILTRO** `ibs_20min` > `0.698` → IC=-0.243 (n=1698)

  - _Acción_: SKIP cuando `ibs_20min` > 0.698
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=5096)

- **FILTRO** `sigma_ewma_delta_pct` > `4.027` → IC=-0.240 (n=1424)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.027
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5370)

- **PATRÓN** `ibs_20min` > `0.822` → IC=+0.318 (n=2538)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.822 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.132` → IC=+0.176 (n=2777)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 2.132 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.335 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.295 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2336` → IC=+0.320 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2336 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.327 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1701` → IC=+0.170 (n=1699)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1701 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.0758` → IC=+0.386 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0758 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6493` → IC=+0.388 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6493 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1845` → IC=+0.228 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1845 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.5284` → IC=+0.215 (n=3028)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5284 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.215 (n=2725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1952 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.223 (n=2435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2739` → IC=+0.240 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2739 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.233 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4611` → IC=+0.222 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4611 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `366.0` → IC=+0.233 (n=2699)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 366.0 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.2093` → IC=+0.260 (n=2185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2093 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `0.8316` → IC=+0.262 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8316 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.281 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5333` → IC=+0.257 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5333 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1537` → IC=+0.264 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1537 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.273 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 196.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.319 (n=1722)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.286 (n=3370)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.541` → IC=+0.305 (n=2589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.541 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` < `0.1306` → IC=+0.295 (n=3537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1306 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `1.6002` → IC=+0.291 (n=3702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6002 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4391)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `2009.7484` → IC=+0.300 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.7484 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.302 (n=2458)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.332 (n=2361)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.189` → IC=+0.328 (n=1559)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.189 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=1356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.314 (n=1603)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.1589` → IC=+0.322 (n=2360)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1589 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.943` → IC=+0.322 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.943 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.1987` → IC=+0.309 (n=3522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1987 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3444` → IC=+0.316 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3444 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.7483` → IC=+0.327 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7483 (IC base=+0.308)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `1576.424` → IC=+0.315 (n=3162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1576.424 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.308 (n=2374)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1632` → IC=+0.237 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1632 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.3884` → IC=+0.231 (n=2612)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3884 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.1742` → IC=+0.234 (n=2588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1742 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.5938` → IC=+0.231 (n=2588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5938 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.235 (n=2723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.237 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4161` → IC=+0.236 (n=2517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4161 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.4974` → IC=+0.233 (n=2248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4974 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.249 (n=2564)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 116.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.0918` → IC=+0.150 (n=1765)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.0918 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.3964` → IC=+0.260 (n=2116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3964 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `1.1729` → IC=+0.261 (n=1900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1729 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` > `0.6103` → IC=+0.258 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6103 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.264 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.289 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `1.7847` → IC=+0.282 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7847 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `2.4261` → IC=+0.267 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4261 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.285 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7536` → IC=-0.247 (n=2868)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7536
  - _Potencial_: sin este filtro IC_bueno=+0.319 (n=2869)

- **FILTRO** `ibs_20min` > `0.6` → IC=-0.233 (n=1343)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=4071)

- **FILTRO** `sigma_ewma_delta_pct` > `8.213` → IC=-0.256 (n=621)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.213
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=4793)

- **PATRÓN** `ibs_20min` > `0.7536` → IC=+0.319 (n=2869)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7536 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `1.1139` → IC=+0.353 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1139 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.445` → IC=+0.160 (n=2352)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.445 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8418` → IC=+0.352 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8418 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.695` → IC=+0.338 (n=1895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.695 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.369 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7975` → IC=+0.357 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7975 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.357 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.168 (n=4071)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.3279` → IC=+0.274 (n=2230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3279 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.705` → IC=+0.136 (n=4242)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.705 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6852` → IC=+0.285 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6852 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.300 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.281 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8106 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.544` → IC=+0.270 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.544 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.283 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.350 (n=2705)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=3046)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=3179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.6511` → IC=+0.335 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6511 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2226` → IC=+0.337 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2226 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.714` → IC=+0.343 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.714 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.7017` → IC=+0.328 (n=2703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7017 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.345 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.5416` → IC=+0.327 (n=2615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5416 (IC base=+0.313)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.314 (n=3801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `2998.9019` → IC=+0.325 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2998.9019 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.330 (n=3254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=3266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.326 (n=3254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3902 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.3122` → IC=+0.322 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3122 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2612` → IC=+0.316 (n=3215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2612 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.605` → IC=+0.331 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.605 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.633` → IC=+0.319 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.633 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2089` → IC=+0.339 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2089 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.357 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.326 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1632` → IC=+0.316 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1632 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.219 (n=6800)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1286` → IC=+0.194 (n=8979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1286 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=21182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5342` → IC=+0.228 (n=20396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5342 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1721` → IC=+0.205 (n=7627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1721 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.663` → IC=+0.259 (n=3994)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.663 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1724` → IC=+0.152 (n=13604)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1724 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6184` → IC=+0.151 (n=13606)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6184 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.207 (n=2931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6092` → IC=+0.186 (n=6628)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6092 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=19358)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.192 (n=8978)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0063 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.185 (n=13582)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0083 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.223 (n=6792)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.205 (n=9742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5294` → IC=+0.236 (n=20365)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5294 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.2005` → IC=+0.178 (n=14927)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2005 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.359` → IC=+0.191 (n=3205)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.359 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.483` → IC=+0.190 (n=18215)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.483 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1911` → IC=+0.165 (n=14417)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1911 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.218 (n=3063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6426` → IC=+0.196 (n=6501)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6426 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.199 (n=19338)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 90.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.255 (n=1120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.0762` → IC=+0.265 (n=1118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0762 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=2274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9415` → IC=+0.289 (n=2234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9415 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.453` → IC=+0.326 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.453 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.285 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8312` → IC=+0.226 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8312 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.229 (n=3213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.253 (n=2841)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.307 (n=1250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=2929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.254 (n=2595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.0082` → IC=+0.307 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0082 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.944` → IC=+0.254 (n=2816)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.944 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.253 (n=2515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.267 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` < `1.554` → IC=+0.263 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.554 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.6782` → IC=+0.254 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6782 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=3032)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1941.7464` → IC=+0.249 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1941.7464 (IC base=+0.249)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.191 (n=1048)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0683` → IC=+0.174 (n=1044)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0683 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.242` → IC=+0.200 (n=3129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.242 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1987` → IC=+0.211 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1987 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.483` → IC=+0.200 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.483 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8507` → IC=+0.135 (n=2086)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8507 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.129 (n=1043)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.1915 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2761` → IC=+0.170 (n=477)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2761 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4105` → IC=+0.129 (n=1027)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4105 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4558` → IC=+0.138 (n=1027)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4558 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.130 (n=3053)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 381.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.180 (n=2992)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0062 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2618` → IC=+0.175 (n=2988)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2618 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.174 (n=1622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.6175` → IC=+0.209 (n=3394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6175 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.227` → IC=+0.174 (n=3700)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.227 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.857` → IC=+0.181 (n=628)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.857 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.028` → IC=+0.155 (n=2986)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.028 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.162 (n=3394)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2068 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.153 (n=2989)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4911` → IC=+0.156 (n=3266)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4911 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.195 (n=1412)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 201.0 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.232 (n=1563)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2614` → IC=+0.233 (n=2295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2614 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=3600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.285 (n=1824)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.962` → IC=+0.304 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.962 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.35` → IC=+0.234 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.35 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.1704` → IC=+0.218 (n=2246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1704 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2006.3984` → IC=+0.224 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.3984 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.243 (n=3109)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.2562` → IC=+0.266 (n=2070)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2562 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.272 (n=1169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0455` → IC=+0.290 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0455 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.666` → IC=+0.283 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.666 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.278 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7638` → IC=+0.240 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7638 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.250 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1877.1084` → IC=+0.247 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1877.1084 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.189 (n=1129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.004 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0824` → IC=+0.171 (n=1122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0824 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2404` → IC=+0.187 (n=3364)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2404 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1517` → IC=+0.189 (n=1879)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1517 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.182` → IC=+0.200 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.182 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8329` → IC=+0.138 (n=2243)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8329 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.174 (n=504)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5013` → IC=+0.137 (n=1099)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.5013 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6915.1659` → IC=+0.196 (n=1525)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6915.1659 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.127 (n=3306)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 124.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.172 (n=2404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4368` → IC=+0.150 (n=3603)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4368 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6697` → IC=+0.188 (n=3603)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6697 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1754` → IC=+0.157 (n=3708)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1754 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.179` → IC=+0.145 (n=854)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 9.179 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.150 (n=2403)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8509 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.172 (n=546)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.7923` → IC=+0.134 (n=2291)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7923 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.5159` → IC=+0.135 (n=3070)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.5159 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6662.7463` → IC=+0.191 (n=1634)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6662.7463 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.141 (n=3007)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 103.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.158 (n=2500)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.206 (n=3748)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4737 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7987` → IC=+0.212 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7987 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.862` → IC=+0.279 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.862 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1669` → IC=+0.132 (n=3748)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1669 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6228` → IC=+0.126 (n=3748)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6228 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1637` → IC=+0.124 (n=3828)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1637 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.134 (n=520)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7998` → IC=+0.127 (n=2428)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7998 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2708.8956` → IC=+0.199 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2708.8956 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.128 (n=2416)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 26.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.152 (n=3463)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0113 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1194` → IC=+0.171 (n=1312)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1194 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=4013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6484` → IC=+0.221 (n=3933)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6484 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2307` → IC=+0.146 (n=3910)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2307 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.228` → IC=+0.145 (n=3484)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.228 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1831` → IC=+0.130 (n=3933)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1831 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.155 (n=558)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4435` → IC=+0.140 (n=1249)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4435 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4793` → IC=+0.136 (n=1248)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4793 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2602.1348` → IC=+0.193 (n=1783)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2602.1348 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.132 (n=3759)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 42.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.245 (n=3365)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1718` → IC=+0.238 (n=1481)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1718 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=3494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3032)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.253 (n=3365)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1878` → IC=+0.232 (n=2062)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1878 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.8508` → IC=+0.226 (n=3486)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8508 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.377` → IC=+0.273 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.377 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6162` → IC=+0.232 (n=3364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6162 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.238` → IC=+0.266 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.238 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.5063` → IC=+0.231 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5063 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=4263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2631.2954` → IC=+0.228 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2631.2954 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.021` → IC=+0.249 (n=1582)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.021 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6207` → IC=+0.248 (n=3489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6207 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1563)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0392` → IC=+0.296 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0392 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `1.2015` → IC=+0.253 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2015 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.959` → IC=+0.275 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.959 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.244 (n=2327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `1.0478` → IC=+0.237 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0478 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.298 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8573` → IC=+0.237 (n=2210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8573 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.5616` → IC=+0.237 (n=2962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5616 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=4393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.199 (n=1774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0044 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1457` → IC=+0.167 (n=2334)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1457 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=5538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.2947` → IC=+0.189 (n=5301)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2947 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.9182` → IC=+0.179 (n=798)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9182 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.479` → IC=+0.207 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.479 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8528` → IC=+0.162 (n=3231)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8528 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `1.1859` → IC=+0.159 (n=1616)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1859 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1552` → IC=+0.170 (n=1364)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1552 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.526` → IC=+0.155 (n=2279)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.526 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.8075` → IC=+0.155 (n=3452)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8075 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.154 (n=5834)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `7305.2542` → IC=+0.187 (n=2404)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7305.2542 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.7105` → IC=+0.141 (n=5844)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.7105 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.136 (n=2576)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 22.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.204 (n=877)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.224 (n=578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.212 (n=1324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.2111` → IC=+0.223 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2111 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6944` → IC=+0.238 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6944 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.825` → IC=+0.221 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.825 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.203 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0887` → IC=+0.208 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0887 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1491` → IC=+0.200 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1491 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.3995` → IC=+0.192 (n=1288)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.3995 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `15543.1144` → IC=+0.203 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15543.1144 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.150 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0033 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.2127` → IC=+0.194 (n=724)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.2127 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.165 (n=712)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 166.0 (IC base=+0.075)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.239 (n=546)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.156 (n=718)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=1693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.7614` → IC=+0.257 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7614 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.162 (n=768)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.954` → IC=+0.181 (n=230)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.954 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8289` → IC=+0.152 (n=1087)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8289 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.183 (n=219)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7717` → IC=+0.156 (n=1072)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7717 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `7771.1014` → IC=+0.173 (n=739)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7771.1014 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.147 (n=554)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 31.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.125 (n=1631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0082 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1814` → IC=+0.210 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1814 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6736` → IC=+0.136 (n=717)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6736 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.0763` → IC=+0.124 (n=602)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0763 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `4074.8497` → IC=+0.137 (n=1456)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 4074.8497 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.145 (n=714)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 41.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.153 (n=476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0073 (IC base=+0.122)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.135 (n=475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0129 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.141 (n=1425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.7273` → IC=+0.225 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7273 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.5064` → IC=+0.147 (n=457)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.5064 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.862` → IC=+0.233 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.862 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.0398` → IC=+0.132 (n=1255)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0398 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.7` → IC=+0.128 (n=1273)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.7 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4196` → IC=+0.153 (n=462)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4196 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=1437)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3046.3244` → IC=+0.150 (n=475)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3046.3244 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.137 (n=455)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 9.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6939` → IC=+0.144 (n=1596)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6939 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `2737.2879` → IC=+0.161 (n=723)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2737.2879 (IC base=+0.077)

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
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.226 (n=8999)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=28190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9655` → IC=+0.299 (n=9001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9655 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9607` → IC=+0.215 (n=3087)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9607 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.845` → IC=+0.259 (n=6607)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.845 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8642` → IC=+0.163 (n=12139)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8642 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.217 (n=3528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6398` → IC=+0.194 (n=8800)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6398 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1768.4709` → IC=+0.181 (n=26982)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1768.4709 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=25625)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.198 (n=8381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0056 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.206 (n=8372)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.4024` → IC=+0.201 (n=22096)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4024 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=9364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.596` → IC=+0.244 (n=25111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.596 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.196` → IC=+0.182 (n=16110)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.196 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.488` → IC=+0.204 (n=23443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.488 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.6247` → IC=+0.182 (n=5613)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6247 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.255 (n=3461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6319` → IC=+0.211 (n=8065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6319 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=24023)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.262 (n=1952)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3097` → IC=+0.235 (n=3783)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3097 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2891)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.314 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.029` → IC=+0.298 (n=2821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.029 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.288 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2835` → IC=+0.241 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2835 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2066.52` → IC=+0.238 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2066.52 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.267 (n=1317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.263 (n=2635)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1299` → IC=+0.289 (n=1737)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1299 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.264 (n=4099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.264 (n=3565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.279 (n=3948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5556 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.1` → IC=+0.264 (n=3616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.287 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5664` → IC=+0.263 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5664 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6396` → IC=+0.272 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6396 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=4186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.263 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.170 (n=1964)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.146 (n=1482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2908` → IC=+0.201 (n=3970)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2908 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.7442` → IC=+0.211 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7442 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.994` → IC=+0.172 (n=692)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 10.994 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6316` → IC=+0.158 (n=1482)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6316 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0621` → IC=+0.143 (n=2015)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0621 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.186 (n=616)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1721` → IC=+0.144 (n=3850)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1721 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5209` → IC=+0.145 (n=3908)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5209 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `287.0` → IC=+0.153 (n=2895)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 287.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.169 (n=3459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0062 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.176 (n=1311)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=1448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.3222` → IC=+0.232 (n=2619)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3222 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1585` → IC=+0.162 (n=3877)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1585 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.001` → IC=+0.147 (n=1850)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.001 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.188` → IC=+0.150 (n=4015)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.188 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0387` → IC=+0.157 (n=3457)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0387 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2217` → IC=+0.202 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2217 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4386` → IC=+0.150 (n=3816)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4386 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.1334` → IC=+0.155 (n=1730)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1334 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=5096)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.182 (n=1254)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 211.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.242 (n=2038)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=4001)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1669)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.858` → IC=+0.311 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.858 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1296` → IC=+0.224 (n=4263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1296 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2033` → IC=+0.234 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2033 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.6118` → IC=+0.230 (n=4396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6118 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=5188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2010.7034` → IC=+0.238 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2010.7034 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.250 (n=1907)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1864` → IC=+0.261 (n=1906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1864 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1985)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.0711` → IC=+0.295 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0711 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.848` → IC=+0.305 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.848 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.3456` → IC=+0.300 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3456 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.256 (n=2797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1990.1574` → IC=+0.254 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1990.1574 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.249 (n=2815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.244)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.188 (n=1559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3604` → IC=+0.147 (n=4107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3604 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8746` → IC=+0.262 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8746 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.154` → IC=+0.170 (n=2273)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.154 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.973` → IC=+0.161 (n=2041)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.973 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8533` → IC=+0.153 (n=3112)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8533 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.198 (n=614)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5179` → IC=+0.153 (n=2010)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5179 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1542` → IC=+0.144 (n=2070)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1542 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5906.3056` → IC=+0.228 (n=2116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5906.3056 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.144 (n=3061)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 86.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.169 (n=3969)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.4641` → IC=+0.163 (n=3967)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4641 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.7057` → IC=+0.201 (n=3968)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7057 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.6467` → IC=+0.157 (n=4607)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6467 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.033` → IC=+0.160 (n=795)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.033 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.028` → IC=+0.155 (n=3459)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.028 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6812` → IC=+0.164 (n=1746)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6812 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.209 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.805` → IC=+0.156 (n=2566)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.805 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5251` → IC=+0.158 (n=3438)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5251 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `6728.8499` → IC=+0.218 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6728.8499 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.172 (n=1338)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 58.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.145 (n=3168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0101 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=3356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.257 (n=3172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8146` → IC=+0.195 (n=1048)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8146 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.192` → IC=+0.271 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.192 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2098` → IC=+0.128 (n=4753)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2098 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1021` → IC=+0.124 (n=4528)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1021 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.147 (n=593)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.8284` → IC=+0.132 (n=3097)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8284 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2769.138` → IC=+0.239 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2769.138 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.159 (n=3909)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0114 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1433` → IC=+0.150 (n=1482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1433 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=4574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.225 (n=4470)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2296` → IC=+0.151 (n=4103)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2296 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.023` → IC=+0.161 (n=4318)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.023 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1941` → IC=+0.143 (n=4442)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1941 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.199 (n=784)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.165 (n=1416)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.5025` → IC=+0.145 (n=1416)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.5025 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2641.0193` → IC=+0.225 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2641.0193 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.149 (n=3790)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 40.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.254 (n=4340)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.240 (n=2912)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.988` → IC=+0.301 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.988 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.2051` → IC=+0.250 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2051 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.906` → IC=+0.300 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.906 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2164` → IC=+0.236 (n=4340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2164 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6387` → IC=+0.242 (n=4340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6387 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.243` → IC=+0.260 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.243 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.5318` → IC=+0.257 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5318 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=5475)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2646.4017` → IC=+0.239 (n=2893)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2646.4017 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0244` → IC=+0.269 (n=1506)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0244 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.249 (n=4715)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.1406` → IC=+0.304 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1406 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.2051` → IC=+0.250 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2051 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2337` → IC=+0.249 (n=4341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2337 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.837` → IC=+0.283 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.837 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.635` → IC=+0.248 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.635 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2189` → IC=+0.264 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2189 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.311 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.5504` → IC=+0.248 (n=3826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5504 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.245 (n=3770)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.234 (n=6659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.5399` → IC=+0.235 (n=7559)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5399 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=7583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.261 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` < `0.9706` → IC=+0.230 (n=6228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9706 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.428` → IC=+0.238 (n=2523)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.428 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `0.7046` → IC=+0.233 (n=2376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7046 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.8771` → IC=+0.229 (n=3598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8771 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.1639` → IC=+0.237 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1639 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4494` → IC=+0.238 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4494 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.231 (n=5392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `3771.3096` → IC=+0.236 (n=5039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3771.3096 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.229 (n=1815)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.211 (n=3618)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.533` → IC=+0.218 (n=5422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.533 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=1815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=2466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.7282` → IC=+0.216 (n=5422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7282 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.7161` → IC=+0.219 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7161 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.681` → IC=+0.223 (n=4941)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.681 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2537` → IC=+0.210 (n=4928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2537 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.7287` → IC=+0.203 (n=4402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7287 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.213 (n=5016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.5361` → IC=+0.216 (n=2350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5361 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8218` → IC=+0.218 (n=3560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8218 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.235 (n=3584)

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

- **PATRÓN** `dist_vwap_pct` < `0.2002` → IC=+0.286 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2002 (IC base=+0.274)

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

- **PATRÓN** `libro_liquidez` > `15901.2298` → IC=+0.287 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15901.2298 (IC base=+0.274)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.260 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3904` → IC=+0.184 (n=1556)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3904 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.173 (n=585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.191 (n=685)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.3612` → IC=+0.171 (n=335)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.3612 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.5576` → IC=+0.170 (n=1864)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.5576 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.338` → IC=+0.189 (n=1530)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 6.338 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.0935` → IC=+0.184 (n=1370)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.0935 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1523` → IC=+0.185 (n=474)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1523 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `2.5013` → IC=+0.176 (n=1547)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.5013 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.1745` → IC=+0.171 (n=702)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.1745 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `14629.5629` → IC=+0.169 (n=705)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14629.5629 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `703.0` → IC=+0.184 (n=1512)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 703.0 (IC base=+0.168)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.244 (n=362)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.211)

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
- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.224 (n=1841)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.4737` → IC=+0.222 (n=2090)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4737 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.4666` → IC=+0.231 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4666 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.8315` → IC=+0.217 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8315 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.4293` → IC=+0.225 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4293 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.251` → IC=+0.221 (n=2125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.251 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.217 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8615 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.0641` → IC=+0.220 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0641 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.217 (n=1942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.1582` → IC=+0.217 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1582 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4017` → IC=+0.234 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4017 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4929` → IC=+0.216 (n=1824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4929 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.247 (n=563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.5101` → IC=+0.219 (n=1689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5101 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.215 (n=626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=1133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.213 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0847 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.7287` → IC=+0.221 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7287 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.199` → IC=+0.210 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.199 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2537` → IC=+0.211 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2537 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.7178` → IC=+0.210 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7178 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.227 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4742` → IC=+0.207 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4742 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.7689` → IC=+0.209 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7689 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.209 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.206)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.236 (n=445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.232 (n=446)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.253 (n=1199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.223 (n=1220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9877` → IC=+0.303 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9877 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `1.094` → IC=+0.244 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.094 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.038` → IC=+0.274 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.038 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.6422` → IC=+0.252 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6422 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `1.2446` → IC=+0.225 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2446 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.226 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.250 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.5098` → IC=+0.232 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5098 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3376.162` → IC=+0.246 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3376.162 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0141` → IC=+0.246 (n=1012)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0141 (IC base=+0.247)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.255 (n=907)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.247)

- **PATRÓN** `drift_60min` |x|≤ `0.5468` → IC=+0.253 (n=890)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5468 (IC base=+0.247)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.267 (n=701)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` < `0.6444` → IC=+0.270 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6444 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.043` → IC=+0.264 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.043 (IC base=+0.247)

- **PATRÓN** `volumen_regimen` < `0.7551` → IC=+0.258 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7551 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.256 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` > `2.214` → IC=+0.273 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.214 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.250 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `4038.9632` → IC=+0.268 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4038.9632 (IC base=+0.247)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.273 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.247)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.144 (n=1003)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0044 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.424` → IC=+0.142 (n=2910)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.424 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1615` → IC=+0.161 (n=1330)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1615 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.267` → IC=+0.147 (n=632)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.267 (IC base=+0.080)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.122 (n=1608)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0071 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.5781` → IC=+0.182 (n=2335)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5781 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.522` → IC=+0.136 (n=1042)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 2.522 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.1532` → IC=+0.193 (n=662)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1532 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `1.4232` → IC=+0.131 (n=751)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4232 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` > `2.5354` → IC=+0.127 (n=751)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.5354 (IC base=+0.103)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.122 (n=733)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0057 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5656` → IC=+0.157 (n=716)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5656 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.165 (n=368)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.0602` → IC=+0.242 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0602 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.139 (n=333)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.057)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.4852` → IC=-0.121 (n=280)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4852
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=545)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.160 (n=383)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0044 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.135 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5264` → IC=+0.164 (n=747)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5264 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.158 (n=396)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.066` → IC=+0.176 (n=183)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 12.066 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.3108` → IC=+0.223 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3108 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2626` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2626 (IC base=+0.049)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9778` → IC=+0.190 (n=321)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.9778 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.7683` → IC=+0.162 (n=232)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.7683 (IC base=+0.040)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.179 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0103 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.120 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.196 (n=629)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.2261` → IC=+0.150 (n=626)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2261 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.003` → IC=+0.253 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.003 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.1082` → IC=+0.184 (n=210)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1082 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.1629` → IC=+0.183 (n=162)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1629 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `1.8779` → IC=+0.138 (n=398)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.8779 (IC base=+0.100)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.386 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.329 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `ibs_20min` < `0.9191` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9191 (IC base=+0.296)

- **PATRÓN** `ibs_20min` > `0.5624` → IC=+0.337 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5624 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.4847` → IC=+0.381 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4847 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.688` → IC=+0.305 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.688 (IC base=+0.296)

- **PATRÓN** `volumen_regimen` < `0.8086` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8086 (IC base=+0.296)

- **PATRÓN** `volumen_regimen` > `0.5665` → IC=+0.298 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5665 (IC base=+0.296)

- **PATRÓN** `volumen_pendiente_norm` > `0.0821` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0821 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` < `2.819` → IC=+0.333 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.819 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.331 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `1584.8` → IC=+0.354 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1584.8 (IC base=+0.296)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.342 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.328)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.368 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.328)

- **PATRÓN** `ibs_20min` < `0.0507` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0507 (IC base=+0.328)

- **PATRÓN** `ibs_20min` > `0.2661` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2661 (IC base=+0.328)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.683` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.683 (IC base=+0.328)

- **PATRÓN** `volumen_regimen` > `0.7932` → IC=+0.409 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7932 (IC base=+0.328)

- **PATRÓN** `volumen_pendiente_norm` > `0.1731` → IC=+0.421 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1731 (IC base=+0.328)

- **PATRÓN** `volumen_spike_ratio` < `1.4553` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4553 (IC base=+0.328)

- **PATRÓN** `volumen_spike_ratio` > `3.1184` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1184 (IC base=+0.328)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.352 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.328)

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
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=104)

- **FILTRO** `ibs_20min` < `0.0328` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0328
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=101)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.265 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=80)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.329 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=120)

- **FILTRO** `volumen_spike_ratio` > `1.817` → IC=-0.318 (n=42)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.817
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=84)

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
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.201 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9045` → IC=+0.311 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9045 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.194` → IC=+0.186 (n=227)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 10.194 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.185 (n=312)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6195 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `1.1935` → IC=+0.181 (n=312)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.1935 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` < `0.2118` → IC=+0.185 (n=955)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2118 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4195` → IC=+0.203 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4195 (IC base=+0.169)

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
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=218)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.322)

- **PATRÓN** `elapsed_s` > `231.9` → IC=+0.397 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 231.9 (IC base=+0.322)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.322)

- **PATRÓN** `drift_60min` |x|≤ `0.6903` → IC=+0.392 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6903 (IC base=+0.322)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.376 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.322)

- **PATRÓN** `ballena_activa_n` < `1043.0` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1043.0 (IC base=+0.322)

- **PATRÓN** `drift_ventana_pct` |x|> `0.453` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.453 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `225.0` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 225.0 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `2.8622` → IC=+0.299 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.8622 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.7139` → IC=+0.308 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7139 (IC base=+0.281)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1283.0` → IC=+0.358 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1283.0 (IC base=+0.281)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=218)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.322)

- **PATRÓN** `elapsed_s` > `231.9` → IC=+0.397 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 231.9 (IC base=+0.322)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.322)

- **PATRÓN** `drift_60min` |x|≤ `0.6903` → IC=+0.392 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6903 (IC base=+0.322)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.376 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.322)

- **PATRÓN** `ballena_activa_n` < `1043.0` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1043.0 (IC base=+0.322)

- **PATRÓN** `drift_ventana_pct` |x|> `0.453` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.453 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `225.0` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 225.0 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `2.8622` → IC=+0.299 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.8622 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.7139` → IC=+0.308 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7139 (IC base=+0.281)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1283.0` → IC=+0.358 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1283.0 (IC base=+0.281)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=297)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=298)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1789)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.176 (n=100)

  - _Acción_: Kelly boost +0.88€ cuando `liq_n` > 2.0 (IC base=+0.078)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.154 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 6.0 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.078)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11682.4811` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 11682.4811
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=129)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=170)

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
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=290)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4362)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=280)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=237)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=177)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.159 (n=177)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 31.0 (IC base=+0.021)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.138 (n=307)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.026)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.163)

- **PATRÓN** `liq_usd_total` > `750.26` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 750.26 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.207 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.173 (n=163)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.04 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `3293.399` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3293.399 (IC base=+0.163)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1738)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1692)

- **FILTRO** `liq_n` < `3.0` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `liq_n` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `liq_usd_total` < `6520.36` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 6520.36
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

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
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1218)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1218)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1671)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1671)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=382)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=382)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.129 (n=173)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=224)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.132 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=436)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=487)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=354)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=467)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=467)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=455)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=3907)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=10011)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.153 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=154)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.163 (n=470)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1137)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.149 (n=371)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=1006)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.139 (n=472)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.51 (IC base=-0.009)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.122 (n=326)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=385)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.129 (n=173)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=543)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.156 (n=257)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1388)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.129 (n=375)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.51 (IC base=-0.020)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=398)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=833)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.133 (n=602)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=762)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.126 (n=642)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=667)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.404` → IC=-0.161 (n=487)

  - _Acción_: SKIP cuando `py_entrada` < 0.404
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=991)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9441)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=29217)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9719)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=30348)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4460)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=1461)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=4425)

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
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3510)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4462)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=430)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.164 (n=409)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1236)

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
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=673)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.175 (n=438)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=880)

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
- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=20866)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=64811)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.224 (n=28131)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=57546)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.153 (n=28471)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=57206)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26444)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=80367)

- **FILTRO** `ibs_7min` > `0.2779` → IC=-0.182 (n=26701)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2779
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=80110)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.126 (n=3531)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=11044)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=3578)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=10997)

- **FILTRO** `ibs_7min` < `0.7102` → IC=-0.211 (n=3642)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7102
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10933)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.203 (n=3620)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=10955)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.264 (n=3398)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=11513)

- **FILTRO** `ibs_7min` > `0.2639` → IC=-0.187 (n=3727)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2639
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=11184)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.177 (n=3718)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=11193)

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
- **FILTRO** `py_entrada` < `0.33` → IC=-0.275 (n=3274)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=11002)

- **FILTRO** `ibs_7min` < `0.7107` → IC=-0.202 (n=3567)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7107
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10709)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.197 (n=3483)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10793)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=3439)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=11326)

- **FILTRO** `ibs_7min` > `0.2715` → IC=-0.178 (n=3691)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2715
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=11074)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.170 (n=3646)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=11119)

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

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=940)

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
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=568)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.141 (n=797)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.132 (n=636)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.164 (n=585)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 459.6089 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4209.805` → IC=+0.129 (n=585)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 4209.805 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.175 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 14.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.142 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 5.0 (IC base=+0.140)

- **PATRÓN** `total_vol_5m` < `287.685` → IC=+0.172 (n=269)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 287.685 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.143 (n=362)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.04 (IC base=+0.140)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.136 (n=366)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=342)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.120 (n=443)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.157 (n=211)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `707.9675` → IC=+0.173 (n=279)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 707.9675 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 59.0 (IC base=+0.127)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4315` → IC=+0.210 (n=136)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4315 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.133 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.161 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 5.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4761.643 (IC base=+0.132)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=224)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.090)

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
- **FILTRO** `sigma_h` < `0.0147` → IC=-0.167 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0147
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

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

- **FILTRO** `sigma_h` < `0.0069` → IC=-0.171 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=506)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=546)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.022)

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

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.2738 (IC base=+0.040)

- **PATRÓN** `streak_estiramiento` < `0.3856` → IC=+0.207 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3856 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.140 (n=209)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 34.0 (IC base=+0.082)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=108)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=866)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1128)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1340)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5788)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3436)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.184 (n=2266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0059 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2335` → IC=+0.158 (n=6794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2335 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1239` → IC=+0.133 (n=6794)

  - _Acción_: Kelly boost +0.67€ cuando `drift_15min` |x|≤ 1.1239 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.133 (n=6793)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0991` → IC=+0.144 (n=2144)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0991 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.5526` → IC=+0.207 (n=6069)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5526 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.959` → IC=+0.225 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.959 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3549)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4340.6205` → IC=+0.173 (n=2265)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4340.6205 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2672)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.246 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0774` → IC=+0.247 (n=409)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0774 (IC base=+0.208)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2654` → IC=+0.230 (n=309)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2654 (IC base=+0.208)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2221` → IC=+0.221 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2221 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_15` > `0.7013` → IC=+0.276 (n=926)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7013 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.237 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.5589` → IC=+0.210 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5589 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.961` → IC=+0.298 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.961 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `11825.4597` → IC=+0.221 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11825.4597 (IC base=+0.208)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.147 (n=1045)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0068 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.146 (n=793)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0824` → IC=+0.137 (n=1060)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0824 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.142 (n=839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.477` → IC=+0.217 (n=1187)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.477 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.143 (n=733)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.6666` → IC=+0.132 (n=1348)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6666 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.949` → IC=+0.281 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.949 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6172.6446` → IC=+0.174 (n=538)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6172.6446 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8333` → IC=+0.146 (n=708)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` > 0.8333 (IC base=+0.046)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.143 (n=1701)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0118 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2399` → IC=+0.175 (n=1702)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2399 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0587` → IC=+0.139 (n=1701)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.0587 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.184 (n=533)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=1553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.142 (n=1501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6944` → IC=+0.232 (n=1134)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6944 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2145` → IC=+0.142 (n=780)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2145 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.9137` → IC=+0.142 (n=1966)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.9137 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.872` → IC=+0.184 (n=394)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 16.872 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2938.7445` → IC=+0.180 (n=772)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2938.7445 (IC base=+0.137)

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

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.388 (n=186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.361)

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

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.378 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.363)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `21.854` → IC=+0.393 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.854 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.532` → IC=+0.365 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.532 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.362 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `4411.1912` → IC=+0.371 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4411.1912 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.203 (n=3141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=3145)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2790)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3496)

- **FILTRO** `libro_liquidez` < `4438.7632` → IC=-0.172 (n=4148)

  - _Acción_: SKIP cuando `libro_liquidez` < 4438.7632
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2138)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.277 (n=1388)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` > `0.116` → IC=+0.208 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.116 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` < `0.6` → IC=+0.200 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6 (IC base=-0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2278` → IC=+0.269 (n=2078)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2278 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.3779` → IC=+0.282 (n=6229)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3779 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.7109` → IC=+0.263 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7109 (IC base=+0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` < `0.0041` → IC=-0.207 (n=1053)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=3162)

- **FILTRO** `sigma_ewma_delta_pct` > `22.161` → IC=-0.232 (n=592)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.161
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=3623)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.183 (n=99)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=4116)

- **FILTRO** `libro_liquidez` < `10092.0361` → IC=-0.195 (n=1390)

  - _Acción_: SKIP cuando `libro_liquidez` < 10092.0361
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=2825)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1422` → IC=+0.290 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1422 (IC base=+0.067)

- **PATRÓN** `ibs_15` > `0.8098` → IC=+0.323 (n=450)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8098 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1067` → IC=+0.286 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1067 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.5528` → IC=+0.286 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5528 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.676` → IC=+0.139 (n=250)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 21.676 (IC base=+0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.230 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.181)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1432` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1432 (IC base=-0.181)

- **PATRÓN** `ibs_15` < `0.6353` → IC=+0.300 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6353 (IC base=-0.181)

- **PATRÓN** `dist_vwap_pct` < `0.052` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.052 (IC base=-0.181)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.309 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.181)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=916)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.160 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0067 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.150 (n=467)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0053 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.177 (n=308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.182 (n=555)

  - _Acción_: Kelly boost +0.91€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.174 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.5639` → IC=+0.239 (n=700)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5639 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6665` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.6665 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.148 (n=538)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.250 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=916)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5223.3427` → IC=+0.172 (n=467)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5223.3427 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.252 (n=1653)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4846` → IC=+0.242 (n=2479)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4846 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.837` → IC=+0.248 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.837 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1962` → IC=+0.257 (n=1125)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1962 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.242 (n=1097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.1951` → IC=+0.294 (n=1653)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1951 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.242` → IC=+0.249 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.242 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.511` → IC=+0.240 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.511 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.251` → IC=+0.238 (n=2603)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.251 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1999` → IC=-0.302 (n=377)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1999
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1132)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.282 (n=513)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=996)

- **FILTRO** `drift_15min` |x|> `1.0221` → IC=-0.302 (n=377)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0221
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1132)

- **FILTRO** `sigma_ewma_delta_pct` > `6.094` → IC=-0.212 (n=328)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.094
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=1181)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.2132` → IC=+0.247 (n=342)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2132 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.295 (n=1029)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2882` → IC=+0.257 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2882 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.012` → IC=-0.244 (n=1307)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.012
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=436)

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

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=1434)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.323 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=-0.008)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.172 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.104)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.160 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.104)

- **PATRÓN** `drift_15min` |x|≤ `0.7469` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.7469 (IC base=+0.104)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2338` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2338 (IC base=+0.104)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.318 (n=31)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.341` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.341 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 52.0 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.136 (n=97)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.047)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.172 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.104)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.160 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.104)

- **PATRÓN** `drift_15min` |x|≤ `0.7469` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.7469 (IC base=+0.104)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2338` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2338 (IC base=+0.104)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.318 (n=31)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.341` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.341 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 52.0 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.136 (n=97)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.047)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.297 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.291 (n=516)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0715` → IC=+0.306 (n=684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0715 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.288 (n=1548)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2158` → IC=+0.289 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2158 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=1611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8354` → IC=+0.309 (n=1548)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8354 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.317 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2752 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.382 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `13022.3239` → IC=+0.301 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13022.3239 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.307 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.285 (n=272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.298 (n=359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `0.3899` → IC=+0.281 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3899 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.280 (n=813)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2257` → IC=+0.294 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2257 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.303 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.8544` → IC=+0.305 (n=727)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8544 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2609` → IC=+0.313 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2609 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.371` → IC=+0.386 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.371 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `14356.961` → IC=+0.311 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14356.961 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.300 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.298 (n=489)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0502` → IC=+0.322 (n=245)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0502 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0631` → IC=+0.292 (n=734)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0631 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.310 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8444` → IC=+0.317 (n=734)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8444 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2913` → IC=+0.316 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2913 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.767` → IC=+0.372 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.767 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1089` → IC=-0.168 (n=239)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1089
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=119)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.146 (n=272)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=96)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1244` → IC=-0.220 (n=130)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1244
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=392)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.182 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=392)

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

- **FILTRO** `drift_15min` |x|> `0.3046` → IC=-0.269 (n=24)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3046
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=47)

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

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5526 sube el IC de +0.132 a +0.207 en UPDOWN_GBM#15min (n=6069). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7013 sube el IC de +0.208 a +0.276 en UPDOWN_GBM#BTC#15min (n=926). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.477 sube el IC de +0.131 a +0.217 en UPDOWN_GBM#ETH#15min (n=1187). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.6944 sube el IC de +0.137 a +0.232 en UPDOWN_GBM#XRP#15min (n=1134). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.086 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=1388). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3779 sube el IC de +0.001 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=6229). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8098 sube el IC de +0.067 a +0.323 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=450). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6353 sube el IC de -0.181 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=88). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5639 sube el IC de +0.148 a +0.239 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=700). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1951 sube el IC de +0.234 a +0.294 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1653). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.026 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=1029). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.008 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1434). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.104 a +0.318 en UPDOWN_GBM_ETH_15M_HORA7 (n=31). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.104 a +0.318 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=31). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8354 sube el IC de +0.285 a +0.309 en UPDOWN_GBM_IBS_ALTO (n=1548). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8544 sube el IC de +0.280 a +0.305 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=727). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8444 sube el IC de +0.290 a +0.317 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=734). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
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
| ✅ BALLENAS_TARDIAS | 52151 | -0.086 | -6675.51€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3479 | +0.087 | -323.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48672 | -0.098 | -6351.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3479 | +0.087 | -323.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3479 | +0.087 | -323.83€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14883 | -0.042 | -1406.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14883 | -0.042 | -1406.97€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 59481 | -0.012 | +2465.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 15327 | +0.003 | +1449.29€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 44154 | -0.017 | +1016.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 59481 | -0.012 | +2465.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 15327 | +0.003 | +1449.29€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 44154 | -0.017 | +1016.14€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 220174 | +0.112 | -9107.76€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#15min | 23974 | +0.178 | -786.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 1032 | +0.024 | -79.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 182691 | +0.104 | -7815.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12477 | +0.095 | -426.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 30287 | +0.101 | -2199.57€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#15min | 92 | -0.202 | +7.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 30158 | +0.102 | -2216.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 22 | +0.167 | +21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 41116 | +0.121 | -724.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5771 | +0.175 | -243.02€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 30238 | +0.118 | -278.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 5065 | +0.080 | -179.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 30340 | +0.099 | -2098.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 117 | -0.105 | +19.63€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 30195 | +0.100 | -2110.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 13 | -0.065 | +4.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 47188 | +0.123 | -1035.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11744 | +0.176 | -348.64€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 30739 | +0.105 | -590.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4693 | +0.103 | -88.25€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 40947 | +0.111 | -1700.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6149 | +0.199 | -239.28€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 935 | +0.048 | -25.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 31182 | +0.095 | -1249.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2681 | +0.109 | -186.79€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 30296 | +0.106 | -1349.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 101 | -0.131 | +17.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 30179 | +0.106 | -1369.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 35995 | +0.188 | -2767.89€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 35995 | +0.188 | -2767.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 8155 | +0.158 | -1008.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 8155 | +0.158 | -1008.07€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5471 | +0.193 | -241.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5471 | +0.193 | -241.32€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7938 | +0.171 | -744.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7938 | +0.171 | -744.07€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6581 | +0.251 | -237.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6581 | +0.251 | -237.92€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7771 | +0.183 | -550.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7771 | +0.183 | -550.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1375 | +0.424 | -56.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1375 | +0.424 | -56.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 587 | +0.437 | -7.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 587 | +0.437 | -7.80€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 246 | +0.399 | -20.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 246 | +0.399 | -20.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 127077 | +0.199 | -9311.43€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 127077 | +0.199 | -9311.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 22038 | +0.175 | -2621.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 22038 | +0.175 | -2621.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 20478 | +0.223 | -688.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 20478 | +0.223 | -688.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21791 | +0.180 | -2286.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21791 | +0.180 | -2286.45€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 20655 | +0.217 | -813.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 20655 | +0.217 | -813.63€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 20955 | +0.205 | -1226.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 20955 | +0.205 | -1226.62€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 21160 | +0.196 | -1674.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 21160 | +0.196 | -1674.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 49420 | +0.116 | +408.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 49420 | +0.116 | +408.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 24608 | +0.117 | +273.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 24608 | +0.117 | +273.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 24812 | +0.115 | +135.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 24812 | +0.115 | +135.53€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2085 | +0.064 | -106.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1360 | +0.073 | -42.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1651 | +0.070 | -61.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1360 | +0.073 | -42.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 101369 | +0.100 | -2152.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 8231 | +0.096 | +173.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 93138 | +0.101 | -2326.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 55294 | +0.104 | -490.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 8231 | +0.096 | +173.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 47063 | +0.106 | -664.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 21862 | +0.109 | -88.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 21862 | +0.109 | -88.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 24213 | +0.083 | -1573.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 24213 | +0.083 | -1573.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 954 | +0.168 | -110.94€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 954 | +0.168 | -110.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 954 | +0.168 | -110.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 954 | +0.168 | -110.94€ | 2 | 4 |
| ✅ GBM_LATE_15M | 69066 | +0.102 | +38917.18€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 69066 | +0.102 | +38917.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11490 | +0.223 | +9787.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11490 | +0.223 | +9787.99€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 10833 | +0.176 | +8753.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10833 | +0.176 | +8753.51€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 12342 | +0.207 | +9763.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 12342 | +0.207 | +9763.51€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 9150 | +0.064 | +3154.28€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 9150 | +0.064 | +3154.28€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 9561 | -0.025 | +2483.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9561 | -0.025 | +2483.49€ | 3 | 14 |
| ✅ GBM_LATE_15M#XRP | 15690 | -0.019 | +4974.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15690 | -0.019 | +4974.40€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 73404 | +0.088 | +43115.58€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 73404 | +0.088 | +43115.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 14256 | -0.002 | +7510.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 14256 | -0.002 | +7510.60€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15772 | +0.008 | +4388.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15772 | +0.008 | +4388.40€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9783 | +0.297 | +11253.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9783 | +0.297 | +11253.11€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 14072 | +0.021 | +4552.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 14072 | +0.021 | +4552.47€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 11151 | +0.052 | +5245.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 11151 | +0.052 | +5245.04€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8370 | +0.313 | +10165.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8370 | +0.313 | +10165.96€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 54337 | +0.179 | +45110.81€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 54337 | +0.179 | +45110.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 8250 | +0.238 | +7614.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 8250 | +0.238 | +7614.84€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8695 | +0.140 | +6553.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8695 | +0.140 | +6553.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8728 | +0.224 | +7557.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8728 | +0.224 | +7557.42€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 9288 | +0.130 | +7282.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 9288 | +0.130 | +7282.42€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 10240 | +0.123 | +7911.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 10240 | +0.123 | +7911.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 9136 | +0.231 | +8191.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 9136 | +0.231 | +8191.18€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14858 | +0.125 | +7540.64€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14858 | +0.125 | +7540.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3941 | +0.125 | +2098.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3941 | +0.125 | +2098.02€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 510 | +0.154 | +284.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 510 | +0.154 | +284.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4344 | +0.125 | +2198.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4344 | +0.125 | +2198.24€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 4026 | +0.099 | +1647.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 4026 | +0.099 | +1647.40€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1357 | +0.168 | +868.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1357 | +0.168 | +868.50€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 69453 | +0.189 | +57848.43€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 69453 | +0.189 | +57848.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10990 | +0.247 | +10504.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10990 | +0.247 | +10504.00€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 11162 | +0.143 | +8168.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 11162 | +0.143 | +8168.05€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11749 | +0.234 | +10585.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11749 | +0.234 | +10585.68€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11511 | +0.145 | +8686.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11511 | +0.145 | +8686.40€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 12255 | +0.129 | +8976.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 12255 | +0.129 | +8976.75€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11786 | +0.240 | +10927.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11786 | +0.240 | +10927.55€ | 0 | 23 |
| ✅ GBM_LATE_5M | 17307 | +0.221 | +14682.62€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 17307 | +0.221 | +14682.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1948 | +0.253 | +1898.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3358 | +0.209 | +2854.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3358 | +0.209 | +2854.60€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1592 | +0.218 | +1323.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1592 | +0.218 | +1323.49€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 5037 | +0.211 | +3979.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 5037 | +0.211 | +3979.47€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3126 | +0.233 | +2817.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3126 | +0.233 | +2817.21€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 2246 | +0.213 | +1809.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2246 | +0.213 | +1809.12€ | 0 | 0 |
| ✅ GBM_LATE_60M | 7216 | +0.090 | +2708.38€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 7216 | +0.090 | +2708.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 287 | +0.279 | +318.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 287 | +0.279 | +318.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2155 | +0.062 | +648.53€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2155 | +0.062 | +648.53€ | 0 | 5 |
| ✅ GBM_LATE_60M#DOGE | 280 | +0.308 | +334.49€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 280 | +0.308 | +334.49€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 2009 | +0.060 | +634.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 2009 | +0.060 | +634.01€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 2201 | +0.064 | +435.33€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2201 | +0.064 | +435.33€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 284 | +0.315 | +337.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 284 | +0.315 | +337.28€ | 0 | 22 |
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
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2721 | +0.094 | +749.04€ | 0 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2721 | +0.094 | +749.04€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 959 | +0.071 | +257.69€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 959 | +0.071 | +257.69€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 59 | +0.205 | +35.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 59 | +0.205 | +35.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 834 | +0.054 | +160.87€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 834 | +0.054 | +160.87€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 706 | +0.155 | +246.24€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 706 | +0.155 | +246.24€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 163 | +0.118 | +48.60€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 163 | +0.118 | +48.60€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 452 | +0.302 | +534.70€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 452 | +0.302 | +534.70€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 452 | +0.302 | +534.70€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 452 | +0.302 | +534.70€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 5226 | +0.096 | +1131.60€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 5226 | +0.096 | +1131.60€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 5226 | +0.096 | +1131.60€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 5226 | +0.096 | +1131.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 2124 | +0.013 | +87.82€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 2124 | +0.013 | +87.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 274 | +0.076 | +41.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 274 | +0.076 | +41.86€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M#BTC | 382 | -0.018 | +5.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 382 | -0.018 | +5.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 195 | +0.023 | +15.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 195 | +0.023 | +15.62€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 456 | +0.026 | +23.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 456 | +0.026 | +23.78€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 364 | -0.025 | -0.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 364 | -0.025 | -0.85€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 453 | +0.014 | +1.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 453 | +0.014 | +1.85€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4748 | +0.020 | +219.99€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4748 | +0.020 | +219.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 889 | +0.018 | +57.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 889 | +0.018 | +57.04€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 376 | +0.066 | +94.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 376 | +0.066 | +94.52€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1790 | +0.025 | +41.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1790 | +0.025 | +41.69€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 828 | +0.012 | +3.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 828 | +0.012 | +3.93€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 624 | -0.003 | +28.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 624 | -0.003 | +28.95€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2984 | -0.038 | -19.58€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2984 | -0.038 | -19.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 899 | -0.042 | -21.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 899 | -0.042 | -21.97€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1084 | -0.023 | +11.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1084 | -0.023 | +11.58€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 967 | -0.053 | -9.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 967 | -0.053 | -9.60€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 27 | +0.017 | -0.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 27 | +0.017 | -0.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 22918 | -0.032 | -226.16€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 11160 | -0.030 | -58.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11758 | -0.034 | -167.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 791 | -0.052 | -39.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 406 | -0.037 | -4.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 385 | -0.069 | -35.57€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 6229 | -0.026 | -28.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2975 | -0.022 | +11.82€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3254 | -0.029 | -40.45€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 2071 | -0.035 | -18.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1069 | -0.037 | -18.40€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 1002 | -0.032 | +0.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 5282 | -0.029 | -20.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2562 | -0.025 | +12.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2720 | -0.033 | -33.61€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4345 | -0.028 | +22.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2132 | -0.028 | +9.79€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2213 | -0.027 | +12.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 4200 | -0.046 | -141.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 2016 | -0.048 | -70.68€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2184 | -0.044 | -70.84€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 78725 | -0.001 | +4139.23€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 78725 | -0.001 | +4139.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 11341 | -0.038 | -155.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 11341 | -0.038 | -155.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 11250 | -0.055 | -327.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 11250 | -0.055 | -327.01€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7632 | -0.053 | -113.59€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7632 | -0.053 | -113.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2217 | -0.058 | -21.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2217 | -0.058 | -21.29€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 106 | -0.028 | -1.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 106 | -0.028 | -1.20€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 828 | -0.118 | -35.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 828 | -0.118 | -35.22€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2334 | -0.065 | -11.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2334 | -0.065 | -11.26€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 876 | -0.021 | -29.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 876 | -0.021 | -29.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 4140 | +0.001 | -13.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 4140 | +0.001 | -13.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 952 | -0.006 | -16.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 952 | -0.006 | -16.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1327 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1327 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 192488 | -0.078 | +2142.05€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 192488 | -0.078 | +2142.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 29486 | -0.101 | -1377.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 29486 | -0.101 | -1377.24€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 29041 | -0.101 | -1039.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 29041 | -0.101 | -1039.84€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9469 | -0.035 | -175.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9469 | -0.035 | -175.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1014 | -0.017 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1014 | -0.017 | -18.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2242 | -0.046 | -28.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2242 | -0.046 | -28.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1012 | -0.021 | -30.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1012 | -0.021 | -30.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2691 | -0.023 | -29.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2691 | -0.023 | -29.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1322 | -0.062 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1322 | -0.062 | -29.21€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1188 | -0.036 | -39.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1188 | -0.036 | -39.26€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2473 | +0.118 | +978.23€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2337 | +0.122 | +965.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 537 | +0.140 | +275.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 537 | +0.140 | +275.54€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 487 | +0.118 | +173.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 487 | +0.118 | +173.41€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 422 | +0.127 | +193.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 422 | +0.127 | +193.85€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 400 | +0.132 | +191.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 400 | +0.132 | +191.83€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 491 | +0.090 | +131.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 491 | +0.090 | +131.01€ | 0 | 1 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2642 | -0.022 | -53.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2642 | -0.022 | -53.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 455 | +0.003 | +17.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 455 | +0.003 | +17.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 472 | -0.055 | -38.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 472 | -0.055 | -38.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 639 | -0.043 | -44.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 639 | -0.043 | -44.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 553 | -0.010 | -8.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 553 | -0.010 | -8.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 523 | -0.001 | +20.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 523 | -0.001 | +20.71€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 1090 | +0.043 | +97.25€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1090 | +0.043 | +97.25€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 361 | +0.018 | +4.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 361 | +0.018 | +4.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 83 | +0.029 | +3.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 83 | +0.029 | +3.15€ | 1 | 3 |
| ✅ STREAK_FADE_15M#SOL | 87 | +0.039 | +10.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 87 | +0.039 | +10.03€ | 2 | 3 |
| ✅ STREAK_FADE_15M#XRP | 559 | +0.061 | +79.33€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 559 | +0.061 | +79.33€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3707 | -0.022 | -139.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3707 | -0.022 | -139.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 638 | -0.025 | -25.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 638 | -0.025 | -25.16€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 191 | -0.039 | -14.67€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 191 | -0.039 | -14.67€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1748 | -0.018 | -59.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1748 | -0.018 | -59.78€ | 2 | 0 |
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
| ✅ STREAK_MOM_5M | 11807 | +0.013 | +62.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11807 | +0.013 | +62.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3035 | +0.017 | +21.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3035 | +0.017 | +21.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3166 | +0.012 | +24.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3166 | +0.012 | +24.53€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2980 | +0.008 | -1.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2980 | +0.008 | -1.87€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2626 | +0.014 | +18.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2626 | +0.014 | +18.86€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 14464 | +0.019 | +7.21€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 14464 | +0.019 | +7.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5807 | +0.021 | +6.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5807 | +0.021 | +6.34€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5187 | +0.020 | +4.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5187 | +0.020 | +4.65€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3470 | +0.014 | -3.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3470 | +0.014 | -3.78€ | 1 | 0 |
| ✅ UPDOWN_GBM | 130886 | +0.060 | +12535.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 32606 | +0.078 | +6376.87€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3718 | -0.000 | +40.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 86215 | +0.062 | +5984.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7898 | -0.002 | +137.25€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11489 | +0.104 | +2149.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2188 | +0.164 | +1024.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 9211 | +0.091 | +1126.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 29830 | +0.056 | +2612.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4455 | +0.080 | +1001.02€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1102 | +0.000 | +22.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 20549 | +0.065 | +1499.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3563 | -0.004 | +85.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 161 | -0.064 | +4.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14559 | +0.074 | +1599.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 12389 | +0.061 | +706.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 30875 | +0.049 | +2201.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7636 | +0.069 | +1178.54€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1064 | +0.006 | +15.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 19113 | +0.052 | +962.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2912 | -0.001 | +42.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 150 | -0.099 | +1.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26824 | +0.041 | +1570.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8766 | +0.034 | +507.19€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 979 | -0.011 | +7.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15569 | +0.054 | +1056.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1374 | +0.003 | +7.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 136 | -0.138 | -8.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 17307 | +0.074 | +2404.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7477 | +0.089 | +1772.00€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9384 | +0.065 | +632.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 49 | +0.010 | +1.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 447 | -0.099 | -2.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1131 | +0.362 | +431.69€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1131 | +0.362 | +431.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 543 | +0.361 | +192.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 543 | +0.361 | +192.93€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 588 | +0.363 | +238.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 588 | +0.363 | +238.76€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 30967 | -0.017 | +7763.73€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 30967 | -0.017 | +7763.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2485 | -0.046 | +651.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2485 | -0.046 | +651.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5745 | -0.115 | +343.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5745 | -0.115 | +343.01€ | 4 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4238 | +0.215 | +2655.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4238 | +0.215 | +2655.55€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8667 | -0.057 | +1310.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8667 | -0.057 | +1310.69€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8538 | -0.052 | +1740.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8538 | -0.052 | +1740.34€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 398 | +0.060 | +42.02€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 398 | +0.060 | +42.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 398 | +0.060 | +42.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 398 | +0.060 | +42.02€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 2063 | +0.285 | +1770.74€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 2063 | +0.285 | +1770.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1085 | +0.280 | +879.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1085 | +0.280 | +879.55€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 978 | +0.290 | +891.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 978 | +0.290 | +891.20€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 922 | -0.122 | -97.81€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 922 | -0.122 | -97.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 312 | -0.080 | -36.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 312 | -0.080 | -36.02€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 298 | -0.087 | -23.95€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 298 | -0.087 | -23.95€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 135 | -0.201 | -9.16€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 135 | -0.201 | -9.16€ | 6 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5611 | +0.291 | +2421.24€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2199 | +0.246 | +347.31€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2172 | +0.283 | +884.97€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1240 | +0.382 | +1188.96€ | 0 | 1 |