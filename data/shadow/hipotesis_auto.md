# Hipótesis automáticas — 2026-11-21 18:19 UTC
_Generado por shadow_postmortem.py sobre 1440158 resoluciones (PNL=+202738.51€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=729)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1088)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8121` → IC=+0.269 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8121 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.315` → IC=+0.192 (n=342)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.315 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=1114)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=518)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=951)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.180 (n=298)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 64.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8117` → IC=+0.269 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8117 (IC base=+0.125)

- **PATRÓN** `banda_z` > `8.502` → IC=+0.197 (n=298)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.502 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.134 (n=809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.129 (n=628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=1014)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8821.377` → IC=+0.133 (n=235)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 8821.377 (IC base=+0.014)

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
- **FILTRO** `restante_s_al_confirmar` < `130.45` → IC=-0.221 (n=12720)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.45
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=38163)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1271)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3813)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.280 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3819)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.44` → IC=-0.166 (n=3514)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.44
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=10544)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `148.13` → IC=-0.253 (n=3497)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 148.13
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10495)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.79` → IC=-0.268 (n=2339)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.79
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=7018)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=30098)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `7909.5457` → IC=+0.152 (n=2456)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7909.5457 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=26488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=32060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=24087)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=8751)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6344.8118` → IC=+0.140 (n=3417)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 6344.8118 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2715)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `16269.689` → IC=+0.180 (n=705)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 16269.689 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2773)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16052.1822` → IC=+0.185 (n=716)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16052.1822 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=2389)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.174 (n=664)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.61 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.153 (n=1555)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.44 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=5486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=2630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=3069)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.140 (n=706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=952)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.645` → IC=+0.234 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.645 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1188)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2056.0295` → IC=+0.141 (n=949)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2056.0295 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.251 (n=987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.428 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=749)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.144)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=483)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=483)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.047)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=1350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.136 (n=1033)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.255 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.125)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=78)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=26518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=22405)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=8428)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=6048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.162 (n=3821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 11.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.175 (n=5875)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.74 (IC base=+0.162)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=3708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=2474)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.246 (n=1788)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.205)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=5895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=4998)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.174 (n=6048)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=4637)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.252 (n=2263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1607)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=5762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=3663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1875)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.427 (n=1018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=1010)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `14027.0561` → IC=+0.449 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14027.0561 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.436 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.455 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `15331.2969` → IC=+0.443 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15331.2969 (IC base=+0.437)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.402 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.399)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.405 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.399)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.414 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.399)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=34603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=34245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.185 (n=5174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.177 (n=11127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=15981)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=14476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6164)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=5938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=12270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=5634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=5986)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=13190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4936)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=5760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=5842)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=12503)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=13574)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.29` → IC=+0.142 (n=11597)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.29 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6089)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=6164)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7694)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.79` → IC=+0.142 (n=7619)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.79 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6414)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=8200)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.93` → IC=+0.137 (n=7685)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.93 (IC base=+0.116)

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

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=1037)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

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
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.440 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.438)

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

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

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

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=69)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

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

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=69)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5058` → IC=+0.139 (n=19831)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5058 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=20085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=13806)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9749` → IC=+0.247 (n=6610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9749 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8597` → IC=+0.291 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8597 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.477` → IC=+0.190 (n=9957)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.477 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.696` → IC=+0.268 (n=5409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.696 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.256 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.742` → IC=+0.233 (n=4790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.742 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=9627)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4849.6034` → IC=+0.151 (n=6610)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4849.6034 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.123 (n=12531)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0065 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.564` → IC=+0.146 (n=25056)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.564 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6674` → IC=+0.190 (n=1667)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6674 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1753` → IC=+0.195 (n=10255)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1753 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8573` → IC=+0.196 (n=6958)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8573 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.233 (n=2539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.2817` → IC=+0.213 (n=8016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2817 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=17656)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.243 (n=1406)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3026` → IC=+0.214 (n=3706)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3026 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=2041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2824)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9825` → IC=+0.274 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9825 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.441` → IC=+0.276 (n=1883)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.441 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2347` → IC=+0.259 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2347 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4412` → IC=+0.211 (n=4044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4412 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2043.4993` → IC=+0.215 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.4993 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.219 (n=3437)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.246 (n=2543)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.270 (n=1269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=3966)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=1739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0762` → IC=+0.281 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0762 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.243 (n=3285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.251 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8591` → IC=+0.245 (n=2430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8591 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.244 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.233 (n=1207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.222 (n=1202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1138` → IC=+0.247 (n=1583)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1138 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.257 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.1998` → IC=+0.232 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1998 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` < `0.5638` → IC=+0.222 (n=3974)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5638 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.75` → IC=+0.265 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.75 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.229 (n=3212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6975 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.268 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.249 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.152 (n=3945)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0069 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0826` → IC=+0.159 (n=1315)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0826 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7085` → IC=+0.172 (n=3943)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7085 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.151 (n=3874)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.944` → IC=+0.142 (n=3622)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.944 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.153 (n=1316)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6279 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.160 (n=1432)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4462` → IC=+0.143 (n=3813)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4462 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5124)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.185 (n=1263)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 167.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.204 (n=2026)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.254 (n=1719)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.916` → IC=+0.281 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.916 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.192 (n=4009)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.35` → IC=+0.223 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.35 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7283` → IC=+0.208 (n=1979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7283 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=5437)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1905.7248` → IC=+0.198 (n=2025)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1905.7248 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.223 (n=3682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.4656` → IC=+0.226 (n=3680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4656 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.227 (n=1897)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.049` → IC=+0.272 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.049 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.731` → IC=+0.270 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.731 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.256 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.151` → IC=+0.232 (n=2692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.151 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1889.1356` → IC=+0.223 (n=1896)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1889.1356 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.224 (n=4025)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.170 (n=237)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5398)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.146 (n=726)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.004 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.251 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.155` → IC=+0.348 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.155 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.5884` → IC=+0.344 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5884 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.174` → IC=+0.214 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.174 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `1.1139` → IC=+0.363 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1139 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` < `0.167` → IC=+0.347 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.167 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.352 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.359 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `2.2799` → IC=+0.350 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2799 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.350 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.0875` → IC=+0.190 (n=1409)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0875 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.3614` → IC=+0.153 (n=701)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.3614 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1504` → IC=+0.158 (n=2633)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1504 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8287` → IC=+0.162 (n=1848)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8287 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.201 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.4319` → IC=+0.173 (n=890)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.4319 (IC base=+0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.189 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=867)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.173 (n=255)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=771)

- **FILTRO** `ibs_20min` > `0.1951` → IC=-0.127 (n=5287)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1951
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2609)

- **FILTRO** `sigma_ewma_delta_pct` > `8.285` → IC=-0.234 (n=852)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.285
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=7044)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.175 (n=352)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.75 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.276 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.6061` → IC=+0.264 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6061 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.881` → IC=+0.160 (n=239)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.881 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `0.6205` → IC=+0.285 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6205 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.280 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.288 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.260 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.269 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.1951` → IC=+0.159 (n=2609)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1951 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.235` → IC=+0.290 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.235 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.8249` → IC=+0.290 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8249 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` < `0.6921` → IC=+0.299 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6921 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` > `1.0428` → IC=+0.293 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0428 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0782` → IC=+0.316 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0782 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.302 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.417` → IC=+0.297 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.417 (IC base=-0.032)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7998` → IC=-0.158 (n=4072)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7998
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=2098)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.179 (n=1258)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4912)

- **FILTRO** `ibs_20min` > `0.7259` → IC=-0.190 (n=2130)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7259
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=6392)

- **PATRÓN** `ibs_20min` > `0.7998` → IC=+0.142 (n=2098)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.7998 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.4517` → IC=+0.346 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4517 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7044` → IC=+0.319 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7044 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3064` → IC=+0.318 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3064 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5309` → IC=+0.324 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5309 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.0999` → IC=+0.286 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0999 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` < `0.231` → IC=+0.263 (n=2525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.231 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.7188` → IC=+0.272 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7188 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.2105` → IC=+0.280 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2105 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.282 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `2.4813` → IC=+0.264 (n=2402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4813 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.270 (n=2402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.188 (n=8680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0111 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.8657` → IC=+0.284 (n=11798)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8657 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.9936` → IC=+0.300 (n=1787)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9936 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.464` → IC=+0.167 (n=11730)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.464 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.278 (n=8628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.296 (n=2140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.6413` → IC=+0.288 (n=5029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6413 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.308 (n=14745)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.153 (n=11466)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0092 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.5161` → IC=+0.174 (n=22257)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5161 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2012` → IC=+0.283 (n=8588)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2012 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.279 (n=5733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8585 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.1887` → IC=+0.285 (n=2866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1887 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.322 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.4526` → IC=+0.303 (n=4263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4526 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.2697` → IC=+0.304 (n=5796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2697 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.312 (n=12795)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.088)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8122` → IC=-0.145 (n=4609)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8122
  - _Potencial_: sin este filtro IC_bueno=+0.309 (n=2375)

- **FILTRO** `ibs_20min` > `0.7` → IC=-0.238 (n=1569)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4715)

- **FILTRO** `sigma_ewma_delta_pct` > `4.062` → IC=-0.240 (n=1323)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.062
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=4961)

- **PATRÓN** `ibs_20min` > `0.8122` → IC=+0.309 (n=2375)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8122 (IC base=+0.010)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.142` → IC=+0.173 (n=2607)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 2.142 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.335 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4454` → IC=+0.288 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4454 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.2311` → IC=+0.314 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2311 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.320 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.010)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.173 (n=1574)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1702 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1562` → IC=+0.390 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1562 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.6693` → IC=+0.394 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6693 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1799` → IC=+0.226 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1799 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.219 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2739` → IC=+0.246 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2739 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4146` → IC=+0.228 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4146 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4483` → IC=+0.221 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4483 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `370.0` → IC=+0.231 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 370.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.1527` → IC=+0.264 (n=1955)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1527 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.0179` → IC=+0.265 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0179 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.292 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.257 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.262 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `197.0` → IC=+0.276 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 197.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.317 (n=1622)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.586` → IC=+0.305 (n=2426)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.586 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1307` → IC=+0.292 (n=3329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1307 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2462` → IC=+0.300 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2462 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.291 (n=4325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2017.84` → IC=+0.296 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2017.84 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.301 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.335 (n=2222)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1874` → IC=+0.328 (n=1465)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1874 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=1274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.0286` → IC=+0.308 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0286 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1532` → IC=+0.318 (n=2218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1532 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.064` → IC=+0.318 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.064 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1987` → IC=+0.309 (n=3305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1987 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3441` → IC=+0.316 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3441 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7396` → IC=+0.325 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7396 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `2004.1719` → IC=+0.316 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.1719 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.312 (n=2239)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7131` → IC=-0.171 (n=1638)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7131
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=4915)

- **PATRÓN** `dist_vwap_pct` > `0.1568` → IC=+0.236 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1568 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.6234` → IC=+0.236 (n=2605)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6234 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1683` → IC=+0.236 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1683 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.5961` → IC=+0.234 (n=2364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5961 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.236 (n=2483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1031` → IC=+0.243 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1031 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4161` → IC=+0.241 (n=2297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4161 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4963` → IC=+0.235 (n=2051)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4963 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.252 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.0913` → IC=+0.153 (n=1639)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0913 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.6099` → IC=+0.260 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6099 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1804` → IC=+0.263 (n=1726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1804 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6137` → IC=+0.258 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6137 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` < `0.1016` → IC=+0.265 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1016 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.1623` → IC=+0.284 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1623 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.7847` → IC=+0.282 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7847 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.4239` → IC=+0.277 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4239 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.282 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.012)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.246 (n=2676)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2685)

- **FILTRO** `ibs_20min` > `0.6087` → IC=-0.238 (n=1260)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6087
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=3803)

- **FILTRO** `sigma_ewma_delta_pct` > `8.256` → IC=-0.266 (n=579)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.256
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=4484)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.313 (n=2685)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `1.1064` → IC=+0.349 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1064 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.445` → IC=+0.157 (n=2193)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.445 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8453` → IC=+0.348 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8453 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `0.6972` → IC=+0.334 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6972 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.336 (n=1849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.366 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.782` → IC=+0.353 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.782 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.353 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.6087` → IC=+0.165 (n=3803)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.6087 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.3254` → IC=+0.274 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3254 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.728` → IC=+0.132 (n=3967)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.728 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.6897` → IC=+0.286 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6897 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0714` → IC=+0.300 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0714 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `2.1231` → IC=+0.280 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1231 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.291 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.065)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.353 (n=2497)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=2822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=2796)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.6512` → IC=+0.338 (n=2795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6512 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2196` → IC=+0.337 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2196 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.305` → IC=+0.340 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.305 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.6286` → IC=+0.325 (n=2795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6286 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.346 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.5318` → IC=+0.325 (n=2412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5318 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `3008.2531` → IC=+0.323 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3008.2531 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0142` → IC=+0.349 (n=2012)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0142 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=3029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.3889` → IC=+0.328 (n=3019)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3889 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.2931` → IC=+0.320 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2931 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2563` → IC=+0.316 (n=2978)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2563 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.181` → IC=+0.326 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.181 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.7164` → IC=+0.314 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7164 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2096` → IC=+0.339 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2096 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.364 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.323 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.15` → IC=+0.317 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.15 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.220 (n=6355)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1263` → IC=+0.193 (n=8381)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1263 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=19807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.229 (n=19045)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5357 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1691` → IC=+0.207 (n=7174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1691 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.255 (n=4984)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1747` → IC=+0.152 (n=12698)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1747 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6212` → IC=+0.151 (n=12697)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6212 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.206 (n=2746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5975` → IC=+0.184 (n=6180)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5975 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=17995)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 85.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.194 (n=8356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0061 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.186 (n=12675)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0082 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.221 (n=6332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=9097)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.247 (n=16737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1947` → IC=+0.180 (n=13890)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1947 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.44` → IC=+0.190 (n=2999)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.44 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.495` → IC=+0.192 (n=16956)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.495 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.7008` → IC=+0.172 (n=5922)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.7008 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.220 (n=2853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6331` → IC=+0.198 (n=6051)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6331 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=17962)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.263 (n=1042)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.1068` → IC=+0.260 (n=1375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1068 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=2122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.293 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.469` → IC=+0.328 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.469 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2317` → IC=+0.282 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2317 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8312` → IC=+0.227 (n=1991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8312 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4364` → IC=+0.227 (n=2986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4364 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.256 (n=2631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.254)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.263 (n=1754)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.1009` → IC=+0.307 (n=1160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1009 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=2713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=2399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.4408` → IC=+0.271 (n=2629)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4408 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.943` → IC=+0.258 (n=2597)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.943 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1005` → IC=+0.257 (n=2318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1005 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.268 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.5521` → IC=+0.264 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5521 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.6917` → IC=+0.257 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6917 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.262 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.188 (n=974)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0033 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.175 (n=973)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=3044)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2519` → IC=+0.204 (n=2911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2519 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.194` → IC=+0.211 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.194 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.571` → IC=+0.205 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.571 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8532` → IC=+0.133 (n=1941)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8532 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0477` → IC=+0.132 (n=1320)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.0477 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.171 (n=445)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5074` → IC=+0.129 (n=1261)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5074 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4558` → IC=+0.142 (n=955)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4558 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `389.0` → IC=+0.132 (n=2834)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 389.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.174 (n=3145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0069 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2543` → IC=+0.175 (n=2767)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2543 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=1499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6123` → IC=+0.211 (n=3144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6123 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2171` → IC=+0.177 (n=3419)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2171 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.904` → IC=+0.177 (n=581)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.904 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.157 (n=2759)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2077` → IC=+0.163 (n=3144)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2077 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0719` → IC=+0.155 (n=2625)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0719 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4807` → IC=+0.157 (n=3016)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4807 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.193 (n=1309)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 204.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.224 (n=1460)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.2567` → IC=+0.232 (n=2147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2567 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=1706)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.04` → IC=+0.305 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.04 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.35` → IC=+0.235 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.35 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.222 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=3915)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2012.7984` → IC=+0.221 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2012.7984 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.245 (n=2907)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0122 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.2537` → IC=+0.267 (n=1937)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2537 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.277 (n=1096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0409` → IC=+0.296 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0409 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.854` → IC=+0.288 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.854 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3531` → IC=+0.286 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3531 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7655` → IC=+0.241 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7655 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1746` → IC=+0.254 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1746 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1881.9767` → IC=+0.251 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.9767 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.238 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.194 (n=1050)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.172 (n=1050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2442` → IC=+0.188 (n=3144)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2442 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.187 (n=1773)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1481 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.235` → IC=+0.202 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.235 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8369` → IC=+0.139 (n=2096)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8369 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.175 (n=472)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.126 (n=1354)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5013` → IC=+0.135 (n=1026)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.5013 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6943.592` → IC=+0.196 (n=1425)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6943.592 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.127 (n=3089)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 123.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.160 (n=2963)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0071 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4295` → IC=+0.149 (n=3367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4295 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1613)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6687` → IC=+0.189 (n=3367)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6687 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1698` → IC=+0.157 (n=3446)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1698 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.531` → IC=+0.141 (n=1149)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.531 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.064` → IC=+0.133 (n=3000)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.064 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8532` → IC=+0.150 (n=2245)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8532 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.172 (n=508)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1884` → IC=+0.134 (n=2821)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1884 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.411` → IC=+0.135 (n=3205)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.411 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6675.8703` → IC=+0.190 (n=1526)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6675.8703 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.155 (n=1091)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.175 (n=1172)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0129 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=3603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.5938` → IC=+0.224 (n=3126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5938 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7942` → IC=+0.216 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7942 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.015` → IC=+0.285 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.015 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1682` → IC=+0.132 (n=3499)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1682 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6269` → IC=+0.124 (n=3498)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6269 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.125 (n=3573)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.7875` → IC=+0.127 (n=2264)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7875 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2711.6854` → IC=+0.197 (n=1586)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2711.6854 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.129 (n=2238)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.150 (n=3233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0111 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.166 (n=1224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.4878` → IC=+0.239 (n=3232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4878 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2261` → IC=+0.147 (n=3654)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2261 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.232` → IC=+0.146 (n=3248)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.232 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.182` → IC=+0.130 (n=3672)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.182 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.859` → IC=+0.126 (n=2448)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.859 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.127 (n=3633)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2766` → IC=+0.150 (n=510)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2766 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4379` → IC=+0.142 (n=1163)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4379 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4431` → IC=+0.135 (n=1163)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4431 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2612.6775` → IC=+0.189 (n=1665)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2612.6775 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.130 (n=3488)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 43.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.245 (n=3144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.169` → IC=+0.241 (n=1384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.169 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=3271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2846)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6648` → IC=+0.255 (n=3144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6648 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1858` → IC=+0.234 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1858 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8293` → IC=+0.228 (n=3242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8293 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.489` → IC=+0.270 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.489 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.236 (n=3144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.267 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.1602` → IC=+0.229 (n=2701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1602 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8259` → IC=+0.228 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8259 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2627.6354` → IC=+0.232 (n=2096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2627.6354 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0165` → IC=+0.248 (n=2186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0165 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6165` → IC=+0.247 (n=3277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6165 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.241 (n=1474)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0381` → IC=+0.297 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0381 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `1.1734` → IC=+0.246 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1734 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.047` → IC=+0.273 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.047 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8673` → IC=+0.240 (n=2185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8673 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0472` → IC=+0.243 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0472 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.293 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8474` → IC=+0.237 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8474 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5546` → IC=+0.238 (n=2774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5546 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.203 (n=1681)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.144` → IC=+0.172 (n=2208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.144 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=5238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.661` → IC=+0.222 (n=3341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.661 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.9008` → IC=+0.183 (n=768)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.9008 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.536` → IC=+0.210 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.536 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.857` → IC=+0.165 (n=3039)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.857 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.1902` → IC=+0.158 (n=1519)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1902 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.170 (n=1296)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.5251` → IC=+0.160 (n=2152)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5251 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=5531)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `7218.9654` → IC=+0.194 (n=2272)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7218.9654 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.3876` → IC=+0.178 (n=3646)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.3876 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.147 (n=2409)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 22.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.206 (n=1202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.105` → IC=+0.233 (n=529)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.105 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.229 (n=1085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.6259` → IC=+0.260 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6259 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3229` → IC=+0.230 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3229 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.927` → IC=+0.226 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.927 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.7008` → IC=+0.225 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7008 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.1483` → IC=+0.198 (n=1263)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.1483 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.212 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.210 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `13762.5784` → IC=+0.205 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13762.5784 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.156 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0032 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2186` → IC=+0.191 (n=661)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.2186 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.163 (n=651)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 171.0 (IC base=+0.069)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.238 (n=514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1328` → IC=+0.160 (n=678)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1328 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.7716` → IC=+0.262 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7716 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1555` → IC=+0.170 (n=735)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1555 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.947` → IC=+0.186 (n=218)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.947 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.160 (n=1029)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8331 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2177` → IC=+0.185 (n=271)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2177 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.4608` → IC=+0.168 (n=507)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4608 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `7912.0475` → IC=+0.179 (n=699)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 7912.0475 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.149 (n=514)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 30.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.137 (n=676)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0044 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.1836` → IC=+0.202 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1836 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `0.6746` → IC=+0.142 (n=676)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6746 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.0768` → IC=+0.126 (n=562)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0768 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `5613.8653` → IC=+0.150 (n=1023)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5613.8653 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.150 (n=664)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 40.0 (IC base=+0.108)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5319` → IC=+0.182 (n=1221)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.5319 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0409` → IC=+0.157 (n=240)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 1.0409 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.885` → IC=+0.213 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.885 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.0462` → IC=+0.126 (n=1203)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0462 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.136 (n=234)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4134` → IC=+0.149 (n=443)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4134 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `3060.3888` → IC=+0.151 (n=456)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3060.3888 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.551` → IC=+0.170 (n=1323)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.551 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2773.9701` → IC=+0.165 (n=682)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2773.9701 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.121 (n=1013)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 19.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.238 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5179` → IC=+0.196 (n=402)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5179 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.931` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.931 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.507` → IC=+0.193 (n=450)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 5.507 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1731` → IC=+0.188 (n=446)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1731 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.1265` → IC=+0.195 (n=369)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1265 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.191 (n=474)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.03 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.202 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.178 (n=225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0225 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.3414` → IC=+0.164 (n=331)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3414 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.161 (n=334)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.35 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.1049` → IC=+0.163 (n=496)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.1049 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.987` → IC=+0.158 (n=481)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 2.987 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8885` → IC=+0.191 (n=331)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8885 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.172 (n=461)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2375` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2375 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `2694.7519` → IC=+0.158 (n=331)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2694.7519 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.172 (n=476)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 20.0 (IC base=+0.156)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.227 (n=8384)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=26259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9669` → IC=+0.302 (n=8375)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9669 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9401` → IC=+0.218 (n=2891)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9401 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.93` → IC=+0.261 (n=6154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.93 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2138` → IC=+0.160 (n=16939)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2138 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.216 (n=3299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6239` → IC=+0.193 (n=8185)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6239 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=23759)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.207 (n=7795)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3978` → IC=+0.200 (n=20562)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3978 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=8719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.253 (n=20566)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1895` → IC=+0.182 (n=14943)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1895 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.347` → IC=+0.204 (n=22853)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.347 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0532` → IC=+0.174 (n=13784)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0532 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.256 (n=3213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6211` → IC=+0.211 (n=7490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6211 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=22262)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.274 (n=1337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3769` → IC=+0.235 (n=4007)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3769 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=4211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8607` → IC=+0.293 (n=2671)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8607 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.031` → IC=+0.300 (n=2630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.031 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.288 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2898` → IC=+0.239 (n=1759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2898 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2043.0977` → IC=+0.240 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.0977 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.267 (n=3661)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.268 (n=2439)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1274` → IC=+0.292 (n=1611)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1274 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=3807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.270 (n=3298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.4656` → IC=+0.287 (n=3219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4656 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.269 (n=3334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.285 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5659` → IC=+0.267 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5659 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6471` → IC=+0.274 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6471 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.272 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.173 (n=1379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0822` → IC=+0.148 (n=1377)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0822 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.3023` → IC=+0.202 (n=3691)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3023 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3435` → IC=+0.202 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3435 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.275` → IC=+0.171 (n=862)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.275 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6348` → IC=+0.155 (n=1377)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6348 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.2255` → IC=+0.146 (n=1377)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.2255 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.192 (n=579)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.144 (n=3574)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5193` → IC=+0.145 (n=3629)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5193 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.152 (n=2679)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 290.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.171 (n=3218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.006 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0833` → IC=+0.176 (n=1219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0833 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6808` → IC=+0.191 (n=3655)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6808 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1534` → IC=+0.162 (n=3606)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1534 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.206` → IC=+0.150 (n=3729)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.206 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0414` → IC=+0.156 (n=3217)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0414 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2211` → IC=+0.196 (n=666)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2211 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.150 (n=3544)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.152 (n=2363)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=4747)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.178 (n=1156)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 212.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.238 (n=1394)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=4389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.314 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.234 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.7509` → IC=+0.239 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7509 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5081)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `1904.2584` → IC=+0.234 (n=1895)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.2584 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.248 (n=3559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1852` → IC=+0.259 (n=1780)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1852 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1841)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.0667` → IC=+0.300 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0667 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.961` → IC=+0.304 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.961 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.300 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.1698` → IC=+0.257 (n=2609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1698 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1999.8384` → IC=+0.253 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.8384 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.248 (n=3452)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.244)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.191 (n=1455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3544` → IC=+0.147 (n=3827)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3544 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8787` → IC=+0.269 (n=1450)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8787 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1482` → IC=+0.166 (n=2147)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1482 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.194` → IC=+0.169 (n=869)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.194 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8575` → IC=+0.154 (n=2899)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8575 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.201 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5167` → IC=+0.156 (n=1870)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5167 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1528` → IC=+0.143 (n=1927)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1528 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5838.1861` → IC=+0.232 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5838.1861 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.143 (n=2838)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.174 (n=3239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0071 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.459` → IC=+0.159 (n=3676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.459 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=1350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5704` → IC=+0.213 (n=3235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5704 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.6296` → IC=+0.157 (n=4261)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6296 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.019` → IC=+0.151 (n=735)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 9.019 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.014` → IC=+0.154 (n=3202)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.014 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.162 (n=2451)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.852 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.207 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1974` → IC=+0.153 (n=3135)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1974 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.524` → IC=+0.157 (n=3182)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.524 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6728.8499` → IC=+0.214 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6728.8499 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.171 (n=1236)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.158 (n=1481)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0131 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=3131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.697` → IC=+0.256 (n=2946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.697 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0518` → IC=+0.207 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0518 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.242` → IC=+0.270 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.242 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2118` → IC=+0.127 (n=4419)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2118 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.123 (n=4208)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.134 (n=553)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5568` → IC=+0.134 (n=1898)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.5568 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2476.871` → IC=+0.223 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2476.871 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.160 (n=3629)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0112 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1427` → IC=+0.151 (n=1376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1427 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=1947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5385` → IC=+0.247 (n=3629)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5385 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.224` → IC=+0.153 (n=3807)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.224 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.039` → IC=+0.161 (n=4001)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.039 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6376` → IC=+0.154 (n=1376)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6376 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.203 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.164 (n=1312)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4777` → IC=+0.142 (n=1312)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4777 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2653.9292` → IC=+0.221 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2653.9292 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.151 (n=3954)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 48.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.256 (n=4044)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=4230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=2708)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.306 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.2027` → IC=+0.252 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2027 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.051` → IC=+0.295 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.051 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2144` → IC=+0.237 (n=4043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2144 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6423` → IC=+0.243 (n=4043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6423 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.255 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5086` → IC=+0.256 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5086 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `3000.832` → IC=+0.238 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3000.832 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0249` → IC=+0.270 (n=1406)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0249 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=3963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.1371` → IC=+0.306 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1371 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `1.1802` → IC=+0.246 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1802 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` < `0.2305` → IC=+0.249 (n=4053)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2305 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.993` → IC=+0.279 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.993 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` < `0.7152` → IC=+0.246 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7152 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` > `1.2193` → IC=+0.265 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2193 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.310 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `1.4335` → IC=+0.248 (n=3993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4335 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `2986.5184` → IC=+0.245 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2986.5184 (IC base=+0.243)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.240 (n=2407)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.5376` → IC=+0.231 (n=7214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5376 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=7259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9296` → IC=+0.259 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9296 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.9468` → IC=+0.225 (n=5886)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9468 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.464` → IC=+0.232 (n=2397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.464 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.7069` → IC=+0.229 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7069 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.881` → IC=+0.224 (n=3398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.881 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.1041` → IC=+0.223 (n=6758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1041 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.231 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.234 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=5163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3729.5434` → IC=+0.231 (n=4808)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3729.5434 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.229 (n=1708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.5336` → IC=+0.220 (n=5110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5336 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.222 (n=1998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=2284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.7282` → IC=+0.218 (n=5110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7282 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.7012` → IC=+0.218 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7012 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.4385` → IC=+0.205 (n=4956)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4385 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.739` → IC=+0.225 (n=4637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.739 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.0965` → IC=+0.214 (n=4093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0965 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.214 (n=4723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5312` → IC=+0.215 (n=2216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5312 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.1876` → IC=+0.222 (n=2282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1876 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.237 (n=3377)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.212)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.280 (n=833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.302 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.4633` → IC=+0.285 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4633 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.5266` → IC=+0.280 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5266 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `1.2271` → IC=+0.275 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2271 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `0.8769` → IC=+0.288 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8769 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.341 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.4917` → IC=+0.278 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4917 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `12913.0263` → IC=+0.282 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12913.0263 (IC base=+0.270)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3879` → IC=+0.188 (n=1542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3879 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.178 (n=579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.192 (n=680)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.3612` → IC=+0.179 (n=331)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.3612 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.5553` → IC=+0.173 (n=1849)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.5553 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.195 (n=1514)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.186 (n=1357)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.091 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.188 (n=472)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.191 (n=512)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.177 (n=695)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.1732 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `14608.6008` → IC=+0.175 (n=699)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 14608.6008 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `698.0` → IC=+0.188 (n=1496)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 698.0 (IC base=+0.173)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `drift_60min` |x|≤ `0.6167` → IC=+0.215 (n=1057)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6167 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.7078` → IC=+0.211 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7078 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.988` → IC=+0.251 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.988 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.32` → IC=+0.245 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.32 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2054` → IC=+0.245 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2054 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.7962` → IC=+0.215 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7962 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.218 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0179` → IC=+0.371 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0179 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.389 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.4483` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4483 (IC base=+0.288)

- **PATRÓN** `ibs_20min` > `0.1912` → IC=+0.309 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1912 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.341` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.341 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.368` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.368 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `1.6184` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6184 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `1.8484` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8484 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 5.0 (IC base=+0.288)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.221 (n=1944)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.4686` → IC=+0.218 (n=1943)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4686 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.4751` → IC=+0.221 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4751 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.147` → IC=+0.212 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.147 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.412` → IC=+0.223 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.412 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.948` → IC=+0.220 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.948 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.8665` → IC=+0.216 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8665 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.213 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.0745` → IC=+0.211 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0745 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `2.1237` → IC=+0.217 (n=1669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1237 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4929` → IC=+0.212 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4929 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.240 (n=521)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.511` → IC=+0.222 (n=1559)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.511 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.213 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.218 (n=1114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.0853` → IC=+0.212 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0853 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.6804` → IC=+0.219 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6804 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.4251` → IC=+0.207 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4251 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.261` → IC=+0.211 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.261 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2588` → IC=+0.214 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2588 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.208 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7214 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.231 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.5069` → IC=+0.209 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5069 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7691` → IC=+0.209 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7691 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `7851.8902` → IC=+0.217 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7851.8902 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.210 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.207)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.227 (n=845)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.221 (n=575)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=1192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.214 (n=1164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.295 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `1.1073` → IC=+0.244 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1073 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.218` → IC=+0.249 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.218 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.246 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.2457` → IC=+0.213 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2457 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.216 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.230 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `2.1576` → IC=+0.223 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1576 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `4456.3994` → IC=+0.246 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4456.3994 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.258 (n=630)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.248)

- **PATRÓN** `drift_60min` |x|≤ `0.6877` → IC=+0.262 (n=944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6877 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=877)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.269 (n=648)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.248)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.272 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` > `0.6007` → IC=+0.252 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6007 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` < `1.2199` → IC=+0.255 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.2199 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.987` → IC=+0.267 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.987 (IC base=+0.248)

- **PATRÓN** `volumen_regimen` < `0.6688` → IC=+0.263 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6688 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.259 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.276 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.248)

- **PATRÓN** `libro_liquidez` > `4596.385` → IC=+0.279 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4596.385 (IC base=+0.248)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.280 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.248)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.149 (n=874)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0041 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.187 (n=1693)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.75 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.147 (n=1203)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.451` → IC=+0.144 (n=552)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.451 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.5922` → IC=+0.165 (n=1918)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.5922 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.175 (n=540)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.082)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5427` → IC=-0.122 (n=331)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5427
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=675)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.175 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0029 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.159 (n=675)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5427 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.162 (n=353)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.066)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.131 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0036 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.248 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.142 (n=300)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.052)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5205` → IC=-0.121 (n=344)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5205
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=699)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.154 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0043 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.5205` → IC=+0.159 (n=699)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5205 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1344` → IC=+0.156 (n=376)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1344 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.791` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.791 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.0953` → IC=+0.278 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0953 (IC base=+0.042)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9861` → IC=+0.199 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9861 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.7504` → IC=+0.162 (n=208)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.7504 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.168 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.01 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.192 (n=550)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.2139` → IC=+0.151 (n=546)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2139 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.064` → IC=+0.234 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.064 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.1218` → IC=+0.190 (n=182)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.1218 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.1089` → IC=+0.175 (n=204)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1089 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `2.1886` → IC=+0.131 (n=453)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.1886 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `1.4564` → IC=+0.140 (n=514)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4564 (IC base=+0.100)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.318 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.6977` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6977 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `1.0069` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0069 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.21` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.21 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.328` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.328 (IC base=+0.292)

- **PATRÓN** `volumen_regimen` < `0.7856` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7856 (IC base=+0.292)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.8927` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8927 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.1829` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1829 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `34.6896` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 34.6896 (IC base=+0.292)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.333 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.325)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.346 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.325)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.452 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.325)

- **PATRÓN** `ibs_20min` < `0.1481` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1481 (IC base=+0.325)

- **PATRÓN** `ibs_20min` > `0.3556` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3556 (IC base=+0.325)

- **PATRÓN** `volumen_regimen` > `0.6564` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6564 (IC base=+0.325)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.325)

- **PATRÓN** `volumen_spike_ratio` < `1.5212` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5212 (IC base=+0.325)

- **PATRÓN** `volumen_spike_ratio` > `2.0251` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0251 (IC base=+0.325)

- **PATRÓN** `libro_liquidez` > `37.2` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 37.2 (IC base=+0.325)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0061` → IC=-0.248 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0061
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=204)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=310)

- **FILTRO** `volumen_regimen` < `0.871` → IC=-0.309 (n=134)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.871
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=274)

- **FILTRO** `sigma_h` < `0.0073` → IC=-0.285 (n=273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=92)

- **FILTRO** `dist_vwap_pct` > `0.4617` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4617
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=337)

- **FILTRO** `sigma_ewma_delta_pct` > `9.308` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.308
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=335)

- **FILTRO** `volumen_pendiente_norm` > `0.046` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=240)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=94)

- **FILTRO** `volumen_regimen` < `0.892` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.892
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=93)

- **FILTRO** `drift_60min` |x|> `0.1665` → IC=-0.316 (n=36)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1665
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

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
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=100)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=103)

- **FILTRO** `volumen_spike_ratio` < `1.4481` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4481
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=77)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=122)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.368 (n=36)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=110)

- **FILTRO** `volumen_pendiente_norm` > `0.1194` → IC=-0.278 (n=34)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1194
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=87)

- **FILTRO** `sigma_h` < `0.0123` → IC=-0.304 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `sigma_ewma_delta_pct` > `4.378` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.378
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=50)

- **FILTRO** `volumen_regimen` < `0.9175` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9175
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=45)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2365` → IC=-0.151 (n=313)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2365
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=943)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.261 (n=371)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.202 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.842` → IC=+0.321 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.842 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.432` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.432 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.416` → IC=+0.166 (n=832)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 8.416 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.193 (n=272)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6242 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.0678` → IC=+0.191 (n=613)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0678 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.4082` → IC=+0.207 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4082 (IC base=+0.165)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7306` → IC=-0.171 (n=77)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7306
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=234)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.163 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0066 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.7306` → IC=+0.136 (n=234)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7306 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.6492` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6492 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.242` → IC=+0.135 (n=433)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.242 (IC base=+0.074)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.178 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0072 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.139 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.7994` → IC=+0.185 (n=236)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7994 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.8076` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.8076 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1088` → IC=+0.156 (n=216)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1088 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.154 (n=273)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6229 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1865` → IC=+0.178 (n=88)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.1865 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.1803` → IC=+0.155 (n=282)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1803 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.7165` → IC=+0.188 (n=158)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.7165 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=+0.003)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.15` → IC=-0.240 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=149)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.283 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.294 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.265)

- **PATRÓN** `dist_vwap_pct` > `0.7481` → IC=+0.397 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7481 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.265)

- **PATRÓN** `volumen_regimen` < `0.7943` → IC=+0.295 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7943 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.315 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.329 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.0595` → IC=+0.300 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0595 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.271 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.265)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=184)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.337)

- **PATRÓN** `elapsed_s` > `208.4` → IC=+0.389 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.4 (IC base=+0.337)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `0.6648` → IC=+0.390 (n=98)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6648 (IC base=+0.337)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.392 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.337)

- **PATRÓN** `ballena_activa_n` < `1046.0` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1046.0 (IC base=+0.337)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3507` → IC=+0.303 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3507 (IC base=+0.293)

- **PATRÓN** `elapsed_s` > `230.8` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.8 (IC base=+0.293)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.330 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.9468` → IC=+0.315 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9468 (IC base=+0.293)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.333 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `1325.0` → IC=+0.384 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1325.0 (IC base=+0.293)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=184)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.337)

- **PATRÓN** `elapsed_s` > `208.4` → IC=+0.389 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.4 (IC base=+0.337)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `0.6648` → IC=+0.390 (n=98)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6648 (IC base=+0.337)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.392 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.337)

- **PATRÓN** `ballena_activa_n` < `1046.0` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1046.0 (IC base=+0.337)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3507` → IC=+0.303 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3507 (IC base=+0.293)

- **PATRÓN** `elapsed_s` > `230.8` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.8 (IC base=+0.293)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.330 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.9468` → IC=+0.315 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9468 (IC base=+0.293)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.333 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `1325.0` → IC=+0.384 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1325.0 (IC base=+0.293)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=287)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=232)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=287)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=1384)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.171 (n=77)

  - _Acción_: Kelly boost +0.85€ cuando `liq_n` > 2.0 (IC base=+0.084)

- **PATRÓN** `liq_usd_total` > `1042.48` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `liq_usd_total` > 1042.48 (IC base=+0.084)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.136 (n=75)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` > 0.5 (IC base=+0.084)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.03 (IC base=+0.084)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11686.6395` → IC=-0.167 (n=40)

  - _Acción_: SKIP cuando `libro_liquidez` < 11686.6395
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=120)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=82)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=90)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.179 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 10.0 (IC base=+0.098)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.5 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `1870.8824` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1870.8824 (IC base=+0.098)

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
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=276)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4193)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=235)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=192)

- **FILTRO** `ballena_activa_n` > `69.0` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `ballena_activa_n` > 69.0
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=147)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.151 (n=147)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 69.0 (IC base=+0.004)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.135 (n=288)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.183)

- **PATRÓN** `liq_usd_total` > `1165.64` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1165.64 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.199 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.227 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.194 (n=109)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.03 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `3279.111` → IC=+0.200 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3279.111 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 14.0 (IC base=+0.183)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1638)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1592)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `ballena_activa_n` > `133.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 133.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=748)

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
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1124)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1124)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1497)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1497)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=347)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=347)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.138 (n=114)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=248)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=405)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=454)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=331)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=431)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=431)

- **FILTRO** `libro_liquidez` < `693.7144` → IC=-0.130 (n=152)

  - _Acción_: SKIP cuando `libro_liquidez` < 693.7144
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=309)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=421)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.125 (n=3436)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=8954)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=91)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.133 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=142)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=88)

