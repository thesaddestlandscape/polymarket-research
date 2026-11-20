# Hipótesis automáticas — 2026-11-20 05:26 UTC
_Generado por shadow_postmortem.py sobre 1417505 resoluciones (PNL=+199159.44€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=729)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.192 (n=1075)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.121)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.121)

- **PATRÓN** `banda_hit_calibrado` > `0.8124` → IC=+0.270 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8124 (IC base=+0.121)

- **PATRÓN** `banda_z` > `8.322` → IC=+0.191 (n=338)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.322 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.127 (n=917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=1104)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.121)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=518)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.189 (n=938)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.180 (n=298)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 64.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8121` → IC=+0.268 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8121 (IC base=+0.122)

- **PATRÓN** `banda_z` > `8.618` → IC=+0.203 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.618 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.131 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=1004)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.122)

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
- **FILTRO** `restante_s_al_confirmar` < `130.88` → IC=-0.218 (n=12586)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.88
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=37759)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.78` → IC=-0.263 (n=1262)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.78
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3789)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.83` → IC=-0.281 (n=1264)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.83
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3793)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.18` → IC=-0.167 (n=3456)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.18
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=10371)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.3` → IC=-0.241 (n=3455)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.3
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10368)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.79` → IC=-0.267 (n=2334)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.79
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=7003)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=29756)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `7955.5375` → IC=+0.154 (n=2436)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7955.5375 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=26139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=31691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=23755)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=8671)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6381.3936` → IC=+0.141 (n=3378)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6381.3936 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2709)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `16269.689` → IC=+0.181 (n=704)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16269.689 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2762)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16056.5393` → IC=+0.185 (n=713)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16056.5393 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=2359)

