# Hipótesis automáticas — 2026-09-21 06:33 UTC
_Generado por shadow_postmortem.py sobre 537808 resoluciones (PNL=+59902.34€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=479)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=447)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.248 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.220 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.804` → IC=+0.254 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.804 (IC base=+0.130)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.223 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.958 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=546)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.130)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=378)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=320)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.255 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.226 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.8026` → IC=+0.265 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8026 (IC base=+0.138)

- **PATRÓN** `banda_z` > `11.136` → IC=+0.230 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.136 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.159 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=461)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.144 (n=116)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 96.0 (IC base=+0.040)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=87)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.253 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.103)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.103)

- **PATRÓN** `banda_z` > `6.043` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 6.043 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `1185.8848` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1185.8848 (IC base=+0.103)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.154)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.705` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ballenas_wallet_edge_medio` > 0.705 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.154)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `145.19` → IC=-0.235 (n=6499)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.19
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=19499)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `140.44` → IC=-0.240 (n=884)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.44
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2655)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `493.55` → IC=-0.151 (n=348)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 493.55
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1044)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `133.5` → IC=-0.278 (n=780)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.5
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=2341)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `160.9` → IC=-0.232 (n=1533)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.9
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4602)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `121.81` → IC=-0.364 (n=1287)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.81
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=3864)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.240 (n=337)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=385)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.173 (n=218)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=449)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.264 (n=163)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=169)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.214 (n=75)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=227)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.324 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=165)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.167 (n=67)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=138)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=155)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.199 (n=13060)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.69 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3266)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `5494.1585` → IC=+0.173 (n=2077)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5494.1585 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=10359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=12656)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.235 (n=9996)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=5332)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `1663.3165` → IC=+0.158 (n=6006)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1663.3165 (IC base=+0.130)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.348 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15670.1365` → IC=+0.231 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15670.1365 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1554)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.261 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=1989)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `15424.767` → IC=+0.209 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15424.767 (IC base=+0.198)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.180 (n=304)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.62 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.144 (n=234)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4624.034 (IC base=+0.103)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=326)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.150 (n=786)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.44 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=555)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.165 (n=219)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.115)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=2602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.144 (n=2229)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.331 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.358 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.243 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.235)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.142 (n=612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.225 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=702)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1296.9414` → IC=+0.148 (n=609)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1296.9414 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.429 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=1027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.311 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=702)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.167)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.361 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=184)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `1271.2794` → IC=+0.159 (n=221)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1271.2794 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.215 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=10446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=10033)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.223 (n=3610)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.178 (n=2580)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `py_entrada` < `0.775` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.275 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.259 (n=658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.358 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.256)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=2517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2409)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.188 (n=1109)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.73 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.320 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=2440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=2357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.193 (n=1775)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.436 (n=455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.429 (n=433)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.426 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `2044.7957` → IC=+0.436 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2044.7957 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.431 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.451 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.469 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `3286.0948` → IC=+0.443 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3286.0948 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.405 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.401)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.401)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.417 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.401)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.402 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.401)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `libro_liquidez` < `6836.9618` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 6836.9618
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=30964)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.240 (n=11654)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=6314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=5352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=5788)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=5538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.226 (n=5545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2010)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=2991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=5727)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.173)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=2793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=2135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=5124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.252 (n=2599)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=6115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=5177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2049)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=4773)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.12` → IC=+0.130 (n=4381)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.12 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.145 (n=4571)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=5784)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.17` → IC=+0.145 (n=4344)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.17 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.202 (n=2408)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.06` → IC=+0.132 (n=2160)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.06 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.140 (n=2256)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=2853)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.53` → IC=+0.146 (n=2162)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.53 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.126 (n=2189)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.142 (n=2324)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.34` → IC=+0.145 (n=2191)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.34 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1573.11` → IC=+0.296 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1573.11 (IC base=+0.290)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.294 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.274)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.338 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `4194.9158` → IC=+0.293 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4194.9158 (IC base=+0.274)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.334 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.385 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `1466.4356` → IC=+0.314 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1466.4356 (IC base=+0.296)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.345 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.338)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.361 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.338)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.338)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.338)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.338)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.444 (n=407)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `2546.95` → IC=+0.438 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2546.95 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.445 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `2057.1892` → IC=+0.459 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2057.1892 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.381)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.72` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=29)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.315 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.274 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.72` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=29)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.315 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.274 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.3551` → IC=+0.125 (n=6393)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.3551 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.239 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.7885` → IC=+0.241 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7885 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` < `0.5952` → IC=+0.244 (n=2031)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5952 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.925` → IC=+0.175 (n=2798)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.925 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `1.2107` → IC=+0.243 (n=1928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2107 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `1.0481` → IC=+0.248 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0481 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.308` → IC=+0.210 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.308 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` > `1.9173` → IC=+0.205 (n=3280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9173 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.571` → IC=+0.132 (n=8772)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.571 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.5667` → IC=+0.201 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5667 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` < `0.1427` → IC=+0.173 (n=2741)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1427 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` < `0.7009` → IC=+0.177 (n=1320)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.7009 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` > `0.8696` → IC=+0.173 (n=2001)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8696 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.168` → IC=+0.225 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.168 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` > `1.5834` → IC=+0.202 (n=4460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5834 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.212 (n=4773)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.063)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.176 (n=550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.173 (n=554)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0081 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3416` → IC=+0.166 (n=1648)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3416 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.173 (n=1104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.063` → IC=+0.277 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.063 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.206 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4398` → IC=+0.165 (n=1533)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4398 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.249 (n=1081)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.293 (n=403)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.245 (n=823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0604` → IC=+0.299 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0604 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.405` → IC=+0.250 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.405 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.230 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.264 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.251 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1773.87` → IC=+0.246 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1773.87 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.235 (n=552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.1134` → IC=+0.250 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1134 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=1305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.212 (n=1273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9922` → IC=+0.259 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9922 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1859` → IC=+0.213 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1859 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.5614` → IC=+0.217 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5614 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.867` → IC=+0.246 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.867 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2524` → IC=+0.218 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2524 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.215 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.0746` → IC=+0.225 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0746 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4035` → IC=+0.220 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4035 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.3852` → IC=+0.215 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3852 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `15821.8878` → IC=+0.222 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15821.8878 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.176 (n=439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.155 (n=436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.168 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6828` → IC=+0.167 (n=1306)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6828 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.6767` → IC=+0.138 (n=222)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.6767 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1259` → IC=+0.153 (n=1173)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1259 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.294` → IC=+0.159 (n=212)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.294 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.189` → IC=+0.137 (n=1181)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.189 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.147 (n=1306)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2085 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.8523` → IC=+0.139 (n=870)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8523 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1575` → IC=+0.176 (n=350)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1575 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4443` → IC=+0.148 (n=1196)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4443 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.146 (n=797)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.145 (n=1113)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 411.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.202 (n=1070)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=1681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=1433)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.093` → IC=+0.246 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.093 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.2145` → IC=+0.188 (n=1588)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2145 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.3675` → IC=+0.191 (n=208)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.3675 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.9269` → IC=+0.205 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9269 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.193 (n=1072)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.224 (n=1366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.219 (n=1219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.1935` → IC=+0.238 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1935 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.543` → IC=+0.239 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.543 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.394` → IC=+0.218 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.394 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3603` → IC=+0.276 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3603 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.8319` → IC=+0.209 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8319 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.2747` → IC=+0.225 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2747 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.230 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1860.9452` → IC=+0.231 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1860.9452 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.225 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.218)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=92)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2021)

- **PATRÓN** `ibs_20min` > `0.9377` → IC=+0.194 (n=328)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.9377 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.3482` → IC=+0.344 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3482 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.682` → IC=+0.321 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.682 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.658` → IC=+0.150 (n=639)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.658 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.8419` → IC=+0.328 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8419 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.0371` → IC=+0.324 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0371 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.1687` → IC=+0.324 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1687 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.338 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.3975` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3975 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.327 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.333 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.1866` → IC=+0.165 (n=299)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1866 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `0.8544` → IC=+0.152 (n=487)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8544 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.235 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.175 (n=605)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.011)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.155 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=292)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.197 (n=87)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=261)

- **FILTRO** `ibs_20min` > `0.2625` → IC=-0.126 (n=2002)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2625
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=987)

- **FILTRO** `sigma_ewma_delta_pct` > `8.637` → IC=-0.205 (n=324)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.637
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2665)

- **PATRÓN** `drift_60min` |x|≤ `0.1707` → IC=+0.167 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1707 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7647 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `1.6268` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6268 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.5528` → IC=+0.272 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5528 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.6528` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6528 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.1487` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1487 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` < `0.1494` → IC=+0.300 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1494 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `2.2264` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2264 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.5504` → IC=+0.266 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5504 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.304 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.2625` → IC=+0.126 (n=987)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.2625 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` > `0.6436` → IC=+0.315 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6436 (IC base=-0.043)

- **PATRÓN** `volumen_regimen` < `1.096` → IC=+0.239 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.096 (IC base=-0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.102` → IC=+0.235 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.102 (IC base=-0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.1566` → IC=+0.268 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1566 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.4773` → IC=+0.267 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4773 (IC base=-0.043)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6331` → IC=-0.192 (n=507)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6331
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1524)

- **FILTRO** `ibs_20min` < `0.6957` → IC=-0.158 (n=1340)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6957
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=691)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.196 (n=396)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=1635)

- **FILTRO** `ibs_20min` > `0.7736` → IC=-0.201 (n=754)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7736
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=2266)

- **PATRÓN** `dist_vwap_pct` > `0.9664` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9664 (IC base=-0.076)

- **PATRÓN** `dist_vwap_pct` < `0.2555` → IC=+0.314 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2555 (IC base=-0.076)

- **PATRÓN** `volumen_regimen` < `0.9948` → IC=+0.276 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9948 (IC base=-0.076)

- **PATRÓN** `volumen_regimen` > `0.6141` → IC=+0.299 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6141 (IC base=-0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.0751` → IC=+0.295 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0751 (IC base=-0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.4081` → IC=+0.285 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4081 (IC base=-0.076)

- **PATRÓN** `volumen_spike_ratio` > `1.8611` → IC=+0.299 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8611 (IC base=-0.076)

- **PATRÓN** `dist_vwap_pct` > `0.9919` → IC=+0.318 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9919 (IC base=-0.023)

- **PATRÓN** `volumen_regimen` < `0.7389` → IC=+0.257 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7389 (IC base=-0.023)

- **PATRÓN** `volumen_regimen` > `1.0812` → IC=+0.294 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0812 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1054` → IC=+0.284 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1054 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.2166` → IC=+0.257 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2166 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5829` → IC=+0.249 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5829 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.191 (n=3020)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0094 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4682` → IC=+0.185 (n=8081)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4682 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `1.0076` → IC=+0.289 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0076 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.553` → IC=+0.153 (n=4294)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.553 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `1.1747` → IC=+0.231 (n=3172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1747 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` > `0.682` → IC=+0.241 (n=2833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.682 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2993` → IC=+0.260 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2993 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.4757` → IC=+0.238 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4757 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` > `2.7143` → IC=+0.240 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7143 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.267 (n=4662)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.148 (n=3052)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0088 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.5517` → IC=+0.150 (n=8059)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5517 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.6767` → IC=+0.243 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6767 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.1711` → IC=+0.237 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1711 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `0.7166` → IC=+0.240 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7166 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.2011` → IC=+0.242 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2011 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2477` → IC=+0.308 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2477 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.6193` → IC=+0.255 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6193 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `2.356` → IC=+0.260 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.356 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.264 (n=3285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 81.0 (IC base=+0.071)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `2.676` → IC=-0.150 (n=653)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.676
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=1477)

- **PATRÓN** `ibs_20min` > `0.8933` → IC=+0.266 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8933 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.29` → IC=+0.164 (n=858)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.29 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.272 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4412` → IC=+0.183 (n=260)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4412 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `2.5889` → IC=+0.195 (n=260)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.5889 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.179 (n=334)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 15.0 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.817` → IC=-0.147 (n=661)

  - _Acción_: SKIP cuando `ibs_20min` > 0.817
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1984)

- **PATRÓN** `ibs_20min` > `0.86` → IC=+0.152 (n=608)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.86 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.2893` → IC=+0.157 (n=322)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.2893 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.0443` → IC=+0.145 (n=727)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.0443 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.6622` → IC=+0.151 (n=737)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6622 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2769` → IC=+0.201 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2769 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.194 (n=269)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `248.0` → IC=+0.191 (n=351)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 248.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6013` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6013 (IC base=-0.000)

- **PATRÓN** `dist_vwap_pct` < `0.1524` → IC=+0.212 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1524 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` > `0.6059` → IC=+0.208 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6059 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.4599` → IC=+0.217 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4599 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1913` → IC=+0.222 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1913 (IC base=-0.000)

- **PATRÓN** `ballena_activa_n` < `481.0` → IC=+0.214 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 481.0 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.285 (n=957)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.255 (n=545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.583` → IC=+0.280 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.583 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.1388` → IC=+0.259 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1388 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.9594` → IC=+0.262 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9594 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.255 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1927.641` → IC=+0.254 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.641 (IC base=+0.244)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.329 (n=517)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.327 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.3357` → IC=+0.291 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3357 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.808` → IC=+0.303 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.808 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.3441` → IC=+0.315 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3441 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.6226` → IC=+0.294 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6226 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.2024` → IC=+0.288 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2024 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.299 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1912.1584` → IC=+0.316 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.1584 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.292 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2709` → IC=-0.196 (n=435)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2709
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=1306)

- **FILTRO** `ibs_20min` > `0.7832` → IC=-0.175 (n=540)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7832
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1623)

- **PATRÓN** `ibs_20min` > `0.902` → IC=+0.173 (n=436)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.902 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` > `0.4453` → IC=+0.228 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4453 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `1.0974` → IC=+0.223 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0974 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.208 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2672` → IC=+0.293 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2672 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.1059` → IC=+0.239 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1059 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.258 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.200 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1481 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.4933` → IC=+0.182 (n=375)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.4933 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` < `1.1615` → IC=+0.192 (n=349)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.1615 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `0.7255` → IC=+0.180 (n=311)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.7255 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.234 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8288 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.1518` → IC=+0.252 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1518 (IC base=-0.009)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.237 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7059` → IC=-0.205 (n=961)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=966)

- **FILTRO** `ibs_20min` > `0.6923` → IC=-0.232 (n=501)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6923
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=1520)

- **FILTRO** `sigma_ewma_delta_pct` > `4.689` → IC=-0.176 (n=449)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.689
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=1572)

- **PATRÓN** `ibs_20min` > `0.7059` → IC=+0.269 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7059 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.8145` → IC=+0.345 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8145 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.155 (n=302)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.297 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `0.636` → IC=+0.283 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.636 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1049` → IC=+0.287 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1049 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.300 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.7979` → IC=+0.301 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7979 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.312 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.211 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.2098` → IC=+0.223 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2098 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.272 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.210 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.204 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.5268` → IC=+0.224 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5268 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.236 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.013)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0161` → IC=+0.317 (n=786)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0161 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.289 (n=553)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` > `0.9097` → IC=+0.344 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9097 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` > `0.1915` → IC=+0.313 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1915 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.487` → IC=+0.297 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.487 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` > `1.0362` → IC=+0.303 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0362 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.311 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` < `1.4418` → IC=+0.278 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4418 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.1855` → IC=+0.288 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1855 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.278 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `2600.216` → IC=+0.285 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2600.216 (IC base=+0.274)

- **PATRÓN** `sigma_h` > `0.0147` → IC=+0.300 (n=868)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0147 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.280 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.271 (n=652)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.3962` → IC=+0.304 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3962 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.5376` → IC=+0.286 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5376 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.8952` → IC=+0.271 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8952 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.477` → IC=+0.290 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.477 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.273 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `1.241` → IC=+0.312 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.241 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.339 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `2.5342` → IC=+0.267 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5342 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.17` → IC=+0.272 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.17 (IC base=+0.271)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.271 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2585.317` → IC=+0.277 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2585.317 (IC base=+0.271)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.171 (n=2387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.201 (n=2382)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.185 (n=2380)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=7420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.5802` → IC=+0.216 (n=7136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5802 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.1688` → IC=+0.194 (n=3099)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1688 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.234` → IC=+0.258 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.234 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `1.2155` → IC=+0.160 (n=4720)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2155 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.158 (n=4719)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6248 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2976` → IC=+0.193 (n=1055)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2976 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.5658` → IC=+0.168 (n=2999)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5658 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.6486` → IC=+0.175 (n=2272)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6486 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2378.8529` → IC=+0.167 (n=4756)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2378.8529 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.179 (n=6050)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 118.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.182 (n=4542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0065 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.202 (n=2269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.208 (n=2299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4779` → IC=+0.226 (n=6807)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4779 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.2249` → IC=+0.159 (n=4987)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2249 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.238` → IC=+0.195 (n=1157)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.238 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.18` → IC=+0.152 (n=4963)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.18 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.224 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5742` → IC=+0.167 (n=2703)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5742 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.2814` → IC=+0.173 (n=2784)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.2814 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.172 (n=5775)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 120.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.220 (n=409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.189 (n=410)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0083 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.3367` → IC=+0.206 (n=1225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3367 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=818)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.073` → IC=+0.310 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.073 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.239 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.181 (n=1126)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.242 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.254 (n=775)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1831` → IC=+0.292 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1831 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3455` → IC=+0.266 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3455 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.073` → IC=+0.255 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.073 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.238 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4177` → IC=+0.259 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4177 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.237 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1781.58` → IC=+0.253 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.58 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.246 (n=352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.0745` → IC=+0.206 (n=352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0745 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=1107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.4118` → IC=+0.226 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4118 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.212 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.506` → IC=+0.236 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.506 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2629` → IC=+0.167 (n=1056)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2629 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.200 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.4154` → IC=+0.200 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4154 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `15762.0138` → IC=+0.169 (n=479)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 15762.0138 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.196 (n=389)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0025 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2883` → IC=+0.154 (n=1160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.2883 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=1060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5553` → IC=+0.183 (n=1160)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5553 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.13` → IC=+0.159 (n=1166)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.13 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.856` → IC=+0.209 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.856 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2113` → IC=+0.154 (n=1160)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2113 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1575` → IC=+0.160 (n=357)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1575 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.143 (n=1050)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.763` → IC=+0.134 (n=700)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.763 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.151 (n=325)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 221.0 (IC base=+0.136)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.225 (n=540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.2094` → IC=+0.214 (n=794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2094 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.786` → IC=+0.278 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.786 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.2133` → IC=+0.196 (n=1149)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.2133 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.9343` → IC=+0.207 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9343 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.208 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `1931.801` → IC=+0.204 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.801 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.236 (n=982)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.252 (n=329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.279 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.256 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.25 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.642` → IC=+0.274 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.642 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3595` → IC=+0.275 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3595 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.6418` → IC=+0.226 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6418 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.2601` → IC=+0.233 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2601 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1862.661` → IC=+0.225 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1862.661 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.221 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.224)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.166 (n=1137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0077 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4318` → IC=+0.161 (n=1135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4318 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.3921` → IC=+0.199 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3921 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1546` → IC=+0.185 (n=756)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1546 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.239 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.048` → IC=+0.152 (n=999)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.048 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6307` → IC=+0.152 (n=1135)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6307 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.223 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4219` → IC=+0.153 (n=370)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4219 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.5308` → IC=+0.177 (n=370)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.5308 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `6915.1659` → IC=+0.182 (n=757)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 6915.1659 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.147 (n=1076)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 168.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.159 (n=1198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0072 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.381` → IC=+0.141 (n=1197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.381 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6186` → IC=+0.170 (n=1197)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6186 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.3435` → IC=+0.137 (n=1289)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.3435 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.91` → IC=+0.177 (n=425)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 6.91 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8526` → IC=+0.142 (n=798)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8526 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.201 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.126 (n=720)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.7982 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.4836` → IC=+0.138 (n=360)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4836 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `9966.3147` → IC=+0.161 (n=543)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 9966.3147 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.157 (n=589)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.01 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=1326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.5169` → IC=+0.200 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5169 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `1.064` → IC=+0.219 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.064 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.569` → IC=+0.252 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.569 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.126 (n=1296)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2233 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` < `0.1661` → IC=+0.128 (n=1294)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1661 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `2.4951` → IC=+0.123 (n=1248)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4951 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=1352)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2888.477` → IC=+0.193 (n=588)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2888.477 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.133 (n=983)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 50.0 (IC base=+0.114)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.151 (n=580)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.006 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.1027` → IC=+0.144 (n=439)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1027 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.208 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.9571` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.9571 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.1948` → IC=+0.137 (n=1204)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1948 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.445` → IC=+0.156 (n=274)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 7.445 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.121 (n=1315)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.1917 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.167 (n=160)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4573` → IC=+0.135 (n=390)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4573 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.1742` → IC=+0.128 (n=530)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.1742 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `3066.2091` → IC=+0.159 (n=438)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3066.2091 (IC base=+0.112)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0184` → IC=+0.209 (n=823)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0184 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1296` → IC=+0.198 (n=412)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1296 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=1278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.198 (n=567)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.7351` → IC=+0.257 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7351 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `1.2191` → IC=+0.224 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2191 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.444` → IC=+0.242 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.444 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `1.209` → IC=+0.200 (n=1234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.209 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `0.8588` → IC=+0.215 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8588 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2376` → IC=+0.277 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2376 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.1696` → IC=+0.207 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1696 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.8114` → IC=+0.204 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8114 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.199 (n=1292)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `2588.9706` → IC=+0.197 (n=823)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2588.9706 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.237 (n=431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.218 (n=586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.218 (n=431)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4426` → IC=+0.247 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4426 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `1.1104` → IC=+0.232 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1104 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.243 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6302` → IC=+0.217 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6302 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.284 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.2444` → IC=+0.196 (n=1015)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2444 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4601` → IC=+0.198 (n=1153)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4601 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2562.5493` → IC=+0.211 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2562.5493 (IC base=+0.205)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.158 (n=557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.172 (n=559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0089 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.154 (n=735)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3963` → IC=+0.181 (n=1668)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.3963 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.3669` → IC=+0.183 (n=493)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.3669 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.719` → IC=+0.175 (n=777)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.719 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.165 (n=964)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8709 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.2058` → IC=+0.151 (n=482)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.2058 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.176 (n=461)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4377` → IC=+0.159 (n=534)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4377 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5596` → IC=+0.173 (n=534)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5596 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=1874)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3232.0177` → IC=+0.151 (n=1112)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3232.0177 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.166 (n=1447)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 166.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.127 (n=1174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0057 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.122 (n=1174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.6561` → IC=+0.132 (n=1759)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6561 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3382` → IC=+0.127 (n=413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.3382 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.144 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 9.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.2422` → IC=+0.148 (n=413)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.2422 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.2846` → IC=+0.160 (n=142)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.2846 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.328` → IC=+0.130 (n=187)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.328 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.7069` → IC=+0.141 (n=182)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.7069 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `14590.6209` → IC=+0.139 (n=275)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 14590.6209 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3374` → IC=+0.139 (n=552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3374 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.143 (n=494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.3447` → IC=+0.197 (n=368)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3447 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.2805` → IC=+0.148 (n=589)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2805 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.41` → IC=+0.148 (n=214)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 4.41 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.7208` → IC=+0.140 (n=493)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.7208 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.1115` → IC=+0.149 (n=477)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1115 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4187` → IC=+0.136 (n=542)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4187 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `334.0` → IC=+0.138 (n=457)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 334.0 (IC base=+0.126)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.267 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.215 (n=163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.215 (n=163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.257 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.433` → IC=+0.251 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.433 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.3651` → IC=+0.253 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3651 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.043` → IC=+0.244 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.043 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.8399` → IC=+0.216 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8399 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.1573` → IC=+0.215 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1573 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2535` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2535 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.3759` → IC=+0.235 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3759 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.391` → IC=+0.272 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.391 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.0789` → IC=+0.173 (n=151)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.0789 (IC base=+0.073)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4189` → IC=-0.127 (n=164)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4189
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=320)

- **FILTRO** `dist_vwap_pct` > `0.3414` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3414
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=450)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.145 (n=246)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0069 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.147 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.245 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.8398` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.8398 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.0671` → IC=+0.133 (n=325)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.0671 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.7231` → IC=+0.131 (n=329)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.7231 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.2136` → IC=+0.152 (n=159)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.2136 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3064.7088` → IC=+0.204 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3064.7088 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 21.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.4189` → IC=+0.158 (n=320)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4189 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.062)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.56 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.8803` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8803 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2547` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2547 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.181 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.022 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.178` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.178 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.576` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.576 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8853` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8853 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.136 (n=201)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6515 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.130 (n=179)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.6848` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.6848 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.200 (n=3028)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=9438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.214 (n=9069)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.8979` → IC=+0.197 (n=1242)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8979 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.603` → IC=+0.226 (n=4417)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.603 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8814` → IC=+0.165 (n=4046)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8814 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.195 (n=1691)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.6244` → IC=+0.187 (n=2895)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6244 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2327.1098` → IC=+0.168 (n=6043)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2327.1098 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.192 (n=6780)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 89.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.191 (n=5498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0069 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1442` → IC=+0.186 (n=3625)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1442 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5657` → IC=+0.238 (n=8235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5657 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2369` → IC=+0.161 (n=5149)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2369 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.903` → IC=+0.198 (n=1166)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.903 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.706` → IC=+0.182 (n=7985)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.706 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.159 (n=2509)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7053 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.245 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.2892` → IC=+0.189 (n=3397)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.2892 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.198 (n=2369)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 24.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.205 (n=517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.207 (n=1030)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3429` → IC=+0.189 (n=1546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3429 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.195 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=1042)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.317 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.472` → IC=+0.350 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.472 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2272` → IC=+0.246 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2272 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.5801` → IC=+0.208 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5801 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=863)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.258 (n=1037)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.262 (n=1053)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1272` → IC=+0.293 (n=520)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1272 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.266 (n=1063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=1076)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.3451` → IC=+0.290 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3451 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.444` → IC=+0.267 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.444 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.295 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `1.8705` → IC=+0.276 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8705 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1773.87` → IC=+0.272 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1773.87 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.193 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0832` → IC=+0.167 (n=484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0832 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=1506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.3102` → IC=+0.201 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3102 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1241` → IC=+0.182 (n=816)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1241 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.755` → IC=+0.166 (n=333)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.755 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.265` → IC=+0.152 (n=1296)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.265 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6272` → IC=+0.180 (n=483)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6272 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2695` → IC=+0.191 (n=208)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2695 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.1195` → IC=+0.158 (n=1226)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1195 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.5037` → IC=+0.153 (n=1245)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5037 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `13659.511` → IC=+0.150 (n=965)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 13659.511 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `481.0` → IC=+0.154 (n=1326)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 481.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.162 (n=1260)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0056 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3172` → IC=+0.158 (n=1260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3172 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.178 (n=426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6443` → IC=+0.192 (n=1260)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6443 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6767` → IC=+0.168 (n=203)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.6767 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1283` → IC=+0.164 (n=1147)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1283 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.5` → IC=+0.165 (n=216)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.5 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.159 (n=1260)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1917 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.196 (n=340)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.159 (n=1162)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7547` → IC=+0.160 (n=774)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7547 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `428.0` → IC=+0.153 (n=936)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 428.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.234 (n=972)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=1522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=1481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.6721` → IC=+0.256 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6721 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.741` → IC=+0.292 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.741 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.2162` → IC=+0.223 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2162 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.9133` → IC=+0.247 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9133 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `1931.1232` → IC=+0.223 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.1232 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.242 (n=1356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.241 (n=1211)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.157` → IC=+0.241 (n=597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.157 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.267 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3648` → IC=+0.271 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3648 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.746` → IC=+0.280 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.746 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3529` → IC=+0.295 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3529 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7875` → IC=+0.237 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7875 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.2286` → IC=+0.237 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2286 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.252 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1915.34` → IC=+0.253 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.34 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.255 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.237)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.180 (n=517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0034 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4353` → IC=+0.142 (n=1547)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4353 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=1616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.6902` → IC=+0.229 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6902 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.5611` → IC=+0.174 (n=443)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.5611 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.224` → IC=+0.161 (n=643)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.224 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.877` → IC=+0.159 (n=1032)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.877 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.236 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5228` → IC=+0.150 (n=658)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5228 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.4706` → IC=+0.152 (n=498)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.4706 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8147.128` → IC=+0.229 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8147.128 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.149 (n=480)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 81.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=1263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4396` → IC=+0.151 (n=1261)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4396 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=580)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6931` → IC=+0.184 (n=1261)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6931 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.362` → IC=+0.139 (n=1262)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.362 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.188 (n=190)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.142 (n=841)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8616 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.1836` → IC=+0.141 (n=421)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.1836 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.255 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.148 (n=1190)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `10998.3764` → IC=+0.207 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10998.3764 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `183.0` → IC=+0.139 (n=1187)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 183.0 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.132 (n=1025)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0079 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.4695` → IC=+0.185 (n=1536)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.4695 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `1.0427` → IC=+0.199 (n=290)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 1.0427 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.403` → IC=+0.229 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.403 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=1069)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2904.4304` → IC=+0.239 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2904.4304 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.126 (n=1170)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 54.0 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.133 (n=1511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0109 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1279` → IC=+0.154 (n=504)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1279 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=1558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.206 (n=1510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.2879` → IC=+0.128 (n=1294)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.2879 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.43` → IC=+0.125 (n=1458)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.43 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.72` → IC=+0.155 (n=665)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.72 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2238` → IC=+0.174 (n=234)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2238 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4566` → IC=+0.138 (n=451)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4566 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.2108` → IC=+0.123 (n=613)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 2.2108 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2839.872` → IC=+0.159 (n=503)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2839.872 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0188` → IC=+0.215 (n=1023)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0188 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.204 (n=1373)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.5124` → IC=+0.245 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5124 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.1878` → IC=+0.225 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1878 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.171` → IC=+0.263 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.171 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.0734` → IC=+0.204 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0734 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6344` → IC=+0.210 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6344 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2361` → IC=+0.240 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2361 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.5313` → IC=+0.233 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5313 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2596.7996` → IC=+0.212 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2596.7996 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.233 (n=559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.220 (n=558)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.201 (n=1765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.257 (n=1672)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.5018` → IC=+0.201 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5018 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.8372` → IC=+0.203 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8372 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.778` → IC=+0.263 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.778 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.237 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.256 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.2198` → IC=+0.196 (n=1311)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2198 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4437` → IC=+0.201 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4437 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2569.2034` → IC=+0.201 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2569.2034 (IC base=+0.201)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=2810)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.158 (n=2388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0093 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.5223` → IC=+0.160 (n=2713)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5223 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=952)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.9399` → IC=+0.211 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9399 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1884` → IC=+0.163 (n=954)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1884 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.4942` → IC=+0.141 (n=1605)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.4942 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.174` → IC=+0.181 (n=443)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.174 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.9026` → IC=+0.163 (n=1137)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.9026 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1736` → IC=+0.183 (n=743)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1736 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.459` → IC=+0.155 (n=895)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.459 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8927` → IC=+0.162 (n=1789)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8927 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=1800)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `2755.3734` → IC=+0.154 (n=2424)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2755.3734 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.193 (n=708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0037 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4792` → IC=+0.153 (n=2119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4792 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.160 (n=724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.1782` → IC=+0.162 (n=933)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1782 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.6851` → IC=+0.143 (n=399)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.6851 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.2426` → IC=+0.126 (n=1896)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.2426 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.225` → IC=+0.141 (n=2104)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 6.225 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.9017` → IC=+0.149 (n=1347)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.9017 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0721` → IC=+0.148 (n=994)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0721 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.138 (n=923)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.8156` → IC=+0.141 (n=1398)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8156 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=2810)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `7357.6757` → IC=+0.146 (n=1893)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 7357.6757 (IC base=+0.133)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.171 (n=314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0056 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.171 (n=317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0033 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.186 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.5194` → IC=+0.199 (n=237)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5194 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2159` → IC=+0.185 (n=163)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.2159 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` < `0.4013` → IC=+0.161 (n=349)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.4013 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.308` → IC=+0.171 (n=384)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 2.308 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `0.8476` → IC=+0.195 (n=237)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.8476 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.3073` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3073 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.194 (n=119)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.6869` → IC=+0.211 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6869 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `12563.2849` → IC=+0.199 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.2849 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.211 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1108` → IC=+0.171 (n=399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1108 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.172 (n=400)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1409 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.142 (n=412)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6091 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.7021` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.7021 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.06` → IC=+0.150 (n=990)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 9.06 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8811` → IC=+0.182 (n=605)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8811 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0696` → IC=+0.162 (n=427)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0696 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4214` → IC=+0.141 (n=302)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4214 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.143 (n=603)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `11328.3365` → IC=+0.147 (n=907)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 11328.3365 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `712.0` → IC=+0.142 (n=862)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 712.0 (IC base=+0.134)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.4173` → IC=+0.173 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4173 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.8576` → IC=+0.167 (n=547)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.8576 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.213` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.213 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.160 (n=835)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0087 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.159 (n=834)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4866` → IC=+0.161 (n=835)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4866 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5456` → IC=+0.157 (n=557)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5456 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.1886` → IC=+0.159 (n=834)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.1886 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `1.006` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 1.006 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.4256` → IC=+0.163 (n=772)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4256 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.161 (n=835)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.0946` → IC=+0.159 (n=734)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0946 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.7181` → IC=+0.156 (n=746)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7181 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1126` → IC=+0.153 (n=771)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1126 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1724` → IC=+0.168 (n=245)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1724 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.5244` → IC=+0.159 (n=819)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.5244 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5194` → IC=+0.153 (n=731)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5194 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=813)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.152 (n=694)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0084 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4933` → IC=+0.166 (n=693)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4933 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.150 (n=244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 4.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.0983` → IC=+0.152 (n=693)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.0983 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6358` → IC=+0.167 (n=163)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6358 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.3871` → IC=+0.141 (n=695)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3871 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.966` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.966 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.140 (n=625)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.0954` → IC=+0.150 (n=610)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0954 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.7253` → IC=+0.144 (n=619)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.7253 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.178 (n=299)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.152 (n=598)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7743` → IC=+0.159 (n=453)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7743 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7633.9254` → IC=+0.162 (n=693)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7633.9254 (IC base=+0.139)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=201)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 1.0 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.341` → IC=+0.144 (n=85)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 2.341 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.1616` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1616 (IC base=+0.060)

- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.140 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0118 (IC base=+0.061)

- **PATRÓN** `drift_60min` |x|≤ `0.3887` → IC=+0.133 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.3887 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.2353` → IC=+0.167 (n=70)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.2353 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.8053` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.8053 (IC base=+0.061)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.218 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=328)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=340)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.212 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.5781` → IC=+0.195 (n=700)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5781 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1926` → IC=+0.162 (n=347)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1926 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.488` → IC=+0.209 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.488 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `2.1127` → IC=+0.151 (n=520)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1127 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=569)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2435.8886` → IC=+0.147 (n=307)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2435.8886 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.279 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.1332` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1332 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.637` → IC=+0.126 (n=193)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.637 (IC base=-0.014)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.173 (n=273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0059 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.5656` → IC=+0.196 (n=241)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5656 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.167 (n=124)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `1.0529` → IC=+0.126 (n=212)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0529 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` < `0.0677` → IC=+0.143 (n=180)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.0677 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.2602` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2602 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `2.0118` → IC=+0.189 (n=178)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.0118 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.4946` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.4946 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.6802` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6802 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.412` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.412 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `3560.4084` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3560.4084 (IC base=+0.040)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.271 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=101)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.243 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=101)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.179 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.143 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5578` → IC=+0.223 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5578 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.5279` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.5279 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.217` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.217 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8144` → IC=+0.144 (n=161)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8144 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6396` → IC=+0.141 (n=215)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6396 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.7617` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.7617 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `1.4015` → IC=+0.151 (n=190)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4015 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=254)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `1108.9201` → IC=+0.167 (n=211)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1108.9201 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.174 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1124 (IC base=-0.044)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=-0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.967` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 2.967 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.1312` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1312 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=-0.044)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.0882` → IC=-0.278 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0882
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=44)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.143 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.6923` → IC=+0.187 (n=196)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.6923 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1941` → IC=+0.148 (n=126)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1941 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.244` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.244 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.0856` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0856 (IC base=+0.075)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.127 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0075 (IC base=-0.054)

- **PATRÓN** `ibs_20min` < `0.0882` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0882 (IC base=-0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.174` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 2.174 (IC base=-0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.1383` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1383 (IC base=-0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.9854` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.9854 (IC base=-0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4444 (IC base=-0.054)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `10.0` → IC=-0.409 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=139)

- **FILTRO** `dist_vwap_pct` > `0.2348` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=165)

- **FILTRO** `volumen_regimen` < `0.7307` → IC=-0.352 (n=59)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7307
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=122)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=136)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=126)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=54)

- **FILTRO** `volumen_spike_ratio` > `2.1911` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.1911
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=55)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=47)

- **FILTRO** `volumen_regimen` < `0.7431` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7431
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=47)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.283 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=44)

- **FILTRO** `drift_60min` |x|> `0.1778` → IC=-0.324 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1778
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=43)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8396` → IC=-0.429 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8396
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **FILTRO** `ibs_20min` > `0.6482` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6482
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=41)

- **FILTRO** `dist_vwap_pct` > `0.0767` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0767
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=41)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=20)

- **FILTRO** `volumen_regimen` < `1.0683` → IC=-0.431 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0683
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2075` → IC=-0.135 (n=113)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2075
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=222)

- **FILTRO** `dist_vwap_pct` > `0.6296` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6296
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=309)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.124 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.077)