- **FILTRO** `restante_min` < `3.99` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `lag_apertura_s` > `60.89` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.89
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.152 (n=409)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1002)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.151 (n=330)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=882)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.146 (n=419)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.51 (IC base=-0.008)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=194)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=440)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.120 (n=480)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=498)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.133 (n=330)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.51 (IC base=-0.020)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.137 (n=353)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=747)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=764)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=398)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.128 (n=617)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=708)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9084)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=28274)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=9458)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=29228)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.199 (n=1693)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5273)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.144 (n=2316)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=4549)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1792)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.137 (n=3233)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.016)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.186 (n=1178)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=3936)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.175 (n=1331)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4086)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1722)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=5319)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.133 (n=2142)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7651` → IC=-0.151 (n=1251)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7651
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3753)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1362)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=4157)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.161 (n=1731)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5254)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3281)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4233)

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
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=372)

- **FILTRO** `drift_20min_pct` |x|> `0.1999` → IC=-0.134 (n=121)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1999
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=364)

- **FILTRO** `libro_liquidez` < `3248.8853` → IC=-0.185 (n=160)

  - _Acción_: SKIP cuando `libro_liquidez` < 3248.8853
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=325)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `ibs_20min` > `0.8734` → IC=-0.126 (n=615)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8734
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=616)

- **FILTRO** `libro_liquidez` < `1612.2849` → IC=-0.147 (n=307)

  - _Acción_: SKIP cuando `libro_liquidez` < 1612.2849
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=924)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=229)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=25279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=57485)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20172)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=62592)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27210)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=55554)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.155 (n=27790)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=54974)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=25691)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=77915)

- **FILTRO** `ibs_7min` > `0.2786` → IC=-0.183 (n=25901)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2786
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=77705)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=3543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=11377)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.321 (n=3722)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=11198)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.256 (n=4918)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=10002)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4350)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=13601)

- **FILTRO** `ibs_7min` > `0.7667` → IC=-0.211 (n=4487)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7667
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=13464)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3348)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10305)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.216 (n=3412)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=10241)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.204 (n=3408)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=10245)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=3182)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10806)

- **FILTRO** `ibs_7min` > `0.2647` → IC=-0.192 (n=3496)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2647
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10492)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.178 (n=3488)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10500)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3406)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10892)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.329 (n=3420)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=10878)

- **FILTRO** `ibs_7min` < `0.2886` → IC=-0.255 (n=4718)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2886
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9580)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.174 (n=3445)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=10853)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.262 (n=4552)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=14424)

- **FILTRO** `ibs_7min` > `0.7222` → IC=-0.186 (n=4738)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=14238)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=3029)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10311)

- **FILTRO** `ibs_7min` < `0.7119` → IC=-0.203 (n=3334)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7119
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10006)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.200 (n=3223)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=10117)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3232)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=10621)

- **FILTRO** `ibs_7min` > `0.272` → IC=-0.178 (n=3463)

  - _Acción_: SKIP cuando `ibs_7min` > 0.272
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10390)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.168 (n=3453)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10400)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=3210)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=9964)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.235 (n=4325)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8849)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3257)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=9917)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.201 (n=4760)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=15297)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=3279)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=10100)

- **FILTRO** `ibs_7min` < `0.7202` → IC=-0.231 (n=4415)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7202
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8964)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.196 (n=3325)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=10054)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.231 (n=4589)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=14192)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1033)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1322)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.167 (n=181)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=667)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=924)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.127 (n=234)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=463)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=592)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.124 (n=107)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=677)

- **FILTRO** `libro_liquidez` < `3306.8101` → IC=-0.146 (n=196)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.8101
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=588)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=554)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.144 (n=757)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.130 (n=609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `451.7672` → IC=+0.166 (n=555)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 451.7672 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3665.592` → IC=+0.131 (n=754)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3665.592 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.187 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `381.982` → IC=+0.165 (n=338)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 381.982 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.157 (n=266)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 9.0 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.129 (n=346)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.153 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.113)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.172 (n=205)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `705.9846` → IC=+0.167 (n=271)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 705.9846 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.184 (n=112)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 59.0 (IC base=+0.126)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4317` → IC=+0.215 (n=128)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4317 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.164 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.179 (n=188)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4761.643 (IC base=+0.134)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.131 (n=304)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=213)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.101)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.157 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0047 (IC base=-0.026)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.265 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.005)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9196` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.9196 (IC base=+0.005)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `6.4329` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.4329
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `73.7179` → IC=-0.172 (n=62)

  - _Acción_: SKIP cuando `T_h` < 73.7179
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=128)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0164` → IC=-0.192 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0164
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `113.7599` → IC=-0.251 (n=565)

  - _Acción_: SKIP cuando `T_h` < 113.7599
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=292)

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.187 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=597)

- **FILTRO** `pct_vs_K` |x|> `2.9641` → IC=-0.375 (n=198)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9641
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=598)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `49.2927` → IC=-0.238 (n=212)

  - _Acción_: SKIP cuando `T_h` > 49.2927
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=72)

- **FILTRO** `sigma_h` < `0.0076` → IC=-0.172 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=101)

- **FILTRO** `pct_vs_K` |x|> `2.368` → IC=-0.324 (n=100)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.368
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=197)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.260 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `T_h` > `144.6658` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 144.6658
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.327 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=125)

- **FILTRO** `T_h` < `69.3311` → IC=-0.309 (n=82)

  - _Acción_: SKIP cuando `T_h` < 69.3311
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=168)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.161 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=182)

- **FILTRO** `T_h` > `57.2148` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `T_h` > 57.2148
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=80)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9843` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `pct_vs_K` |x|≤ 1.9843 (IC base=-0.098)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `T_h` > `109.7804` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `T_h` > 109.7804
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.01` → IC=-0.237 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=159)

- **FILTRO** `T_h` < `87.9882` → IC=-0.225 (n=118)

  - _Acción_: SKIP cuando `T_h` < 87.9882
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=119)

- **FILTRO** `sigma_h` < `0.0091` → IC=-0.261 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=134)

- **FILTRO** `T_h` > `35.877` → IC=-0.137 (n=133)

  - _Acción_: SKIP cuando `T_h` > 35.877
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=45)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1171` → IC=+0.447 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1171 (IC base=+0.336)