- **PATRÓN** `py_entrada` > `0.615` → IC=+0.172 (n=614)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.615 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.151 (n=1536)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.44 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=5406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 8.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=2578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.333 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=3016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.145 (n=697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=938)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.252 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1177)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.252 (n=981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=481)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.161 (n=481)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.047)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=1326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.133 (n=1018)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.253 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=78)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=26098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=22049)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.226 (n=8303)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=5950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.175 (n=5814)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.163)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=3631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.209 (n=2423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.246 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.205)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=5805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=4921)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.174 (n=5961)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4568)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1587)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=5680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.190 (n=3611)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=4211)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.184)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.427 (n=1012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=1003)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `13955.5496` → IC=+0.448 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13955.5496 (IC base=+0.423)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.435 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `15243.1529` → IC=+0.442 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15243.1529 (IC base=+0.436)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=29383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=33897)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=5124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.177 (n=10951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=15734)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=14240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6113)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=14283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=12113)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=4792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.260 (n=5927)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=4850)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=4885)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=5692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=5784)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=12333)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=13332)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.3` → IC=+0.143 (n=11482)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.3 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=6017)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=6051)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.82` → IC=+0.142 (n=7502)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.82 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6316)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=8055)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.96` → IC=+0.137 (n=7567)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.96 (IC base=+0.116)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.435 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.435)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4987` → IC=+0.139 (n=19507)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4987 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=19727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=13573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.975` → IC=+0.246 (n=6509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.975 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8374` → IC=+0.287 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8374 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.475` → IC=+0.190 (n=9800)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.475 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.268 (n=5311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6975 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3036` → IC=+0.253 (n=2025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3036 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7429` → IC=+0.231 (n=4710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7429 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=9498)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4773.1132` → IC=+0.151 (n=6503)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4773.1132 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.123 (n=12314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0065 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5636` → IC=+0.146 (n=24622)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5636 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.4069` → IC=+0.190 (n=2339)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.4069 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1723` → IC=+0.194 (n=10056)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1723 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8594` → IC=+0.196 (n=6818)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8594 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.296` → IC=+0.233 (n=2488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.296 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4565` → IC=+0.210 (n=17339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4565 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=17298)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.246 (n=1391)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.2996` → IC=+0.214 (n=3650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2996 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=2017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.273 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.435` → IC=+0.277 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.435 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2349` → IC=+0.256 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2349 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4434` → IC=+0.210 (n=3981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4434 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=4562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2038.2656` → IC=+0.215 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.2656 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.218 (n=3363)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.249 (n=2488)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.272 (n=1244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=3878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.0756` → IC=+0.281 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0756 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.957` → IC=+0.246 (n=3823)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.957 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.245 (n=3224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.251 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4488` → IC=+0.242 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4488 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.8601` → IC=+0.245 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8601 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=4270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.233 (n=1182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.223 (n=1180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1131` → IC=+0.246 (n=1558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1131 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.223 (n=2519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.8942` → IC=+0.257 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8942 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1983` → IC=+0.232 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1983 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.76` → IC=+0.264 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.76 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6992` → IC=+0.229 (n=3156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6992 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.267 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4452` → IC=+0.250 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4452 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `15809.9496` → IC=+0.224 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15809.9496 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.153 (n=3863)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0068 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2724` → IC=+0.148 (n=3398)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.2724 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=2750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7084` → IC=+0.173 (n=3862)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7084 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.149` → IC=+0.151 (n=3791)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.149 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.942` → IC=+0.141 (n=3540)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.942 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6292` → IC=+0.153 (n=1288)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6292 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0981` → IC=+0.161 (n=1406)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0981 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.142 (n=3732)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7903` → IC=+0.137 (n=2488)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.7903 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5019)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `190.0` → IC=+0.179 (n=1619)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 190.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.013` → IC=+0.203 (n=1469)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=4623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.916` → IC=+0.280 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.916 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.191 (n=3947)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.221 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.7293` → IC=+0.206 (n=1950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7293 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=5353)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `1903.9584` → IC=+0.195 (n=1995)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1903.9584 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.224 (n=3624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.3028` → IC=+0.230 (n=2740)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3028 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.228 (n=1870)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.272 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.736` → IC=+0.270 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.736 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.255 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.232 (n=2644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1986)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1882.9554` → IC=+0.226 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.9554 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.225 (n=3940)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.168 (n=233)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=5308)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.144 (n=709)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.248 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1538` → IC=+0.346 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1538 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.5766` → IC=+0.343 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5766 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.213 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.1225` → IC=+0.363 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1225 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.0768` → IC=+0.341 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0768 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.351 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.359 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.349 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.348 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.0866` → IC=+0.193 (n=1386)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.0866 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.3551` → IC=+0.163 (n=677)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3551 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1476` → IC=+0.158 (n=2586)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1476 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8315` → IC=+0.165 (n=1810)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8315 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.208 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.4336` → IC=+0.174 (n=872)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4336 (IC base=+0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.196 (n=156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=854)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.172 (n=251)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=759)

- **FILTRO** `ibs_20min` > `0.1966` → IC=-0.127 (n=5211)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1966
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=2568)

- **FILTRO** `sigma_ewma_delta_pct` > `8.292` → IC=-0.233 (n=840)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.292
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=6939)

- **PATRÓN** `ibs_20min` > `0.7544` → IC=+0.176 (n=344)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7544 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.9728` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9728 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.249` → IC=+0.141 (n=343)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 2.249 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.284 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.624 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.281 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.290 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.262 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.270 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.1966` → IC=+0.163 (n=2568)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1966 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.2322` → IC=+0.291 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2322 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.3189` → IC=+0.291 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3189 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.299 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `1.043` → IC=+0.294 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.043 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0777` → IC=+0.314 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0777 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4313` → IC=+0.303 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4313 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.4143` → IC=+0.298 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4143 (IC base=-0.031)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7973` → IC=-0.157 (n=4000)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7973
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=2061)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.176 (n=1247)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4814)

- **FILTRO** `ibs_20min` > `0.7297` → IC=-0.190 (n=2090)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7297
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=6292)

- **PATRÓN** `ibs_20min` > `0.7973` → IC=+0.140 (n=2061)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.7973 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.44` → IC=+0.337 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.44 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7065` → IC=+0.319 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7065 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` < `0.1089` → IC=+0.299 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1089 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1723` → IC=+0.306 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1723 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.8911` → IC=+0.308 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8911 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.0763` → IC=+0.290 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0763 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.6427` → IC=+0.275 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6427 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.0635` → IC=+0.277 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0635 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.281 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `2.1811` → IC=+0.264 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1811 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.442` → IC=+0.270 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.442 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.190 (n=8526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.011 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.8657` → IC=+0.283 (n=11592)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8657 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.9695` → IC=+0.300 (n=1764)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9695 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.464` → IC=+0.167 (n=11512)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.464 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.6939` → IC=+0.278 (n=8480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6939 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.296 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.639` → IC=+0.287 (n=4946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.639 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.308 (n=14494)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.161 (n=8288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0105 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5163` → IC=+0.174 (n=21874)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5163 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.2745` → IC=+0.283 (n=8748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2745 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.281 (n=3708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `1.1887` → IC=+0.287 (n=2808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1887 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.324 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `1.4529` → IC=+0.305 (n=4176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4529 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.2684` → IC=+0.304 (n=5677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2684 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.312 (n=12525)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.087)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8111` → IC=-0.145 (n=4534)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8111
  - _Potencial_: sin este filtro IC_bueno=+0.310 (n=2336)

- **FILTRO** `ibs_20min` > `0.7029` → IC=-0.239 (n=1541)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7029
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=4624)

- **FILTRO** `sigma_ewma_delta_pct` > `4.068` → IC=-0.241 (n=1303)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.068
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=4862)

- **PATRÓN** `ibs_20min` > `0.8111` → IC=+0.310 (n=2336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8111 (IC base=+0.010)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.132` → IC=+0.174 (n=2559)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 2.132 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.333 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.449` → IC=+0.288 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.449 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.2336` → IC=+0.313 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2336 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.314 (n=1928)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.010)

- **PATRÓN** `ibs_20min` < `0.1705` → IC=+0.174 (n=1542)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1705 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.153` → IC=+0.392 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.153 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.6396` → IC=+0.394 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6396 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1775` → IC=+0.227 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1775 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6958` → IC=+0.220 (n=2230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6958 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.245 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.417` → IC=+0.232 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.417 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4502` → IC=+0.221 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4502 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `371.0` → IC=+0.233 (n=2470)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 371.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.1504` → IC=+0.265 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1504 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `0.6836` → IC=+0.252 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6836 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.1628` → IC=+0.270 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1628 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.303 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.536` → IC=+0.261 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.536 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1537` → IC=+0.268 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1537 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `176.0` → IC=+0.278 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 176.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.318 (n=1599)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.582` → IC=+0.305 (n=2384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.582 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1311` → IC=+0.292 (n=3275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1311 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2398` → IC=+0.299 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2398 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2013.3448` → IC=+0.295 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2013.3448 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.302 (n=2158)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.336 (n=2186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1857` → IC=+0.326 (n=1443)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1857 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=1259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.0286` → IC=+0.308 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0286 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1531` → IC=+0.317 (n=2183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1531 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.056` → IC=+0.317 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.056 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.401` → IC=+0.307 (n=3393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.401 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1985` → IC=+0.308 (n=3249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1985 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3435` → IC=+0.314 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3435 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7396` → IC=+0.323 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7396 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.307 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1993.9956` → IC=+0.315 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1993.9956 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.311 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7135` → IC=-0.172 (n=1610)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7135
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=4831)

- **PATRÓN** `dist_vwap_pct` > `0.1545` → IC=+0.236 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1545 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.611` → IC=+0.235 (n=2559)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.611 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1683` → IC=+0.236 (n=2324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1683 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.5971` → IC=+0.233 (n=2324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5971 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.242 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4118` → IC=+0.241 (n=2257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4118 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.251 (n=2302)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.0913` → IC=+0.155 (n=1611)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.0913 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.3722` → IC=+0.262 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3722 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.1804` → IC=+0.265 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1804 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6165` → IC=+0.258 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6165 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.295 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.7865` → IC=+0.286 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7865 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.279 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.284 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.011)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.246 (n=2636)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2638)

- **FILTRO** `ibs_20min` > `0.6111` → IC=-0.237 (n=1241)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6111
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=3757)

- **FILTRO** `sigma_ewma_delta_pct` > `8.264` → IC=-0.268 (n=572)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.264
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=4426)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.313 (n=2638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `1.0764` → IC=+0.350 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0764 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.439` → IC=+0.157 (n=2152)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.439 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8458` → IC=+0.346 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8458 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `0.6967` → IC=+0.334 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6967 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.335 (n=1821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.366 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.432` → IC=+0.365 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.432 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.351 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.6111` → IC=+0.164 (n=3757)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.6111 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.3224` → IC=+0.276 (n=2005)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3224 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.736` → IC=+0.133 (n=3917)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.736 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` < `0.6909` → IC=+0.285 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6909 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.297 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `2.1191` → IC=+0.282 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1191 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.292 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.064)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.352 (n=2450)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=2763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=2878)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.6512` → IC=+0.338 (n=2743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6512 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2172` → IC=+0.336 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2172 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.819` → IC=+0.336 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.819 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.6291` → IC=+0.324 (n=2742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6291 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.346 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.531` → IC=+0.324 (n=2366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.531 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `3008.0552` → IC=+0.324 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3008.0552 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.332 (n=2956)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.316 (n=2661)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=2961)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.3889` → IC=+0.329 (n=2958)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3889 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.3441` → IC=+0.314 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3441 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2536` → IC=+0.317 (n=2913)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2536 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.219` → IC=+0.323 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.219 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.7171` → IC=+0.316 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7171 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2096` → IC=+0.339 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2096 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.363 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4152` → IC=+0.324 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4152 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1501` → IC=+0.316 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1501 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.220 (n=6251)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.192 (n=8244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=19438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.537` → IC=+0.229 (n=18729)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.537 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.167` → IC=+0.205 (n=7064)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.167 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.747` → IC=+0.259 (n=3673)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.747 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1745` → IC=+0.151 (n=12489)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1745 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.151 (n=12488)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6223 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.205 (n=2704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5958` → IC=+0.183 (n=6080)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5958 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.190 (n=17694)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 85.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.193 (n=8220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0061 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.188 (n=12466)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0081 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0843` → IC=+0.222 (n=6225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0843 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=8931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.248 (n=16449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1919` → IC=+0.180 (n=13660)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1919 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.448` → IC=+0.190 (n=2950)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.448 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.496` → IC=+0.193 (n=16645)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.496 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.166 (n=13234)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1888 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.218 (n=2804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6306` → IC=+0.198 (n=5945)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6306 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=17647)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.258 (n=1026)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.263 (n=1025)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9426` → IC=+0.292 (n=2048)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9426 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.453` → IC=+0.327 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.453 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2317` → IC=+0.279 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2317 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8356` → IC=+0.226 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8356 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4397` → IC=+0.226 (n=2937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4397 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3395)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2042.82` → IC=+0.227 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.82 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.257 (n=2578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.265 (n=1720)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.1` → IC=+0.308 (n=1135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.261 (n=2350)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.0604` → IC=+0.300 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0604 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.242` → IC=+0.261 (n=2880)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.242 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.258 (n=2272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.2997` → IC=+0.269 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2997 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `2.2687` → IC=+0.260 (n=2177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2687 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.6807` → IC=+0.257 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6807 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.262 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1925.6008` → IC=+0.256 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1925.6008 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.192 (n=953)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0033 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0663` → IC=+0.172 (n=952)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0663 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2535` → IC=+0.206 (n=2856)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2535 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1927` → IC=+0.211 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1927 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.572` → IC=+0.205 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.572 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.854` → IC=+0.134 (n=1904)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.854 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0479` → IC=+0.133 (n=1295)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.0479 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.170 (n=440)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.7718` → IC=+0.129 (n=1874)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7718 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4591` → IC=+0.141 (n=937)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4591 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `390.0` → IC=+0.134 (n=2778)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 390.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.180 (n=2715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0059 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2506` → IC=+0.176 (n=2713)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2506 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=1468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.212 (n=3083)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6112 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2125` → IC=+0.176 (n=3355)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2125 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.871` → IC=+0.182 (n=574)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.871 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.158 (n=2697)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.163 (n=3083)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2068 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.154 (n=2565)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4807` → IC=+0.156 (n=2956)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4807 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.194 (n=1280)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 204.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.219 (n=2117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.2541` → IC=+0.231 (n=2114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2541 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=3308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.023` → IC=+0.304 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.023 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.233 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.71` → IC=+0.220 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.71 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=3851)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2007.4196` → IC=+0.219 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.4196 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.246 (n=2857)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0121 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.2503` → IC=+0.269 (n=1905)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2503 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.277 (n=1085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0415` → IC=+0.296 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0415 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.854` → IC=+0.286 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.854 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3529` → IC=+0.283 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3529 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.241 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1766` → IC=+0.252 (n=1845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1766 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1984.9796` → IC=+0.255 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1984.9796 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `4.0` → IC=+0.240 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 4.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.194 (n=1038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0807` → IC=+0.174 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0807 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2452` → IC=+0.188 (n=3090)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2452 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1465` → IC=+0.188 (n=1743)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1465 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.227` → IC=+0.199 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.227 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.838` → IC=+0.136 (n=2060)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.838 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.172 (n=465)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.129 (n=1332)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5007` → IC=+0.135 (n=1009)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.5007 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6954.443` → IC=+0.195 (n=1401)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 6954.443 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.126 (n=3036)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 123.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.160 (n=2916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.007 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4255` → IC=+0.149 (n=3313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4255 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6688` → IC=+0.189 (n=3313)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6688 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1673` → IC=+0.157 (n=3395)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1673 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.534` → IC=+0.142 (n=1134)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.534 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.055` → IC=+0.134 (n=2946)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.055 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8537` → IC=+0.151 (n=2209)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8537 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.175 (n=497)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1879` → IC=+0.134 (n=2775)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1879 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4111` → IC=+0.136 (n=3153)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4111 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6618.0659` → IC=+0.193 (n=1502)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6618.0659 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.156 (n=1077)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.171 (n=1148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0128 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5938` → IC=+0.224 (n=3079)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5938 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.7777` → IC=+0.212 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7777 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.005` → IC=+0.287 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.005 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1661` → IC=+0.130 (n=3445)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1661 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.122 (n=3521)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.7832` → IC=+0.125 (n=2230)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7832 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2708.6353` → IC=+0.196 (n=1562)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2708.6353 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.127 (n=1475)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 19.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.144 (n=3620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0122 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1181` → IC=+0.167 (n=1206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1181 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6442` → IC=+0.223 (n=3616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6442 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.222` → IC=+0.148 (n=3595)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.222 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.237` → IC=+0.146 (n=3197)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.237 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1787` → IC=+0.130 (n=3616)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1787 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8594` → IC=+0.127 (n=2410)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8594 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1625` → IC=+0.128 (n=3571)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1625 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.145 (n=500)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4361` → IC=+0.145 (n=1144)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4361 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4414` → IC=+0.135 (n=1144)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4414 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2604.5498` → IC=+0.189 (n=1639)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2604.5498 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.131 (n=3428)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 43.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.246 (n=3101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.168` → IC=+0.241 (n=1364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.168 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=3218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6648` → IC=+0.255 (n=3099)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6648 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1837` → IC=+0.233 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1837 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8119` → IC=+0.226 (n=3195)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8119 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.527` → IC=+0.261 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.527 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6195` → IC=+0.235 (n=3099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6195 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.266 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.228 (n=3026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4362` → IC=+0.228 (n=3026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4362 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2620.2181` → IC=+0.232 (n=2066)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.2181 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0166` → IC=+0.248 (n=2150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0166 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6109` → IC=+0.248 (n=3224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6109 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=1586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.241 (n=1451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.299 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `1.1517` → IC=+0.255 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1517 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.075` → IC=+0.269 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.075 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8673` → IC=+0.240 (n=2150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8673 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0469` → IC=+0.244 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0469 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2844` → IC=+0.290 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2844 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8444` → IC=+0.238 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8444 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5529` → IC=+0.238 (n=2728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5529 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.205 (n=1650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1419` → IC=+0.170 (n=2166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1419 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=5126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.4225` → IC=+0.198 (n=4398)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4225 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2329` → IC=+0.172 (n=1853)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.2329 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.208 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8592` → IC=+0.163 (n=2979)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8592 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1917` → IC=+0.159 (n=1490)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1917 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.171 (n=1273)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5264` → IC=+0.161 (n=2113)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5264 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=4159)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7289.8412` → IC=+0.192 (n=2232)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7289.8412 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.387` → IC=+0.179 (n=3597)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.387 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.148 (n=2368)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 22.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.205 (n=1189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1038` → IC=+0.230 (n=524)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1038 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.225 (n=1071)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.6225` → IC=+0.254 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6225 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.3183` → IC=+0.224 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3183 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.221 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.6273` → IC=+0.221 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6273 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.0908` → IC=+0.210 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0908 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `2.1568` → IC=+0.206 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1568 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `13775.8941` → IC=+0.203 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13775.8941 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.157 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0032 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.2163` → IC=+0.194 (n=654)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.2163 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.142 (n=970)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 236.0 (IC base=+0.073)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.228 (n=664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1315` → IC=+0.158 (n=664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1315 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=1564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.778` → IC=+0.264 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.778 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.872` → IC=+0.186 (n=234)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.872 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.932` → IC=+0.196 (n=215)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.932 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.165 (n=1006)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8342 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.191 (n=202)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.7716` → IC=+0.168 (n=991)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.7716 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7977.8596` → IC=+0.178 (n=684)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7977.8596 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.150 (n=656)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 37.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.133 (n=669)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0044 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.1841` → IC=+0.200 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1841 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `0.6756` → IC=+0.143 (n=667)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6756 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.077` → IC=+0.124 (n=554)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.077 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `5613.8653` → IC=+0.148 (n=1010)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5613.8653 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.129 (n=1300)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 80.0 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.152 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.007 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=1244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` > `0.5319` → IC=+0.177 (n=1183)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.5319 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.2076` → IC=+0.127 (n=623)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.2076 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.859` → IC=+0.215 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.859 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.136 (n=226)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4134` → IC=+0.142 (n=428)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4134 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2438.4131` → IC=+0.132 (n=883)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2438.4131 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.3611` → IC=+0.199 (n=978)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3611 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2742.7184` → IC=+0.163 (n=663)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2742.7184 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.121 (n=977)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 19.0 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.238 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.8608` → IC=+0.181 (n=396)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.8608 (IC base=+0.179)

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

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.173 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0105 (IC base=+0.156)

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

- **PATRÓN** `dist_vwap_pct` < `0.2927` → IC=+0.158 (n=460)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2927 (IC base=+0.156)

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
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.225 (n=8247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=25774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9677` → IC=+0.301 (n=8245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9677 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.9142` → IC=+0.215 (n=2851)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9142 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.92` → IC=+0.260 (n=6062)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.92 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.160 (n=16657)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2145 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.213 (n=4420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6204` → IC=+0.192 (n=8052)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6204 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.199 (n=23348)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.208 (n=7659)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3917` → IC=+0.201 (n=20202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3917 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=8596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4854` → IC=+0.254 (n=20202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4854 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1873` → IC=+0.183 (n=14688)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1873 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.345` → IC=+0.204 (n=22434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.345 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.7006` → IC=+0.179 (n=6776)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.7006 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.255 (n=3155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.213 (n=7356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.215 (n=21854)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.274 (n=1314)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3735` → IC=+0.235 (n=3943)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3735 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8625` → IC=+0.294 (n=2630)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8625 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.822` → IC=+0.343 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.822 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.286 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4504` → IC=+0.232 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4504 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2913` → IC=+0.240 (n=1730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2913 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2037.22` → IC=+0.241 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2037.22 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.245 (n=3217)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.271 (n=2393)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1255` → IC=+0.293 (n=1578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1255 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.269 (n=3722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=3232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.4651` → IC=+0.288 (n=3155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4651 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.024` → IC=+0.270 (n=3735)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.024 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.271 (n=3270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.285 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.272 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6471` → IC=+0.275 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6471 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.276 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.175 (n=1357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.147 (n=1353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.3041` → IC=+0.203 (n=3624)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3041 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3398` → IC=+0.199 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3398 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.267` → IC=+0.169 (n=849)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.267 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6356` → IC=+0.156 (n=1353)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6356 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0674` → IC=+0.146 (n=1839)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0674 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.188 (n=568)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.272 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.145 (n=3510)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5212` → IC=+0.146 (n=3563)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5212 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.154 (n=2627)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 291.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.172 (n=3156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0059 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0826` → IC=+0.176 (n=1197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0826 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6811` → IC=+0.192 (n=3586)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6811 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1514` → IC=+0.162 (n=3535)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1514 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.2` → IC=+0.150 (n=3652)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.2 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0441` → IC=+0.155 (n=3155)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0441 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2211` → IC=+0.196 (n=653)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2211 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.437` → IC=+0.149 (n=3475)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.437 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.153 (n=2316)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=4659)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.177 (n=1134)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 213.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.234 (n=1866)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=4315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.222 (n=3675)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.973` → IC=+0.315 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.973 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2056` → IC=+0.231 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2056 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.7503` → IC=+0.237 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7503 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=4999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1902.0057` → IC=+0.231 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1902.0057 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.250 (n=3504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1834` → IC=+0.261 (n=1749)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1834 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=1814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0667` → IC=+0.301 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0667 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.962` → IC=+0.303 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.962 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3465` → IC=+0.300 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3465 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.258 (n=2562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.248 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1991.42` → IC=+0.260 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1991.42 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.249 (n=3380)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.191 (n=1427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3472` → IC=+0.147 (n=3759)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3472 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8802` → IC=+0.268 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8802 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.168 (n=2108)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.181` → IC=+0.167 (n=856)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.181 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.859` → IC=+0.153 (n=2848)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.859 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.199 (n=572)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5167` → IC=+0.157 (n=1838)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5167 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.143 (n=1893)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5828.7817` → IC=+0.235 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5828.7817 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.143 (n=2780)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.170 (n=3612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0081 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4539` → IC=+0.160 (n=3610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4539 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=1329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.7033` → IC=+0.203 (n=3610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7033 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1638` → IC=+0.164 (n=3429)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1638 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.014` → IC=+0.155 (n=3141)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.014 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8545` → IC=+0.164 (n=2407)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8545 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.206 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1948` → IC=+0.154 (n=3077)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1948 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5245` → IC=+0.159 (n=3123)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5245 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6703.3145` → IC=+0.215 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6703.3145 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.174 (n=1215)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 57.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.155 (n=1453)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0129 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=3079)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.255 (n=2899)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.0347` → IC=+0.201 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0347 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.229` → IC=+0.270 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.229 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2102` → IC=+0.125 (n=4348)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2102 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.120 (n=4139)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.131 (n=545)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.4852` → IC=+0.123 (n=4244)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4852 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2471.8484` → IC=+0.220 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2471.8484 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.160 (n=3582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0111 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.142` → IC=+0.154 (n=1357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.142 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=1923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5385` → IC=+0.247 (n=3580)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5385 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2221` → IC=+0.154 (n=3757)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2221 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.039` → IC=+0.160 (n=3947)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.039 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6385` → IC=+0.156 (n=1357)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6385 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.200 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4357` → IC=+0.165 (n=1294)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4357 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4754` → IC=+0.142 (n=1294)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4754 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2652.8351` → IC=+0.222 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2652.8351 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.152 (n=3894)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.256 (n=3981)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=4158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.241 (n=2667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.9882` → IC=+0.307 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9882 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.2` → IC=+0.250 (n=2023)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.062` → IC=+0.294 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.062 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2164` → IC=+0.236 (n=3982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2164 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.242 (n=3982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.0791` → IC=+0.252 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0791 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.5049` → IC=+0.255 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5049 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `3000.8154` → IC=+0.238 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3000.8154 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.025` → IC=+0.269 (n=1380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.025 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=3889)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1371` → IC=+0.307 (n=1820)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1371 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `1.1575` → IC=+0.245 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1575 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.2281` → IC=+0.249 (n=3985)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2281 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.022` → IC=+0.278 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.022 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7155` → IC=+0.246 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7155 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2189` → IC=+0.264 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2189 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.309 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4331` → IC=+0.248 (n=3922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4331 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2986.2027` → IC=+0.244 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2986.2027 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.231 (n=6275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.5348` → IC=+0.233 (n=7127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5348 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=7163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9296` → IC=+0.260 (n=2377)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9296 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.9422` → IC=+0.226 (n=5849)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9422 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.457` → IC=+0.232 (n=2367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.457 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7072` → IC=+0.231 (n=2227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7072 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.8819` → IC=+0.223 (n=3374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8819 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1041` → IC=+0.224 (n=6676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1041 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.232 (n=1993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.448` → IC=+0.235 (n=2338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.448 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=5125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `3736.219` → IC=+0.231 (n=4751)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3736.219 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.230 (n=1678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.5295` → IC=+0.219 (n=5018)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5295 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.218 (n=1943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=2255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.7297` → IC=+0.216 (n=5018)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7297 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.6997` → IC=+0.219 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6997 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4381` → IC=+0.205 (n=4931)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4381 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.762` → IC=+0.223 (n=4547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.762 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.255` → IC=+0.212 (n=4618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.255 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.212 (n=4627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2238` → IC=+0.211 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2238 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.213 (n=2175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.219 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.236 (n=2204)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.210)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.279 (n=831)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.302 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.295 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1414 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.275 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `0.8769` → IC=+0.288 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8769 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.339 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.278 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `12915.1097` → IC=+0.281 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12915.1097 (IC base=+0.270)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.265 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3876` → IC=+0.188 (n=1537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3876 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=577)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.194 (n=678)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1382 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.7` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.106` → IC=+0.197 (n=1346)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.106 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2377` → IC=+0.184 (n=1537)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.2377 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1521` → IC=+0.190 (n=469)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1521 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.191 (n=510)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.178 (n=693)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.1732 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `14608.6008` → IC=+0.175 (n=697)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 14608.6008 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `696.0` → IC=+0.187 (n=1492)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 696.0 (IC base=+0.174)

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
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.223 (n=1921)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4679` → IC=+0.219 (n=1921)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4679 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.472` → IC=+0.223 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.472 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.1451` → IC=+0.214 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1451 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.4066` → IC=+0.224 (n=1939)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4066 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.962` → IC=+0.222 (n=1745)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.962 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `0.8705` → IC=+0.219 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8705 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.215 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4029` → IC=+0.231 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4029 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4937` → IC=+0.213 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4937 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.240 (n=514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.511` → IC=+0.221 (n=1541)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.511 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.212 (n=577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.217 (n=1102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.0863` → IC=+0.212 (n=1541)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0863 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.6792` → IC=+0.218 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6792 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.4225` → IC=+0.206 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4225 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.34` → IC=+0.211 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.34 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2637` → IC=+0.213 (n=1541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2637 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.7218` → IC=+0.208 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7218 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.232 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.5091` → IC=+0.210 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5091 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.7757` → IC=+0.210 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7757 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2035)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `7817.0551` → IC=+0.214 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7817.0551 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.208 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.206)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.227 (n=845)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.221 (n=574)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=1191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.295 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `1.1073` → IC=+0.244 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1073 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.218` → IC=+0.248 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.218 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.246 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.216 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.230 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `2.1576` → IC=+0.222 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1576 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `4459.289` → IC=+0.245 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4459.289 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.260 (n=628)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.6874` → IC=+0.263 (n=941)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6874 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.270 (n=646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.273 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` > `0.6006` → IC=+0.252 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6006 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` < `0.3365` → IC=+0.260 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3365 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.987` → IC=+0.267 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.987 (IC base=+0.249)

- **PATRÓN** `volumen_regimen` < `0.6688` → IC=+0.266 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6688 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1033` → IC=+0.260 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1033 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.276 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `4596.2142` → IC=+0.282 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4596.2142 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.281 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.249)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.154 (n=845)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.004 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.7497` → IC=+0.188 (n=1627)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7497 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.1543` → IC=+0.148 (n=1170)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1543 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.361` → IC=+0.132 (n=528)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 10.361 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.5998` → IC=+0.157 (n=1821)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5998 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.169 (n=505)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.072)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5412` → IC=-0.120 (n=327)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5412
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=665)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.183 (n=260)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0029 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.158 (n=665)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5412 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.168 (n=347)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.066)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.128 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0036 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0653` → IC=+0.250 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0653 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.141 (n=296)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.052)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6356` → IC=-0.150 (n=181)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6356
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=545)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.156 (n=353)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0043 (IC base=+0.065)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.125 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.259 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1326` → IC=+0.164 (n=367)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1326 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.717` → IC=+0.183 (n=165)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.717 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.277 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=+0.040)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9861` → IC=+0.198 (n=289)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.9861 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.7478` → IC=+0.165 (n=204)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.7478 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.164 (n=373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.01 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.188 (n=533)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.2137` → IC=+0.148 (n=526)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2137 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `1.1218` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.1218 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.1631` → IC=+0.176 (n=137)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1631 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `1.4645` → IC=+0.139 (n=496)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4645 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.123 (n=258)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.03 (IC base=+0.095)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=304)

- **FILTRO** `dist_vwap_pct` > `0.2458` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2458
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=387)

- **FILTRO** `volumen_regimen` < `0.871` → IC=-0.306 (n=132)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.871
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=270)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.296 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=194)

- **FILTRO** `dist_vwap_pct` > `0.4497` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4497
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=333)

- **FILTRO** `sigma_ewma_delta_pct` > `9.318` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.318
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=324)

- **FILTRO** `volumen_pendiente_norm` > `0.046` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=232)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=92)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.286 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=82)

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

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.472 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=102)

- **FILTRO** `volumen_regimen` < `0.7594` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7594
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=102)

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
- **FILTRO** `hora_utc` > `5.0` → IC=-0.344 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=101)

- **FILTRO** `volumen_pendiente_norm` > `0.1194` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1194
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=87)

- **FILTRO** `sigma_ewma_delta_pct` > `4.378` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.378
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=50)

- **FILTRO** `volumen_regimen` < `0.9175` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9175
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=45)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2374` → IC=-0.152 (n=311)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2374
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=936)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.251 (n=363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.68` → IC=+0.199 (n=801)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.68 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.8341` → IC=+0.313 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8341 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.174 (n=443)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.6243` → IC=+0.195 (n=267)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6243 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.0678` → IC=+0.192 (n=601)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0678 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.208 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.162)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7305` → IC=-0.179 (n=76)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7305
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=231)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.150 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0065 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.7305` → IC=+0.135 (n=231)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7305 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.6492` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6492 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.242` → IC=+0.134 (n=430)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.242 (IC base=+0.075)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.15` → IC=-0.132 (n=153)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=299)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.140 (n=173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0045 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.182 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.007 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1065` → IC=+0.138 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1065 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.180 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.146 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.798` → IC=+0.178 (n=231)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.798 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.7852` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7852 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1055` → IC=+0.164 (n=212)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1055 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.232` → IC=+0.159 (n=268)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 9.232 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6244 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1883` → IC=+0.171 (n=86)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1883 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.1795` → IC=+0.157 (n=275)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1795 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.7165` → IC=+0.186 (n=154)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.7165 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=221)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.002)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.0526` → IC=-0.226 (n=111)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0526
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=112)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.286 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.279 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` > `0.8523` → IC=+0.305 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8523 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` > `0.7432` → IC=+0.393 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7432 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.867` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.867 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.291 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.0893` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0893 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.4822` → IC=+0.325 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4822 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.3612` → IC=+0.293 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3612 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `690.9598` → IC=+0.264 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 690.9598 (IC base=+0.260)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.337 (n=170)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.342 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.336)

- **PATRÓN** `elapsed_s` > `209.5` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.5 (IC base=+0.336)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `1.0148` → IC=+0.373 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0148 (IC base=+0.336)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.388 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `1039.0` → IC=+0.413 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1039.0 (IC base=+0.336)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3492` → IC=+0.305 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3492 (IC base=+0.294)

- **PATRÓN** `elapsed_s` > `230.5` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.5 (IC base=+0.294)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.341 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.8978` → IC=+0.325 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8978 (IC base=+0.294)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.337 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `1728.0` → IC=+0.339 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1728.0 (IC base=+0.294)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.337 (n=170)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.342 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.336)

- **PATRÓN** `elapsed_s` > `209.5` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.5 (IC base=+0.336)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `1.0148` → IC=+0.373 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0148 (IC base=+0.336)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.388 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `1039.0` → IC=+0.413 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1039.0 (IC base=+0.336)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3492` → IC=+0.305 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3492 (IC base=+0.294)

- **PATRÓN** `elapsed_s` > `230.5` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.5 (IC base=+0.294)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.341 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.8978` → IC=+0.325 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8978 (IC base=+0.294)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.337 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `1728.0` → IC=+0.339 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1728.0 (IC base=+0.294)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=286)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=231)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=286)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1312)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 2.0 (IC base=+0.092)

- **PATRÓN** `liq_usd_total` > `1042.48` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1042.48 (IC base=+0.092)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.5 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.133 (n=96)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.03 (IC base=+0.092)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9873` → IC=-0.130 (n=52)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9873
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=107)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=74)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=82)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.184 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 10.0 (IC base=+0.096)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.143 (n=82)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.5 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `1873.4616` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1873.4616 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `4.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 4.0 (IC base=+0.096)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `1211.34` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_usd_total` < 1211.34
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=46)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=274)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4183)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=220)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=177)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.295 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=204)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.150 (n=101)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=+0.213 (n=106)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.213 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.002)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.132 (n=286)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=+0.021)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.194)

- **PATRÓN** `liq_usd_total` > `3482.11` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 3482.11 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.207 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.218 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `3229.7474` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3229.7474 (IC base=+0.194)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.194)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1634)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1588)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=745)

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
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1109)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1109)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1463)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1463)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=337)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=337)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.140 (n=112)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=240)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=397)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=446)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=326)

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
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=416)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.124 (n=3277)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=8552)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.132 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=131)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

- **FILTRO** `restante_min` < `3.99` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.152 (n=383)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=958)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.149 (n=303)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=843)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.143 (n=401)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.51 (IC base=-0.008)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.124 (n=187)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=425)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.140 (n=337)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=716)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.123 (n=731)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=386)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.131 (n=592)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=684)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=8918)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=27826)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.169 (n=9303)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=28775)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.200 (n=1662)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5185)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.143 (n=2279)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=4474)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1755)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=3171)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.016)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.176 (n=1247)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=3785)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.176 (n=1310)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4020)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.195 (n=1697)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5232)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2102)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.031)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7659` → IC=-0.152 (n=1230)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7659
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3691)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.162 (n=1710)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5160)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3237)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4189)

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
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1171)

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
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=371)

- **FILTRO** `drift_20min_pct` |x|> `0.2017` → IC=-0.131 (n=120)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2017
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=364)

- **FILTRO** `libro_liquidez` < `3247.9585` → IC=-0.183 (n=159)

  - _Acción_: SKIP cuando `libro_liquidez` < 3247.9585
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=325)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `ibs_20min` > `0.875` → IC=-0.131 (n=602)

  - _Acción_: SKIP cuando `ibs_20min` > 0.875
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=614)

- **FILTRO** `libro_liquidez` < `1610.1196` → IC=-0.147 (n=304)

  - _Acción_: SKIP cuando `libro_liquidez` < 1610.1196
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=912)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=24953)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=56481)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=19878)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=61556)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.224 (n=26787)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=54647)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.155 (n=27346)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=54088)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.246 (n=25280)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=76623)

- **FILTRO** `ibs_7min` > `0.2791` → IC=-0.183 (n=25459)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2791
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=76444)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=3500)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=11166)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.320 (n=3662)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=11004)

- **FILTRO** `ibs_7min` < `0.7077` → IC=-0.255 (n=4838)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7077
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=9828)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4269)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=13370)

- **FILTRO** `ibs_7min` > `0.7655` → IC=-0.211 (n=4409)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7655
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=13230)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.125 (n=3252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=10204)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=3298)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10158)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.214 (n=3362)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10094)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.205 (n=3356)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=10100)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=3128)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10634)

- **FILTRO** `ibs_7min` > `0.2646` → IC=-0.193 (n=3439)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2646
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10323)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.178 (n=3436)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10326)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10696)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.329 (n=3376)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=10684)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.254 (n=4621)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=9439)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.173 (n=3409)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=10651)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=4486)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=14175)

- **FILTRO** `ibs_7min` > `0.7238` → IC=-0.185 (n=4665)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7238
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=13996)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=2975)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=10146)

