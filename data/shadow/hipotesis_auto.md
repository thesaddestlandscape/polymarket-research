# Hipótesis automáticas — 2026-11-18 22:44 UTC
_Generado por shadow_postmortem.py sobre 1398547 resoluciones (PNL=+195697.39€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=729)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.194 (n=1067)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8124` → IC=+0.270 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8124 (IC base=+0.122)

- **PATRÓN** `banda_z` > `8.339` → IC=+0.192 (n=336)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.339 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=1096)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=518)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.192 (n=930)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.180 (n=298)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 64.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8183` → IC=+0.289 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8183 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.618` → IC=+0.202 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.618 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.133 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=996)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.124)

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
- **FILTRO** `restante_s_al_confirmar` < `131.06` → IC=-0.217 (n=12474)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.06
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=37426)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `123.08` → IC=-0.263 (n=1252)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.08
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3758)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.04` → IC=-0.282 (n=1256)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.04
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3769)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.38` → IC=-0.164 (n=3419)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.38
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=10258)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.8` → IC=-0.239 (n=3418)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.8
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10255)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.73` → IC=-0.268 (n=2329)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.73
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=6989)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=29451)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `7993.7521` → IC=+0.154 (n=2419)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7993.7521 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=25835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=31190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=23434)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8618)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6395.739` → IC=+0.142 (n=3353)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6395.739 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2703)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `16274.2937` → IC=+0.180 (n=702)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 16274.2937 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2758)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16067.9503` → IC=+0.185 (n=712)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16067.9503 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=2334)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.169 (n=647)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.151 (n=1522)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.44 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=5353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.174 (n=2609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.378 (n=1798)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=2561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=2983)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.143 (n=925)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.254 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1168)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.251 (n=978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=746)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=477)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.164 (n=477)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.049)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=1311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.134 (n=1003)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.254 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.200 (n=24461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=21728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.226 (n=8195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=5885)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.175 (n=5758)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.74 (IC base=+0.164)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.212 (n=3577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.209 (n=2557)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.249 (n=1748)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.207)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=5743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.175 (n=4853)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=5882)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=4518)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=4030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1561)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=4750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=4155)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=1006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=996)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `13909.1087` → IC=+0.448 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13909.1087 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12510.8319` → IC=+0.445 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12510.8319 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=398)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.422)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.422)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.422)