- **PATRÓN** `ibs_20min` > `0.6592` → IC=+0.157 (n=231)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.6592 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.2075` → IC=+0.125 (n=222)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2075 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.145 (n=105)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.037)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.557` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.557
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **FILTRO** `volumen_regimen` < `0.7797` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=76)

- **PATRÓN** `ibs_20min` > `0.6592` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.6592 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4652` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4652 (IC base=-0.024)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1361 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` < `0.1782` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1782 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.8706` → IC=+0.123 (n=83)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.8706 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3566.36` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3566.36 (IC base=+0.097)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.8361` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8361
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=55)

- **FILTRO** `ibs_20min` > `0.3115` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3115
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=81)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0042 (IC base=+0.059)

- **PATRÓN** `drift_60min` |x|≤ `0.2855` → IC=+0.125 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.2855 (IC base=+0.059)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.8361` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8361 (IC base=+0.059)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `1549.4073` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1549.4073 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.005)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.206 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.176 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0079 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.174 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.7083` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7083 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.6353` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6353 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.03 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.038)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.138 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 16.0 (IC base=+0.108)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=603)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2849.7532` → IC=+0.176 (n=205)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2849.7532 (IC base=+0.108)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.138 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 16.0 (IC base=+0.108)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=603)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2849.7532` → IC=+0.176 (n=205)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2849.7532 (IC base=+0.108)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=76)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=110)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=129)