- **FILTRO** `ibs_7min` < `0.7121` → IC=-0.202 (n=3279)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7121
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9842)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.195 (n=3269)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=9852)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=3177)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=10470)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.180 (n=3409)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10238)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.168 (n=3388)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=10259)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=3163)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=9811)

- **FILTRO** `ibs_7min` < `0.2955` → IC=-0.234 (n=4280)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2955
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=8694)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3192)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9782)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4676)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=15064)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=4262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=8895)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=3237)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9920)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.231 (n=4327)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8830)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.196 (n=3286)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=9871)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.231 (n=4522)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=13932)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1025)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1314)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.167 (n=181)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=651)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=923)

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
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=541)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.146 (n=746)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=1482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `443.866` → IC=+0.165 (n=547)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 443.866 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3650.3048` → IC=+0.135 (n=743)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3650.3048 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.186 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 14.0 (IC base=+0.140)

- **PATRÓN** `total_vol_5m` < `498.39` → IC=+0.159 (n=379)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 498.39 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.158 (n=261)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 9.0 (IC base=+0.140)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.129 (n=343)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.135 (n=302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.168 (n=203)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `697.8088` → IC=+0.163 (n=268)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 697.8088 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 59.0 (IC base=+0.125)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4183` → IC=+0.195 (n=185)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio` |x|> 0.4183 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.173 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `4680.799` → IC=+0.175 (n=186)

  - _Acción_: Kelly boost +0.88€ cuando `total_vol_5m` < 4680.799 (IC base=+0.134)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.134 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 13.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=210)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **FILTRO** `pct_vs_K` |x|> `3.395` → IC=-0.143 (n=326)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.395
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=639)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.155 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0046 (IC base=-0.028)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2538` → IC=-0.233 (n=73)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2538
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=221)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.270 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.000)