- **PATRÓN** `libro_liquidez` > `4833.5247` → IC=+0.425 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4833.5247 (IC base=+0.422)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.401 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.414 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.398)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=38)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=29049)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=33567)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=5064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.177 (n=10790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=15538)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=14101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6069)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.195 (n=4980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=11965)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5405)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.260 (n=5870)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.216 (n=4798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4836)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=4826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5577)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=5725)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=12176)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=13109)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.3` → IC=+0.143 (n=11284)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.3 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5936)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.145 (n=5943)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=7460)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.5` → IC=+0.145 (n=5630)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.5 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6240)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=7931)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.99` → IC=+0.137 (n=7472)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.99 (IC base=+0.116)

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

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.448 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

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
- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

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
- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

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
- **PATRÓN** `drift_60min` |x|≤ `0.496` → IC=+0.140 (n=19243)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.496 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=19498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=13364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.975` → IC=+0.246 (n=6418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.975 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8334` → IC=+0.288 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8334 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.479` → IC=+0.191 (n=9659)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.479 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.697` → IC=+0.269 (n=5234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.697 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.304` → IC=+0.252 (n=1997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.304 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7474` → IC=+0.232 (n=4641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7474 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=9398)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4741.9684` → IC=+0.151 (n=6414)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4741.9684 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.124 (n=12128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0064 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5638` → IC=+0.146 (n=24252)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5638 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.4015` → IC=+0.189 (n=2292)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.4015 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1703` → IC=+0.194 (n=9893)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1703 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8592` → IC=+0.196 (n=6704)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8592 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.234 (n=2442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4559` → IC=+0.209 (n=17046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4559 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=17008)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.246 (n=1362)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3752` → IC=+0.213 (n=4085)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3752 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.274 (n=1854)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.45` → IC=+0.277 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.45 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2349` → IC=+0.256 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2349 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4431` → IC=+0.210 (n=3919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4431 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2032.58` → IC=+0.215 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2032.58 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.218 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.249 (n=2453)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0931` → IC=+0.273 (n=1225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0931 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=3824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=1682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.0752` → IC=+0.281 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0752 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.961` → IC=+0.248 (n=3766)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.961 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.246 (n=3169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.250 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.243 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.8611` → IC=+0.245 (n=2341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8611 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=4213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.241 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.242)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.235 (n=1160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.247 (n=1532)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.224 (n=2472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.8958` → IC=+0.260 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8958 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1942` → IC=+0.234 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1942 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.768` → IC=+0.263 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.768 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6977` → IC=+0.231 (n=3108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6977 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.270 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.4472` → IC=+0.249 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4472 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `15828.3807` → IC=+0.225 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15828.3807 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.182 (n=1676)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0037 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0813` → IC=+0.163 (n=1265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0813 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=2709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.3599` → IC=+0.206 (n=2529)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3599 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.586` → IC=+0.138 (n=605)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.586 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.943` → IC=+0.140 (n=3470)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.943 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6285` → IC=+0.153 (n=1265)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6285 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0982` → IC=+0.159 (n=1387)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0982 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4465` → IC=+0.143 (n=3664)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4465 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=4932)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `192.0` → IC=+0.180 (n=1590)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 192.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.206 (n=1449)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.255 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.929` → IC=+0.283 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.929 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.192 (n=3886)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3506` → IC=+0.224 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3506 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7296` → IC=+0.209 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7296 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=5268)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2011.3382` → IC=+0.200 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2011.3382 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.223 (n=3563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.233 (n=1781)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=1536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.230 (n=1835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0488` → IC=+0.272 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0488 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.754` → IC=+0.267 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.754 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3464` → IC=+0.253 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3464 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.233 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1880.2292` → IC=+0.225 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.2292 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.225 (n=3862)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.171 (n=229)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=5234)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.146 (n=704)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.004 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.244 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.347 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1481 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.19` → IC=+0.214 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.19 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.1165` → IC=+0.362 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1165 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.1672` → IC=+0.345 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1672 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.3052` → IC=+0.349 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3052 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.361 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `2.2831` → IC=+0.348 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2831 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.349 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.0875` → IC=+0.189 (n=1366)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0875 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.35` → IC=+0.164 (n=661)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.35 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.1456` → IC=+0.157 (n=2543)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1456 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` < `0.8299` → IC=+0.163 (n=1777)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8299 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.209 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.4345` → IC=+0.172 (n=856)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.4345 (IC base=+0.058)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.194 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=842)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.172 (n=248)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=749)

- **FILTRO** `ibs_20min` > `0.1967` → IC=-0.127 (n=5138)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1967
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=2532)

- **FILTRO** `sigma_ewma_delta_pct` > `8.31` → IC=-0.233 (n=828)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.31
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=6842)

- **PATRÓN** `ibs_20min` > `0.7544` → IC=+0.174 (n=339)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.7544 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.9668` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9668 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.917` → IC=+0.168 (n=233)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.917 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.6202` → IC=+0.288 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6202 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.285 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.291 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.262 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.273 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.1967` → IC=+0.161 (n=2532)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1967 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.2309` → IC=+0.288 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2309 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.3174` → IC=+0.289 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3174 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.298 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` > `1.0437` → IC=+0.292 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0437 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0781` → IC=+0.313 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0781 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.1364` → IC=+0.303 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1364 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.4111` → IC=+0.295 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4111 (IC base=-0.032)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7967` → IC=-0.157 (n=3950)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7967
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=2035)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.174 (n=1233)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4752)

- **FILTRO** `ibs_20min` > `0.7299` → IC=-0.190 (n=2064)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7299
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=6201)

- **PATRÓN** `ibs_20min` > `0.7967` → IC=+0.140 (n=2035)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.7967 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.7343` → IC=+0.340 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7343 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7077` → IC=+0.320 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7077 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` < `0.1089` → IC=+0.300 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1089 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1716` → IC=+0.305 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1716 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5191` → IC=+0.315 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5191 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.0666` → IC=+0.285 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0666 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.7201` → IC=+0.273 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7201 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.0622` → IC=+0.277 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0622 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.289 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.4755` → IC=+0.264 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4755 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.270 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.191 (n=8409)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0109 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8654` → IC=+0.283 (n=11417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8654 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9594` → IC=+0.298 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9594 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.463` → IC=+0.167 (n=11321)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.463 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.280 (n=8339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.296 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6413` → IC=+0.287 (n=4869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6413 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=14254)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.161 (n=8156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0105 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5172` → IC=+0.173 (n=21538)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5172 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.271` → IC=+0.283 (n=8595)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.271 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.281 (n=3641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6971 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `1.1887` → IC=+0.285 (n=2758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1887 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.326 (n=1827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `1.452` → IC=+0.305 (n=4096)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.452 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.2702` → IC=+0.304 (n=5569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2702 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.312 (n=12277)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.087)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8084` → IC=-0.143 (n=4466)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8084
  - _Potencial_: sin este filtro IC_bueno=+0.308 (n=2302)

- **FILTRO** `ibs_20min` > `0.7065` → IC=-0.238 (n=1514)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7065
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=4548)

- **FILTRO** `sigma_ewma_delta_pct` > `4.071` → IC=-0.240 (n=1281)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.071
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=4781)

- **PATRÓN** `ibs_20min` > `0.8084` → IC=+0.308 (n=2302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8084 (IC base=+0.010)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.942` → IC=+0.184 (n=2256)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 2.942 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.331 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4486` → IC=+0.289 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4486 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.2408` → IC=+0.310 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2408 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.313 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.010)

- **PATRÓN** `ibs_20min` < `0.1722` → IC=+0.172 (n=1517)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1722 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` < `0.1519` → IC=+0.391 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1519 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.414 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4267 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1747` → IC=+0.230 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1747 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.223 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.247 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4168` → IC=+0.232 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4168 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4647` → IC=+0.219 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4647 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `373.0` → IC=+0.234 (n=2424)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 373.0 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `0.6828` → IC=+0.253 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6828 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `1.1631` → IC=+0.270 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1631 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.306 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.4236` → IC=+0.262 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4236 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1537` → IC=+0.269 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1537 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `176.0` → IC=+0.281 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 176.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.319 (n=1579)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=3493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=1874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.577` → IC=+0.305 (n=2351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.577 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1311` → IC=+0.292 (n=3238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1311 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2528` → IC=+0.300 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2528 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2011.52` → IC=+0.296 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2011.52 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.304 (n=2216)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.335 (n=2149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.306)

- **PATRÓN** `drift_60min` |x|≤ `0.1841` → IC=+0.325 (n=1419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1841 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.322 (n=1237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.306)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.312 (n=1459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` < `0.0278` → IC=+0.307 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0278 (IC base=+0.306)

- **PATRÓN** `ibs_20min` > `0.1519` → IC=+0.318 (n=2149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1519 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.083` → IC=+0.316 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.083 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.407` → IC=+0.307 (n=3339)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.407 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` < `0.1985` → IC=+0.307 (n=3197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1985 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.3445` → IC=+0.313 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3445 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` > `2.7489` → IC=+0.321 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7489 (IC base=+0.306)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.306)

- **PATRÓN** `libro_liquidez` > `1988.8084` → IC=+0.314 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.8084 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.311 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.306)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7142` → IC=-0.178 (n=1586)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7142
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=4759)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.237 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.3664` → IC=+0.238 (n=2283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3664 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1652` → IC=+0.236 (n=2282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1652 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.5949` → IC=+0.235 (n=2282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5949 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.238 (n=2396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1031` → IC=+0.245 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1031 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4162` → IC=+0.242 (n=2216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4162 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.254 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.0911` → IC=+0.154 (n=1587)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.0911 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` > `0.7781` → IC=+0.260 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7781 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1622` → IC=+0.263 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1622 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.1864` → IC=+0.266 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1864 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6165` → IC=+0.260 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6165 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.295 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.7842` → IC=+0.288 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7842 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.283 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.287 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.011)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7451` → IC=-0.246 (n=2596)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7451
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2603)

- **FILTRO** `ibs_20min` > `0.6111` → IC=-0.236 (n=1230)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6111
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=3695)

- **FILTRO** `sigma_ewma_delta_pct` > `8.272` → IC=-0.270 (n=563)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.272
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=4362)

- **PATRÓN** `ibs_20min` > `0.7451` → IC=+0.313 (n=2603)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7451 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `1.0733` → IC=+0.349 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0733 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.438` → IC=+0.157 (n=2118)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.438 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.842` → IC=+0.347 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.842 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `0.6934` → IC=+0.335 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6934 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.336 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.364 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.4268` → IC=+0.364 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4268 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.353 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.6111` → IC=+0.162 (n=3695)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.6111 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` < `0.3207` → IC=+0.275 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3207 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.748` → IC=+0.131 (n=3859)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.748 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` < `0.6914` → IC=+0.284 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6914 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.0702` → IC=+0.297 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0702 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` < `2.1186` → IC=+0.281 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1186 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.290 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.063)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.354 (n=2408)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=2722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=2827)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.9014` → IC=+0.361 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9014 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.5439` → IC=+0.339 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5439 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.813` → IC=+0.336 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.813 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.6293` → IC=+0.325 (n=2695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6293 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.347 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.5345` → IC=+0.326 (n=2324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5345 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `2668.14` → IC=+0.320 (n=1796)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2668.14 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.331 (n=2906)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=2910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.315 (n=2915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.3867` → IC=+0.329 (n=2905)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3867 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2512` → IC=+0.317 (n=2861)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2512 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.271` → IC=+0.323 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.271 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.7178` → IC=+0.317 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7178 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2085` → IC=+0.337 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2085 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.366 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.322 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1493` → IC=+0.317 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1493 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.219 (n=6157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1246` → IC=+0.192 (n=8124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1246 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=19206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5367` → IC=+0.229 (n=18464)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5367 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1654` → IC=+0.206 (n=6943)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1654 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.752` → IC=+0.258 (n=3615)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.752 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.151 (n=12311)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1753 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6217` → IC=+0.152 (n=12311)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6217 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.206 (n=2669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5988` → IC=+0.184 (n=5993)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5988 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.190 (n=17409)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 85.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.193 (n=8122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.006 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.188 (n=12284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.0838` → IC=+0.223 (n=6135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0838 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=8800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.248 (n=16221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.190 (n=2909)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.499` → IC=+0.194 (n=16421)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.499 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.1867` → IC=+0.167 (n=13052)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1867 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.220 (n=2758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6299` → IC=+0.198 (n=5857)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6299 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.201 (n=17367)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.187)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.261 (n=1012)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.0746` → IC=+0.262 (n=1009)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0746 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9427` → IC=+0.291 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9427 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.469` → IC=+0.326 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.469 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.280 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.84` → IC=+0.227 (n=1929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.84 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.226 (n=2892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2037.5` → IC=+0.229 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2037.5 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.258 (n=2541)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.267 (n=1694)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.0988` → IC=+0.309 (n=1120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0988 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=2322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.301 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0588 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.25` → IC=+0.262 (n=2841)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.25 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.258 (n=2238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.270 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.4477` → IC=+0.269 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4477 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6917` → IC=+0.258 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6917 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.262 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1793.28` → IC=+0.259 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1793.28 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.255 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.256)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.192 (n=942)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0032 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.066` → IC=+0.173 (n=938)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.066 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2551` → IC=+0.206 (n=2811)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2551 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1888` → IC=+0.214 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1888 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.588` → IC=+0.206 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.588 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6236` → IC=+0.136 (n=937)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6236 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0495` → IC=+0.134 (n=1274)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.0495 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.172 (n=434)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.7741` → IC=+0.130 (n=1844)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.7741 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4602` → IC=+0.144 (n=922)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4602 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `392.0` → IC=+0.134 (n=2734)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 392.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.181 (n=2677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0059 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2474` → IC=+0.176 (n=2677)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2474 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.4508` → IC=+0.226 (n=2676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4508 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.885` → IC=+0.182 (n=565)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.885 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.012` → IC=+0.159 (n=2660)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.012 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2049` → IC=+0.164 (n=3041)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2049 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.2285` → IC=+0.156 (n=3244)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.2285 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.4805` → IC=+0.157 (n=2914)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4805 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.198 (n=1262)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 205.0 (IC base=+0.154)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.222 (n=2088)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.2524` → IC=+0.232 (n=2087)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2524 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.218 (n=2930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.044` → IC=+0.307 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.044 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.238 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.7115` → IC=+0.222 (n=1386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7115 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=3795)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2003.6763` → IC=+0.223 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2003.6763 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.246 (n=2478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.2486` → IC=+0.269 (n=1875)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2486 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.276 (n=1069)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0409` → IC=+0.295 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0409 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.845` → IC=+0.283 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.845 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.282 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.243 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1786` → IC=+0.252 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1786 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1876.5734` → IC=+0.253 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.5734 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.239 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.193 (n=1018)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.177 (n=1017)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2441` → IC=+0.189 (n=3048)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2441 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1446` → IC=+0.188 (n=1714)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1446 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.227` → IC=+0.197 (n=520)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.227 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8386` → IC=+0.136 (n=2032)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8386 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.1804` → IC=+0.126 (n=1016)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 1.1804 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2879` → IC=+0.173 (n=460)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2879 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.519` → IC=+0.126 (n=1314)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.519 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5044` → IC=+0.136 (n=995)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.5044 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6932.744` → IC=+0.197 (n=1382)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6932.744 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.126 (n=2985)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 123.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.162 (n=2877)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0069 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.422` → IC=+0.149 (n=3265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.422 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6688` → IC=+0.190 (n=3265)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6688 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.554` → IC=+0.144 (n=1117)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 6.554 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8525` → IC=+0.151 (n=2177)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8525 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.175 (n=487)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.189` → IC=+0.134 (n=2733)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.189 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.516` → IC=+0.138 (n=2774)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.516 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `6553.9493` → IC=+0.193 (n=1480)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6553.9493 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.157 (n=1053)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.134)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.171 (n=1136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0128 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.138 (n=3109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5946` → IC=+0.223 (n=3038)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5946 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.2025` → IC=+0.188 (n=1816)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2025 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.005` → IC=+0.286 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.005 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1639` → IC=+0.129 (n=3400)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1639 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.123 (n=3475)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.7792` → IC=+0.125 (n=2200)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7792 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2698.4352` → IC=+0.198 (n=1542)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2698.4352 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.128 (n=1147)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 16.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.144 (n=3566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0121 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1174` → IC=+0.167 (n=1190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1174 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.4932` → IC=+0.240 (n=3138)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4932 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.239` → IC=+0.147 (n=3156)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.239 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.131 (n=3566)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1776 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8584` → IC=+0.128 (n=2379)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.8584 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.162` → IC=+0.128 (n=3523)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.162 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.147 (n=497)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4339` → IC=+0.145 (n=1128)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4339 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4341` → IC=+0.136 (n=1128)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4341 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2595.0847` → IC=+0.191 (n=1617)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2595.0847 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.131 (n=3364)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 43.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.247 (n=3054)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1677` → IC=+0.241 (n=1344)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1677 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.234 (n=1875)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8036` → IC=+0.227 (n=3153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8036 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.529` → IC=+0.261 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.529 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.236 (n=3054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.266 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.229 (n=2981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8253` → IC=+0.229 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8253 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2613.5209` → IC=+0.234 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.5209 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0167` → IC=+0.247 (n=2122)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0167 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6054` → IC=+0.247 (n=3181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6054 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.300 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `1.1484` → IC=+0.251 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1484 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.087` → IC=+0.268 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.087 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.242 (n=2121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.241 (n=3182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.295 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.8402` → IC=+0.238 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8402 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.5519` → IC=+0.238 (n=2689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5519 (IC base=+0.239)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.207 (n=1614)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1407` → IC=+0.173 (n=2130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1407 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=5055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.4201` → IC=+0.200 (n=4325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4201 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2301` → IC=+0.176 (n=1806)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2301 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.54` → IC=+0.210 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.54 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.8592` → IC=+0.165 (n=2925)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8592 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.1921` → IC=+0.164 (n=1463)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1921 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1566` → IC=+0.173 (n=1261)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1566 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.5264` → IC=+0.160 (n=2078)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5264 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8061` → IC=+0.159 (n=3148)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8061 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=5353)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `7287.1688` → IC=+0.193 (n=2195)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7287.1688 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.387` → IC=+0.178 (n=3538)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.387 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.148 (n=2304)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 22.0 (IC base=+0.101)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.203 (n=1181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1037` → IC=+0.230 (n=520)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1037 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.225 (n=1066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.6218` → IC=+0.251 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6218 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.3171` → IC=+0.222 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3171 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.946` → IC=+0.221 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.946 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.6275` → IC=+0.220 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6275 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.0911` → IC=+0.208 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0911 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.205 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.4033` → IC=+0.193 (n=1158)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4033 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `13763.2454` → IC=+0.201 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13763.2454 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.159 (n=491)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0032 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.2154` → IC=+0.194 (n=648)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.2154 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.144 (n=961)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 234.0 (IC base=+0.073)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.231 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1311` → IC=+0.159 (n=649)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1311 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=1534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.7781` → IC=+0.265 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7781 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.5978` → IC=+0.193 (n=311)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.5978 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.932` → IC=+0.198 (n=210)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.932 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.167 (n=983)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8342 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.1614` → IC=+0.156 (n=492)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.1614 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.194 (n=263)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.7716` → IC=+0.175 (n=969)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.7716 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `7946.3404` → IC=+0.181 (n=669)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 7946.3404 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.124 (n=990)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0055 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.1841` → IC=+0.198 (n=653)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1841 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6765` → IC=+0.140 (n=653)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6765 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `7843.145` → IC=+0.155 (n=673)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7843.145 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.150 (n=649)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 41.0 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.154 (n=429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.007 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=1218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.183 (n=1150)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5357 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.147 (n=222)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.866` → IC=+0.221 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.866 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.0461` → IC=+0.126 (n=1132)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0461 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2226` → IC=+0.140 (n=223)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2226 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.143 (n=416)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `3009.802` → IC=+0.159 (n=429)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3009.802 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.3611` → IC=+0.197 (n=949)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3611 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `2721.3379` → IC=+0.162 (n=645)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2721.3379 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.120 (n=938)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 19.0 (IC base=+0.089)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.237 (n=299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.8554` → IC=+0.180 (n=395)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.8554 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5179` → IC=+0.197 (n=400)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5179 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.93` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.93 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.507` → IC=+0.194 (n=449)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 5.507 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1731` → IC=+0.188 (n=444)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1731 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0802` → IC=+0.209 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0802 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.1265` → IC=+0.195 (n=368)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1265 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.192 (n=472)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.03 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2724.4103` → IC=+0.204 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2724.4103 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.173 (n=494)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0105 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.3425` → IC=+0.164 (n=331)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3425 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.3471` → IC=+0.163 (n=330)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3471 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.163 (n=494)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.1 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `1.1922` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1922 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.969` → IC=+0.159 (n=124)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.969 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.889` → IC=+0.190 (n=330)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.889 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.172 (n=458)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2376` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2376 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4819` → IC=+0.196 (n=159)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4819 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.6395` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.6395 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.172 (n=474)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 20.0 (IC base=+0.156)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.225 (n=8130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=25449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9676` → IC=+0.302 (n=8120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9676 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9066` → IC=+0.216 (n=2820)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9066 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.919` → IC=+0.260 (n=5976)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.919 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2136` → IC=+0.160 (n=16419)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2136 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2405` → IC=+0.212 (n=4363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2405 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6207` → IC=+0.193 (n=7935)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6207 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.200 (n=23025)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.209 (n=7554)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1505` → IC=+0.202 (n=9953)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1505 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=8467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.253 (n=19904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1853` → IC=+0.182 (n=14459)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1853 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.515` → IC=+0.205 (n=21035)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.515 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0533` → IC=+0.175 (n=13351)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0533 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.255 (n=3103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6211` → IC=+0.213 (n=7242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6211 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.215 (n=21505)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.272 (n=1300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3709` → IC=+0.235 (n=3883)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3709 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8625` → IC=+0.294 (n=2591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8625 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.038` → IC=+0.301 (n=2551)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.038 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.233` → IC=+0.287 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.233 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2917` → IC=+0.239 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2917 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4269)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2031.19` → IC=+0.242 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.19 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.246 (n=3142)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.268 (n=3532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.270 (n=2356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1252` → IC=+0.294 (n=1554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1252 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.269 (n=3672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.272 (n=3185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.4658` → IC=+0.288 (n=3107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4658 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.718` → IC=+0.270 (n=3833)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.718 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.271 (n=3220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.282 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5653` → IC=+0.274 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5653 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6526` → IC=+0.276 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6526 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1791.6` → IC=+0.270 (n=2354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1791.6 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.276 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.162 (n=2665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0047 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0805` → IC=+0.150 (n=1332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0805 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.3055` → IC=+0.203 (n=3569)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3055 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3323` → IC=+0.202 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3323 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.166 (n=837)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6345` → IC=+0.156 (n=1332)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6345 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0678` → IC=+0.146 (n=1811)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0678 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.190 (n=562)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1711` → IC=+0.145 (n=3456)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1711 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5208` → IC=+0.147 (n=3509)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5208 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `407.0` → IC=+0.148 (n=3878)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 407.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.172 (n=3106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0059 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.082` → IC=+0.176 (n=1178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.082 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=1302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.3204` → IC=+0.236 (n=2351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3204 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.974` → IC=+0.147 (n=3202)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.974 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0421` → IC=+0.155 (n=3102)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0421 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2209` → IC=+0.197 (n=642)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2209 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.434` → IC=+0.149 (n=3414)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.434 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.152 (n=2276)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=4582)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.177 (n=1119)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 215.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.237 (n=1354)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=4260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.223 (n=3621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.97` → IC=+0.319 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.97 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2058` → IC=+0.232 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2058 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.7509` → IC=+0.239 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7509 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=4921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `1898.9266` → IC=+0.234 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1898.9266 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.249 (n=3448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.245 (n=1309)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1827` → IC=+0.260 (n=1722)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1827 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=1781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.065` → IC=+0.302 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.065 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.986` → IC=+0.305 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.986 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3484` → IC=+0.300 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3484 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1714` → IC=+0.257 (n=2522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1714 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1918)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1985.3584` → IC=+0.258 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1985.3584 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.250 (n=3310)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.192 (n=1405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0038 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3465` → IC=+0.147 (n=3708)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3465 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.88` → IC=+0.270 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.88 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.145` → IC=+0.169 (n=2072)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.145 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.963` → IC=+0.161 (n=1851)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.963 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.153 (n=2810)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8577 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.201 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5159` → IC=+0.155 (n=1814)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5159 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1549` → IC=+0.145 (n=1868)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1549 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5775.4039` → IC=+0.237 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5775.4039 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.143 (n=2730)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.171 (n=3561)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0081 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4528` → IC=+0.160 (n=3558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4528 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.7037` → IC=+0.203 (n=3558)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7037 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1617` → IC=+0.164 (n=3377)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1617 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.02` → IC=+0.155 (n=3102)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.02 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8545` → IC=+0.164 (n=2373)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8545 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.207 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1947` → IC=+0.154 (n=3031)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1947 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.524` → IC=+0.158 (n=3077)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.524 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6703.3145` → IC=+0.218 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6703.3145 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.175 (n=1188)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 57.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.155 (n=1432)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0129 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=3045)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.6979` → IC=+0.255 (n=2861)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6979 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.0319` → IC=+0.203 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0319 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.234` → IC=+0.271 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.234 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.131 (n=2863)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8739 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.121 (n=4083)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2771` → IC=+0.128 (n=538)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2771 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.8157` → IC=+0.127 (n=2793)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8157 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2462.6457` → IC=+0.220 (n=1946)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2462.6457 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.159 (n=3532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0111 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1417` → IC=+0.155 (n=1339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1417 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=1897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5413` → IC=+0.244 (n=3532)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5413 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.054` → IC=+0.159 (n=3895)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.054 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1909` → IC=+0.143 (n=4014)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1909 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.202 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4341` → IC=+0.164 (n=1276)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4341 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2648.2907` → IC=+0.218 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2648.2907 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.151 (n=3827)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 48.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.257 (n=3922)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=4102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=2617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.9882` → IC=+0.307 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9882 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.199` → IC=+0.252 (n=1984)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.199 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.07` → IC=+0.294 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.07 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2168` → IC=+0.238 (n=3920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2168 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.243 (n=3921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.254 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5002` → IC=+0.255 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5002 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2629.3094` → IC=+0.243 (n=2613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2629.3094 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0251` → IC=+0.270 (n=1360)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0251 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=4100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1373` → IC=+0.307 (n=1793)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1373 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.2269` → IC=+0.249 (n=3926)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2269 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.039` → IC=+0.278 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.039 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7155` → IC=+0.245 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7155 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2151` → IC=+0.263 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2151 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.314 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4322` → IC=+0.247 (n=3861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4322 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2982.5888` → IC=+0.245 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2982.5888 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.232 (n=6242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.5333` → IC=+0.233 (n=7094)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5333 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=7142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9295` → IC=+0.261 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9295 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.9425` → IC=+0.226 (n=5825)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9425 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.573` → IC=+0.232 (n=3525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.573 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.7069` → IC=+0.232 (n=2218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7069 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.881` → IC=+0.225 (n=3360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.881 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.225 (n=6641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.1648` → IC=+0.233 (n=1986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1648 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.235 (n=2327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.229 (n=5108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3736.219` → IC=+0.232 (n=4729)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3736.219 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.231 (n=1665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.4133` → IC=+0.220 (n=4374)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4133 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.218 (n=1933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.6139` → IC=+0.212 (n=4374)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6139 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.7008` → IC=+0.219 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7008 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.1872` → IC=+0.204 (n=4290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1872 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.764` → IC=+0.221 (n=4502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.764 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.2537` → IC=+0.210 (n=4587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2537 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.210 (n=4589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.208 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.5312` → IC=+0.211 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5312 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.1859` → IC=+0.218 (n=2219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1859 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.234 (n=2167)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.208)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.279 (n=829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.302 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.270 (n=946)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.295 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1414 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.275 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `0.8769` → IC=+0.289 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8769 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.346 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.4871` → IC=+0.277 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4871 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.189` → IC=+0.271 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.189 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `12913.0263` → IC=+0.282 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12913.0263 (IC base=+0.270)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.265 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3873` → IC=+0.187 (n=1534)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3873 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.176 (n=573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.138` → IC=+0.193 (n=675)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.138 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.7` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.834` → IC=+0.185 (n=1775)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 10.834 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.187 (n=1350)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.091 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` < `0.272` → IC=+0.176 (n=1811)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.272 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1521` → IC=+0.189 (n=467)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1521 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.191 (n=509)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `1.8071` → IC=+0.176 (n=1017)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8071 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `14600.5038` → IC=+0.173 (n=696)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 14600.5038 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `695.0` → IC=+0.187 (n=1489)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 695.0 (IC base=+0.173)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.222 (n=922)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.5997` → IC=+0.212 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5997 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.231 (n=943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.7126` → IC=+0.212 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7126 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.277` → IC=+0.246 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.277 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.3489` → IC=+0.209 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3489 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2042` → IC=+0.244 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2042 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.7931` → IC=+0.215 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7931 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2386.909` → IC=+0.233 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2386.909 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.217 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.286 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.300 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.7923` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7923 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.216` → IC=+0.258 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.216 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.971` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.971 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2388.306` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2388.306 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.223 (n=1917)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4675` → IC=+0.220 (n=1916)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4675 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4728` → IC=+0.223 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4728 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.1451` → IC=+0.213 (n=1916)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1451 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.4062` → IC=+0.225 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4062 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.962` → IC=+0.222 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.962 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `0.8705` → IC=+0.220 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8705 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.215 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4027` → IC=+0.230 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4027 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4929` → IC=+0.213 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4929 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.240 (n=514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.5101` → IC=+0.221 (n=1534)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5101 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.211 (n=575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=1095)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.0863` → IC=+0.211 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0863 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.6796` → IC=+0.218 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6796 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.4225` → IC=+0.205 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4225 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.345` → IC=+0.210 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.345 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2648` → IC=+0.212 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2648 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.7217` → IC=+0.206 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7217 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.230 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.5091` → IC=+0.209 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5091 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.7743` → IC=+0.208 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7743 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=2026)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `7821.1761` → IC=+0.215 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7821.1761 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.208 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.205)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.229 (n=842)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.227 (n=572)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.236 (n=1276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.218 (n=1156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.297 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.8389` → IC=+0.247 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8389 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.218` → IC=+0.252 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.218 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.6422` → IC=+0.247 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6422 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `1.2465` → IC=+0.216 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2465 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.219 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.234 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `2.1551` → IC=+0.224 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1551 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1478)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `4456.3994` → IC=+0.251 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4456.3994 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.261 (n=620)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.248)

- **PATRÓN** `drift_60min` |x|≤ `0.6874` → IC=+0.261 (n=931)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6874 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.267 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.248)

- **PATRÓN** `ibs_20min` < `0.7357` → IC=+0.273 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7357 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` > `0.6006` → IC=+0.248 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6006 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` < `0.3365` → IC=+0.261 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3365 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.985` → IC=+0.267 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.985 (IC base=+0.248)

- **PATRÓN** `volumen_regimen` < `0.6688` → IC=+0.264 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6688 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` < `0.1033` → IC=+0.260 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1033 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` > `1.8326` → IC=+0.266 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8326 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.248)

- **PATRÓN** `libro_liquidez` > `3991.9492` → IC=+0.273 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3991.9492 (IC base=+0.248)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.280 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.248)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.151 (n=821)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.004 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.7428` → IC=+0.188 (n=1579)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7428 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.149 (n=1143)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.421` → IC=+0.136 (n=511)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 10.421 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.6059` → IC=+0.150 (n=1747)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6059 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.1499` → IC=+0.157 (n=476)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1499 (IC base=+0.065)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5427` → IC=-0.120 (n=322)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5427
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=656)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.121 (n=674)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0055 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.160 (n=656)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5427 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.172 (n=339)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.067)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.129 (n=308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0036 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.253 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.144 (n=290)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.054)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.5262` → IC=-0.138 (n=241)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5262
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=470)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.158 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0043 (IC base=+0.070)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9304` → IC=+0.262 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9304 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1316` → IC=+0.171 (n=363)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1316 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.65` → IC=+0.185 (n=163)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.65 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.1007` → IC=+0.276 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1007 (IC base=+0.038)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7174` → IC=+0.141 (n=567)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.7174 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.7456` → IC=+0.160 (n=198)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.7456 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.165 (n=365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0099 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.1884` → IC=+0.249 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1884 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.928` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.928 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` > `1.1167` → IC=+0.190 (n=172)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.1167 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.1644` → IC=+0.169 (n=134)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1644 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `1.4597` → IC=+0.135 (n=485)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4597 (IC base=+0.090)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.124 (n=256)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.03 (IC base=+0.090)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1888` → IC=-0.320 (n=98)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1888
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=296)

- **FILTRO** `dist_vwap_pct` > `0.2422` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2422
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=381)

- **FILTRO** `sigma_h` < `0.0066` → IC=-0.283 (n=261)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=88)

- **FILTRO** `dist_vwap_pct` > `0.4497` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4497
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=329)

- **FILTRO** `sigma_ewma_delta_pct` > `9.318` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.318
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=319)

- **FILTRO** `volumen_pendiente_norm` > `0.0463` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0463
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=227)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.300 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=67)

- **FILTRO** `ibs_20min` < `0.0866` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0866
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=81)

- **FILTRO** `volumen_spike_ratio` < `1.6757` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6757
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=73)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=75)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.278 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=77)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=98)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

- **FILTRO** `libro_liquidez` < `5528.1887` → IC=-0.259 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 5528.1887
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.471 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=102)

- **FILTRO** `volumen_regimen` < `0.7435` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7435
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=102)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=102)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.329 (n=33)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=67)

- **FILTRO** `volumen_spike_ratio` < `1.4481` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4481
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=75)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.361 (n=34)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `volumen_pendiente_norm` > `0.1196` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1196
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=84)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=111)

- **FILTRO** `sigma_ewma_delta_pct` > `4.378` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.378
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=49)

- **FILTRO** `volumen_regimen` < `0.9175` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9175
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=44)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=42)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2375` → IC=-0.151 (n=310)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2375
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=931)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.253 (n=362)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.201 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.68` → IC=+0.196 (n=793)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.68 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.8305` → IC=+0.310 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8305 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.618` → IC=+0.175 (n=438)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.618 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.6275` → IC=+0.197 (n=265)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6275 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.191 (n=596)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.213 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.161)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7305` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7305
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=228)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.158 (n=77)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0065 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.7305` → IC=+0.130 (n=228)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.7305 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.6315` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6315 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.242` → IC=+0.136 (n=427)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.242 (IC base=+0.076)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.2345` → IC=-0.149 (n=112)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2345
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=337)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.136 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0044 (IC base=+0.132)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.178 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.007 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1059` → IC=+0.135 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1059 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.174 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.140 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 8.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.798` → IC=+0.174 (n=228)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.798 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1039` → IC=+0.160 (n=210)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1039 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.38` → IC=+0.155 (n=265)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 9.38 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.625` → IC=+0.182 (n=86)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.625 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.1915 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` < `0.1814` → IC=+0.153 (n=272)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1814 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.7318` → IC=+0.182 (n=152)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.7318 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=219)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.689` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.689 (IC base=+0.003)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.15` → IC=-0.240 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=148)

- **FILTRO** `volumen_regimen` < `0.9454` → IC=-0.146 (n=111)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9454
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=112)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.290 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.281 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` > `0.8523` → IC=+0.304 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8523 (IC base=+0.261)

- **PATRÓN** `dist_vwap_pct` > `0.7432` → IC=+0.393 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7432 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.261)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.294 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.0893` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0893 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` > `2.3612` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3612 (IC base=+0.261)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.347 (n=161)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3462` → IC=+0.336 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3462 (IC base=+0.334)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.407 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.334)

- **PATRÓN** `drift_15min` |x|≤ `2.3858` → IC=+0.358 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3858 (IC base=+0.334)

- **PATRÓN** `drift_60min` |x|≤ `1.0148` → IC=+0.375 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0148 (IC base=+0.334)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.384 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.334)

- **PATRÓN** `ballena_activa_n` < `1046.0` → IC=+0.409 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1046.0 (IC base=+0.334)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.320 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.300)

- **PATRÓN** `elapsed_s` > `231.3` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 231.3 (IC base=+0.300)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.342 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.8978` → IC=+0.325 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8978 (IC base=+0.300)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.347 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.300)

- **PATRÓN** `ballena_activa_n` < `1330.0` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1330.0 (IC base=+0.300)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.347 (n=161)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3462` → IC=+0.336 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3462 (IC base=+0.334)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.407 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.334)

- **PATRÓN** `drift_15min` |x|≤ `2.3858` → IC=+0.358 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3858 (IC base=+0.334)

- **PATRÓN** `drift_60min` |x|≤ `1.0148` → IC=+0.375 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0148 (IC base=+0.334)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.384 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.334)

- **PATRÓN** `ballena_activa_n` < `1046.0` → IC=+0.409 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1046.0 (IC base=+0.334)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.320 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.300)

- **PATRÓN** `elapsed_s` > `231.3` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 231.3 (IC base=+0.300)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.342 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.8978` → IC=+0.325 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8978 (IC base=+0.300)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.347 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.300)

- **PATRÓN** `ballena_activa_n` < `1330.0` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1330.0 (IC base=+0.300)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=281)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=226)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=281)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=1247)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `liq_n` > 2.0 (IC base=+0.079)

- **PATRÓN** `liq_usd_total` > `1042.48` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `liq_usd_total` > 1042.48 (IC base=+0.079)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` > 0.5 (IC base=+0.079)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9627` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9627
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=117)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.236 (n=51)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=73)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.078)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.078)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.425` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

- **PATRÓN** `liq_usd_total` > `4866.9` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `liq_usd_total` > 4866.9 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.140 (n=98)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 46.0 (IC base=+0.064)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=25)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=270)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=4172)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=210)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=167)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.295 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=194)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.160 (n=98)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=+0.213 (n=99)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.011)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=283)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.019)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.193)

- **PATRÓN** `liq_usd_total` > `3798.53` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 3798.53 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.217 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.214 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.206 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `3293.399` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3293.399 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.193)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1631)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1585)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=740)

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
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1095)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1095)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1440)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1440)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=327)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=327)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.135 (n=83)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=259)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=395)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=444)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=324)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=429)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=429)

- **FILTRO** `libro_liquidez` < `692.3639` → IC=-0.128 (n=151)

  - _Acción_: SKIP cuando `libro_liquidez` < 692.3639
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=308)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=410)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.124 (n=3182)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=8294)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.133 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=129)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `restante_min` < `3.99` → IC=-0.132 (n=66)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.171 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.153 (n=373)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=919)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.151 (n=293)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=824)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.144 (n=391)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.51 (IC base=-0.008)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.129 (n=184)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=416)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.136 (n=330)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=696)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.125 (n=715)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=378)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.128 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=407)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.135 (n=582)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=667)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.177 (n=8791)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=27440)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=9150)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=28375)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.198 (n=1638)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5107)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.142 (n=2244)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=4412)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.135 (n=1727)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.134 (n=3124)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.177 (n=1227)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=3744)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.176 (n=1290)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3963)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.195 (n=1668)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=5161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.133 (n=2074)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