- **FILTRO** `libro_liquidez` < `2453.3967` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `libro_liquidez` < 2453.3967
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=109)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=201)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=187)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1540)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=49)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=59)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `36073.08` → IC=-0.147 (n=49)

  - _Acción_: SKIP cuando `liq_usd_total` < 36073.08
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=101)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **PATRÓN** `liq_n` > `17.0` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `liq_n` > 17.0 (IC base=+0.033)

- **PATRÓN** `liq_usd_total` > `73032.76` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `liq_usd_total` > 73032.76 (IC base=+0.033)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.998` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.998
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=80)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=692)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=423)

- **FILTRO** `liq_n` < `8.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_n` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=112)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.7738` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.7738
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=96)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=466)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=308)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=308)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.134 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=243)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=170)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=170)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.138 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=140)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=70)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=86)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=183)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=72)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=226)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=226)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=113)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7243)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1058)

- **FILTRO** `libro_liquidez` < `15906.9303` → IC=-0.152 (n=268)

  - _Acción_: SKIP cuando `libro_liquidez` < 15906.9303
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=805)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.177 (n=3058)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=9594)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.171 (n=3205)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=9919)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.218 (n=520)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1658)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.170 (n=549)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=1793)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.203 (n=550)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=1666)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.200 (n=582)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1752)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.165 (n=571)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1763)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.185 (n=538)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=1617)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.193 (n=561)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1775)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2616)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2760)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=2766)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.160 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=342)