- **PATRÓN** `pct_vs_K` |x|≤ `1.8519` → IC=+0.210 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.8519 (IC base=+0.000)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `6.4329` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.4329
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `96.8103` → IC=-0.160 (n=92)

  - _Acción_: SKIP cuando `T_h` < 96.8103
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=93)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `87.9918` → IC=-0.251 (n=420)

  - _Acción_: SKIP cuando `T_h` < 87.9918
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=424)

- **FILTRO** `sigma_h` < `0.0056` → IC=-0.190 (n=195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=585)

- **FILTRO** `T_h` > `142.427` → IC=-0.163 (n=194)

  - _Acción_: SKIP cuando `T_h` > 142.427
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=586)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `49.2217` → IC=-0.232 (n=207)

  - _Acción_: SKIP cuando `T_h` > 49.2217
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=70)

- **FILTRO** `sigma_h` < `0.0075` → IC=-0.177 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0075
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=99)

- **FILTRO** `T_h` > `143.1485` → IC=-0.176 (n=72)

  - _Acción_: SKIP cuando `T_h` > 143.1485
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=217)

- **FILTRO** `T_h` < `90.2078` → IC=-0.170 (n=95)

  - _Acción_: SKIP cuando `T_h` < 90.2078
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=194)

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
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.323 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=123)