- **PATRÓN** `libro_liquidez` > `1750.0536` → IC=+0.125 (n=2288)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1750.0536 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.179 (n=1314)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=4046)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.160 (n=1685)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5082)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3200)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4152)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.198 (n=336)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1148)

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
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=370)

- **FILTRO** `drift_20min_pct` |x|> `0.2017` → IC=-0.131 (n=120)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2017
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=363)

- **FILTRO** `libro_liquidez` < `3247.9585` → IC=-0.183 (n=159)

  - _Acción_: SKIP cuando `libro_liquidez` < 3247.9585
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=324)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `libro_liquidez` < `1991.6564` → IC=-0.140 (n=398)

  - _Acción_: SKIP cuando `libro_liquidez` < 1991.6564
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=811)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=244)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=24566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=55815)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.300 (n=19535)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=60846)

- **FILTRO** `ibs_7min` < `0.2105` → IC=-0.237 (n=20063)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2105
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=60318)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.154 (n=26996)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=53385)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.246 (n=24946)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=75530)

- **FILTRO** `ibs_7min` > `0.2792` → IC=-0.183 (n=25117)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2792
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=75359)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.160 (n=3445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=11013)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.320 (n=3594)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=10864)

- **FILTRO** `ibs_7min` < `0.7089` → IC=-0.255 (n=4770)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7089
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=9688)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.280 (n=4212)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=13173)