- **PATRÓN** `sigma_h` < `0.0147` → IC=+0.349 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0147 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.347 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.336)

- **PATRÓN** `T_h` < `0.3491` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3491 (IC base=+0.336)

- **PATRÓN** `T_h` > `0.4449` → IC=+0.358 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4449 (IC base=+0.336)

- **PATRÓN** `dist_50` > `0.4594` → IC=+0.483 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4594 (IC base=+0.336)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.355 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.336)

- **PATRÓN** `edge` > `0.1` → IC=+0.426 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.392)

- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.410 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.3751` → IC=+0.439 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3751 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.392)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.196)

- **PATRÓN** `T_h` < `0.7285` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7285 (IC base=+0.196)

- **PATRÓN** `T_h` > `1.4804` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4804 (IC base=+0.196)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.196)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1015` → IC=+0.467 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1015 (IC base=+0.414)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.426 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.414)

- **PATRÓN** `T_h` < `1.2028` → IC=+0.441 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2028 (IC base=+0.414)

- **PATRÓN** `dist_50` > `0.4134` → IC=+0.484 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4134 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.414)

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

- **PATRÓN** `edge` > `0.1937` → IC=+0.472 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1937 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.475 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.465)

- **PATRÓN** `T_h` < `0.8021` → IC=+0.458 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8021 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.4557` → IC=+0.493 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4557 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=477)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=516)

- **PATRÓN** `streak_estiramiento` < `0.3762` → IC=+0.127 (n=159)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.3762 (IC base=+0.018)

- **PATRÓN** `streak_estiramiento` < `0.835` → IC=+0.127 (n=357)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.835 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.124 (n=269)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.060)

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
- **FILTRO** `regimen_ma_toques` < `2.0` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `regimen_ma_toques` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=218)

- **PATRÓN** `streak_estiramiento` < `0.2115` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.2115 (IC base=+0.034)

- **PATRÓN** `streak_estiramiento` < `0.5965` → IC=+0.163 (n=179)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.5965 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.142 (n=191)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 35.0 (IC base=+0.087)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=97)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=118)

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
- **FILTRO** `streak_estiramiento` > `0.6751` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6751
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=29)

- **PATRÓN** `streak_estiramiento` < `0.5703` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.5703 (IC base=-0.016)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1101)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1350)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1316)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5441)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3257)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.184 (n=2110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.2319` → IC=+0.158 (n=6329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2319 (IC base=+0.133)

- **PATRÓN** `drift_15min` |x|≤ `1.1201` → IC=+0.135 (n=6328)

  - _Acción_: Kelly boost +0.68€ cuando `drift_15min` |x|≤ 1.1201 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0646` → IC=+0.133 (n=6327)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0646 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0998` → IC=+0.143 (n=1990)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0998 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=5857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.5595` → IC=+0.210 (n=5654)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5595 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.199` → IC=+0.232 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.199 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3372)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4339.4069` → IC=+0.171 (n=2110)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4339.4069 (IC base=+0.133)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=2455)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.253 (n=289)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.247 (n=381)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.205)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2684` → IC=+0.224 (n=288)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2684 (IC base=+0.205)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2266` → IC=+0.218 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2266 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.231 (n=800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.275 (n=865)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.387` → IC=+0.218 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.387 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.5442` → IC=+0.209 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5442 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.133` → IC=+0.299 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.133 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `11859.2402` → IC=+0.224 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11859.2402 (IC base=+0.205)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.162 (n=486)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0047 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.148 (n=736)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.085` → IC=+0.137 (n=986)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.085 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.144 (n=781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4846` → IC=+0.218 (n=1104)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4846 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1236` → IC=+0.143 (n=692)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1236 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.6448` → IC=+0.134 (n=1256)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.6448 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.055` → IC=+0.288 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.055 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6099.7428` → IC=+0.172 (n=501)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6099.7428 (IC base=+0.132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8421` → IC=+0.150 (n=646)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` > 0.8421 (IC base=+0.048)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0139` → IC=+0.139 (n=705)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0139 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.145 (n=1602)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.012 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2381` → IC=+0.176 (n=1603)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2381 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.142 (n=1603)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0926` → IC=+0.189 (n=500)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0926 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=1466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.141 (n=1484)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.7` → IC=+0.236 (n=1073)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.212` → IC=+0.149 (n=728)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.212 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.9039` → IC=+0.143 (n=1855)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.9039 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.354` → IC=+0.186 (n=367)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 17.354 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2947.2049` → IC=+0.183 (n=727)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2947.2049 (IC base=+0.139)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.363 (n=531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.376 (n=530)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.378 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.370 (n=735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.395 (n=796)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2656` → IC=+0.378 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2656 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.5497` → IC=+0.362 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5497 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.787` → IC=+0.395 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.787 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9641.0136` → IC=+0.379 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9641.0136 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.365 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.363 (n=335)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2194` → IC=+0.374 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2194 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1464` → IC=+0.395 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1464 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.361 (n=388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.383 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2499` → IC=+0.386 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2499 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.785` → IC=+0.380 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.785 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `15168.2778` → IC=+0.386 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15168.2778 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `412.0` → IC=+0.384 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 412.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.364 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.1063` → IC=+0.364 (n=278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1063 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1288` → IC=+0.378 (n=277)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1288 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.369 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.380 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.361)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.397 (n=416)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.367 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` < `0.6628` → IC=+0.364 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6628 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.857` → IC=+0.397 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.857 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `4293.66` → IC=+0.374 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4293.66 (IC base=+0.361)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0108` → IC=-0.234 (n=2024)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0108
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3930)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.223 (n=2614)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3340)

- **FILTRO** `libro_liquidez` < `4366.1664` → IC=-0.173 (n=3929)

  - _Acción_: SKIP cuando `libro_liquidez` < 4366.1664
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=2025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.214 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.089)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.278 (n=1313)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1154` → IC=+0.203 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1154 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` < `0.5893` → IC=+0.199 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5893 (IC base=-0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2288` → IC=+0.270 (n=1933)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2288 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.283 (n=5811)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.699` → IC=+0.266 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.699 (IC base=+0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0738` → IC=-0.241 (n=1947)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0738
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=1949)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.214 (n=973)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=2923)

- **FILTRO** `sigma_ewma_delta_pct` > `22.279` → IC=-0.244 (n=552)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.279
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=3344)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.145 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0032 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2685` → IC=+0.272 (n=156)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2685 (IC base=+0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.145` → IC=+0.278 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.145 (IC base=+0.064)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.317 (n=468)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.281 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.5257` → IC=+0.284 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5257 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.895` → IC=+0.139 (n=236)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 21.895 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.225 (n=78)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.182)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0902` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0902 (IC base=-0.182)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.287 (n=78)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.182)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.182)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.310 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.182)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=862)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.160 (n=660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0066 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.176 (n=291)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3015` → IC=+0.190 (n=520)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3015 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5657` → IC=+0.243 (n=660)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5657 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1198` → IC=+0.153 (n=413)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1198 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.149 (n=505)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.266 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=862)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5128.1918` → IC=+0.161 (n=440)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5128.1918 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.260 (n=996)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4769` → IC=+0.243 (n=2263)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4769 (IC base=+0.238)