- **FILTRO** `ibs_20min` > `0.1763` → IC=-0.142 (n=107)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1763
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=327)

- **FILTRO** `libro_liquidez` < `16818.2369` → IC=-0.146 (n=210)

  - _Acción_: SKIP cuando `libro_liquidez` < 16818.2369
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=630)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=221)

- **FILTRO** `ibs_20min` < `0.0992` → IC=-0.243 (n=72)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0992
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=217)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.188 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=189)

- **FILTRO** `drift_20min_pct` |x|> `0.1486` → IC=-0.159 (n=89)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1486
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=175)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=719)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=223)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.032)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=9097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=20154)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.277 (n=7055)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=22196)

- **FILTRO** `ibs_7min` < `0.2924` → IC=-0.236 (n=7312)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2924
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=21939)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.159 (n=9879)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=19372)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9137)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=27511)

- **FILTRO** `ibs_7min` > `0.2944` → IC=-0.179 (n=9161)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2944
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=27487)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1144)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3643)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.254 (n=1578)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3209)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.180 (n=1145)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3642)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.151 (n=4247)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=2078)

- **FILTRO** `drift_7min_pct` |x|> `0.1117` → IC=-0.125 (n=2146)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1117
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4179)

- **FILTRO** `ibs_7min` > `0.7917` → IC=-0.204 (n=1581)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7917
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4744)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3876)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1222)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3858)