- **FILTRO** `ibs_7min` > `0.7671` → IC=-0.211 (n=4346)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7671
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=13039)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=3241)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=10044)

- **FILTRO** `ibs_7min` < `0.7122` → IC=-0.213 (n=3317)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7122
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=9968)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.203 (n=3309)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9976)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=3088)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10490)

- **FILTRO** `ibs_7min` > `0.2647` → IC=-0.192 (n=3394)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2647
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10184)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.177 (n=3384)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10194)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3309)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10562)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.328 (n=3319)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=10552)

- **FILTRO** `ibs_7min` < `0.2892` → IC=-0.253 (n=4577)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2892
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9294)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.173 (n=3388)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=10483)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=4425)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=13976)

- **FILTRO** `ibs_7min` > `0.7239` → IC=-0.185 (n=4600)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7239
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=13801)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=3235)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9717)

- **FILTRO** `ibs_7min` < `0.7126` → IC=-0.203 (n=3238)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7126
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9714)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.195 (n=3231)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=9721)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=3128)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=10330)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.179 (n=3361)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10097)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.168 (n=3336)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10122)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=3110)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=9709)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.235 (n=4223)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8596)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3146)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9673)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.200 (n=4614)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=14850)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=3181)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9815)

- **FILTRO** `ibs_7min` < `0.7217` → IC=-0.229 (n=4288)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7217
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8708)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.194 (n=3244)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=9752)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.230 (n=4470)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=13720)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1022)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1311)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=921)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=345)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=462)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=592)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.124 (n=107)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=677)