- **FILTRO** `T_h` < `68.901` → IC=-0.305 (n=80)

  - _Acción_: SKIP cuando `T_h` < 68.901
  - _Potencial_: sin este filtro IC_bueno=-0.290 (n=165)

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.172 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=178)

- **FILTRO** `pct_vs_K` |x|> `2.7213` → IC=-0.389 (n=79)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7213
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=158)

- **PATRÓN** `pct_vs_K` |x|≤ `1.89` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `pct_vs_K` |x|≤ 1.89 (IC base=-0.107)

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
- **FILTRO** `sigma_h` > `0.0147` → IC=-0.217 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0147
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=178)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.247 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=159)

- **FILTRO** `T_h` > `127.8336` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `T_h` > 127.8336
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=178)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.303 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=116)

- **FILTRO** `sigma_h` < `0.0088` → IC=-0.278 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=132)

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

- **PATRÓN** `edge` > `0.1` → IC=+0.427 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.392)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.412 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.3751` → IC=+0.441 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3751 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=340)
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

- **PATRÓN** `T_h` < `0.659` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.659 (IC base=+0.194)

- **PATRÓN** `T_h` > `1.4441` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4441 (IC base=+0.194)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.234 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.194)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.411)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.424 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.411)

- **PATRÓN** `T_h` < `1.2028` → IC=+0.439 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2028 (IC base=+0.411)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.483 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.411)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=473)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=509)

- **PATRÓN** `streak_estiramiento` < `0.2936` → IC=+0.136 (n=119)

  - _Acción_: Kelly boost +0.68€ cuando `streak_estiramiento` < 0.2936 (IC base=+0.016)

- **PATRÓN** `streak_estiramiento` < `0.836` → IC=+0.121 (n=352)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.836 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.120 (n=264)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 29.0 (IC base=+0.058)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 106.0 (IC base=+0.083)

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
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=214)

- **PATRÓN** `streak_estiramiento` < `0.2108` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `streak_estiramiento` < 0.2108 (IC base=+0.031)

- **PATRÓN** `streak_estiramiento` < `0.5927` → IC=+0.155 (n=175)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.5927 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.149 (n=166)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 30.0 (IC base=+0.083)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=95)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=116)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=40)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1094)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1311)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5360)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3171)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.187 (n=2067)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0057 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2298` → IC=+0.158 (n=6194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2298 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1031` → IC=+0.134 (n=6193)

  - _Acción_: Kelly boost +0.67€ cuando `drift_15min` |x|≤ 1.1031 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.065` → IC=+0.132 (n=6193)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.065 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0999` → IC=+0.144 (n=1945)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0999 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=5726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.210 (n=5541)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.166` → IC=+0.230 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.166 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3340)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4397.201` → IC=+0.172 (n=2064)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4397.201 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=2410)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.250 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.247 (n=377)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2684` → IC=+0.226 (n=286)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2684 (IC base=+0.204)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2264` → IC=+0.216 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2264 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.231 (n=792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `ibs_15` > `0.7058` → IC=+0.274 (n=857)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7058 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.3858` → IC=+0.220 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3858 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.5415` → IC=+0.207 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5415 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.192` → IC=+0.301 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.192 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.223 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.204)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.165 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0047 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.146 (n=729)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1369` → IC=+0.137 (n=728)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.1369 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.142 (n=775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.4862` → IC=+0.218 (n=1092)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4862 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1236` → IC=+0.141 (n=684)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1236 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.6408` → IC=+0.133 (n=1242)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6408 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.055` → IC=+0.287 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.055 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6114.254` → IC=+0.169 (n=496)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 6114.254 (IC base=+0.130)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8462` → IC=+0.145 (n=624)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` > 0.8462 (IC base=+0.045)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0139` → IC=+0.145 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0139 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.143 (n=1569)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0119 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2366` → IC=+0.176 (n=1571)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2366 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.142 (n=1570)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0933` → IC=+0.190 (n=492)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0933 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=1437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.141 (n=1450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.5283` → IC=+0.206 (n=1402)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5283 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.2083` → IC=+0.153 (n=715)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2083 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.8775` → IC=+0.143 (n=1820)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.8775 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.44` → IC=+0.181 (n=358)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 17.44 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2948.5018` → IC=+0.186 (n=712)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2948.5018 (IC base=+0.139)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1089` → IC=+0.363 (n=525)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1089 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.378 (n=524)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1069` → IC=+0.377 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1069 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.371 (n=726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.396 (n=786)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1548` → IC=+0.377 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1548 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.787` → IC=+0.398 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.787 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9596.597` → IC=+0.383 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9596.597 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.414 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.367 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.378 (n=170)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.401 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.383 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.8078` → IC=+0.386 (n=376)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8078 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.396 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.392 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `8216.2794` → IC=+0.386 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8216.2794 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.404 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.364 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.362 (n=274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.375 (n=367)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.370 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.379 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.398 (n=411)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.1241` → IC=+0.365 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1241 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` < `0.6628` → IC=+0.364 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6628 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.397 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `4286.0807` → IC=+0.367 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4286.0807 (IC base=+0.362)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2563)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3317)