- **FILTRO** `ibs_7min` < `0.7518` → IC=-0.189 (n=1270)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7518
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3810)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.174 (n=1262)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=3818)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.258 (n=1268)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=3870)

- **FILTRO** `ibs_7min` > `0.2589` → IC=-0.173 (n=1284)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2589
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3854)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.185 (n=1280)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3858)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.169 (n=1293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=3233)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.309 (n=1104)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=3422)

- **FILTRO** `ibs_7min` < `0.196` → IC=-0.260 (n=1131)

  - _Acción_: SKIP cuando `ibs_7min` < 0.196
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3395)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.214 (n=1091)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=3435)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.237 (n=1569)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=5150)

- **FILTRO** `ibs_7min` > `0.7598` → IC=-0.177 (n=1679)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7598
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=5040)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=3254)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.238 (n=1417)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=3392)

- **FILTRO** `ibs_7min` < `0.7425` → IC=-0.181 (n=1200)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7425
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=3609)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.178 (n=1201)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3608)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1233)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3703)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.173 (n=1232)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3704)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.191 (n=1203)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3733)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.263 (n=1207)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=3951)

- **FILTRO** `ibs_7min` < `0.7024` → IC=-0.230 (n=1289)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7024
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3869)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1679)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=5270)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.279 (n=1138)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3753)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.232 (n=1222)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=3669)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.211 (n=1173)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3718)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.204 (n=1628)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=4953)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1033)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=514)

- **FILTRO** `libro_liquidez` < `10550.0548` → IC=-0.148 (n=140)

  - _Acción_: SKIP cuando `libro_liquidez` < 10550.0548
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=420)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=542)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.130 (n=706)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.151 (n=236)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 459.6089 (IC base=+0.115)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `312.745` → IC=+0.140 (n=109)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 312.745 (IC base=+0.139)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.096)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.170 (n=95)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.092)

- **PATRÓN** `total_vol_5m` < `391.8444` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 391.8444 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 69.0 (IC base=+0.092)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.180 (n=123)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.185 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 6300.756 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 37.0 (IC base=+0.139)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.151 (n=124)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.141 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 13.0 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `257344.8` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 257344.8 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `3728.9067` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3728.9067 (IC base=+0.104)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.341 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=218)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.122 (n=109)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0044 (IC base=-0.141)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.365 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=51)

- **FILTRO** `T_h` > `87.9957` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=76)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.222 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.141)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0142` → IC=-0.206 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.8485` → IC=-0.243 (n=173)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8485
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=174)

- **FILTRO** `pct_vs_K` |x|> `3.4841` → IC=-0.439 (n=97)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4841
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=189)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `81.2732` → IC=-0.175 (n=81)

  - _Acción_: SKIP cuando `T_h` > 81.2732
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

- **FILTRO** `pct_vs_K` |x|> `2.7217` → IC=-0.337 (n=41)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7217
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=81)

- **FILTRO** `T_h` > `144.6113` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` > 144.6113
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=77)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.443 (n=33)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=67)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4552` → IC=-0.378 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4552
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **FILTRO** `sigma_h` > `0.0095` → IC=-0.300 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=72)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.380 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=72)

- **FILTRO** `T_h` > `64.7514` → IC=-0.331 (n=63)

  - _Acción_: SKIP cuando `T_h` > 64.7514
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0146` → IC=-0.167 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0146
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=61)

- **FILTRO** `T_h` > `135.1308` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `T_h` > 135.1308
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `pct_vs_K` |x|> `5.0364` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.0364
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=61)

- **FILTRO** `sigma_h` < `0.0142` → IC=-0.360 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **FILTRO** `T_h` > `63.9197` → IC=-0.384 (n=41)

  - _Acción_: SKIP cuando `T_h` > 63.9197
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.462 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.386)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.472 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.386)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.444 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.386)

- **PATRÓN** `dist_50` > `0.4444` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.386)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.464 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.386)

- **PATRÓN** `edge` > `0.1023` → IC=+0.457 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.420)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.461 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.420)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.420)

- **PATRÓN** `dist_50` > `0.3938` → IC=+0.483 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3938 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.446 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.420)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.433)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.2825` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2825 (IC base=+0.480)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.469 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.480)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.460 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.480)

- **PATRÓN** `T_h` > `1.1094` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1094 (IC base=+0.480)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.480)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.462 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.480)

- **PATRÓN** `edge` > `0.1327` → IC=+0.471 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1327 (IC base=+0.473)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.474 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.473)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.471 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.473)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.486 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.473)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.462 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.473)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.473)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=149)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=259)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `streak_estiramiento` < 0.4576 (IC base=+0.030)

- **PATRÓN** `streak_estiramiento` < `0.5654` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.5654 (IC base=+0.039)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `ballena_activa_n` > `52.0` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 52.0
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=33)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_racha` < 990711.2 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 52.0 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.120 (n=77)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 50.0 (IC base=+0.054)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=77)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=87)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=671)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=677)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=368)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=538)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1076)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=657)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=660)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2671)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1372)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1380)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.214 (n=632)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.1627` → IC=+0.191 (n=1226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1627 (IC base=+0.184)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2178` → IC=+0.187 (n=464)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.2178 (IC base=+0.184)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1305` → IC=+0.227 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1305 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.198 (n=980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 11.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.185 (n=1403)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 16.0 (IC base=+0.184)

- **PATRÓN** `ibs_15` > `0.6129` → IC=+0.259 (n=1392)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6129 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.4448` → IC=+0.185 (n=328)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.4448 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.5589` → IC=+0.172 (n=1372)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.5589 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.101` → IC=+0.269 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.101 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2972.0706` → IC=+0.189 (n=928)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2972.0706 (IC base=+0.184)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=477)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.221 (n=220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.286 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.203)

- **PATRÓN** `drift_15min` |x|≤ `0.3804` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3804 (IC base=+0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.232 (n=110)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.203)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1492` → IC=+0.281 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1492 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.226 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.268 (n=330)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.3824` → IC=+0.281 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3824 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.257 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `14933.948` → IC=+0.230 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14933.948 (IC base=+0.203)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `25.228` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 25.228
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=307)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.161 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0034 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.156 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0058 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.167 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.140)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.161 (n=219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.140)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.263` → IC=+0.168 (n=227)

  - _Acción_: Kelly boost +0.84€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.263 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.140 (n=331)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 16.0 (IC base=+0.140)

- **PATRÓN** `ibs_15` > `0.6192` → IC=+0.218 (n=328)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6192 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.5388` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.5388 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.157` → IC=+0.158 (n=255)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.157 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.56` → IC=+0.208 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.56 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `9553.1781` → IC=+0.142 (n=149)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 9553.1781 (IC base=+0.140)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.167 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `ibs_15` > `0.2175` → IC=-0.250 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2175
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=69)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.233 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.195 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.155)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.188 (n=155)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=+0.155)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3414` → IC=+0.229 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3414 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.192 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 11.0 (IC base=+0.155)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.239 (n=174)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.116` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.116 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.4684` → IC=+0.162 (n=190)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4684 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=136)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `3004.732` → IC=+0.265 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3004.732 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.213 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.155)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.7151` → IC=-0.143 (n=96)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.7151
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=772)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.662` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 15.662 (IC base=+0.010)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.242 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.192 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.178)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0402` → IC=+0.187 (n=378)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.0402 (IC base=+0.178)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0926` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0926 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.231 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.178)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.274 (n=378)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1219` → IC=+0.191 (n=228)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1219 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.6263` → IC=+0.182 (n=441)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.6263 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.006` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.006 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.489` → IC=+0.178 (n=340)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 7.489 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2857.7208` → IC=+0.250 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2857.7208 (IC base=+0.178)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.165 (n=422)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.1176 (IC base=+0.045)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.377 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.339)

- **PATRÓN** `drift_60min` |x|≤ `0.1089` → IC=+0.349 (n=249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1089 (IC base=+0.339)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.364 (n=248)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=+0.339)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.392 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.339)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.361 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.339)

- **PATRÓN** `ibs_15` > `0.7856` → IC=+0.382 (n=372)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7856 (IC base=+0.339)

- **PATRÓN** `dist_vwap_pct` > `0.4241` → IC=+0.385 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4241 (IC base=+0.339)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.117` → IC=+0.352 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.117 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.345 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.356 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.339)

- **PATRÓN** `ballena_activa_n` < `475.0` → IC=+0.364 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 475.0 (IC base=+0.339)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.345 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.389 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.343)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.350 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.343)

- **PATRÓN** `drift_15min` |x|≤ `0.4202` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4202 (IC base=+0.343)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.366 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.343)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.414 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.372 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.343)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.342 (n=220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.343)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.377 (n=210)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.343)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.418 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.597` → IC=+0.349 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.597 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `15510.5632` → IC=+0.347 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15510.5632 (IC base=+0.343)