- **FILTRO** `libro_liquidez` < `3306.8101` → IC=-0.146 (n=196)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.8101
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=588)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4304` → IC=+0.146 (n=742)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4304 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=1464)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `441.7389` → IC=+0.161 (n=541)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 441.7389 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3613.3092` → IC=+0.145 (n=736)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3613.3092 (IC base=+0.126)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.186 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 14.0 (IC base=+0.140)

- **PATRÓN** `total_vol_5m` < `498.39` → IC=+0.158 (n=378)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 498.39 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.157 (n=260)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 9.0 (IC base=+0.140)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.161 (n=113)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.137 (n=298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.116)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.173 (n=203)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `866.7487` → IC=+0.154 (n=304)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 866.7487 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 59.0 (IC base=+0.127)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4183` → IC=+0.201 (n=182)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4183 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.182 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 5.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `6100.528` → IC=+0.167 (n=241)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 6100.528 (IC base=+0.142)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.137 (n=301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.158 (n=150)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.104)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.155 (n=317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0046 (IC base=-0.029)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.276 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.000)

- **PATRÓN** `pct_vs_K` |x|≤ `1.8236` → IC=+0.204 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.8236 (IC base=+0.000)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` < `0.0107` → IC=-0.136 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=25)

- **FILTRO** `T_h` < `243.9505` → IC=-0.182 (n=64)

  - _Acción_: SKIP cuando `T_h` < 243.9505
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=25)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `96.5959` → IC=-0.167 (n=91)

  - _Acción_: SKIP cuando `T_h` < 96.5959
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=91)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `112.3739` → IC=-0.251 (n=551)

  - _Acción_: SKIP cuando `T_h` < 112.3739
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=285)

- **FILTRO** `sigma_h` < `0.0056` → IC=-0.191 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=578)

- **FILTRO** `T_h` > `142.427` → IC=-0.170 (n=192)

  - _Acción_: SKIP cuando `T_h` > 142.427
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=578)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.225 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=137)

- **FILTRO** `T_h` > `143.1485` → IC=-0.185 (n=71)

  - _Acción_: SKIP cuando `T_h` > 143.1485
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=214)

- **FILTRO** `pct_vs_K` |x|> `2.8429` → IC=-0.345 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8429
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=216)

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
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.326 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=123)

- **FILTRO** `T_h` < `68.1921` → IC=-0.302 (n=79)

  - _Acción_: SKIP cuando `T_h` < 68.1921
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=163)

- **FILTRO** `sigma_h` > `0.0102` → IC=-0.195 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=177)

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.183 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=176)

- **FILTRO** `T_h` > `57.2148` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `T_h` > 57.2148
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=78)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9861` → IC=+0.145 (n=119)

  - _Acción_: Kelly boost +0.72€ cuando `pct_vs_K` |x|≤ 1.9861 (IC base=-0.110)

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
- **FILTRO** `sigma_h` > `0.013` → IC=-0.216 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=156)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.247 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=158)

- **FILTRO** `T_h` > `62.8653` → IC=-0.219 (n=176)

  - _Acción_: SKIP cuando `T_h` > 62.8653
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=59)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.300 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=114)

- **FILTRO** `sigma_h` < `0.0088` → IC=-0.278 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=129)

- **FILTRO** `T_h` < `113.9448` → IC=-0.179 (n=129)

  - _Acción_: SKIP cuando `T_h` < 113.9448
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=43)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1171` → IC=+0.446 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1171 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.013` → IC=+0.360 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.338)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.338)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.338)

- **PATRÓN** `dist_50` > `0.4679` → IC=+0.482 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4679 (IC base=+0.338)

- **PATRÓN** `edge` > `0.1` → IC=+0.427 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.392)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.411 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.3751` → IC=+0.441 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3751 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.392)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1144` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1144 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.227 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.194)

- **PATRÓN** `T_h` > `1.4441` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4441 (IC base=+0.194)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.234 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.194)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.466 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.410)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.423 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.410)

- **PATRÓN** `T_h` < `1.2028` → IC=+0.439 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2028 (IC base=+0.410)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.483 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.410)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1635` → IC=+0.486 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1635 (IC base=+0.439)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.469 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.439)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.439)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.473 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.439)

- **PATRÓN** `edge` > `0.1937` → IC=+0.472 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1937 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.475 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.464)

- **PATRÓN** `T_h` < `0.8072` → IC=+0.458 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8072 (IC base=+0.464)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4572` → IC=+0.493 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4572 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=467)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=508)

- **PATRÓN** `streak_estiramiento` < `0.3694` → IC=+0.124 (n=155)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.3694 (IC base=+0.015)

- **PATRÓN** `streak_estiramiento` < `0.836` → IC=+0.120 (n=351)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.836 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.141 (n=129)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 14.0 (IC base=+0.057)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.074)

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
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=208)

- **PATRÓN** `streak_estiramiento` < `0.2049` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.2049 (IC base=+0.027)

- **PATRÓN** `streak_estiramiento` < `0.5927` → IC=+0.155 (n=175)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.5927 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.149 (n=166)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 30.0 (IC base=+0.083)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=94)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=39)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `streak_estiramiento` > `0.6751` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6751
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `streak_estiramiento` < `0.5723` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.5723 (IC base=-0.022)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1091)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1349)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1309)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5290)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3086)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.186 (n=2021)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0056 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.2289` → IC=+0.159 (n=6062)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2289 (IC base=+0.134)