- **FILTRO** `libro_liquidez` < `4378.065` → IC=-0.171 (n=3880)

  - _Acción_: SKIP cuando `libro_liquidez` < 4378.065
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=2000)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.213 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.088)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.277 (n=1304)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` > `0.115` → IC=+0.202 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.115 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` < `0.5827` → IC=+0.199 (n=1383)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.5827 (IC base=-0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2298` → IC=+0.272 (n=1884)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2298 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.285 (n=5668)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.6812` → IC=+0.270 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6812 (IC base=+0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0733` → IC=-0.244 (n=1911)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0733
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=1912)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.216 (n=955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=2868)

- **FILTRO** `sigma_ewma_delta_pct` > `22.161` → IC=-0.248 (n=542)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.161
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=3281)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.144 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0032 (IC base=+0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2678` → IC=+0.277 (n=155)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2678 (IC base=+0.065)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.145` → IC=+0.276 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.145 (IC base=+0.065)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.318 (n=464)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.279 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.5257` → IC=+0.283 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5257 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.006` → IC=+0.137 (n=235)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 22.006 (IC base=+0.065)

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
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=855)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.158 (n=655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0066 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.161 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.191 (n=516)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.167 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5671` → IC=+0.242 (n=654)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5671 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.150 (n=409)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.149 (n=502)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.266 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=855)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5128.1918` → IC=+0.162 (n=436)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5128.1918 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.259 (n=974)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.468` → IC=+0.245 (n=2211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.468 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.8107` → IC=+0.256 (n=1946)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8107 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2039` → IC=+0.261 (n=1002)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2039 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.243 (n=1512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3871` → IC=+0.274 (n=2211)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3871 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.161` → IC=+0.258 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.161 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.498` → IC=+0.244 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.498 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.199` → IC=-0.293 (n=351)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.199
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=1054)

- **FILTRO** `drift_15min` |x|> `0.987` → IC=-0.299 (n=351)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.987
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1054)

- **FILTRO** `sigma_ewma_delta_pct` > `6.094` → IC=-0.207 (n=309)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.094
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=1096)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.204)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.204)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.204)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0623` → IC=+0.241 (n=953)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0623 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.296 (n=953)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` < `0.4621` → IC=+0.253 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4621 (IC base=-0.025)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.244 (n=1245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=416)

- **FILTRO** `drift_60min` |x|> `0.1571` → IC=-0.252 (n=414)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1571
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=1247)

- **FILTRO** `drift_15min` |x|> `1.2992` → IC=-0.279 (n=415)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2992
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1246)

- **FILTRO** `sigma_ewma_delta_pct` > `7.379` → IC=-0.226 (n=506)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.379
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=1155)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=1640)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.222)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0717` → IC=+0.283 (n=1186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0717 (IC base=-0.009)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.292 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.009)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=1335)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.7684` → IC=+0.331 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7684 (IC base=-0.009)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.154 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0063 (IC base=+0.080)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.080)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.293 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.080)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.154 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0063 (IC base=+0.080)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.080)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.293 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.080)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.298 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.292 (n=484)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.311 (n=485)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1514` → IC=+0.285 (n=967)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1514 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2201` → IC=+0.290 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2201 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.298 (n=1317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8368` → IC=+0.310 (n=1452)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8368 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.313 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.707` → IC=+0.386 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.707 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.283 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `13084.0601` → IC=+0.298 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13084.0601 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.305 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.302 (n=337)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `0.3865` → IC=+0.278 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3865 (IC base=+0.278)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2704` → IC=+0.282 (n=255)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2704 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2292` → IC=+0.286 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2292 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.302 (n=705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.8572` → IC=+0.309 (n=683)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8572 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.312 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.5603` → IC=+0.278 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5603 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.43` → IC=+0.394 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.43 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.279 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `15655.8789` → IC=+0.313 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15655.8789 (IC base=+0.278)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.291 (n=688)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0071 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0501` → IC=+0.319 (n=230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0501 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.294 (n=688)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.311 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.297 (n=662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.289 (n=487)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8448` → IC=+0.313 (n=687)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8448 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2911` → IC=+0.309 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2911 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` < `0.6633` → IC=+0.288 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6633 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.379 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1091` → IC=-0.158 (n=232)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1091
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=115)

- **FILTRO** `ballena_activa_n` > `46.0` → IC=-0.143 (n=239)

  - _Acción_: SKIP cuando `ballena_activa_n` > 46.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=118)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.172 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=380)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.220 (n=80)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=165)

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

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.008` → IC=-0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=29)

- **FILTRO** `drift_60min` |x|> `0.2902` → IC=-0.262 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2902
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=39)

- **FILTRO** `sigma_h` < `0.006` → IC=-0.219 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=31)

- **FILTRO** `drift_15min` |x|> `0.5336` → IC=-0.227 (n=20)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5336
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=41)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9868` → IC=+0.261 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9868 (IC base=+0.129)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.357 (n=3175)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0178` → IC=+0.389 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0178 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9765` → IC=+0.200 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9765 (IC base=+0.073)

- **PATRÓN** `T_h` > `109.9778` → IC=+0.327 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.9778 (IC base=+0.309)