- **PATRÓN** `ballena_activa_n` < `585.0` → IC=+0.402 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 585.0 (IC base=+0.343)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.365 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.1039` → IC=+0.347 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1039 (IC base=+0.331)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.342 (n=163)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.331)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.359 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.383 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.331)

- **PATRÓN** `ibs_15` > `0.7403` → IC=+0.391 (n=163)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7403 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` > `0.4449` → IC=+0.349 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4449 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` < `0.1175` → IC=+0.348 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1175 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.275` → IC=+0.362 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.275 (IC base=+0.331)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.343 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `3507.1457` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3507.1457 (IC base=+0.331)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.013` → IC=-0.212 (n=599)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1800)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.189 (n=776)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1623)

- **FILTRO** `libro_liquidez` < `3907.8213` → IC=-0.134 (n=1583)

  - _Acción_: SKIP cuando `libro_liquidez` < 3907.8213
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=816)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.261 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=-0.060)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.266 (n=591)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6314 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` > `0.5648` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.5648 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.180 (n=463)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2675 (IC base=-0.060)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1175` → IC=+0.240 (n=975)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1175 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1786` → IC=+0.241 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1786 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3542` → IC=+0.281 (n=1459)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3542 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.8637` → IC=+0.277 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8637 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.221 (n=363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1091)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.226 (n=479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=975)

- **FILTRO** `sigma_ewma_delta_pct` > `19.716` → IC=-0.245 (n=257)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.716
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1197)

- **FILTRO** `libro_liquidez` < `16115.0866` → IC=-0.203 (n=959)

  - _Acción_: SKIP cuando `libro_liquidez` < 16115.0866
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=495)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.186 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0027 (IC base=+0.083)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.278 (n=70)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.083)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.083)

- **PATRÓN** `ibs_15` > `0.8109` → IC=+0.349 (n=137)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8109 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1316` → IC=+0.298 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1316 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `0.5257` → IC=+0.278 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5257 (IC base=+0.083)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6642` → IC=-0.208 (n=94)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6642
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=282)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=359)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.174 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0051 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0771` → IC=+0.216 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0771 (IC base=+0.140)

- **PATRÓN** `drift_15min` |x|≤ `0.4223` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `drift_15min` |x|≤ 0.4223 (IC base=+0.140)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.153 (n=188)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.140)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.236 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `ibs_15` > `0.6642` → IC=+0.257 (n=282)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6642 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1175` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1175 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.579` → IC=+0.156 (n=225)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.579 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=359)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `10966.626` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 10966.626 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.239 (n=593)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `0.7762` → IC=+0.233 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7762 (IC base=+0.226)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2` → IC=+0.257 (n=269)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.246 (n=262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.226)

- **PATRÓN** `ibs_15` < `0.356` → IC=+0.265 (n=593)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.356 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.7133` → IC=+0.269 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7133 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.01` → IC=+0.243 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.01 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.254` → IC=+0.230 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.254 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `3531.6592` → IC=+0.229 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3531.6592 (IC base=+0.226)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1671` → IC=-0.225 (n=194)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1671
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=377)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.257 (n=142)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=429)

- **FILTRO** `sigma_ewma_delta_pct` > `18.011` → IC=-0.133 (n=300)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.011
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2422)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.161)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.161)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0726` → IC=+0.220 (n=244)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0726 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3636` → IC=+0.260 (n=273)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3636 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.1863` → IC=+0.216 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1863 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0196` → IC=-0.262 (n=360)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0196
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=362)

- **FILTRO** `drift_15min` |x|> `1.2` → IC=-0.242 (n=180)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=542)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=181)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=541)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1533` → IC=+0.281 (n=135)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1533 (IC base=-0.045)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.370 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.313 (n=405)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` > `1.0689` → IC=+0.402 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0689 (IC base=-0.045)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.2378` → IC=+0.160 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2378 (IC base=+0.077)

- **PATRÓN** `drift_15min` |x|≤ `0.5874` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `drift_15min` |x|≤ 0.5874 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.077)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.2378` → IC=+0.160 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2378 (IC base=+0.077)

- **PATRÓN** `drift_15min` |x|≤ `0.5874` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `drift_15min` |x|≤ 0.5874 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.077)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.296 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.295 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.320 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.300 (n=203)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.327 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.328 (n=609)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2735` → IC=+0.332 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2735 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.324 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.293 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `14356.961` → IC=+0.305 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14356.961 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.310 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.295 (n=154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.335 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.284)

- **PATRÓN** `drift_15min` |x|≤ `0.3892` → IC=+0.283 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3892 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.291 (n=113)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1428` → IC=+0.326 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1428 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.304 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.312 (n=339)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.365 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.359 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `15942.3752` → IC=+0.326 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15942.3752 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.309 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.1133` → IC=+0.309 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1133 (IC base=+0.298)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.314 (n=181)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.298)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.343 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.330 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.298)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.342 (n=270)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.6102` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6102 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` < `0.167` → IC=+0.299 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.167 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.167` → IC=+0.328 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.167 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.308 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2669` → IC=-0.181 (n=67)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2669
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=204)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1129` → IC=-0.181 (n=67)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1129
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=204)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.121` → IC=-0.164 (n=105)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.121
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=327)

- **FILTRO** `drift_15min` |x|> `0.4386` → IC=-0.135 (n=146)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4386
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=286)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.14` → IC=-0.141 (n=51)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.14
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=106)

- **FILTRO** `drift_60min` |x|> `0.1544` → IC=-0.214 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1544
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1066` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1066
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `79.3918` → IC=+0.177 (n=255)

  - _Acción_: Kelly boost +0.89€ cuando `T_h` > 79.3918 (IC base=+0.170)

- **PATRÓN** `ratio` < `0.9749` → IC=+0.462 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9749 (IC base=+0.170)

- **PATRÓN** `T_h` > `145.8152` → IC=+0.403 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8152 (IC base=+0.339)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.371 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.339)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.4275` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `T_h` > 144.4275 (IC base=+0.136)

- **PATRÓN** `ratio` < `0.9934` → IC=+0.286 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9934 (IC base=+0.136)

- **PATRÓN** `T_h` > `97.9834` → IC=+0.301 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 97.9834 (IC base=+0.293)

- **PATRÓN** `ratio` > `1.0413` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0413 (IC base=+0.293)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `89.3454` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 89.3454 (IC base=+0.220)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.401 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.220)

- **PATRÓN** `T_h` > `102.4835` → IC=+0.338 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 102.4835 (IC base=+0.316)