- **PATRÓN** `drift_15min` |x|≤ `1.0926` → IC=+0.134 (n=6062)

  - _Acción_: Kelly boost +0.67€ cuando `drift_15min` |x|≤ 1.0926 (IC base=+0.134)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0646` → IC=+0.134 (n=6065)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0646 (IC base=+0.134)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.144 (n=2513)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=5624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` > `0.5652` → IC=+0.212 (n=5415)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5652 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.2` → IC=+0.233 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.2 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3305)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4421.5109` → IC=+0.171 (n=2021)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4421.5109 (IC base=+0.134)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=2368)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.226 (n=746)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.245 (n=374)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2678` → IC=+0.230 (n=283)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2678 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2268` → IC=+0.212 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2268 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7058` → IC=+0.273 (n=848)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7058 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.222 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1123` → IC=+0.202 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1123 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.238` → IC=+0.305 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.238 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `11835.8417` → IC=+0.218 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11835.8417 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.164 (n=474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0047 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.147 (n=720)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.137` → IC=+0.133 (n=718)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.137 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.487` → IC=+0.217 (n=1077)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.487 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.144 (n=672)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.6305` → IC=+0.132 (n=1227)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6305 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.063` → IC=+0.290 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.063 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6089.1003` → IC=+0.170 (n=489)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6089.1003 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8462` → IC=+0.145 (n=609)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.72€ cuando `ibs_15` > 0.8462 (IC base=+0.047)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.014` → IC=+0.144 (n=677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.014 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.146 (n=1537)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.012 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2349` → IC=+0.179 (n=1537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2349 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.143 (n=1537)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0933` → IC=+0.194 (n=481)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0933 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=1414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.5319` → IC=+0.210 (n=1373)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5319 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.3587` → IC=+0.156 (n=518)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3587 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.497` → IC=+0.178 (n=349)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 17.497 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2946.3003` → IC=+0.187 (n=697)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2946.3003 (IC base=+0.141)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.377 (n=519)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.372 (n=719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7903` → IC=+0.396 (n=779)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7903 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.263` → IC=+0.383 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.263 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.899` → IC=+0.397 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.899 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.382 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9610.6074 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.413 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.366 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.377 (n=169)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.401 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.382 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.386 (n=374)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.3736` → IC=+0.394 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3736 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.392 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `8167.5504` → IC=+0.386 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8167.5504 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.403 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.368 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.382 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1063` → IC=+0.364 (n=271)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1063 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.374 (n=362)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.371 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.368 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.373 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.397 (n=405)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.1233` → IC=+0.370 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1233 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.889` → IC=+0.396 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.889 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `4242.86` → IC=+0.371 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4242.86 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.206 (n=2900)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2901)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2510)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3291)

- **PATRÓN** `ibs_15` > `0.6307` → IC=+0.276 (n=1290)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6307 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` > `0.115` → IC=+0.202 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.115 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` < `0.5693` → IC=+0.199 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5693 (IC base=-0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.272 (n=1841)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=+0.000)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.285 (n=5533)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` > `0.6758` → IC=+0.269 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6758 (IC base=+0.000)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0726` → IC=-0.246 (n=1876)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0726
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=1888)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.218 (n=941)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=2823)

- **FILTRO** `sigma_ewma_delta_pct` > `22.182` → IC=-0.250 (n=534)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.182
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=3230)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.147 (n=352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0032 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2675` → IC=+0.287 (n=153)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2675 (IC base=+0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1455` → IC=+0.269 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1455 (IC base=+0.064)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.317 (n=457)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.277 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.2456` → IC=+0.278 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2456 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.006` → IC=+0.140 (n=234)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 22.006 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.225 (n=78)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.183)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0902` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0902 (IC base=-0.183)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.287 (n=78)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.183)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.183)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.310 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.183)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=848)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.160 (n=571)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.006 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.162 (n=572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3015` → IC=+0.190 (n=511)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3015 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.166 (n=468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5679` → IC=+0.240 (n=649)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5679 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6372` → IC=+0.159 (n=121)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6372 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.147 (n=500)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.914` → IC=+0.266 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.914 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=848)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5066.1005` → IC=+0.160 (n=433)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5066.1005 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.260 (n=952)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.4641` → IC=+0.244 (n=2161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4641 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.804` → IC=+0.255 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.804 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.265 (n=980)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.245 (n=956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3871` → IC=+0.273 (n=2161)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3871 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.3913` → IC=+0.263 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3913 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.423` → IC=+0.249 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.423 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1986` → IC=-0.292 (n=344)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1986
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1036)

- **FILTRO** `drift_60min` |x|> `0.2019` → IC=-0.286 (n=344)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2019
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=1036)

- **FILTRO** `drift_15min` |x|> `0.9594` → IC=-0.292 (n=344)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9594
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1036)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.203)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1327 (IC base=-0.203)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0622` → IC=+0.240 (n=938)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0622 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.295 (n=938)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` < `0.4621` → IC=+0.252 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4621 (IC base=-0.025)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1201` → IC=-0.267 (n=821)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1201
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=823)

- **FILTRO** `sigma_h` > `0.0123` → IC=-0.243 (n=1232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=412)

- **FILTRO** `drift_15min` |x|> `1.2903` → IC=-0.282 (n=410)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2903
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=1234)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1623)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0718` → IC=+0.282 (n=1166)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0718 (IC base=-0.010)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.292 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.010)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=1311)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` > `0.7632` → IC=+0.329 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7632 (IC base=-0.010)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.150 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0067 (IC base=+0.095)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.134 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.095)

- **PATRÓN** `drift_15min` |x|≤ `0.7295` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.7295 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.15` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.15 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.293 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 49.0 (IC base=+0.095)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.150 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0067 (IC base=+0.095)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.134 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.095)

- **PATRÓN** `drift_15min` |x|≤ `0.7295` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.7295 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.15` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.15 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.293 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 49.0 (IC base=+0.095)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.297 (n=480)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.286 (n=479)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.312 (n=481)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1514` → IC=+0.284 (n=958)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1514 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2213` → IC=+0.288 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2213 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.298 (n=1305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8372` → IC=+0.310 (n=1437)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8372 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2719` → IC=+0.311 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2719 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.826` → IC=+0.385 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.826 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.282 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13088.9696` → IC=+0.296 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13088.9696 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.308 (n=253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.300 (n=333)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.277)

- **PATRÓN** `drift_15min` |x|≤ `0.3855` → IC=+0.277 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3855 (IC base=+0.277)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2704` → IC=+0.283 (n=252)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2704 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2298` → IC=+0.284 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2298 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.301 (n=698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.302 (n=757)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.310 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` < `0.5589` → IC=+0.276 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5589 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.592` → IC=+0.393 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.592 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `15684.0606` → IC=+0.316 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15684.0606 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.292 (n=681)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0501` → IC=+0.321 (n=227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0501 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.065` → IC=+0.292 (n=681)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.065 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1016` → IC=+0.305 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1016 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.296 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.289 (n=481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8444` → IC=+0.313 (n=682)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8444 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.285` → IC=+0.310 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.285 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` < `0.6422` → IC=+0.288 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6422 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.379 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.288)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1148` → IC=-0.157 (n=231)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1148
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=114)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.143 (n=236)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=119)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.169 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=376)

- **FILTRO** `ballena_activa_n` > `67.0` → IC=-0.221 (n=59)

  - _Acción_: SKIP cuando `ballena_activa_n` > 67.0
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=181)

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
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=167)

- **FILTRO** `drift_15min` |x|> `0.3423` → IC=-0.283 (n=21)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3423
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=42)

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

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0074` → IC=-0.167 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=29)

- **FILTRO** `drift_60min` |x|> `0.2763` → IC=-0.214 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2763
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=38)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `sigma_h` < `0.006` → IC=-0.219 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0801` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0801
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0898` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0898
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0058` → IC=-0.250 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9869` → IC=+0.261 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9869 (IC base=+0.130)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.357 (n=3139)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0178` → IC=+0.388 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0178 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.174 (n=277)

  - _Acción_: Kelly boost +0.87€ cuando `ratio` < 0.9922 (IC base=+0.076)

- **PATRÓN** `T_h` > `109.882` → IC=+0.326 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.882 (IC base=+0.308)

- **PATRÓN** `ratio` > `1.0154` → IC=+0.382 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0154 (IC base=+0.308)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9824` → IC=+0.365 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9824 (IC base=+0.188)