- **PATRÓN** `drift_15min` |x|≤ `0.8211` → IC=+0.251 (n=1993)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8211 (IC base=+0.238)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2028` → IC=+0.258 (n=1027)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2028 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.240 (n=1543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.238)

- **PATRÓN** `ibs_15` < `0.3893` → IC=+0.270 (n=2263)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3893 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1647` → IC=+0.253 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1647 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.522` → IC=+0.245 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.522 (IC base=+0.238)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2015` → IC=-0.296 (n=356)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2015
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=1072)

- **FILTRO** `drift_60min` |x|> `0.2019` → IC=-0.293 (n=356)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2019
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1072)

- **FILTRO** `drift_15min` |x|> `1.0019` → IC=-0.307 (n=356)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0019
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1072)

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

- **PATRÓN** `ibs_15` < `0.3793` → IC=+0.296 (n=968)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3793 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.4634` → IC=+0.251 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4634 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1214` → IC=-0.271 (n=839)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1214
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=842)

- **FILTRO** `drift_60min` |x|> `0.1584` → IC=-0.251 (n=419)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1584
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=1262)

- **FILTRO** `drift_15min` |x|> `1.3182` → IC=-0.282 (n=420)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.3182
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=1261)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=1660)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.223)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.223)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.283 (n=1213)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=-0.009)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.290 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.009)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=1366)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.7832` → IC=+0.327 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7832 (IC base=-0.009)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.135 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0068 (IC base=+0.085)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.128 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.085)

- **PATRÓN** `drift_15min` |x|≤ `0.7362` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.7362 (IC base=+0.085)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.300 (n=28)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.0974` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0974 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.2049` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.2049 (IC base=+0.053)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.135 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0068 (IC base=+0.085)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.128 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.085)

- **PATRÓN** `drift_15min` |x|≤ `0.7362` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.7362 (IC base=+0.085)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.300 (n=28)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.0974` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0974 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.2049` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.2049 (IC base=+0.053)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.300 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.294 (n=489)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.311 (n=489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0688` → IC=+0.284 (n=1464)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0688 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2201` → IC=+0.290 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2201 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8372` → IC=+0.310 (n=1465)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8372 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2746` → IC=+0.313 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2746 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.703` → IC=+0.384 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.703 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.284 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13084.0601` → IC=+0.300 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13084.0601 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.308 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.301 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.278)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2704` → IC=+0.280 (n=257)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2704 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3894` → IC=+0.285 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3894 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.301 (n=712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.302 (n=772)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2573` → IC=+0.309 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2573 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.5693` → IC=+0.278 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5693 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.41` → IC=+0.391 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.41 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.279 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `15643.6309` → IC=+0.315 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15643.6309 (IC base=+0.278)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.298 (n=305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0502` → IC=+0.321 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0502 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.065` → IC=+0.293 (n=693)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.065 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1013` → IC=+0.308 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1013 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.298 (n=667)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.289 (n=492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8452` → IC=+0.314 (n=693)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8452 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2913` → IC=+0.310 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2913 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.379 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.163 (n=96)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=295)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.145 (n=240)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=119)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.167 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=381)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.220 (n=80)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=167)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.14` → IC=-0.149 (n=55)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.14
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
- **FILTRO** `sigma_h` < `0.0081` → IC=-0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.103` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.103
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=27)

- **FILTRO** `sigma_h` < `0.0062` → IC=-0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=31)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0764` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0764
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9868` → IC=+0.254 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9868 (IC base=+0.124)

- **PATRÓN** `T_h` > `115.9373` → IC=+0.356 (n=3204)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.9373 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.391 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.992` → IC=+0.155 (n=279)

  - _Acción_: Kelly boost +0.77€ cuando `ratio` < 0.992 (IC base=+0.068)

- **PATRÓN** `T_h` > `110.5638` → IC=+0.329 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.5638 (IC base=+0.310)

- **PATRÓN** `ratio` > `1.0147` → IC=+0.379 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0147 (IC base=+0.310)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9793` → IC=+0.363 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9793 (IC base=+0.185)

- **PATRÓN** `T_h` > `111.996` → IC=+0.353 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0238` → IC=+0.404 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0238 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0386` → IC=+0.415 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0386 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5595 sube el IC de +0.133 a +0.210 en UPDOWN_GBM#15min (n=5654). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.205 a +0.275 en UPDOWN_GBM#BTC#15min (n=865). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4846 sube el IC de +0.132 a +0.218 en UPDOWN_GBM#ETH#15min (n=1104). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.7 sube el IC de +0.139 a +0.236 en UPDOWN_GBM#XRP#15min (n=1073). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.089 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1313). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.001 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=5811). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.064 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=468). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.182 a +0.287 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5657 sube el IC de +0.147 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=660). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3893 sube el IC de +0.238 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2263). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.206 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3793 sube el IC de -0.026 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=968). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.223 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.009 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1366). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.085 a +0.300 en UPDOWN_GBM_ETH_15M_HORA7 (n=28). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.085 a +0.300 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=28). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8372 sube el IC de +0.284 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1465). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.278 a +0.302 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=772). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8452 sube el IC de +0.289 a +0.314 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=693). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.363 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=796). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.383 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.361 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=416). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2287 | +0.084 | +242.96€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2287 | +0.084 | +242.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1875 | +0.084 | +203.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1875 | +0.084 | +203.47€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1386 | -0.028 | +69.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1386 | -0.028 | +69.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1067 | -0.043 | +53.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1067 | -0.043 | +53.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 220 | +0.045 | +24.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 220 | +0.045 | +24.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 92 | -0.043 | -11.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 92 | -0.043 | -11.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 50883 | -0.087 | -6542.93€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3301 | +0.092 | -319.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 47582 | -0.100 | -6223.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5084 | -0.116 | -817.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5084 | -0.116 | -817.04€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3301 | +0.092 | -319.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3301 | +0.092 | -319.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5091 | -0.108 | -951.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5091 | -0.108 | -951.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14058 | -0.046 | -1349.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14058 | -0.046 | -1349.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13992 | -0.120 | -1554.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13992 | -0.120 | -1554.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9357 | -0.138 | -1550.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9357 | -0.138 | -1550.15€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 55418 | -0.012 | +2759.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14274 | +0.003 | +1475.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 41144 | -0.017 | +1283.60€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 55418 | -0.012 | +2759.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14274 | +0.003 | +1475.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 41144 | -0.017 | +1283.60€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 207391 | +0.113 | -8353.64€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23024 | +0.179 | -749.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 967 | +0.018 | -76.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 171633 | +0.106 | -7106.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11767 | +0.095 | -420.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 28444 | +0.102 | -2007.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 83 | -0.182 | +13.02€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 28338 | +0.103 | -2017.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 8 | +0.040 | +8.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 38914 | +0.123 | -597.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5683 | +0.177 | -225.96€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 28409 | +0.120 | -178.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4780 | +0.082 | -170.70€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 28492 | +0.099 | -1988.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 97 | -0.116 | +14.79€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 28376 | +0.100 | -1993.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 44368 | +0.124 | -920.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11056 | +0.178 | -313.91€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 28869 | +0.106 | -521.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4431 | +0.103 | -76.45€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 38703 | +0.111 | -1658.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6008 | +0.199 | -249.08€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 870 | +0.042 | -22.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 29284 | +0.096 | -1200.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2541 | +0.106 | -186.72€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 28470 | +0.107 | -1180.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 97 | -0.136 | +11.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 28357 | +0.108 | -1195.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 33746 | +0.189 | -2518.96€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 33746 | +0.189 | -2518.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7650 | +0.162 | -896.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7650 | +0.162 | -896.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5036 | +0.194 | -213.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5036 | +0.194 | -213.77€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7471 | +0.172 | -691.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7471 | +0.172 | -691.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6186 | +0.252 | -218.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6186 | +0.252 | -218.28€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7324 | +0.184 | -512.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7324 | +0.184 | -512.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1312 | +0.424 | -53.13€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1312 | +0.424 | -53.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 554 | +0.437 | -7.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 554 | +0.437 | -7.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 216 | +0.399 | -17.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 216 | +0.399 | -17.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 119275 | +0.200 | -8658.67€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 119275 | +0.200 | -8658.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 20676 | +0.176 | -2429.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 20676 | +0.176 | -2429.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19224 | +0.223 | -638.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19224 | +0.223 | -638.94€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 20458 | +0.181 | -2126.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 20458 | +0.181 | -2126.99€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19392 | +0.217 | -772.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19392 | +0.217 | -772.54€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 19689 | +0.205 | -1158.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 19689 | +0.205 | -1158.52€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 19836 | +0.198 | -1531.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 19836 | +0.198 | -1531.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 46346 | +0.116 | +355.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 46346 | +0.116 | +355.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 23081 | +0.117 | +227.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 23081 | +0.117 | +227.20€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 23265 | +0.116 | +128.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 23265 | +0.116 | +128.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2717 | +0.294 | -7.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2717 | +0.294 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1243 | +0.283 | -25.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1243 | +0.283 | -25.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1332 | +0.297 | +10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1332 | +0.297 | +10.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1258 | +0.438 | -5.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1258 | +0.438 | -5.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 600 | +0.435 | -7.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 600 | +0.435 | -7.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 606 | +0.441 | +0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 606 | +0.441 | +0.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2032 | +0.064 | -101.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1307 | +0.074 | -37.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1598 | +0.071 | -56.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1307 | +0.074 | -37.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 94556 | +0.101 | -1976.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7666 | +0.097 | +186.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 86890 | +0.101 | -2163.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 51623 | +0.105 | -433.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7666 | +0.097 | +186.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 43957 | +0.107 | -619.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 20294 | +0.111 | -41.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 20294 | +0.111 | -41.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 22639 | +0.083 | -1501.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 22639 | +0.083 | -1501.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 64397 | +0.102 | +36191.75€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 64397 | +0.102 | +36191.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10688 | +0.224 | +9177.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10688 | +0.224 | +9177.24€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 10051 | +0.176 | +8081.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10051 | +0.176 | +8081.03€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 11528 | +0.206 | +9074.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11528 | +0.206 | +9074.67€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8516 | +0.062 | +2877.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8516 | +0.062 | +2877.25€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8922 | -0.026 | +2292.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8922 | -0.026 | +2292.15€ | 4 | 17 |
| ✅ GBM_LATE_15M#XRP | 14692 | -0.020 | +4689.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 14692 | -0.020 | +4689.42€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 68393 | +0.087 | +39921.92€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 68393 | +0.087 | +39921.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13268 | -0.002 | +6938.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13268 | -0.002 | +6938.64€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 14696 | +0.007 | +4065.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 14696 | +0.007 | +4065.28€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9204 | +0.295 | +10537.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9204 | +0.295 | +10537.36€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13052 | +0.018 | +4179.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13052 | +0.018 | +4179.43€ | 1 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10424 | +0.049 | +4794.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10424 | +0.049 | +4794.71€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7749 | +0.313 | +9406.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7749 | +0.313 | +9406.50€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 50700 | +0.179 | +42136.05€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 50700 | +0.179 | +42136.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7665 | +0.239 | +7129.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7665 | +0.239 | +7129.63€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8072 | +0.141 | +6061.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8072 | +0.141 | +6061.84€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8165 | +0.224 | +7069.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8165 | +0.224 | +7069.76€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8679 | +0.129 | +6775.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8679 | +0.129 | +6775.52€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9559 | +0.123 | +7389.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9559 | +0.123 | +7389.10€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8560 | +0.232 | +7710.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8560 | +0.232 | +7710.19€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 13973 | +0.127 | +7155.50€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 13973 | +0.127 | +7155.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3601 | +0.126 | +1968.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3601 | +0.126 | +1968.59€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4100 | +0.128 | +2075.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4100 | +0.128 | +2075.12€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3826 | +0.104 | +1590.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3826 | +0.104 | +1590.78€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1260 | +0.167 | +786.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1260 | +0.167 | +786.94€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 64649 | +0.189 | +53792.73€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 64649 | +0.189 | +53792.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10219 | +0.249 | +9845.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10219 | +0.249 | +9845.39€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10380 | +0.142 | +7508.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10380 | +0.142 | +7508.49€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10965 | +0.234 | +9860.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10965 | +0.234 | +9860.47€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10698 | +0.144 | +8042.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10698 | +0.144 | +8042.28€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11388 | +0.129 | +8342.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11388 | +0.129 | +8342.45€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10999 | +0.240 | +10193.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10999 | +0.240 | +10193.64€ | 0 | 22 |
| ✅ GBM_LATE_5M | 16429 | +0.218 | +13828.73€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 16429 | +0.218 | +13828.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1907 | +0.252 | +1847.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1907 | +0.252 | +1847.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3316 | +0.210 | +2857.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3316 | +0.210 | +2857.79€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1524 | +0.214 | +1243.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1524 | +0.214 | +1243.40€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4668 | +0.209 | +3635.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4668 | +0.209 | +3635.56€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 2947 | +0.228 | +2611.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2947 | +0.228 | +2611.15€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 2067 | +0.210 | +1633.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2067 | +0.210 | +1633.69€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6145 | +0.070 | +1914.69€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 6145 | +0.070 | +1914.69€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 105 | +0.257 | +103.49€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 105 | +0.257 | +103.49€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1999 | +0.060 | +575.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1999 | +0.060 | +575.45€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 103 | +0.319 | +120.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 103 | +0.319 | +120.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1857 | +0.055 | +592.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1857 | +0.055 | +592.94€ | 1 | 5 |
| ✅ GBM_LATE_60M#SOL | 1980 | +0.059 | +408.36€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1980 | +0.059 | +408.36€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 101 | +0.316 | +113.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 101 | +0.316 | +113.45€ | 0 | 22 |
| 🚫 GBM_LATE_60M_FADE | 773 | -0.248 | -39.55€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 773 | -0.248 | -39.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 6 | +0.037 | +3.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 6 | +0.037 | +3.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 273 | -0.260 | -24.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 273 | -0.260 | -24.35€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 274 | -0.243 | -7.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 274 | -0.243 | -7.28€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 213 | -0.249 | -10.93€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 213 | -0.249 | -10.93€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2345 | +0.090 | +595.41€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2345 | +0.090 | +595.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 887 | +0.069 | +203.50€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 887 | +0.069 | +203.50€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 807 | +0.061 | +155.40€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 807 | +0.061 | +155.40€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 648 | +0.152 | +235.69€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 648 | +0.152 | +235.69€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 395 | +0.316 | +487.05€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 395 | +0.316 | +487.05€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 395 | +0.316 | +487.05€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 395 | +0.316 | +487.05€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4813 | +0.095 | +1046.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4813 | +0.095 | +1046.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4813 | +0.095 | +1046.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4813 | +0.095 | +1046.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1708 | +0.017 | +96.01€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1708 | +0.017 | +96.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 208 | +0.081 | +37.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 208 | +0.081 | +37.35€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 335 | -0.010 | +7.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 335 | -0.010 | +7.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 115 | +0.056 | +25.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 115 | +0.056 | +25.23€ | 2 | 3 |
| ✅ LIQUIDACIONES_15M#ETH | 386 | +0.026 | +21.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 386 | +0.026 | +21.80€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 350 | -0.014 | +2.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 350 | -0.014 | +2.82€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 314 | +0.013 | +0.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 314 | +0.013 | +0.82€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4534 | +0.017 | +182.31€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4534 | +0.017 | +182.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 860 | +0.015 | +47.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 860 | +0.015 | +47.72€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 334 | +0.062 | +80.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 334 | +0.062 | +80.07€ | 0 | 7 |
| ✅ LIQUIDACIONES_5M#ETH | 1690 | +0.020 | +31.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1690 | +0.020 | +31.68€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 789 | +0.015 | +5.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 789 | +0.015 | +5.57€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 620 | -0.006 | +23.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 620 | -0.006 | +23.43€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2716 | -0.034 | -7.44€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2716 | -0.034 | -7.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 831 | -0.034 | -14.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 831 | -0.034 | -14.09€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 978 | -0.014 | +18.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 978 | -0.014 | +18.93€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 897 | -0.055 | -11.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 897 | -0.055 | -11.36€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 7 | -0.019 | -0.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 7 | -0.019 | -0.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 20355 | -0.031 | -139.53€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 9843 | -0.033 | -125.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 10512 | -0.028 | -13.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 729 | -0.049 | -33.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 367 | -0.037 | -5.84€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 362 | -0.060 | -27.39€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5461 | -0.026 | -19.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2595 | -0.024 | +4.03€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2866 | -0.028 | -23.19€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1862 | -0.032 | -2.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 951 | -0.043 | -29.62€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 911 | -0.020 | +26.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4656 | -0.031 | -49.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2243 | -0.030 | -18.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2413 | -0.032 | -30.23€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3887 | -0.023 | +52.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1893 | -0.030 | -6.37€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1994 | -0.017 | +58.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3760 | -0.041 | -87.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1794 | -0.048 | -68.86€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1966 | -0.034 | -18.82€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 76044 | +0.000 | +4169.45€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 76044 | +0.000 | +4169.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13831 | +0.027 | +1926.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13831 | +0.027 | +1926.29€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10531 | -0.038 | -131.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10531 | -0.038 | -131.61€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 13982 | +0.026 | +1571.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 13982 | +0.026 | +1571.35€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10523 | -0.053 | -262.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10523 | -0.053 | -262.94€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12964 | -0.004 | +373.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12964 | -0.004 | +373.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14213 | +0.019 | +692.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14213 | +0.019 | +692.96€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7403 | -0.053 | -108.41€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7403 | -0.053 | -108.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2104 | -0.058 | -18.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2104 | -0.058 | -18.56€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 819 | -0.116 | -32.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 819 | -0.116 | -32.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2238 | -0.067 | -13.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2238 | -0.067 | -13.43€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 870 | -0.019 | -28.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 870 | -0.019 | -28.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3385 | +0.003 | -0.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3385 | +0.003 | -0.98€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_5M#XRP | 196 | -0.015 | -1.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 196 | -0.015 | -1.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 186370 | -0.078 | +2216.75€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 186370 | -0.078 | +2216.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 32871 | -0.076 | +1930.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 32871 | -0.076 | +1930.60€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 27641 | -0.102 | -1375.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 27641 | -0.102 | -1375.66€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33274 | -0.068 | +1618.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33274 | -0.068 | +1618.90€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 27193 | -0.100 | -944.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 27193 | -0.100 | -944.90€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33231 | -0.059 | +191.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33231 | -0.059 | +191.57€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32160 | -0.069 | +796.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32160 | -0.069 | +796.24€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9314 | -0.036 | -192.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9314 | -0.036 | -192.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1009 | -0.017 | -19.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1009 | -0.017 | -19.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2185 | -0.046 | -29.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2185 | -0.046 | -29.12€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2675 | -0.024 | -32.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2675 | -0.024 | -32.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1297 | -0.064 | -32.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1297 | -0.064 | -32.97€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1139 | -0.042 | -46.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1139 | -0.042 | -46.49€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2352 | +0.120 | +940.54€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2216 | +0.123 | +927.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 511 | +0.141 | +264.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 511 | +0.141 | +264.33€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 461 | +0.113 | +156.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 461 | +0.113 | +156.38€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 410 | +0.126 | +185.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 410 | +0.126 | +185.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 375 | +0.134 | +182.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 375 | +0.134 | +182.24€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 459 | +0.101 | +139.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 459 | +0.101 | +139.00€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2486 | -0.022 | -43.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2486 | -0.022 | -43.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 444 | +0.009 | +23.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 444 | +0.009 | +23.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 458 | -0.048 | -30.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 458 | -0.048 | -30.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 604 | -0.046 | -43.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 604 | -0.046 | -43.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 515 | -0.003 | -0.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 515 | -0.003 | -0.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 465 | -0.014 | +6.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 465 | -0.014 | +6.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1303 | -0.041 | +136.66€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 601 | -0.066 | +27.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 472 | -0.061 | +51.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 458 | -0.011 | +72.15€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 337 | +0.010 | +80.90€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 244 | -0.037 | +36.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 208 | -0.029 | +35.13€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1017 | -0.031 | +167.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1653 | -0.184 | -31.00€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 652 | -0.173 | -8.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 581 | -0.169 | -4.11€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 71 | -0.199 | -3.91€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 555 | -0.195 | -29.62€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 492 | -0.202 | -36.25€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 63 | -0.131 | +6.63€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 446 | -0.185 | +6.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 415 | -0.181 | +4.99€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 31 | -0.227 | +1.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1488 | -0.184 | -35.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 165 | -0.183 | +4.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 590 | +0.377 | +533.67€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 132 | +0.172 | +100.16€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 132 | +0.172 | +100.16€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#ETH | 135 | +0.369 | +106.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 135 | +0.369 | +106.67€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 323 | +0.460 | +326.84€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 323 | +0.460 | +326.84€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 590 | +0.377 | +533.67€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1031 | +0.040 | +85.25€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1031 | +0.040 | +85.25€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 80 | +0.024 | +1.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 80 | +0.024 | +1.80€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 507 | +0.062 | +73.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 507 | +0.062 | +73.50€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3640 | -0.023 | -143.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3640 | -0.023 | -143.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 626 | -0.030 | -28.54€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 626 | -0.030 | -28.54€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 177 | -0.048 | -15.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 177 | -0.048 | -15.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1710 | -0.018 | -59.02€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1710 | -0.018 | -59.02€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 132 | -0.022 | -9.96€ | 1 | 1 |
| ✅ STREAK_FADE_60M#60min | 132 | -0.022 | -9.96€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 47 | -0.051 | -3.25€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 47 | -0.051 | -3.25€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 81 | -0.006 | -6.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 81 | -0.006 | -6.44€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11655 | +0.013 | +63.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11655 | +0.013 | +63.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3007 | +0.017 | +21.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3007 | +0.017 | +21.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3106 | +0.013 | +23.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3106 | +0.013 | +23.88€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2940 | +0.008 | -3.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2940 | +0.008 | -3.49€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2602 | +0.015 | +21.93€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2602 | +0.015 | +21.93€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13530 | +0.019 | +7.19€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13530 | +0.019 | +7.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5460 | +0.020 | +2.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5460 | +0.020 | +2.90€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4779 | +0.020 | +4.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4779 | +0.020 | +4.90€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3291 | +0.015 | -0.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3291 | +0.015 | -0.61€ | 1 | 0 |
| ✅ UPDOWN_GBM | 122700 | +0.060 | +11706.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 30464 | +0.078 | +5995.96€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3496 | -0.000 | +42.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 81048 | +0.062 | +5545.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7274 | -0.002 | +128.75€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10785 | +0.103 | +1982.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2015 | +0.165 | +946.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8680 | +0.090 | +1037.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 27669 | +0.057 | +2452.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4069 | +0.080 | +915.83€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1023 | -0.001 | +21.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19151 | +0.066 | +1429.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3276 | -0.005 | +80.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 150 | -0.066 | +4.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 13755 | +0.074 | +1502.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2001 | +0.154 | +847.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11668 | +0.061 | +655.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 28670 | +0.050 | +2054.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7069 | +0.071 | +1104.19€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 990 | +0.005 | +15.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 17772 | +0.052 | +891.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2699 | -0.001 | +40.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 140 | -0.099 | +2.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 25495 | +0.041 | +1454.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8251 | +0.033 | +482.35€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 910 | -0.010 | +8.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14909 | +0.052 | +965.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1299 | +0.004 | +8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 126 | -0.141 | -10.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16324 | +0.073 | +2263.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7059 | +0.089 | +1699.37€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8868 | +0.063 | +565.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 416 | -0.101 | -3.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1061 | +0.363 | +392.86€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1061 | +0.363 | +392.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 507 | +0.362 | +177.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 507 | +0.362 | +177.09€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 554 | +0.361 | +215.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 554 | +0.361 | +215.78€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 28990 | -0.018 | +7211.73€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 28990 | -0.018 | +7211.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2255 | -0.046 | +602.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2255 | -0.046 | +602.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5328 | -0.116 | +283.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5328 | -0.116 | +283.32€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1239 | +0.220 | +1030.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1239 | +0.220 | +1030.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3896 | +0.217 | +2462.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3896 | +0.217 | +2462.70€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8184 | -0.058 | +1210.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8184 | -0.058 | +1210.83€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8088 | -0.053 | +1621.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8088 | -0.053 | +1621.12€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 362 | +0.060 | +31.26€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 362 | +0.060 | +31.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 362 | +0.060 | +31.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 362 | +0.060 | +31.26€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1953 | +0.284 | +1665.85€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1953 | +0.284 | +1665.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1029 | +0.278 | +828.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1029 | +0.278 | +828.29€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 924 | +0.289 | +837.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 924 | +0.289 | +837.56€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 899 | -0.119 | -94.76€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 899 | -0.119 | -94.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 289 | -0.084 | -22.53€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 289 | -0.084 | -22.53€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 122 | -0.194 | -8.05€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 122 | -0.194 | -8.05€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5282 | +0.295 | +2363.04€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2051 | +0.252 | +319.31€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2045 | +0.287 | +880.07€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1186 | +0.381 | +1163.66€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.025 n=1490 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1490 IC=+0.025 PNL=+72.07€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 847 celda(s) pasan gate riguroso completo de 3053 evaluadas (n>=40) y 4166 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=8246 IC=+0.033 PNL=+482.17€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=2045/15 IC=+0.287 PNL=+880.07€ | BTC: n=2051/15 IC=+0.252 PNL=+319.31€ | SOL: n=1186/15 IC=+0.381 PNL=+1163.66€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.136 n=1144/60 | contraria IC=+0.184 n=1214 | gap=-0.048 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=641, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2698/40 IC=-0.001 PNL=+40.81€ | BTC#60min: n=3274/40 IC=-0.005 PNL=+80.42€ | SOL#60min: n=1299/40 IC=+0.004 PNL=+8.03€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=819248 | tras_1loss IC=+0.102 n=620077 | tras_2loss IC=+0.073 n=246477/40 | gap=-0.029 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=1247 PNL=+702.09€
  - _Datos_: n=1247 IC=+0.151 PNL=+702.09€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.08 con n=1482 PNL=+659.16€
  - _Datos_: n=1482 IC=+0.125 PNL=+659.16€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=4315 PNL=+2500.00€
  - _Datos_: n=4315 IC=+0.335 PNL=+2500.00€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1235 IC=+0.063 PNL=+122.36€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1235 IC=+0.063 PNL=+122.36€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=116 IC=+0.161 PNL=+68.05€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=116 IC=+0.161 PNL=+68.05€

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
  - _Estado_: n=4763 IC=-0.007 PNL=-52.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4763 IC=-0.007 PNL=-52.01€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2508 IC=+0.008 PNL=+181.26€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2508 IC=+0.008 PNL=+181.26€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1490 IC=+0.025 PNL=+72.07€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1490 IC=+0.025 PNL=+72.07€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.133 > 0.1 con n=8434 PNL=+4016.95€
  - _Datos_: n=8434 IC=+0.133 PNL=+4016.95€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=4068 IC=+0.081 PNL=+916.34€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=4068 IC=+0.081 PNL=+916.34€

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
  - _Estado_: n=1653 IC=+0.041 PNL=+133.58€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1653 IC=+0.041 PNL=+133.58€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=204 IC=-0.024 PNL=-5.76€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=204 IC=-0.024 PNL=-5.76€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.316 n=395) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=395 IC=+0.316 PNL=+487.05€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=1377 PNL=+550.62€
  - _Datos_: n=1377 IC=+0.117 PNL=+550.62€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=275 IC=-0.128 PNL=+0.99€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=275 IC=-0.128 PNL=+0.99€

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
  - _Estado_: n=50383 IC=+0.069 PNL=+6735.33€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=50383 IC=+0.069 PNL=+6735.33€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.127 < -0.1 con n=840 PNL=+137.72€
  - _Datos_: n=840 IC=-0.127 PNL=+137.72€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4920 IC=+0.067 PNL=+592.19€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4920 IC=+0.067 PNL=+592.19€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=212 IC=-0.084 PNL=+4.83€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=212 IC=-0.084 PNL=+4.83€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1311 IC=+0.098 PNL=+318.47€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1311 IC=+0.098 PNL=+318.47€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 7/20 ops en el filtro definido (IC actual=-0.058 PNL=-1.16€)
  - _Datos_: n=7 IC=-0.058 PNL=-1.16€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=48921 IC=-0.138 PNL=+2999.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=48921 IC=-0.138 PNL=+2999.91€

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
  - _Estado_: n=5255 IC=+0.135 PNL=+3674.06€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5255 IC=+0.135 PNL=+3674.06€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=12753 IC=+0.057 PNL=+1085.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12753 IC=+0.057 PNL=+1085.45€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=5295 PNL=+2999.67€
  - _Datos_: n=5295 IC=+0.102 PNL=+2999.67€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.221 < -0.1 con n=5325 PNL=-441.97€
  - _Datos_: n=5325 IC=-0.221 PNL=-441.97€

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
  - _Estado_: n=133 IC=+0.070 PNL=+22.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=133 IC=+0.070 PNL=+22.11€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.095 n=2449) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2449 IC=+0.095 PNL=+480.64€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=695) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=695 IC=+0.414 PNL=+1018.76€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=20667 IC=+0.176 PNL=-2426.67€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=20667 IC=+0.176 PNL=-2426.67€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.231 > 0.1 con n=340 PNL=+236.58€
  - _Datos_: n=340 IC=+0.231 PNL=+236.58€