- **PATRÓN** `ratio` > `1.0153` → IC=+0.380 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0153 (IC base=+0.309)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9804` → IC=+0.366 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9804 (IC base=+0.188)

- **PATRÓN** `T_h` > `111.9952` → IC=+0.354 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9952 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0245` → IC=+0.402 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0245 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0398` → IC=+0.416 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0398 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de +0.132 a +0.210 en UPDOWN_GBM#15min (n=5541). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7058 sube el IC de +0.204 a +0.274 en UPDOWN_GBM#BTC#15min (n=857). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4862 sube el IC de +0.130 a +0.218 en UPDOWN_GBM#ETH#15min (n=1092). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5283 sube el IC de +0.139 a +0.206 en UPDOWN_GBM#XRP#15min (n=1402). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.088 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=1304). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.001 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=5668). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.065 a +0.318 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=464). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.183 a +0.287 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5671 sube el IC de +0.146 a +0.242 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=654). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3871 sube el IC de +0.241 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2211). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.204 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.025 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=953). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.222 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.009 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1335). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.080 a +0.293 en UPDOWN_GBM_ETH_15M_HORA7 (n=27). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.080 a +0.293 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=27). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8368 sube el IC de +0.283 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1452). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8572 sube el IC de +0.278 a +0.309 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=683). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8448 sube el IC de +0.289 a +0.313 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=687). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.364 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=786). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8078 sube el IC de +0.365 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=376). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.362 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=411). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2274 | +0.082 | +223.13€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2274 | +0.082 | +223.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1862 | +0.082 | +183.64€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1862 | +0.082 | +183.64€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1336 | -0.023 | +72.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1336 | -0.023 | +72.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1033 | -0.037 | +60.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1033 | -0.037 | +60.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 206 | +0.048 | +18.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 206 | +0.048 | +18.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 90 | -0.033 | -9.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 90 | -0.033 | -9.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 50345 | -0.086 | -6367.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3250 | +0.089 | -315.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 47095 | -0.098 | -6052.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5051 | -0.115 | -803.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5051 | -0.115 | -803.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3250 | +0.089 | -315.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3250 | +0.089 | -315.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5057 | -0.108 | -953.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5057 | -0.108 | -953.91€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13827 | -0.044 | -1300.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13827 | -0.044 | -1300.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13823 | -0.116 | -1449.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13823 | -0.116 | -1449.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9337 | -0.138 | -1543.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9337 | -0.138 | -1543.71€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 54424 | -0.012 | +2784.32€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14018 | +0.004 | +1480.23€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 40406 | -0.017 | +1304.09€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 54424 | -0.012 | +2784.32€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14018 | +0.004 | +1480.23€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 40406 | -0.017 | +1304.09€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 204446 | +0.113 | -8326.62€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22805 | +0.179 | -737.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 953 | +0.016 | -75.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 169087 | +0.105 | -7090.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11601 | +0.094 | -422.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 28019 | +0.102 | -1995.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 83 | -0.182 | +13.02€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 27919 | +0.103 | -1999.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 38410 | +0.124 | -606.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5665 | +0.177 | -231.57€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 27986 | +0.120 | -187.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4717 | +0.082 | -166.00€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 28067 | +0.099 | -1983.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 95 | -0.119 | +13.37€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 27957 | +0.100 | -1985.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 43719 | +0.124 | -890.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10897 | +0.178 | -297.48€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 28440 | +0.106 | -513.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4370 | +0.103 | -70.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 38180 | +0.111 | -1659.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5968 | +0.199 | -246.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 856 | +0.041 | -21.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 28847 | +0.095 | -1199.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2509 | +0.104 | -191.45€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 28051 | +0.107 | -1190.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 97 | -0.136 | +11.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 27938 | +0.108 | -1204.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 33265 | +0.189 | -2486.80€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 33265 | +0.189 | -2486.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7539 | +0.162 | -872.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7539 | +0.162 | -872.41€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4942 | +0.194 | -205.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4942 | +0.194 | -205.92€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7367 | +0.172 | -686.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7367 | +0.172 | -686.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6109 | +0.251 | -219.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6109 | +0.251 | -219.96€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7229 | +0.183 | -515.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7229 | +0.183 | -515.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1305 | +0.423 | -53.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1305 | +0.423 | -53.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 549 | +0.436 | -8.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 549 | +0.436 | -8.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 214 | +0.398 | -18.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 214 | +0.398 | -18.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 117494 | +0.200 | -8563.50€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 117494 | +0.200 | -8563.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 20363 | +0.176 | -2377.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 20363 | +0.176 | -2377.28€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 18936 | +0.223 | -635.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 18936 | +0.223 | -635.35€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 20160 | +0.181 | -2103.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 20160 | +0.181 | -2103.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19101 | +0.217 | -758.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19101 | +0.217 | -758.27€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 19396 | +0.205 | -1162.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 19396 | +0.205 | -1162.93€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 19538 | +0.197 | -1526.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 19538 | +0.197 | -1526.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 45647 | +0.116 | +349.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 45647 | +0.116 | +349.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 22731 | +0.117 | +211.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 22731 | +0.117 | +211.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 22916 | +0.116 | +137.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 22916 | +0.116 | +137.82€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 606 | +0.441 | +0.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2018 | +0.065 | -99.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1293 | +0.075 | -35.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1584 | +0.071 | -54.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1293 | +0.075 | -35.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 93015 | +0.101 | -2011.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7533 | +0.097 | +180.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 85482 | +0.101 | -2191.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 50793 | +0.105 | -450.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7533 | +0.097 | +180.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 43260 | +0.107 | -630.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 19939 | +0.110 | -48.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 19939 | +0.110 | -48.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 22283 | +0.082 | -1512.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 22283 | +0.082 | -1512.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 63311 | +0.102 | +35599.55€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 63311 | +0.102 | +35599.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10503 | +0.225 | +9025.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10503 | +0.225 | +9025.76€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 9858 | +0.177 | +7900.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9858 | +0.177 | +7900.05€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 11345 | +0.206 | +8913.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11345 | +0.206 | +8913.69€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8373 | +0.061 | +2830.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8373 | +0.061 | +2830.41€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8789 | -0.025 | +2300.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8789 | -0.025 | +2300.23€ | 4 | 16 |
| ✅ GBM_LATE_15M#XRP | 14443 | -0.020 | +4629.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 14443 | -0.020 | +4629.41€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 67232 | +0.087 | +39252.28€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 67232 | +0.087 | +39252.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13035 | -0.002 | +6846.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13035 | -0.002 | +6846.35€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 14447 | +0.007 | +3996.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 14447 | +0.007 | +3996.87€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9062 | +0.295 | +10362.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9062 | +0.295 | +10362.53€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12820 | +0.017 | +4091.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12820 | +0.017 | +4091.29€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10272 | +0.049 | +4736.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10272 | +0.049 | +4736.02€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7596 | +0.313 | +9219.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7596 | +0.313 | +9219.21€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 49858 | +0.179 | +41370.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 49858 | +0.179 | +41370.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7529 | +0.239 | +7001.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7529 | +0.239 | +7001.70€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7917 | +0.141 | +5943.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7917 | +0.141 | +5943.06€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8034 | +0.223 | +6935.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8034 | +0.223 | +6935.77€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8536 | +0.130 | +6667.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8536 | +0.130 | +6667.15€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9412 | +0.122 | +7238.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9412 | +0.122 | +7238.35€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8430 | +0.232 | +7584.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8430 | +0.232 | +7584.69€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 13753 | +0.127 | +7031.64€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 13753 | +0.127 | +7031.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3563 | +0.126 | +1959.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3563 | +0.126 | +1959.65€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4030 | +0.129 | +2045.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4030 | +0.129 | +2045.80€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3714 | +0.101 | +1505.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3714 | +0.101 | +1505.19€ | 0 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1260 | +0.167 | +786.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1260 | +0.167 | +786.94€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 63558 | +0.189 | +52838.39€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 63558 | +0.189 | +52838.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10036 | +0.250 | +9689.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10036 | +0.250 | +9689.83€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10188 | +0.142 | +7347.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10188 | +0.142 | +7347.57€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10786 | +0.234 | +9695.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10786 | +0.234 | +9695.38€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10507 | +0.145 | +7905.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10507 | +0.145 | +7905.13€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11220 | +0.128 | +8191.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11220 | +0.128 | +8191.82€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10821 | +0.240 | +10008.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10821 | +0.240 | +10008.66€ | 0 | 22 |
| ✅ GBM_LATE_5M | 16191 | +0.218 | +13607.92€ | 0 | 27 |
| ✅ GBM_LATE_5M#5min | 16191 | +0.218 | +13607.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1833 | +0.250 | +1766.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1833 | +0.250 | +1766.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3307 | +0.210 | +2848.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3307 | +0.210 | +2848.43€ | 0 | 23 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 4615 | +0.210 | +3613.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4615 | +0.210 | +3613.89€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 2942 | +0.229 | +2608.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2942 | +0.229 | +2608.61€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 2041 | +0.210 | +1610.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2041 | +0.210 | +1610.49€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5905 | +0.065 | +1720.37€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 5905 | +0.065 | +1720.37€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 59 | +0.254 | +51.23€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 59 | +0.254 | +51.23€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1967 | +0.060 | +571.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1967 | +0.060 | +571.81€ | 1 | 6 |
| ✅ GBM_LATE_60M#DOGE | 59 | +0.320 | +67.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 59 | +0.320 | +67.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1823 | +0.055 | +577.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1823 | +0.055 | +577.39€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1937 | +0.058 | +400.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1937 | +0.058 | +400.12€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 60 | +0.274 | +52.63€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 60 | +0.274 | +52.63€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE | 756 | -0.251 | -41.68€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 756 | -0.251 | -41.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 269 | -0.257 | -22.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 269 | -0.257 | -22.31€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 273 | -0.245 | -9.62€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 273 | -0.245 | -9.62€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 210 | -0.245 | -9.40€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 210 | -0.245 | -9.40€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2313 | +0.087 | +583.22€ | 1 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2313 | +0.087 | +583.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 879 | +0.069 | +198.81€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 879 | +0.069 | +198.81€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 796 | +0.060 | +154.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 796 | +0.060 | +154.70€ | 1 | 15 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 638 | +0.147 | +229.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 638 | +0.147 | +229.71€ | 1 | 10 |
| ✅ LATE_WINDOW_5MIN | 362 | +0.316 | +436.70€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 362 | +0.316 | +436.70€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 362 | +0.316 | +436.70€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 362 | +0.316 | +436.70€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4710 | +0.096 | +1037.00€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4710 | +0.096 | +1037.00€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4710 | +0.096 | +1037.00€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4710 | +0.096 | +1037.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1635 | +0.020 | +96.93€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1635 | +0.020 | +96.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 183 | +0.089 | +36.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 183 | +0.089 | +36.96€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 329 | -0.014 | +6.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 329 | -0.014 | +6.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 107 | +0.051 | +20.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 107 | +0.051 | +20.85€ | 2 | 4 |
| ✅ LIQUIDACIONES_15M#ETH | 377 | +0.030 | +23.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 377 | +0.030 | +23.64€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 348 | -0.014 | +2.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 348 | -0.014 | +2.78€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 291 | +0.029 | +5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 291 | +0.029 | +5.75€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4509 | +0.016 | +172.16€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4509 | +0.016 | +172.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 240 | +0.004 | -5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 240 | +0.004 | -5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 858 | +0.014 | +45.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 858 | +0.014 | +45.19€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 319 | +0.061 | +74.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 319 | +0.061 | +74.83€ | 0 | 7 |
| ✅ LIQUIDACIONES_5M#ETH | 1686 | +0.019 | +30.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1686 | +0.019 | +30.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 786 | +0.013 | +4.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 786 | +0.013 | +4.00€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 620 | -0.006 | +23.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 620 | -0.006 | +23.43€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2667 | -0.034 | -6.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2667 | -0.034 | -6.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 813 | -0.036 | -15.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 813 | -0.036 | -15.95€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 958 | -0.011 | +21.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 958 | -0.011 | +21.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 892 | -0.054 | -9.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 892 | -0.054 | -9.89€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 19456 | -0.030 | -110.41€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 9407 | -0.033 | -119.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 10049 | -0.028 | +8.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 679 | -0.054 | -38.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 345 | -0.036 | -6.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 334 | -0.071 | -32.32€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5185 | -0.026 | -18.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2468 | -0.024 | -1.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2717 | -0.028 | -16.63€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1799 | -0.031 | +5.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 917 | -0.042 | -21.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 882 | -0.020 | +27.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4440 | -0.031 | -43.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2139 | -0.030 | -15.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2301 | -0.032 | -27.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3732 | -0.022 | +66.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1815 | -0.031 | -7.63€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1917 | -0.013 | +74.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3621 | -0.041 | -81.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1723 | -0.048 | -66.31€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1898 | -0.034 | -15.68€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 74822 | +0.000 | +4129.91€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 74822 | +0.000 | +4129.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13600 | +0.028 | +1907.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13600 | +0.028 | +1907.66€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10362 | -0.038 | -154.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10362 | -0.038 | -154.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 13757 | +0.025 | +1563.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 13757 | +0.025 | +1563.95€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10360 | -0.053 | -256.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10360 | -0.053 | -256.40€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12761 | -0.004 | +382.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12761 | -0.004 | +382.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13982 | +0.019 | +687.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13982 | +0.019 | +687.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7359 | -0.053 | -110.77€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7359 | -0.053 | -110.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2079 | -0.059 | -19.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2079 | -0.059 | -19.80€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 100 | -0.020 | -0.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 100 | -0.020 | -0.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 818 | -0.116 | -32.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 818 | -0.116 | -32.47€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2223 | -0.068 | -15.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2223 | -0.068 | -15.51€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 870 | -0.019 | -28.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 870 | -0.019 | -28.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3384 | +0.003 | -0.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3384 | +0.003 | -0.47€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_5M#XRP | 196 | -0.015 | -1.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 196 | -0.015 | -1.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 183337 | -0.077 | +2322.81€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 183337 | -0.077 | +2322.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 32305 | -0.076 | +1923.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 32305 | -0.076 | +1923.60€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 27218 | -0.102 | -1383.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 27218 | -0.102 | -1383.60€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 32721 | -0.068 | +1609.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 32721 | -0.068 | +1609.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 26768 | -0.100 | -931.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 26768 | -0.100 | -931.82€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 32714 | -0.059 | +276.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 32714 | -0.059 | +276.84€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 31611 | -0.069 | +827.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 31611 | -0.069 | +827.81€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9263 | -0.035 | -183.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9263 | -0.035 | -183.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1009 | -0.017 | -19.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1009 | -0.017 | -19.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2161 | -0.046 | -27.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2161 | -0.046 | -27.55€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2674 | -0.024 | -33.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2674 | -0.024 | -33.11€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1297 | -0.064 | -32.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1297 | -0.064 | -32.97€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1113 | -0.035 | -38.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1113 | -0.035 | -38.54€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2321 | +0.120 | +928.27€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2185 | +0.124 | +915.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 504 | +0.140 | +258.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 504 | +0.140 | +258.61€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 457 | +0.117 | +160.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 457 | +0.117 | +160.11€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 406 | +0.125 | +181.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 406 | +0.125 | +181.97€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 370 | +0.134 | +180.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 370 | +0.134 | +180.52€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 448 | +0.100 | +134.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 448 | +0.100 | +134.47€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2452 | -0.022 | -43.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2452 | -0.022 | -43.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 439 | +0.008 | +21.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 439 | +0.008 | +21.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 451 | -0.050 | -32.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 451 | -0.050 | -32.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 599 | -0.046 | -42.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 599 | -0.046 | -42.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 508 | -0.002 | +1.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 508 | -0.002 | +1.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 455 | -0.014 | +8.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 455 | -0.014 | +8.06€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1278 | -0.043 | +129.38€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 590 | -0.069 | +23.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 461 | -0.066 | +46.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 449 | -0.014 | +68.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 328 | +0.006 | +76.97€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 239 | -0.031 | +38.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 203 | -0.022 | +36.21€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 992 | -0.033 | +160.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1624 | -0.184 | -34.87€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 637 | -0.173 | -10.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 566 | -0.169 | -6.57€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 71 | -0.199 | -3.91€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 545 | -0.197 | -31.84€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 482 | -0.204 | -38.47€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 63 | -0.131 | +6.63€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 442 | -0.185 | +7.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 411 | -0.180 | +5.81€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 31 | -0.227 | +1.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1459 | -0.184 | -39.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 165 | -0.183 | +4.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 576 | +0.377 | +523.21€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#BTC | 128 | +0.169 | +97.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 128 | +0.169 | +97.55€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#ETH | 131 | +0.372 | +107.98€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 131 | +0.372 | +107.98€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 317 | +0.459 | +317.69€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 317 | +0.459 | +317.69€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 576 | +0.377 | +523.21€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1020 | +0.038 | +79.86€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1020 | +0.038 | +79.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 78 | +0.025 | +2.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 78 | +0.025 | +2.06€ | 1 | 2 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 498 | +0.058 | +67.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 498 | +0.058 | +67.85€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3629 | -0.023 | -142.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3629 | -0.023 | -142.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 624 | -0.029 | -27.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 624 | -0.029 | -27.52€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 175 | -0.042 | -14.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 175 | -0.042 | -14.78€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1703 | -0.018 | -59.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1703 | -0.018 | -59.57€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 131 | -0.026 | -10.42€ | 3 | 1 |
| ✅ STREAK_FADE_60M#60min | 131 | -0.026 | -10.42€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 46 | -0.062 | -3.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 46 | -0.062 | -3.71€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 81 | -0.006 | -6.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 81 | -0.006 | -6.44€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11621 | +0.013 | +67.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11621 | +0.013 | +67.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3003 | +0.018 | +23.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3003 | +0.018 | +23.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3084 | +0.014 | +27.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3084 | +0.014 | +27.83€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2937 | +0.008 | -4.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2937 | +0.008 | -4.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2597 | +0.014 | +20.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2597 | +0.014 | +20.41€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13255 | +0.019 | +11.53€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13255 | +0.019 | +11.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5379 | +0.020 | +2.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5379 | +0.020 | +2.14€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4671 | +0.020 | +6.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4671 | +0.020 | +6.74€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3205 | +0.016 | +2.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3205 | +0.016 | +2.66€ | 1 | 0 |
| ✅ UPDOWN_GBM | 120739 | +0.060 | +11484.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 29784 | +0.078 | +5853.36€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3449 | -0.000 | +43.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 79937 | +0.062 | +5463.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7162 | -0.002 | +129.88€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10614 | +0.103 | +1939.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1948 | +0.167 | +921.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8576 | +0.090 | +1020.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 27243 | +0.057 | +2416.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3984 | +0.081 | +898.17€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1006 | -0.001 | +21.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 18897 | +0.066 | +1412.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3209 | -0.005 | +78.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 147 | -0.064 | +5.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 13460 | +0.075 | +1470.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1935 | +0.155 | +818.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11439 | +0.061 | +652.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 28258 | +0.050 | +2020.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6950 | +0.071 | +1078.81€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 973 | +0.006 | +15.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 17545 | +0.052 | +879.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2654 | +0.000 | +43.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 136 | -0.101 | +2.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 25156 | +0.040 | +1419.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8069 | +0.033 | +467.27€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 897 | -0.009 | +10.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14769 | +0.052 | +945.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1299 | +0.004 | +8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 122 | -0.145 | -10.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16006 | +0.073 | +2219.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6898 | +0.089 | +1668.92€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8711 | +0.063 | +552.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 405 | -0.102 | -3.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1048 | +0.364 | +389.59€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1048 | +0.364 | +389.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 501 | +0.365 | +178.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 501 | +0.365 | +178.38€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 547 | +0.362 | +211.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 547 | +0.362 | +211.21€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 28421 | -0.017 | +7188.60€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 28421 | -0.017 | +7188.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2180 | -0.047 | +602.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2180 | -0.047 | +602.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5242 | -0.116 | +291.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5242 | -0.116 | +291.08€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1192 | +0.224 | +1007.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1192 | +0.224 | +1007.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3819 | +0.220 | +2453.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3819 | +0.220 | +2453.22€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8046 | -0.056 | +1229.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8046 | -0.056 | +1229.35€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7942 | -0.054 | +1605.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7942 | -0.054 | +1605.59€ | 5 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 354 | +0.056 | +29.35€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 354 | +0.056 | +29.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 354 | +0.056 | +29.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 354 | +0.056 | +29.35€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1935 | +0.283 | +1647.14€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1935 | +0.283 | +1647.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1019 | +0.278 | +820.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1019 | +0.278 | +820.77€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 916 | +0.289 | +826.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 916 | +0.289 | +826.37€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 895 | -0.119 | -93.93€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 895 | -0.119 | -93.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 289 | -0.084 | -22.53€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 289 | -0.084 | -22.53€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 104 | -0.198 | -15.53€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 104 | -0.198 | -15.53€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 119 | -0.186 | -6.52€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 119 | -0.186 | -6.52€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5190 | +0.295 | +2283.78€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2007 | +0.252 | +271.76€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2012 | +0.288 | +854.54€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1171 | +0.382 | +1157.48€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.026 n=1474 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1474 IC=+0.026 PNL=+73.86€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 847 celda(s) pasan gate riguroso completo de 3030 evaluadas (n>=40) y 4146 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=8064 IC=+0.033 PNL=+466.06€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=2012/15 IC=+0.288 PNL=+854.54€ | BTC: n=2007/15 IC=+0.252 PNL=+271.76€ | SOL: n=1171/15 IC=+0.382 PNL=+1157.48€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.137 n=1132/60 | contraria IC=+0.185 n=1188 | gap=-0.048 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=635, boost estimado=+0.008. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2652/40 IC=+0.000 PNL=+43.88€ | BTC#60min: n=3207/40 IC=-0.005 PNL=+78.26€ | SOL#60min: n=1299/40 IC=+0.004 PNL=+8.03€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=806274 | tras_1loss IC=+0.102 n=610303 | tras_2loss IC=+0.073 n=242722/40 | gap=-0.029 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.153 > 0.08 con n=1213 PNL=+697.47€
  - _Datos_: n=1213 IC=+0.153 PNL=+697.47€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=1450 PNL=+634.70€
  - _Datos_: n=1450 IC=+0.122 PNL=+634.70€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=4234 PNL=+2406.75€
  - _Datos_: n=4234 IC=+0.335 PNL=+2406.75€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1214 IC=+0.063 PNL=+121.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1214 IC=+0.063 PNL=+121.29€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=115 IC=+0.167 PNL=+70.09€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=115 IC=+0.167 PNL=+70.09€

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
  - _Estado_: n=4696 IC=-0.005 PNL=-45.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4696 IC=-0.005 PNL=-45.77€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2462 IC=+0.006 PNL=+175.94€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2462 IC=+0.006 PNL=+175.94€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1474 IC=+0.026 PNL=+73.86€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1474 IC=+0.026 PNL=+73.86€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.1 con n=8254 PNL=+3904.52€
  - _Datos_: n=8254 IC=+0.132 PNL=+3904.52€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3982 IC=+0.081 PNL=+897.92€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3982 IC=+0.081 PNL=+897.92€

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
  - _Estado_: n=1602 IC=+0.042 PNL=+129.89€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1602 IC=+0.042 PNL=+129.89€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=198 IC=-0.025 PNL=-5.73€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=198 IC=-0.025 PNL=-5.73€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.316 n=362) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=362 IC=+0.316 PNL=+436.70€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=1356 PNL=+544.90€
  - _Datos_: n=1356 IC=+0.118 PNL=+544.90€

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
  - _Estado_: n=49573 IC=+0.069 PNL=+6591.83€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=49573 IC=+0.069 PNL=+6591.83€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.130 < -0.1 con n=826 PNL=+130.20€
  - _Datos_: n=826 IC=-0.130 PNL=+130.20€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4802 IC=+0.068 PNL=+586.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4802 IC=+0.068 PNL=+586.71€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=207 IC=-0.084 PNL=+5.80€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=207 IC=-0.084 PNL=+5.80€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1280 IC=+0.098 PNL=+316.48€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1280 IC=+0.098 PNL=+316.48€

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
  - _Estado_: n=48024 IC=-0.138 PNL=+2947.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=48024 IC=-0.138 PNL=+2947.37€

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
  - _Estado_: n=5144 IC=+0.135 PNL=+3580.69€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=5144 IC=+0.135 PNL=+3580.69€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=12546 IC=+0.056 PNL=+1065.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12546 IC=+0.056 PNL=+1065.67€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.101 > 0.08 con n=5194 PNL=+2913.93€
  - _Datos_: n=5194 IC=+0.101 PNL=+2913.93€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.221 < -0.1 con n=5222 PNL=-434.40€
  - _Datos_: n=5222 IC=-0.221 PNL=-434.40€

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
  - _Estado_: n=131 IC=+0.071 PNL=+22.07€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=131 IC=+0.071 PNL=+22.07€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2385) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2385 IC=+0.096 PNL=+473.94€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=694) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=694 IC=+0.414 PNL=+1016.03€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=20354 IC=+0.176 PNL=-2372.35€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=20354 IC=+0.176 PNL=-2372.35€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.232 > 0.1 con n=337 PNL=+234.92€
  - _Datos_: n=337 IC=+0.232 PNL=+234.92€