- **PATRÓN** `T_h` > `111.9922` → IC=+0.355 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9922 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0245` → IC=+0.402 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0245 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0398` → IC=+0.416 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0398 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5652 sube el IC de +0.134 a +0.212 en UPDOWN_GBM#15min (n=5415). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7058 sube el IC de +0.202 a +0.273 en UPDOWN_GBM#BTC#15min (n=848). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.487 sube el IC de +0.131 a +0.217 en UPDOWN_GBM#ETH#15min (n=1077). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5319 sube el IC de +0.141 a +0.210 en UPDOWN_GBM#XRP#15min (n=1373). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6307 sube el IC de -0.087 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1290). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.000 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=5533). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.064 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=457). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.183 a +0.287 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5679 sube el IC de +0.146 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=649). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3871 sube el IC de +0.241 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2161). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.203 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.025 a +0.295 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=938). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.010 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1311). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.095 a +0.293 en UPDOWN_GBM_ETH_15M_HORA7 (n=27). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.095 a +0.293 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=27). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8372 sube el IC de +0.282 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1437). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.277 a +0.302 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=757). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8444 sube el IC de +0.288 a +0.313 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=682). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.364 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=779). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.364 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=374). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.363 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=405). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2266 | +0.083 | +227.79€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2266 | +0.083 | +227.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1854 | +0.083 | +188.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1854 | +0.083 | +188.30€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1297 | -0.021 | +69.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1297 | -0.021 | +69.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1000 | -0.036 | +53.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1000 | -0.036 | +53.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 201 | +0.052 | +21.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 201 | +0.052 | +21.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 89 | -0.028 | -8.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 89 | -0.028 | -8.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 49900 | -0.086 | -6364.81€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3197 | +0.088 | -305.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 46703 | -0.097 | -6059.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5010 | -0.115 | -804.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5010 | -0.115 | -804.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3197 | +0.088 | -305.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3197 | +0.088 | -305.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5025 | -0.107 | -954.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5025 | -0.107 | -954.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13677 | -0.042 | -1326.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13677 | -0.042 | -1326.79€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13673 | -0.115 | -1428.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13673 | -0.115 | -1428.47€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9318 | -0.138 | -1545.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9318 | -0.138 | -1545.59€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 53607 | -0.012 | +2727.29€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13808 | +0.004 | +1475.08€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 39799 | -0.017 | +1252.21€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 53607 | -0.012 | +2727.29€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13808 | +0.004 | +1475.08€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 39799 | -0.017 | +1252.21€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 202022 | +0.113 | -8268.71€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22655 | +0.180 | -714.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 937 | +0.017 | -73.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 166964 | +0.105 | -7058.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11466 | +0.094 | -421.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 27667 | +0.102 | -1973.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 82 | -0.179 | +13.53€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 27569 | +0.103 | -1978.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 37995 | +0.124 | -614.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5653 | +0.177 | -235.60€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 27636 | +0.120 | -183.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4664 | +0.081 | -172.74€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 27716 | +0.099 | -1957.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 94 | -0.115 | +14.54€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 27607 | +0.100 | -1961.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 43191 | +0.124 | -869.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10779 | +0.179 | -274.20€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 28081 | +0.106 | -520.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4319 | +0.103 | -65.64€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 37757 | +0.111 | -1681.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5951 | +0.199 | -246.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 840 | +0.042 | -19.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 28486 | +0.095 | -1225.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2480 | +0.104 | -189.73€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 27696 | +0.107 | -1172.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 96 | -0.133 | +12.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 27585 | +0.108 | -1188.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 32826 | +0.190 | -2395.89€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 32826 | +0.190 | -2395.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7444 | +0.163 | -847.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7444 | +0.163 | -847.45€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4855 | +0.196 | -189.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4855 | +0.196 | -189.72€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7274 | +0.173 | -663.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7274 | +0.173 | -663.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6037 | +0.252 | -210.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6037 | +0.252 | -210.89€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7137 | +0.184 | -498.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7137 | +0.184 | -498.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1296 | +0.425 | -48.47€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1296 | +0.425 | -48.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 541 | +0.439 | -4.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 541 | +0.439 | -4.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 527 | +0.422 | -21.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 527 | +0.422 | -21.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 214 | +0.398 | -18.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 214 | +0.398 | -18.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 116048 | +0.200 | -8492.35€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 116048 | +0.200 | -8492.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 20106 | +0.176 | -2349.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 20106 | +0.176 | -2349.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 18707 | +0.224 | -627.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 18707 | +0.224 | -627.07€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19913 | +0.181 | -2086.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19913 | +0.181 | -2086.28€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18863 | +0.217 | -753.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18863 | +0.217 | -753.86€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 19160 | +0.204 | -1160.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 19160 | +0.204 | -1160.68€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 19299 | +0.197 | -1515.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 19299 | +0.197 | -1515.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 45050 | +0.116 | +355.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 45050 | +0.116 | +355.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 22428 | +0.117 | +221.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 22428 | +0.117 | +221.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 22622 | +0.116 | +134.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 22622 | +0.116 | +134.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2717 | +0.294 | -7.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2717 | +0.294 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1243 | +0.283 | -25.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1243 | +0.283 | -25.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1332 | +0.297 | +10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1332 | +0.297 | +10.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1258 | +0.438 | -5.42€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1258 | +0.438 | -5.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 600 | +0.435 | -7.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 600 | +0.435 | -7.20€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 606 | +0.441 | +0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 606 | +0.441 | +0.37€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2002 | +0.066 | -92.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1277 | +0.078 | -28.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1568 | +0.073 | -47.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1277 | +0.078 | -28.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 91739 | +0.101 | -2018.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7423 | +0.097 | +174.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 84316 | +0.101 | -2193.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 50099 | +0.105 | -455.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7423 | +0.097 | +174.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 42676 | +0.107 | -630.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 19648 | +0.110 | -53.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 19648 | +0.110 | -53.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 21992 | +0.082 | -1510.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 21992 | +0.082 | -1510.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ GBM_LATE_15M | 62397 | +0.102 | +35036.34€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 62397 | +0.102 | +35036.34€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10339 | +0.225 | +8905.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10339 | +0.225 | +8905.54€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 9693 | +0.177 | +7739.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9693 | +0.177 | +7739.52€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 11177 | +0.207 | +8812.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11177 | +0.207 | +8812.44€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8271 | +0.061 | +2771.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8271 | +0.061 | +2771.95€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 8667 | -0.026 | +2251.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8667 | -0.026 | +2251.06€ | 4 | 16 |
| ✅ GBM_LATE_15M#XRP | 14250 | -0.020 | +4555.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 14250 | -0.020 | +4555.83€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 66193 | +0.087 | +38580.81€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 66193 | +0.087 | +38580.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12830 | -0.002 | +6750.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12830 | -0.002 | +6750.17€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 14219 | +0.007 | +3898.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 14219 | +0.007 | +3898.63€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8940 | +0.295 | +10224.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8940 | +0.295 | +10224.79€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12615 | +0.017 | +3994.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12615 | +0.017 | +3994.28€ | 1 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10124 | +0.048 | +4636.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10124 | +0.048 | +4636.05€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7465 | +0.313 | +9076.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7465 | +0.313 | +9076.90€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 49155 | +0.179 | +40870.93€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 49155 | +0.179 | +40870.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7421 | +0.240 | +6916.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7421 | +0.240 | +6916.57€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7801 | +0.142 | +5851.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7801 | +0.142 | +5851.91€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7919 | +0.224 | +6865.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7919 | +0.224 | +6865.91€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8415 | +0.130 | +6568.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8415 | +0.130 | +6568.08€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9287 | +0.122 | +7149.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9287 | +0.122 | +7149.16€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8312 | +0.233 | +7519.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8312 | +0.233 | +7519.31€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 13526 | +0.127 | +6925.03€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 13526 | +0.127 | +6925.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3533 | +0.126 | +1921.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3533 | +0.126 | +1921.41€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 508 | +0.157 | +288.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 508 | +0.157 | +288.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3942 | +0.129 | +2002.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3942 | +0.129 | +2002.92€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3611 | +0.102 | +1479.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3611 | +0.102 | +1479.42€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1255 | +0.168 | +785.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1255 | +0.168 | +785.18€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 62627 | +0.189 | +52015.80€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 62627 | +0.189 | +52015.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9884 | +0.250 | +9553.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9884 | +0.250 | +9553.14€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10025 | +0.142 | +7177.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10025 | +0.142 | +7177.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10627 | +0.234 | +9576.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10627 | +0.234 | +9576.67€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10361 | +0.144 | +7781.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10361 | +0.144 | +7781.79€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11072 | +0.127 | +8034.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11072 | +0.127 | +8034.71€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10658 | +0.241 | +9891.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10658 | +0.241 | +9891.78€ | 0 | 22 |
| ✅ GBM_LATE_5M | 16083 | +0.218 | +13477.35€ | 0 | 27 |
| ✅ GBM_LATE_5M#5min | 16083 | +0.218 | +13477.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1793 | +0.250 | +1724.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1793 | +0.250 | +1724.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3301 | +0.210 | +2820.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3301 | +0.210 | +2820.64€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 4598 | +0.209 | +3577.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4598 | +0.209 | +3577.64€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 2920 | +0.230 | +2604.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2920 | +0.230 | +2604.84€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5709 | +0.061 | +1582.10€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 5709 | +0.061 | +1582.10€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 23 | +0.260 | +17.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 23 | +0.260 | +17.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1938 | +0.061 | +557.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1938 | +0.061 | +557.51€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 24 | +0.346 | +23.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 24 | +0.346 | +23.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1796 | +0.057 | +580.19€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1796 | +0.057 | +580.19€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1902 | +0.056 | +388.33€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1902 | +0.056 | +388.33€ | 0 | 9 |
| ✅ GBM_LATE_60M#XRP | 26 | +0.250 | +14.70€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 26 | +0.250 | +14.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE | 745 | -0.251 | -40.80€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 745 | -0.251 | -40.80€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 267 | -0.258 | -22.59€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 267 | -0.258 | -22.59€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 270 | -0.246 | -9.52€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 270 | -0.246 | -9.52€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 206 | -0.245 | -9.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 206 | -0.245 | -9.36€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2297 | +0.087 | +579.14€ | 1 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2297 | +0.087 | +579.14€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 872 | +0.069 | +195.07€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 872 | +0.069 | +195.07€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 789 | +0.059 | +152.66€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 789 | +0.059 | +152.66€ | 1 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 636 | +0.147 | +231.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 636 | +0.147 | +231.41€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 345 | +0.318 | +421.84€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 345 | +0.318 | +421.84€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 345 | +0.318 | +421.84€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 345 | +0.318 | +421.84€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4641 | +0.096 | +1035.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4641 | +0.096 | +1035.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4641 | +0.096 | +1035.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4641 | +0.096 | +1035.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1565 | +0.014 | +77.23€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1565 | +0.014 | +77.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 163 | +0.076 | +26.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 163 | +0.076 | +26.55€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M#BTC | 323 | -0.017 | +5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 323 | -0.017 | +5.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 98 | +0.030 | +13.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 98 | +0.030 | +13.56€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#ETH | 366 | +0.033 | +26.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 366 | +0.033 | +26.16€ | 1 | 2 |
| ✅ LIQUIDACIONES_15M#SOL | 342 | -0.015 | +2.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 342 | -0.015 | +2.34€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 273 | +0.020 | +2.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 273 | +0.020 | +2.86€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4488 | +0.015 | +158.02€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4488 | +0.015 | +158.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 240 | +0.004 | -5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 240 | +0.004 | -5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 855 | +0.012 | +41.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 855 | +0.012 | +41.63€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 309 | +0.056 | +67.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 309 | +0.056 | +67.39€ | 0 | 7 |
| ✅ LIQUIDACIONES_5M#ETH | 1683 | +0.019 | +28.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1683 | +0.019 | +28.75€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 781 | +0.011 | +2.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 781 | +0.011 | +2.47€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 620 | -0.006 | +23.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 620 | -0.006 | +23.43€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2630 | -0.033 | -6.07€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2630 | -0.033 | -6.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 801 | -0.034 | -14.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 801 | -0.034 | -14.36€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 943 | -0.012 | +19.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 943 | -0.012 | +19.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 884 | -0.054 | -10.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 884 | -0.054 | -10.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 18892 | -0.031 | -121.74€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 9130 | -0.034 | -127.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 9762 | -0.028 | +5.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 658 | -0.053 | -35.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 336 | -0.035 | -5.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 322 | -0.071 | -30.68€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5006 | -0.026 | -22.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2382 | -0.024 | -6.48€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2624 | -0.027 | -15.81€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1760 | -0.031 | +5.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 897 | -0.043 | -24.07€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 863 | -0.019 | +29.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4303 | -0.029 | -22.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2069 | -0.029 | -11.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2234 | -0.029 | -10.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3630 | -0.022 | +64.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1768 | -0.030 | -3.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1862 | -0.013 | +67.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3535 | -0.044 | -110.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1678 | -0.051 | -76.56€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1857 | -0.037 | -33.80€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 73756 | -0.000 | +4026.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 73756 | -0.000 | +4026.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13401 | +0.027 | +1870.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13401 | +0.027 | +1870.60€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10224 | -0.039 | -161.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10224 | -0.039 | -161.71€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 13558 | +0.025 | +1544.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 13558 | +0.025 | +1544.69€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10221 | -0.053 | -270.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10221 | -0.053 | -270.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12572 | -0.004 | +356.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12572 | -0.004 | +356.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13780 | +0.019 | +687.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13780 | +0.019 | +687.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7322 | -0.054 | -114.41€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7322 | -0.054 | -114.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2056 | -0.061 | -22.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2056 | -0.061 | -22.02€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 96 | -0.031 | -1.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 96 | -0.031 | -1.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 817 | -0.117 | -33.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 817 | -0.117 | -33.11€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2216 | -0.069 | -16.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2216 | -0.069 | -16.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 868 | -0.018 | -27.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 868 | -0.018 | -27.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3383 | +0.003 | +0.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3383 | +0.003 | +0.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 199 | +0.007 | -1.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 199 | +0.007 | -1.73€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 180857 | -0.077 | +2266.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 180857 | -0.077 | +2266.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 31843 | -0.076 | +1850.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 31843 | -0.076 | +1850.42€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 26863 | -0.102 | -1367.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 26863 | -0.102 | -1367.30€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 32272 | -0.068 | +1585.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 32272 | -0.068 | +1585.13€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 26410 | -0.100 | -935.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 26410 | -0.100 | -935.55€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 32283 | -0.059 | +271.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 32283 | -0.059 | +271.84€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 31186 | -0.069 | +861.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 31186 | -0.069 | +861.66€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9243 | -0.035 | -180.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9243 | -0.035 | -180.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1009 | -0.017 | -19.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1009 | -0.017 | -19.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2151 | -0.045 | -25.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2151 | -0.045 | -25.63€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2672 | -0.024 | -33.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2672 | -0.024 | -33.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1296 | -0.064 | -32.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1296 | -0.064 | -32.46€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1106 | -0.034 | -37.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1106 | -0.034 | -37.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2299 | +0.122 | +937.37€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2163 | +0.126 | +924.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 503 | +0.140 | +256.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 503 | +0.140 | +256.65€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 451 | +0.116 | +156.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 451 | +0.116 | +156.84€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 405 | +0.127 | +184.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 405 | +0.127 | +184.01€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 364 | +0.142 | +188.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 364 | +0.142 | +188.80€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 440 | +0.104 | +138.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 440 | +0.104 | +138.47€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2416 | -0.019 | -22.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2416 | -0.019 | -22.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 430 | +0.009 | +22.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 430 | +0.009 | +22.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 444 | -0.045 | -26.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 444 | -0.045 | -26.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 595 | -0.044 | -40.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 595 | -0.044 | -40.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 498 | +0.004 | +8.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 498 | +0.004 | +8.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 449 | -0.010 | +12.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 449 | -0.010 | +12.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1267 | -0.044 | +123.42€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 586 | -0.071 | +19.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 457 | -0.069 | +43.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 445 | -0.015 | +66.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 324 | +0.006 | +75.05€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 236 | -0.029 | +37.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 200 | -0.020 | +35.52€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 981 | -0.034 | +154.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1606 | -0.185 | -35.21€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 629 | -0.173 | -10.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 558 | -0.170 | -6.79€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 71 | -0.199 | -3.91€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 539 | -0.197 | -31.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 476 | -0.205 | -37.91€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 63 | -0.131 | +6.63€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 438 | -0.186 | +6.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 407 | -0.182 | +5.14€ | 6 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 31 | -0.227 | +1.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1441 | -0.185 | -39.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 165 | -0.183 | +4.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 575 | +0.377 | +522.87€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#BTC | 128 | +0.169 | +97.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 128 | +0.169 | +97.55€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#ETH | 130 | +0.371 | +107.64€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 130 | +0.371 | +107.64€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 317 | +0.459 | +317.69€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 317 | +0.459 | +317.69€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 575 | +0.377 | +522.87€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1013 | +0.037 | +77.05€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1013 | +0.037 | +77.05€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 77 | +0.019 | +0.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 77 | +0.019 | +0.67€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 492 | +0.057 | +66.44€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 492 | +0.057 | +66.44€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3622 | -0.023 | -141.61€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3622 | -0.023 | -141.61€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 623 | -0.028 | -27.00€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 623 | -0.028 | -27.00€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 174 | -0.045 | -15.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 174 | -0.045 | -15.30€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1698 | -0.018 | -59.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1698 | -0.018 | -59.10€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 130 | -0.030 | -11.72€ | 3 | 1 |
| ✅ STREAK_FADE_60M#60min | 130 | -0.030 | -11.72€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 46 | -0.062 | -3.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 46 | -0.062 | -3.71€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 81 | -0.006 | -6.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 81 | -0.006 | -6.44€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11606 | +0.013 | +67.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11606 | +0.013 | +67.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3000 | +0.018 | +23.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3000 | +0.018 | +23.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3074 | +0.014 | +27.73€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3074 | +0.014 | +27.73€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2937 | +0.008 | -4.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2937 | +0.008 | -4.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2595 | +0.014 | +20.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2595 | +0.014 | +20.38€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12998 | +0.019 | +7.39€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12998 | +0.019 | +7.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5309 | +0.021 | +5.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5309 | +0.021 | +5.47€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4569 | +0.019 | +2.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4569 | +0.019 | +2.45€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3120 | +0.015 | -0.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3120 | +0.015 | -0.53€ | 1 | 0 |
| ✅ UPDOWN_GBM | 118799 | +0.060 | +11268.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 29165 | +0.078 | +5739.20€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3406 | -0.000 | +40.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 78767 | +0.062 | +5364.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7060 | -0.002 | +127.87€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10399 | +0.103 | +1881.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1885 | +0.166 | +890.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8424 | +0.090 | +993.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 26847 | +0.057 | +2370.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3907 | +0.080 | +869.19€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 990 | -0.001 | +20.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 18654 | +0.067 | +1397.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3151 | -0.005 | +78.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 145 | -0.065 | +5.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 13178 | +0.074 | +1430.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1876 | +0.153 | +787.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11216 | +0.062 | +643.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 27850 | +0.050 | +1994.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6836 | +0.072 | +1071.46€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 958 | +0.005 | +15.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 17312 | +0.052 | +864.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2610 | -0.000 | +41.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 134 | -0.103 | +2.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 24824 | +0.040 | +1403.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7914 | +0.033 | +465.57€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 885 | -0.010 | +9.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14606 | +0.052 | +931.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1299 | +0.004 | +8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 120 | -0.147 | -10.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 15699 | +0.073 | +2189.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6747 | +0.090 | +1655.79€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8555 | +0.062 | +534.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 399 | -0.103 | -2.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1038 | +0.364 | +386.63€ | 0 | 7 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1038 | +0.364 | +386.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 498 | +0.364 | +175.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 498 | +0.364 | +175.03€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 540 | +0.363 | +211.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 540 | +0.363 | +211.60€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 27909 | -0.018 | +6944.84€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 27909 | -0.018 | +6944.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2106 | -0.048 | +578.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2106 | -0.048 | +578.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5169 | -0.116 | +271.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5169 | -0.116 | +271.64€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1150 | +0.220 | +953.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1150 | +0.220 | +953.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3745 | +0.220 | +2403.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3745 | +0.220 | +2403.78€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7923 | -0.057 | +1177.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7923 | -0.057 | +1177.19€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7816 | -0.054 | +1559.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7816 | -0.054 | +1559.33€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 347 | +0.059 | +33.54€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 347 | +0.059 | +33.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 347 | +0.059 | +33.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 347 | +0.059 | +33.54€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1916 | +0.282 | +1621.12€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1916 | +0.282 | +1621.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1009 | +0.277 | +805.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1009 | +0.277 | +805.08€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 907 | +0.288 | +816.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 907 | +0.288 | +816.04€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 888 | -0.118 | -92.38€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 888 | -0.118 | -92.38€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 285 | -0.085 | -22.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 285 | -0.085 | -22.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 103 | -0.195 | -15.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 103 | -0.195 | -15.02€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 117 | -0.181 | -5.50€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 117 | -0.181 | -5.50€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 5145 | +0.295 | +2268.34€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1988 | +0.252 | +269.90€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1994 | +0.288 | +842.21€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1163 | +0.382 | +1156.24€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.024 n=1460 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1460 IC=+0.024 PNL=+71.73€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 840 celda(s) pasan gate riguroso completo de 3018 evaluadas (n>=40) y 4133 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=7909 IC=+0.033 PNL=+467.79€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1994/15 IC=+0.288 PNL=+842.21€ | BTC: n=1988/15 IC=+0.252 PNL=+269.90€ | SOL: n=1163/15 IC=+0.382 PNL=+1156.24€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.134 n=1115/60 | contraria IC=+0.185 n=1176 | gap=-0.051 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=628, boost estimado=+0.010. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2608/40 IC=-0.000 PNL=+41.16€ | BTC#60min: n=3149/40 IC=-0.005 PNL=+78.68€ | SOL#60min: n=1299/40 IC=+0.004 PNL=+8.03€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=795504 | tras_1loss IC=+0.102 n=602103 | tras_2loss IC=+0.073 n=239649/40 | gap=-0.028 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.154 > 0.08 con n=1195 PNL=+692.47€
  - _Datos_: n=1195 IC=+0.154 PNL=+692.47€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.08 con n=1427 PNL=+637.19€
  - _Datos_: n=1427 IC=+0.125 PNL=+637.19€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=4196 PNL=+2384.48€
  - _Datos_: n=4196 IC=+0.335 PNL=+2384.48€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1202 IC=+0.062 PNL=+118.09€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1202 IC=+0.062 PNL=+118.09€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=111 IC=+0.181 PNL=+74.29€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=111 IC=+0.181 PNL=+74.29€

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
  - _Estado_: n=4636 IC=-0.005 PNL=-43.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4636 IC=-0.005 PNL=-43.44€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2420 IC=+0.004 PNL=+171.31€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2420 IC=+0.004 PNL=+171.31€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1460 IC=+0.024 PNL=+71.73€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1460 IC=+0.024 PNL=+71.73€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.134 > 0.1 con n=8075 PNL=+3876.05€
  - _Datos_: n=8075 IC=+0.134 PNL=+3876.05€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3905 IC=+0.080 PNL=+868.43€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3905 IC=+0.080 PNL=+868.43€

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
  - _Estado_: n=1580 IC=+0.042 PNL=+126.62€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1580 IC=+0.042 PNL=+126.62€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=196 IC=-0.030 PNL=-6.77€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=196 IC=-0.030 PNL=-6.77€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.318 n=345) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=345 IC=+0.318 PNL=+421.84€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.02 con n=1342 PNL=+553.16€
  - _Datos_: n=1342 IC=+0.120 PNL=+553.16€

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
  - _Estado_: n=48750 IC=+0.069 PNL=+6493.52€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=48750 IC=+0.069 PNL=+6493.52€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=810 PNL=+116.83€
  - _Datos_: n=810 IC=-0.137 PNL=+116.83€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4694 IC=+0.068 PNL=+578.50€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4694 IC=+0.068 PNL=+578.50€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=204 IC=-0.078 PNL=+7.38€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=204 IC=-0.078 PNL=+7.38€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1260 IC=+0.097 PNL=+306.17€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1260 IC=+0.097 PNL=+306.17€

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
  - _Estado_: n=47338 IC=-0.138 PNL=+2888.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=47338 IC=-0.138 PNL=+2888.96€

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
  - _Estado_: n=5055 IC=+0.135 PNL=+3469.94€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5055 IC=+0.135 PNL=+3469.94€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=12361 IC=+0.056 PNL=+1044.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12361 IC=+0.056 PNL=+1044.35€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=5110 PNL=+2881.35€
  - _Datos_: n=5110 IC=+0.102 PNL=+2881.35€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.221 < -0.1 con n=5153 PNL=-416.04€
  - _Datos_: n=5153 IC=-0.221 PNL=-416.04€

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
  - _Estado_: n=129 IC=+0.065 PNL=+20.72€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=129 IC=+0.065 PNL=+20.72€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=2356) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2356 IC=+0.097 PNL=+471.64€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.415 n=693) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=693 IC=+0.415 PNL=+1018.07€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=20095 IC=+0.176 PNL=-2345.20€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=20095 IC=+0.176 PNL=-2345.20€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.233 > 0.1 con n=331 PNL=+231.88€
  - _Datos_: n=331 IC=+0.233 PNL=+231.88€