- **PATRÓN** `ratio` > `1.0083` → IC=+0.344 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0083 (IC base=+0.316)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1402` → IC=+0.455 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1402 (IC base=+0.404)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6129 sube el IC de +0.184 a +0.259 en UPDOWN_GBM#15min (n=1392). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.203 a +0.268 en UPDOWN_GBM#BTC#15min (n=330). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6192 sube el IC de +0.140 a +0.218 en UPDOWN_GBM#ETH#15min (n=328). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.155 a +0.239 en UPDOWN_GBM#SOL#15min (n=174). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.178 a +0.274 en UPDOWN_GBM#XRP#15min (n=378). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.045 a +0.165 en UPDOWN_GBM#XRP#15min (n=422). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6314 sube el IC de -0.060 a +0.266 en UPDOWN_GBM_15M_TARDIO (n=591). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3542 sube el IC de -0.039 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1459). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8109 sube el IC de +0.083 a +0.349 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=137). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6642 sube el IC de +0.140 a +0.257 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=282). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.356 sube el IC de +0.226 a +0.265 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=593). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.161 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3636 sube el IC de -0.044 a +0.260 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=273). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.045 a +0.313 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=405). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.291 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=609). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.284 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=339). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.298 a +0.342 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=270). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7856 sube el IC de +0.339 a +0.382 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=372). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.343 a +0.377 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=210). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7403 sube el IC de +0.331 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=163). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1240 | +0.089 | +150.18€ | 2 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1240 | +0.089 | +150.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 912 | +0.099 | +126.83€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 912 | +0.099 | +126.83€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 242 | +0.045 | +4.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 242 | +0.045 | +4.70€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 23251 | -0.092 | -3088.19€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1392 | -0.046 | -208.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 21859 | -0.095 | -2879.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3539 | -0.088 | -578.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3539 | -0.088 | -578.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1392 | -0.046 | -208.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1392 | -0.046 | -208.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6660 | -0.032 | -604.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6660 | -0.032 | -604.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6135 | -0.095 | -438.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6135 | -0.095 | -438.42€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5151 | -0.180 | -1098.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5151 | -0.180 | -1098.04€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 15642 | -0.033 | +4140.29€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4116 | -0.002 | +1828.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 11526 | -0.043 | +2311.32€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 15642 | -0.033 | +4140.29€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4116 | -0.002 | +1828.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 11526 | -0.043 | +2311.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1389 | -0.101 | -179.14€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 155 | -0.048 | -17.42€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1234 | -0.108 | -161.72€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 765 | -0.091 | -95.93€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 131 | -0.041 | -12.20€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 634 | -0.101 | -83.73€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 426 | -0.126 | -69.33€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 402 | -0.129 | -64.11€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 85021 | +0.113 | -4329.41€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13043 | +0.183 | -434.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 335 | -0.102 | -47.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 65989 | +0.100 | -3659.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5654 | +0.110 | -187.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 10983 | +0.097 | -974.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 43 | -0.167 | -2.82€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 10925 | +0.099 | -960.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 17200 | +0.132 | -346.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4066 | +0.201 | -142.02€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 10936 | +0.112 | -162.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2156 | +0.108 | -19.93€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11023 | +0.088 | -1073.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 50 | -0.077 | -4.56€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 10958 | +0.089 | -1057.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 18141 | +0.124 | -349.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5040 | +0.175 | -80.60€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11047 | +0.106 | -208.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2042 | +0.098 | -51.29€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 16674 | +0.115 | -944.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3801 | +0.186 | -211.98€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 238 | -0.062 | +6.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11179 | +0.093 | -622.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1456 | +0.130 | -116.76€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11000 | +0.102 | -640.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 43 | -0.033 | +7.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 10944 | +0.103 | -648.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 13474 | +0.191 | -900.30€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 13474 | +0.191 | -900.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3255 | +0.168 | -348.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3255 | +0.168 | -348.47€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 976 | +0.194 | -1.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 976 | +0.194 | -1.87€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3185 | +0.181 | -274.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3185 | +0.181 | -274.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2851 | +0.240 | -85.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2851 | +0.240 | -85.78€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3128 | +0.190 | -203.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3128 | +0.190 | -203.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 639 | +0.427 | -21.57€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 639 | +0.427 | -21.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 242 | +0.430 | -5.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 242 | +0.430 | -5.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 240 | +0.434 | -3.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 240 | +0.434 | -3.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 149 | +0.401 | -11.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 149 | +0.401 | -11.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 46221 | +0.197 | -3686.99€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 46221 | +0.197 | -3686.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8021 | +0.174 | -956.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8021 | +0.174 | -956.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7367 | +0.224 | -270.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7367 | +0.224 | -270.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 7988 | +0.173 | -969.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 7988 | +0.173 | -969.79€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7456 | +0.219 | -291.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7456 | +0.219 | -291.91€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 7631 | +0.204 | -502.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 7631 | +0.204 | -502.74€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 7758 | +0.193 | -695.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 7758 | +0.193 | -695.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 17364 | +0.120 | +194.05€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 17364 | +0.120 | +194.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 8614 | +0.124 | +152.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 8614 | +0.124 | +152.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 8750 | +0.116 | +41.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 8750 | +0.116 | +41.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1377 | +0.290 | -13.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1377 | +0.290 | -13.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 613 | +0.274 | -21.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 613 | +0.274 | -21.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 661 | +0.296 | +6.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 661 | +0.296 | +6.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 103 | +0.338 | +1.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 103 | +0.338 | +1.04€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 605 | +0.437 | -0.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 605 | +0.437 | -0.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 284 | +0.437 | -0.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 284 | +0.437 | -0.92€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 281 | +0.440 | +0.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 281 | +0.440 | +0.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 40 | +0.381 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 40 | +0.381 | -0.11€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1003 | +0.076 | -38.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 349 | +0.061 | -27.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 654 | +0.084 | -10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 59 | +0.139 | +5.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 59 | +0.139 | +5.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 788 | +0.085 | -12.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 134 | +0.088 | -1.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 654 | +0.084 | -10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 156 | +0.006 | -31.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 156 | +0.006 | -31.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 31589 | +0.098 | -952.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2625 | +0.091 | +23.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 28964 | +0.099 | -976.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 17835 | +0.103 | -270.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2625 | +0.091 | +23.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 15210 | +0.105 | -294.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 5773 | +0.110 | -12.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 5773 | +0.110 | -12.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 7981 | +0.080 | -670.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 7981 | +0.080 | -670.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 765 | +0.228 | -90.32€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 765 | +0.228 | -90.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 765 | +0.228 | -90.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 765 | +0.228 | -90.32€ | 1 | 4 |
| ✅ GBM_LATE_15M | 22975 | +0.079 | +10721.44€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 22975 | +0.079 | +10721.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3806 | +0.192 | +2747.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3806 | +0.192 | +2747.42€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 3406 | +0.173 | +2300.65€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3406 | +0.173 | +2300.65€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 3953 | +0.200 | +2971.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3953 | +0.200 | +2971.69€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3422 | +0.014 | +648.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3422 | +0.014 | +648.11€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3337 | -0.033 | +786.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3337 | -0.033 | +786.38€ | 4 | 16 |
| ✅ GBM_LATE_15M#XRP | 5051 | -0.045 | +1267.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5051 | -0.045 | +1267.19€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 24268 | +0.082 | +12705.27€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 24268 | +0.082 | +12705.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4607 | +0.015 | +2587.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4607 | +0.015 | +2587.45€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5077 | +0.010 | +1008.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5077 | +0.010 | +1008.86€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3427 | +0.263 | +3455.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3427 | +0.263 | +3455.75€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3904 | -0.003 | +700.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3904 | -0.003 | +700.05€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3948 | +0.022 | +1472.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3948 | +0.022 | +1472.20€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3305 | +0.272 | +3480.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3305 | +0.272 | +3480.97€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 18586 | +0.167 | +13688.34€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 18586 | +0.167 | +13688.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2784 | +0.206 | +2206.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2784 | +0.206 | +2206.25€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2953 | +0.148 | +2110.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2953 | +0.148 | +2110.71€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2894 | +0.209 | +2312.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2894 | +0.209 | +2312.48€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3108 | +0.134 | +2116.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3108 | +0.134 | +2116.14€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3479 | +0.113 | +2315.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3479 | +0.113 | +2315.39€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3368 | +0.201 | +2627.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3368 | +0.201 | +2627.37€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4568 | +0.122 | +1845.33€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4568 | +0.122 | +1845.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1285 | +0.117 | +540.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1285 | +0.117 | +540.11€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1251 | +0.142 | +555.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1251 | +0.142 | +555.52€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 975 | +0.087 | +276.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 975 | +0.087 | +276.00€ | 2 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 23065 | +0.173 | +16887.60€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 23065 | +0.173 | +16887.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3630 | +0.219 | +3035.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3630 | +0.219 | +3035.02€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3609 | +0.148 | +2335.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3609 | +0.148 | +2335.86€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3749 | +0.227 | +3244.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3749 | +0.227 | +3244.67€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3743 | +0.135 | +2495.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3743 | +0.135 | +2495.74€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4059 | +0.108 | +2462.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4059 | +0.108 | +2462.74€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4275 | +0.202 | +3313.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4275 | +0.202 | +3313.57€ | 0 | 26 |
| ✅ GBM_LATE_5M | 6442 | +0.143 | +3558.03€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 6442 | +0.143 | +3558.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 589 | +0.185 | +410.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 589 | +0.185 | +410.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1682 | +0.141 | +1074.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1682 | +0.141 | +1074.97€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 2035 | +0.146 | +1108.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2035 | +0.146 | +1108.89€ | 0 | 32 |
| ✅ GBM_LATE_5M#SOL | 428 | +0.060 | +82.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 428 | +0.060 | +82.58€ | 1 | 7 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1491 | +0.067 | +646.71€ | 2 | 12 |
| ✅ GBM_LATE_60M#60min | 1491 | +0.067 | +646.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 536 | +0.084 | +216.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 536 | +0.084 | +216.93€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 495 | +0.073 | +267.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 495 | +0.073 | +267.26€ | 2 | 17 |
| ✅ GBM_LATE_60M#SOL | 460 | +0.039 | +162.52€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 460 | +0.039 | +162.52€ | 1 | 11 |
| 🚫 GBM_LATE_60M_FADE | 337 | -0.267 | -28.94€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 337 | -0.267 | -28.94€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 127 | -0.221 | -9.65€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 127 | -0.221 | -9.65€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 112 | -0.281 | -11.47€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 112 | -0.281 | -11.47€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 98 | -0.300 | -7.82€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 98 | -0.300 | -7.82€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 643 | +0.057 | +122.23€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 643 | +0.057 | +122.23€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 253 | +0.049 | +41.89€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 253 | +0.049 | +41.89€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 189 | +0.029 | -3.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 189 | +0.029 | -3.13€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 201 | +0.091 | +83.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 201 | +0.091 | +83.47€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 81 | +0.259 | +61.45€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 81 | +0.259 | +61.45€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 81 | +0.259 | +61.45€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 81 | +0.259 | +61.45€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1705 | +0.100 | +466.26€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1705 | +0.100 | +466.26€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1705 | +0.100 | +466.26€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1705 | +0.100 | +466.26€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 367 | -0.080 | -33.57€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 367 | -0.080 | -33.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 125 | -0.020 | -3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 125 | -0.020 | -3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1738 | +0.005 | +8.87€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1738 | +0.005 | +8.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 88 | -0.022 | -4.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 88 | -0.022 | -4.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 184 | -0.005 | +7.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 184 | -0.005 | +7.92€ | 2 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 123 | -0.036 | -5.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 123 | -0.036 | -5.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 739 | +0.034 | +27.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 739 | +0.034 | +27.15€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 463 | -0.005 | -7.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 463 | -0.005 | -7.69€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 141 | -0.052 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 141 | -0.052 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 997 | -0.046 | -28.21€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 997 | -0.046 | -28.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 286 | -0.042 | -11.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 286 | -0.042 | -11.87€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 327 | -0.035 | -4.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 327 | -0.035 | -4.23€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 384 | -0.060 | -12.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 384 | -0.060 | -12.11€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 14107 | -0.012 | -211.91€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14107 | -0.012 | -211.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2824 | -0.024 | -65.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2824 | -0.024 | -65.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 25776 | -0.009 | +1157.42€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 25776 | -0.009 | +1157.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4520 | +0.014 | +573.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4520 | +0.014 | +573.32€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4062 | -0.027 | -40.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4062 | -0.027 | -40.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4550 | +0.011 | +395.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4550 | +0.011 | +395.79€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3842 | -0.051 | -130.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3842 | -0.051 | -130.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4311 | -0.011 | +171.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4311 | -0.011 | +171.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4491 | +0.004 | +187.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4491 | +0.004 | +187.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5477 | -0.052 | -127.29€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5477 | -0.052 | -127.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1274 | -0.071 | -30.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1274 | -0.071 | -30.69€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 553 | -0.118 | -21.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 553 | -0.118 | -21.12€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1557 | -0.070 | -28.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1557 | -0.070 | -28.81€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 847 | -0.016 | -25.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 847 | -0.016 | -25.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 65899 | -0.074 | +1467.54€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 65899 | -0.074 | +1467.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11112 | -0.080 | +633.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11112 | -0.080 | +633.77€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10218 | -0.093 | -451.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10218 | -0.093 | -451.98€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 11245 | -0.070 | +609.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 11245 | -0.070 | +609.17€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 9745 | -0.094 | -184.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 9745 | -0.094 | -184.01€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 12107 | -0.049 | +346.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 12107 | -0.049 | +346.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 11472 | -0.063 | +514.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 11472 | -0.063 | +514.09€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6900 | -0.024 | -102.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6900 | -0.024 | -102.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1608 | -0.025 | -3.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1608 | -0.025 | -3.87€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1534 | -0.019 | -8.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1534 | -0.019 | -8.45€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1022 | -0.039 | -16.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1022 | -0.039 | -16.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1077 | +0.108 | +359.61€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 941 | +0.115 | +347.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 217 | +0.139 | +109.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 217 | +0.139 | +109.57€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 186 | +0.096 | +44.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 186 | +0.096 | +44.24€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 189 | +0.092 | +58.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 189 | +0.092 | +58.12€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 164 | +0.139 | +78.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 164 | +0.139 | +78.91€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 185 | +0.104 | +56.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 185 | +0.104 | +56.17€ | 0 | 5 |
| ✅ PRICE_TARGET_GBM | 514 | -0.087 | -18.52€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 233 | -0.130 | -42.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 185 | -0.174 | -45.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 179 | -0.080 | +4.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 135 | -0.091 | -3.97€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 102 | +0.000 | +19.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 80 | -0.012 | +13.30€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 400 | -0.114 | -36.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 633 | -0.210 | -40.11€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 259 | -0.197 | -33.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 222 | -0.192 | -32.62€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 223 | -0.229 | -24.49€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 191 | -0.241 | -29.15€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 151 | -0.199 | +17.39€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 135 | -0.201 | +12.72€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 548 | -0.213 | -49.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 251 | +0.413 | +202.21€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 65 | +0.396 | +60.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 65 | +0.396 | +60.03€ | 0 | 3 |
| ✅ RESOLUTION_SNIPER#SOL | 158 | +0.481 | +146.93€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 158 | +0.481 | +146.93€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#sniper | 251 | +0.413 | +202.21€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 446 | +0.036 | +19.36€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 446 | +0.036 | +19.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 210 | +0.038 | +7.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 210 | +0.038 | +7.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 48 | -0.020 | -3.52€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 48 | -0.020 | -3.52€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 162 | +0.037 | +11.44€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 162 | +0.037 | +11.44€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 2623 | -0.025 | -115.45€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2623 | -0.025 | -115.45€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 565 | -0.022 | -22.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 565 | -0.022 | -22.81€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1099 | -0.028 | -50.77€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1099 | -0.028 | -50.77€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 65 | -0.037 | -4.30€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 65 | -0.037 | -4.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 28 | +0.033 | -0.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 28 | +0.033 | -0.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7236 | +0.024 | +111.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7236 | +0.024 | +111.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1565 | +0.034 | +46.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1565 | +0.034 | +46.22€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2191 | +0.013 | +6.15€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2191 | +0.013 | +6.15€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1359 | +0.032 | +38.70€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1359 | +0.032 | +38.70€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6747 | +0.011 | -48.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6747 | +0.011 | -48.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2690 | +0.016 | -7.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2690 | +0.016 | -7.31€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2653 | +0.011 | -17.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2653 | +0.011 | -17.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1404 | -0.001 | -23.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1404 | -0.001 | -23.39€ | 2 | 0 |
| ✅ UPDOWN_GBM | 32150 | +0.031 | +1892.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 8619 | +0.062 | +1482.21€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1183 | +0.005 | +8.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 20293 | +0.022 | +387.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1932 | +0.006 | +15.38€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3029 | +0.071 | +332.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 462 | +0.153 | +187.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 23 | -0.020 | -0.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2544 | +0.057 | +145.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 5995 | +0.032 | +388.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1079 | +0.077 | +240.03€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 328 | +0.021 | +7.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3675 | +0.028 | +126.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 866 | +0.002 | +13.84€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 47 | -0.112 | +0.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3780 | +0.040 | +214.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 434 | +0.144 | +164.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 18 | +0.000 | -0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3328 | +0.026 | +49.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 6778 | +0.020 | +277.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2270 | +0.044 | +247.20€ | 0 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 316 | +0.006 | +7.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3488 | +0.010 | +20.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 664 | +0.004 | -1.84€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 40 | -0.143 | +3.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 7852 | +0.017 | +199.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2190 | +0.022 | +131.45€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 310 | -0.006 | -2.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4916 | +0.018 | +70.46€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 402 | +0.015 | +3.38€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 34 | -0.167 | -2.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4714 | +0.035 | +482.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2184 | +0.076 | +511.18€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 188 | -0.005 | -3.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2342 | -0.001 | -25.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 121 | -0.142 | +1.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 496 | +0.339 | +146.94€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 496 | +0.339 | +146.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 279 | +0.343 | +81.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 279 | +0.343 | +81.10€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 217 | +0.331 | +65.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 217 | +0.331 | +65.84€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 10643 | -0.043 | +2260.59€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 10643 | -0.043 | +2260.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 626 | -0.045 | +333.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 626 | -0.045 | +333.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1992 | -0.122 | +53.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1992 | -0.122 | +53.46€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 265 | +0.163 | +157.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 265 | +0.163 | +157.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1166 | +0.199 | +663.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1166 | +0.199 | +663.65€ | 2 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3293 | -0.064 | +523.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3293 | -0.064 | +523.17€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3301 | -0.077 | +530.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3301 | -0.077 | +530.12€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 122 | +0.057 | +11.27€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 122 | +0.057 | +11.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 122 | +0.057 | +11.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 122 | +0.057 | +11.27€ | 2 | 4 |
| ✅ UPDOWN_GBM_IBS_ALTO | 811 | +0.291 | +661.12€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 811 | +0.291 | +661.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 451 | +0.284 | +342.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 451 | +0.284 | +342.51€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 360 | +0.298 | +318.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 360 | +0.298 | +318.60€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 703 | -0.107 | -79.70€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 703 | -0.107 | -79.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 196 | -0.066 | -11.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 196 | -0.066 | -11.78€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 69 | -0.162 | -8.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 69 | -0.162 | -8.81€ | 3 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 60 | -0.210 | -9.56€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 60 | -0.210 | -9.56€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2170 | +0.302 | +1087.84€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 737 | +0.250 | +107.54€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 800 | +0.289 | +322.26€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 633 | +0.376 | +658.04€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.023 n=430 — no justifica filtro, seguir monitorizando
  - _Datos_: n=430 IC=+0.023 PNL=+23.10€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 497 celda(s) pasan gate riguroso completo de 2129 evaluadas (n>=40) y 3137 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.021 < 0.08 — monitorear
  - _Datos_: n=2188 IC=+0.021 PNL=+130.48€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=800/15 IC=+0.289 PNL=+322.26€ | BTC: n=737/15 IC=+0.250 PNL=+107.54€ | SOL: n=633/15 IC=+0.376 PNL=+658.04€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 29 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.098 n=242/60 | contraria IC=+0.145 n=229 | gap=-0.047 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=266, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=663/40 IC=+0.005 PNL=-1.33€ | BTC#60min: n=864/40 IC=+0.002 PNL=+13.86€ | SOL#60min: n=401/40 IC=+0.014 PNL=+2.77€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.052 n=301915 | tras_1loss IC=+0.075 n=235133 | tras_2loss IC=+0.044 n=99777/40 | gap=+0.008 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=285 PNL=+183.63€
  - _Datos_: n=285 IC=+0.179 PNL=+183.63€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.212 > 0.08 con n=335 PNL=+234.80€
  - _Datos_: n=335 IC=+0.212 PNL=+234.80€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.269 > 0.08 con n=37 PNL=+31.71€
  - _Datos_: n=37 IC=+0.269 PNL=+31.71€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=1806 PNL=+1050.67€
  - _Datos_: n=1806 IC=+0.334 PNL=+1050.67€

**🟡 H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=250 PNL=+33.14€
  - _Datos_: n=250 IC=+0.083 PNL=+33.14€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=49 IC=+0.186 PNL=+32.29€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=49 IC=+0.186 PNL=+32.29€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 3/15 ops en el filtro definido (IC actual=+0.045 PNL=+5.14€)
  - _Datos_: n=3 IC=+0.045 PNL=+5.14€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 1/20 ops en el filtro definido (IC actual=+0.008 PNL=+1.96€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.96€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=1399 IC=+0.012 PNL=+4.97€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1399 IC=+0.012 PNL=+4.97€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=529 IC=-0.010 PNL=+10.34€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=529 IC=-0.010 PNL=+10.34€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=430 IC=+0.023 PNL=+23.10€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=430 IC=+0.023 PNL=+23.10€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.1 con n=1854 PNL=+1137.11€
  - _Datos_: n=1854 IC=+0.184 PNL=+1137.11€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1077 IC=+0.077 PNL=+240.06€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1077 IC=+0.077 PNL=+240.06€

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
  - _Estado_: n=470 IC=+0.015 PNL=+35.03€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=470 IC=+0.015 PNL=+35.03€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=40 IC=+0.024 PNL=+0.32€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=40 IC=+0.024 PNL=+0.32€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.259 n=81) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=81 IC=+0.259 PNL=+61.45€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=618 PNL=+240.86€
  - _Datos_: n=618 IC=+0.124 PNL=+240.86€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: n=11031 IC=+0.055 PNL=+1350.27€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=11031 IC=+0.055 PNL=+1350.27€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.167 < -0.1 con n=205 PNL=+17.31€
  - _Datos_: n=205 IC=-0.167 PNL=+17.31€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1679 IC=+0.045 PNL=+179.11€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1679 IC=+0.045 PNL=+179.11€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=65 IC=-0.127 PNL=+3.73€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=65 IC=-0.127 PNL=+3.73€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.1 con n=343 PNL=+105.98€
  - _Datos_: n=343 IC=+0.132 PNL=+105.98€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 4/20 ops en el filtro definido (IC actual=-0.067 PNL=-2.04€)
  - _Datos_: n=4 IC=-0.067 PNL=-2.04€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=15870 IC=-0.138 PNL=+1078.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=15870 IC=-0.138 PNL=+1078.57€

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
  - _Estado_: n=1739 IC=+0.136 PNL=+922.58€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1739 IC=+0.136 PNL=+922.58€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=3394 IC=+0.019 PNL=+108.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3394 IC=+0.019 PNL=+108.52€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=1878 PNL=+976.81€
  - _Datos_: n=1878 IC=+0.084 PNL=+976.81€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.241 < -0.1 con n=1576 PNL=-188.81€
  - _Datos_: n=1576 IC=-0.241 PNL=-188.81€

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

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 33/40 ops en el filtro definido (IC actual=-0.043 PNL=+2.97€)
  - _Datos_: n=33 IC=-0.043 PNL=+2.97€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.093 n=884) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=884 IC=+0.093 PNL=+210.12€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=421) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=421 IC=+0.410 PNL=+589.92€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=8014 IC=+0.174 PNL=-955.02€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8014 IC=+0.174 PNL=-955.02€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.205 > 0.1 con n=127 PNL=+76.45€
  - _Datos_: n=127 IC=+0.205 PNL=+76.45€
