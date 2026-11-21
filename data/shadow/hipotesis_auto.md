# Hipótesis automáticas — 2026-11-21 22:48 UTC
_Generado por shadow_postmortem.py sobre 1442818 resoluciones (PNL=+203206.34€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=729)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1089)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8121` → IC=+0.269 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8121 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.315` → IC=+0.192 (n=342)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.315 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=1115)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.124)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=518)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=952)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.180 (n=298)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 64.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.8117` → IC=+0.269 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8117 (IC base=+0.126)

- **PATRÓN** `banda_z` > `8.502` → IC=+0.197 (n=298)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.502 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.134 (n=810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.129 (n=628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=1015)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.126)

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
- **FILTRO** `restante_s_al_confirmar` < `130.39` → IC=-0.221 (n=12735)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.39
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=38216)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.91` → IC=-0.264 (n=1271)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.91
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.280 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3819)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.48` → IC=-0.165 (n=3521)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.48
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=10566)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `147.64` → IC=-0.255 (n=3502)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.64
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10507)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.7` → IC=-0.267 (n=2342)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.7
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=7029)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=30127)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `7901.6819` → IC=+0.152 (n=2458)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7901.6819 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=26678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=32060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=24124)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=8760)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6334.6659` → IC=+0.139 (n=3422)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 6334.6659 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=2219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=2716)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `16269.5677` → IC=+0.181 (n=706)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 16269.5677 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2775)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16044.722` → IC=+0.186 (n=717)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16044.722 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=2393)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.175 (n=665)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `6825.0558` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 6825.0558 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.153 (n=1556)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.44 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=5498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=2681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 8.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=2640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=3075)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.141 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=952)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.645` → IC=+0.234 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.645 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1189)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2053.6258` → IC=+0.142 (n=950)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2053.6258 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.252 (n=988)
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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.136 (n=1033)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.256 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=78)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=25185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=22405)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=8446)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=6060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.175 (n=5885)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=3721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=2474)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.246 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.205)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=5907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=4998)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=6058)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=4646)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=4662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.252 (n=2263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1610)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=3663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.185)

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

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.211 (n=29878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=34312)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=5211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.177 (n=11127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=16011)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=14512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.275 (n=6180)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=5973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=12288)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=4873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=5992)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=4927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=4946)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.206 (n=4970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=5854)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=12524)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=13606)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.29` → IC=+0.142 (n=11627)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.29 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6099)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=6180)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7694)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.79` → IC=+0.142 (n=7637)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.79 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6425)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=8218)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.92` → IC=+0.138 (n=7694)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.92 (IC base=+0.116)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5051` → IC=+0.140 (n=19872)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5051 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=20141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=13806)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.975` → IC=+0.247 (n=6626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.975 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8679` → IC=+0.294 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8679 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.474` → IC=+0.191 (n=9978)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.474 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6958` → IC=+0.269 (n=5422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6958 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.256 (n=2060)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.233 (n=4800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=9638)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4843.1021` → IC=+0.151 (n=6624)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4843.1021 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.123 (n=12579)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0065 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5641` → IC=+0.146 (n=25108)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5641 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6703` → IC=+0.191 (n=1695)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6703 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1756` → IC=+0.195 (n=10261)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1756 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8575` → IC=+0.196 (n=6975)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8575 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.233 (n=2544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4558` → IC=+0.209 (n=17725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4558 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.229 (n=17696)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.243 (n=1413)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3021` → IC=+0.215 (n=3713)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3021 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=2051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2824)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9826` → IC=+0.274 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9826 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.806` → IC=+0.292 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.806 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.259 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4413` → IC=+0.211 (n=4052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4413 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2043.62` → IC=+0.215 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.62 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.219 (n=3447)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.246 (n=2544)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.269 (n=1272)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=3977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=1739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0765` → IC=+0.281 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0765 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0726` → IC=+0.243 (n=3292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0726 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.252 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8591` → IC=+0.245 (n=2436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8591 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.244 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.233 (n=1207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.222 (n=1202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1138` → IC=+0.247 (n=1585)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1138 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.8928` → IC=+0.257 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8928 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.745` → IC=+0.238 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.745 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.747` → IC=+0.265 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.747 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.697` → IC=+0.229 (n=3218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.697 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.269 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4415` → IC=+0.248 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4415 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.152 (n=3957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0069 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2766` → IC=+0.146 (n=3482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.2766 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7084` → IC=+0.172 (n=3953)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7084 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.151 (n=3874)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.944` → IC=+0.141 (n=3633)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.944 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.154 (n=1318)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6279 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.161 (n=1436)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4465` → IC=+0.143 (n=3823)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4465 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4191` → IC=+0.137 (n=3822)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4191 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=5137)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.184 (n=1269)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 167.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.204 (n=2028)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.254 (n=1724)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.913` → IC=+0.281 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.913 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.192 (n=4013)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.224 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7284` → IC=+0.208 (n=1983)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7284 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=5448)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1906.3268` → IC=+0.198 (n=2028)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1906.3268 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0125` → IC=+0.223 (n=4190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0125 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.4653` → IC=+0.227 (n=3687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4653 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.227 (n=1897)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.272 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.722` → IC=+0.270 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.722 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3453` → IC=+0.255 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3453 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1502` → IC=+0.232 (n=2697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1502 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2015)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1890.9784` → IC=+0.224 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1890.9784 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.224 (n=4034)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.170 (n=237)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5407)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.145 (n=727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.250 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1555` → IC=+0.349 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1555 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.5901` → IC=+0.343 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5901 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.174` → IC=+0.214 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.174 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `1.1121` → IC=+0.361 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1121 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1672` → IC=+0.347 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1672 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.354 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.359 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `2.2799` → IC=+0.351 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2799 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.350 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.0876` → IC=+0.190 (n=1412)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0876 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.3617` → IC=+0.157 (n=706)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3617 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1509` → IC=+0.158 (n=2633)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1509 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8288` → IC=+0.162 (n=1851)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8288 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.201 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.4323` → IC=+0.174 (n=891)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4323 (IC base=+0.059)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.189 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=870)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.174 (n=256)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=773)

- **FILTRO** `ibs_20min` > `0.1949` → IC=-0.127 (n=5301)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1949
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=2611)

- **FILTRO** `sigma_ewma_delta_pct` > `8.272` → IC=-0.234 (n=854)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.272
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=7058)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.173 (n=353)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.75 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.9803` → IC=+0.278 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9803 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.6236` → IC=+0.265 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6236 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.674` → IC=+0.173 (n=163)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.674 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `0.6233` → IC=+0.282 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6233 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.1591` → IC=+0.275 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1591 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.286 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.267 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.1949` → IC=+0.160 (n=2611)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1949 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.2351` → IC=+0.293 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2351 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `1.037` → IC=+0.291 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.037 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` < `0.6921` → IC=+0.299 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6921 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` > `1.0412` → IC=+0.294 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0412 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0782` → IC=+0.317 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0782 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.303 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.4145` → IC=+0.298 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4145 (IC base=-0.032)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.8` → IC=-0.158 (n=4083)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=2104)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.179 (n=1259)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4928)

- **FILTRO** `ibs_20min` > `0.7254` → IC=-0.190 (n=2134)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7254
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=6404)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.143 (n=2104)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.8 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.4523` → IC=+0.349 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4523 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.320 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3056` → IC=+0.313 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3056 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5282` → IC=+0.322 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5282 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.1048` → IC=+0.283 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1048 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` < `0.2319` → IC=+0.263 (n=2525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2319 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.7188` → IC=+0.272 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7188 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.2109` → IC=+0.281 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2109 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.283 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.4813` → IC=+0.264 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4813 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.270 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.188 (n=8685)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0111 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.8657` → IC=+0.284 (n=11816)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8657 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.9972` → IC=+0.302 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9972 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.462` → IC=+0.167 (n=11749)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.462 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.279 (n=8644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.297 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.6418` → IC=+0.288 (n=5037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6418 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.308 (n=14772)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.153 (n=11494)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0092 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.5161` → IC=+0.175 (n=22300)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5161 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2017` → IC=+0.283 (n=8589)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2017 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.859` → IC=+0.279 (n=5745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.859 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.1881` → IC=+0.285 (n=2873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1881 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.322 (n=1904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.4528` → IC=+0.303 (n=4271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4528 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.2695` → IC=+0.304 (n=5808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2695 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.312 (n=12821)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.088)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8122` → IC=-0.145 (n=4614)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8122
  - _Potencial_: sin este filtro IC_bueno=+0.310 (n=2379)

- **FILTRO** `ibs_20min` > `0.7` → IC=-0.238 (n=1570)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4723)

- **FILTRO** `sigma_ewma_delta_pct` > `4.054` → IC=-0.240 (n=1327)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.054
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=4966)

- **PATRÓN** `ibs_20min` > `0.8122` → IC=+0.310 (n=2379)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8122 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.141` → IC=+0.173 (n=2610)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 2.141 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.335 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.289 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2309` → IC=+0.314 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2309 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.320 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.173 (n=1575)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1702 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.156` → IC=+0.390 (n=1386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.156 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.6658` → IC=+0.394 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6658 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.18` → IC=+0.227 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.18 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.219 (n=2268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.246 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.228 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4477` → IC=+0.221 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4477 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `370.0` → IC=+0.232 (n=2511)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 370.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.7352` → IC=+0.257 (n=2332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7352 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.018` → IC=+0.265 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.018 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.289 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5333` → IC=+0.257 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5333 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1506` → IC=+0.260 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1506 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `197.0` → IC=+0.276 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 197.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.317 (n=1624)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.588` → IC=+0.305 (n=2428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.588 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1308` → IC=+0.292 (n=3332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1308 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2528` → IC=+0.300 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2528 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.291 (n=4329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2018.2048` → IC=+0.296 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2018.2048 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.302 (n=2208)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.336 (n=2221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.1873` → IC=+0.328 (n=1465)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1873 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=1279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` < `0.0286` → IC=+0.309 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0286 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.1538` → IC=+0.318 (n=2220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1538 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.064` → IC=+0.318 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.064 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.199` → IC=+0.309 (n=3309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.199 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3441` → IC=+0.316 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3441 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.7404` → IC=+0.325 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7404 (IC base=+0.308)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `2004.3184` → IC=+0.317 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.3184 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.312 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1571` → IC=+0.235 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1571 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.6263` → IC=+0.236 (n=2607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6263 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1672` → IC=+0.236 (n=2371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1672 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.5961` → IC=+0.234 (n=2371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5961 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.236 (n=2491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1031` → IC=+0.244 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1031 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4147` → IC=+0.241 (n=2302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4147 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4963` → IC=+0.235 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4963 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.252 (n=2346)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.0913` → IC=+0.153 (n=1643)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0913 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.381` → IC=+0.261 (n=1920)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.381 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1802` → IC=+0.264 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1802 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6142` → IC=+0.259 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6142 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.266 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.1624` → IC=+0.284 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1624 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.7847` → IC=+0.283 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7847 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.278 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.282 (n=1696)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.012)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.247 (n=2682)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=2690)

- **FILTRO** `ibs_20min` > `0.6078` → IC=-0.238 (n=1267)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6078
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=3802)

- **FILTRO** `sigma_ewma_delta_pct` > `8.236` → IC=-0.265 (n=580)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.236
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=4489)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.314 (n=2690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `1.1116` → IC=+0.352 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1116 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.158 (n=2197)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8446` → IC=+0.349 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8446 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `0.6972` → IC=+0.335 (n=1757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6972 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.337 (n=1853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.367 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.4314` → IC=+0.362 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4314 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.353 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.6078` → IC=+0.165 (n=3802)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6078 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.3257` → IC=+0.274 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3257 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.728` → IC=+0.133 (n=3972)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.728 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.6897` → IC=+0.286 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6897 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0714` → IC=+0.300 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0714 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.7975` → IC=+0.284 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7975 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.292 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.065)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.353 (n=2504)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=2943)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.6511` → IC=+0.338 (n=2801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6511 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2198` → IC=+0.337 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2198 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.819` → IC=+0.337 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.819 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.6288` → IC=+0.325 (n=2801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6288 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.284` → IC=+0.346 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.284 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.5319` → IC=+0.326 (n=2417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5319 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `3007.9702` → IC=+0.323 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3007.9702 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0142` → IC=+0.349 (n=2016)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0142 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=3032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=3029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.3889` → IC=+0.328 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3889 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.2969` → IC=+0.321 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2969 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2569` → IC=+0.316 (n=2978)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2569 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.179` → IC=+0.324 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.179 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.7164` → IC=+0.315 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7164 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2103` → IC=+0.341 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2103 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.364 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4143` → IC=+0.323 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4143 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1485` → IC=+0.316 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1485 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.220 (n=6365)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1262` → IC=+0.193 (n=8399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1262 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=19860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.229 (n=19085)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5357 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1693` → IC=+0.207 (n=7204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1693 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.983` → IC=+0.255 (n=4995)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.983 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.152 (n=12722)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1736 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.152 (n=12721)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6213 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.206 (n=2748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5975` → IC=+0.184 (n=6193)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5975 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=18038)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 85.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.194 (n=8390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0061 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.186 (n=12689)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0082 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.221 (n=6346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=9145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5253` → IC=+0.239 (n=19026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5253 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1951` → IC=+0.180 (n=13893)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1951 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.434` → IC=+0.191 (n=3004)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.434 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.494` → IC=+0.192 (n=16996)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.494 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1892` → IC=+0.165 (n=13482)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1892 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.220 (n=2857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6327` → IC=+0.198 (n=6063)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6327 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.200 (n=18001)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.263 (n=1045)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.264 (n=1043)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=2122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9415` → IC=+0.293 (n=2086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9415 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.46` → IC=+0.328 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.46 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2318` → IC=+0.281 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2318 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8312` → IC=+0.226 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8312 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.227 (n=2995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.256 (n=2636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.254)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.263 (n=1757)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.1003` → IC=+0.306 (n=1159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1003 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=2720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=2399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.4423` → IC=+0.271 (n=2635)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4423 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.936` → IC=+0.258 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.936 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1005` → IC=+0.257 (n=2323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1005 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.268 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.5528` → IC=+0.264 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5528 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.6917` → IC=+0.258 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6917 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.262 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.188 (n=975)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0033 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.175 (n=975)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=3051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2517` → IC=+0.204 (n=2918)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2517 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1946` → IC=+0.211 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1946 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.571` → IC=+0.205 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.571 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.853` → IC=+0.133 (n=1945)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.853 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0477` → IC=+0.132 (n=1322)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.0477 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.172 (n=446)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4059` → IC=+0.130 (n=957)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4059 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.455` → IC=+0.141 (n=957)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.455 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `389.0` → IC=+0.132 (n=2840)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 389.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.174 (n=3148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0069 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2543` → IC=+0.175 (n=2773)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2543 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=1505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6123` → IC=+0.211 (n=3148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6123 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2174` → IC=+0.177 (n=3419)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2174 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.904` → IC=+0.177 (n=581)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.904 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.157 (n=2764)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.162 (n=3148)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2065 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.154 (n=2630)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4814` → IC=+0.157 (n=3021)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4814 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.193 (n=1312)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 204.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.225 (n=1464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.233 (n=2152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=1711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.034` → IC=+0.304 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.034 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.236 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.222 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=3925)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2014.5584` → IC=+0.221 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.5584 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.245 (n=2913)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0122 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.2526` → IC=+0.268 (n=1941)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2526 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.277 (n=1104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0415` → IC=+0.296 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0415 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.845` → IC=+0.288 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.845 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3529` → IC=+0.286 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3529 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7655` → IC=+0.241 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7655 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1738` → IC=+0.255 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1738 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1882.4784` → IC=+0.250 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.4784 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.238 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.194 (n=1052)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0815` → IC=+0.172 (n=1050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0815 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2442` → IC=+0.188 (n=3149)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2442 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1482` → IC=+0.186 (n=1780)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1482 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.235` → IC=+0.203 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.235 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8369` → IC=+0.138 (n=2100)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8369 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.176 (n=473)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.517` → IC=+0.127 (n=1356)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.517 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5028` → IC=+0.135 (n=1028)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5028 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6941.7258` → IC=+0.197 (n=1428)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6941.7258 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.126 (n=3095)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 123.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.161 (n=2970)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0071 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4293` → IC=+0.149 (n=3373)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4293 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6686` → IC=+0.189 (n=3372)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6686 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1698` → IC=+0.157 (n=3446)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1698 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.521` → IC=+0.141 (n=1152)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.521 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.064` → IC=+0.133 (n=3005)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.064 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8532` → IC=+0.151 (n=2248)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8532 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.172 (n=508)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1879` → IC=+0.135 (n=2825)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1879 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.5144` → IC=+0.136 (n=2868)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.5144 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6670.9737` → IC=+0.191 (n=1529)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6670.9737 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.155 (n=1092)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.173 (n=1171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0129 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=3614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.5937` → IC=+0.225 (n=3134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5937 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7969` → IC=+0.214 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7969 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.005` → IC=+0.286 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.005 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1668` → IC=+0.132 (n=3508)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1668 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6262` → IC=+0.124 (n=3507)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6262 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1624` → IC=+0.124 (n=3583)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1624 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.7881` → IC=+0.127 (n=2269)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7881 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2712.4658` → IC=+0.197 (n=1590)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2712.4658 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.128 (n=2247)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.151 (n=3239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0111 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1187` → IC=+0.166 (n=1228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1187 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=3762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.223 (n=3684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.227` → IC=+0.147 (n=3654)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.227 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.231` → IC=+0.146 (n=3258)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.231 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.18` → IC=+0.130 (n=3681)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.18 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.7051` → IC=+0.126 (n=3288)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.7051 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.127 (n=3641)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2764` → IC=+0.149 (n=511)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2764 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.438` → IC=+0.142 (n=1166)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.438 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4431` → IC=+0.135 (n=1166)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4431 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2612.6775` → IC=+0.189 (n=1669)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2612.6775 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.131 (n=3498)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 43.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.246 (n=3150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1686` → IC=+0.241 (n=1387)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1686 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2846)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6647` → IC=+0.255 (n=3150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6647 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1865` → IC=+0.235 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1865 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8385` → IC=+0.228 (n=3245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8385 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.489` → IC=+0.270 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.489 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.619` → IC=+0.236 (n=3150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.619 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.267 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4732` → IC=+0.228 (n=3075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4732 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.5355` → IC=+0.228 (n=2748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5355 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2628.6921` → IC=+0.233 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2628.6921 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0216` → IC=+0.251 (n=1488)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0216 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.6163` → IC=+0.247 (n=3283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6163 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.241 (n=1474)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0381` → IC=+0.297 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0381 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.3265` → IC=+0.245 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3265 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.054` → IC=+0.271 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.054 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8679` → IC=+0.241 (n=2189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8679 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.0478` → IC=+0.243 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0478 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.293 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8502` → IC=+0.236 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8502 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.5546` → IC=+0.238 (n=2780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5546 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.203 (n=1682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1437` → IC=+0.171 (n=2213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1437 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=5252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.6609` → IC=+0.222 (n=3348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6609 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.908` → IC=+0.179 (n=777)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.908 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.514` → IC=+0.210 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.514 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.164 (n=3046)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8561 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1883` → IC=+0.158 (n=1523)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1883 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1556` → IC=+0.170 (n=1296)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1556 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5256` → IC=+0.160 (n=2157)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5256 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=5543)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7207.1498` → IC=+0.194 (n=2277)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7207.1498 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.3878` → IC=+0.178 (n=3652)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.3878 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.2276` → IC=+0.121 (n=949)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.2276 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.148 (n=2413)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 22.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.206 (n=1204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.105` → IC=+0.233 (n=529)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.105 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.229 (n=1087)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.6262` → IC=+0.260 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6262 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3245` → IC=+0.231 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3245 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.927` → IC=+0.226 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.927 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.7004` → IC=+0.227 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7004 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.212 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.211 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `13761.5829` → IC=+0.205 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13761.5829 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.156 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0032 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2186` → IC=+0.191 (n=661)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.2186 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.163 (n=651)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 171.0 (IC base=+0.069)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.239 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1325` → IC=+0.158 (n=680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1325 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.77` → IC=+0.260 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.77 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1561` → IC=+0.169 (n=740)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1561 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.947` → IC=+0.186 (n=218)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.947 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8313` → IC=+0.159 (n=1030)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8313 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2177` → IC=+0.185 (n=271)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2177 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.4672` → IC=+0.169 (n=508)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4672 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7908.6344` → IC=+0.180 (n=701)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 7908.6344 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.150 (n=515)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 30.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.121 (n=1540)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0081 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1832` → IC=+0.203 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1832 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6744` → IC=+0.144 (n=677)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6744 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.0768` → IC=+0.127 (n=564)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.0768 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `5598.5419` → IC=+0.150 (n=1025)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5598.5419 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.150 (n=664)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 40.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.5312` → IC=+0.181 (n=1227)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.5312 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.0555` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 1.0555 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.873` → IC=+0.225 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.873 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.0461` → IC=+0.126 (n=1208)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0461 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.136 (n=234)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4134` → IC=+0.148 (n=444)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4134 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `3060.0718` → IC=+0.152 (n=458)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3060.0718 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5517` → IC=+0.170 (n=1327)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.5517 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.2656` → IC=+0.139 (n=178)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2656 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2774.5236` → IC=+0.166 (n=684)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2774.5236 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.121 (n=1300)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 27.0 (IC base=+0.092)

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

- **PATRÓN** `volumen_regimen` < `0.8885` → IC=+0.191 (n=331)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8885 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2375` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2375 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.172 (n=476)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 20.0 (IC base=+0.156)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.227 (n=8396)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=26329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.967` → IC=+0.302 (n=8394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.967 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9451` → IC=+0.216 (n=2922)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9451 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.92` → IC=+0.261 (n=6166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.92 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2131` → IC=+0.160 (n=16975)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2131 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.216 (n=3304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.624` → IC=+0.193 (n=8203)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.624 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=23815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.207 (n=7811)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1533` → IC=+0.202 (n=10298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1533 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=8775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.253 (n=20596)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.19` → IC=+0.182 (n=14947)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.19 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.347` → IC=+0.204 (n=22898)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.347 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.053` → IC=+0.174 (n=13807)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.053 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.256 (n=3221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.621` → IC=+0.211 (n=7504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.621 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=22301)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.274 (n=1341)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3766` → IC=+0.235 (n=4015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3766 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=4222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8611` → IC=+0.294 (n=2678)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8611 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.026` → IC=+0.301 (n=2635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.026 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.233` → IC=+0.288 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.233 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.288` → IC=+0.240 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.288 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2043.5843` → IC=+0.240 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.5843 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.267 (n=3667)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.268 (n=2444)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1273` → IC=+0.292 (n=1613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1273 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.267 (n=3816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.270 (n=3298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.466` → IC=+0.287 (n=3226)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.466 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.269 (n=3340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.285 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.267 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6471` → IC=+0.275 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6471 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.273 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.174 (n=1380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0822` → IC=+0.148 (n=1380)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0822 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.3023` → IC=+0.202 (n=3698)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3023 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3441` → IC=+0.202 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3441 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.273` → IC=+0.171 (n=863)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.273 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6345` → IC=+0.155 (n=1380)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6345 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.2253` → IC=+0.146 (n=1380)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.2253 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.193 (n=581)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.166` → IC=+0.144 (n=3581)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.166 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5192` → IC=+0.145 (n=3635)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5192 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.153 (n=2685)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 290.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.171 (n=3223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.006 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0835` → IC=+0.174 (n=1224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0835 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6811` → IC=+0.191 (n=3663)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6811 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1534` → IC=+0.162 (n=3606)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1534 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.206` → IC=+0.150 (n=3738)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.206 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0413` → IC=+0.155 (n=3223)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0413 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2211` → IC=+0.196 (n=668)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2211 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.150 (n=3552)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.151 (n=2368)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=4757)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.178 (n=1159)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 212.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.238 (n=1397)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.979` → IC=+0.315 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.979 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.235 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.7556` → IC=+0.239 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7556 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=5092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `1904.5482` → IC=+0.234 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.5482 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.248 (n=3570)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1846` → IC=+0.259 (n=1783)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1846 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1841)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0672` → IC=+0.299 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0672 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.959` → IC=+0.304 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.959 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3469` → IC=+0.300 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3469 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.257 (n=2613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.248 (n=1961)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `2000.0284` → IC=+0.253 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2000.0284 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.248 (n=3459)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.191 (n=1453)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0039 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3536` → IC=+0.147 (n=3834)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3536 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=4532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8785` → IC=+0.268 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8785 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1486` → IC=+0.166 (n=2158)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1486 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.181` → IC=+0.169 (n=869)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.181 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8575` → IC=+0.153 (n=2905)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8575 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.201 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5168` → IC=+0.156 (n=1874)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5168 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1532` → IC=+0.144 (n=1931)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1532 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5837.0711` → IC=+0.232 (n=1976)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5837.0711 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.142 (n=2844)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 85.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.169 (n=3687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0082 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4586` → IC=+0.160 (n=3683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4586 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5701` → IC=+0.214 (n=3242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5701 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.6317` → IC=+0.157 (n=4265)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.6317 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.022` → IC=+0.154 (n=737)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.022 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.014` → IC=+0.154 (n=3206)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.014 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.162 (n=2456)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8521 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.207 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1955` → IC=+0.155 (n=3140)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1955 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5231` → IC=+0.158 (n=3188)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5231 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6728.8499` → IC=+0.215 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6728.8499 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.171 (n=1236)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.157 (n=1478)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0131 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=3145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.6964` → IC=+0.256 (n=2953)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6964 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0603` → IC=+0.202 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0603 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.234` → IC=+0.270 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.234 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2099` → IC=+0.127 (n=4429)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2099 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.122 (n=4219)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.136 (n=553)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5569` → IC=+0.134 (n=1903)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.5569 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2476.871` → IC=+0.223 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2476.871 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.159 (n=3639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0112 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1427` → IC=+0.151 (n=1378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1427 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=1956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5385` → IC=+0.247 (n=3636)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5385 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.2242` → IC=+0.153 (n=3807)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2242 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.033` → IC=+0.161 (n=4009)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.033 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6376` → IC=+0.153 (n=1378)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6376 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.202 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.164 (n=1314)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4777` → IC=+0.141 (n=1314)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4777 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2654.0431` → IC=+0.222 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2654.0431 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.151 (n=3962)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.256 (n=4054)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=4242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=2708)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.9873` → IC=+0.307 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9873 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.204` → IC=+0.252 (n=2064)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.204 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.05` → IC=+0.295 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.05 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2136` → IC=+0.237 (n=4052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2136 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6424` → IC=+0.243 (n=4052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6424 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.255 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5086` → IC=+0.256 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5086 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `3000.4354` → IC=+0.238 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3000.4354 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0249` → IC=+0.270 (n=1406)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0249 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=3973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1371` → IC=+0.306 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1371 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `1.1893` → IC=+0.248 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1893 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.2306` → IC=+0.249 (n=4054)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2306 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.278 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.246 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7154 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.266 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.312 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.248 (n=4000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2986.3631` → IC=+0.245 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2986.3631 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.240 (n=2416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.5361` → IC=+0.232 (n=7231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5361 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=7284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9294` → IC=+0.260 (n=2412)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9294 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.9521` → IC=+0.225 (n=5892)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9521 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.455` → IC=+0.231 (n=2405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.455 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.7071` → IC=+0.230 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7071 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.881` → IC=+0.224 (n=3404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.881 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.224 (n=6775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.231 (n=2022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.235 (n=2372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=5174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3728.5072` → IC=+0.231 (n=4821)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3728.5072 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.229 (n=1712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.212 (n=2329)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4156` → IC=+0.223 (n=4518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4156 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=1735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=2284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.7292` → IC=+0.218 (n=5137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7292 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.705` → IC=+0.218 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.705 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.4405` → IC=+0.205 (n=4959)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4405 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.733` → IC=+0.225 (n=4661)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.733 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.25` → IC=+0.211 (n=4666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.25 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.214 (n=4749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5301` → IC=+0.217 (n=2225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5301 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8123` → IC=+0.219 (n=3372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8123 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.237 (n=3403)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.212)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.280 (n=833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.272 (n=946)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.302 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.280 (n=949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.4633` → IC=+0.285 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4633 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.6801` → IC=+0.278 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6801 (IC base=+0.270)

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

- **PATRÓN** `volumen_spike_ratio` > `1.4175` → IC=+0.272 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4175 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `12913.0263` → IC=+0.282 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12913.0263 (IC base=+0.270)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3878` → IC=+0.187 (n=1543)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3878 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.178 (n=579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.192 (n=680)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.3612` → IC=+0.175 (n=333)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3612 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.5564` → IC=+0.173 (n=1850)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.5564 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.194 (n=1516)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.0909` → IC=+0.185 (n=1358)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.0909 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` < `0.272` → IC=+0.176 (n=1820)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.272 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.188 (n=472)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.4122` → IC=+0.191 (n=512)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4122 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.176 (n=696)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1732 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `14608.6008` → IC=+0.174 (n=700)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 14608.6008 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.188 (n=1498)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 699.0 (IC base=+0.172)

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
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.221 (n=1952)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.4667` → IC=+0.218 (n=1952)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4667 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.4724` → IC=+0.222 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4724 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.147` → IC=+0.212 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.147 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4155` → IC=+0.223 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4155 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.943` → IC=+0.221 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.943 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.216 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `1.2247` → IC=+0.211 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2247 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.213 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.210 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4029` → IC=+0.227 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4029 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4937` → IC=+0.211 (n=1702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4937 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.242 (n=525)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.5081` → IC=+0.223 (n=1573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5081 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.215 (n=605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.218 (n=1114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.213 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0847 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.6928` → IC=+0.218 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6928 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.4307` → IC=+0.207 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4307 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.212 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2534` → IC=+0.215 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2534 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.209 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7214 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.231 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1565` → IC=+0.209 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1565 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7713` → IC=+0.210 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7713 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `7877.6521` → IC=+0.218 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7877.6521 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.210 (n=1565)

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
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.151 (n=878)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0041 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.189 (n=1706)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.75 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.1569` → IC=+0.149 (n=1213)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1569 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.435` → IC=+0.143 (n=555)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.435 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.5949` → IC=+0.165 (n=1927)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.5949 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.176 (n=541)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.082)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.175 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0029 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5444` → IC=+0.160 (n=677)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5444 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.166 (n=357)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.068)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.131 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0036 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.248 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.0702` → IC=+0.140 (n=301)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.0702 (IC base=+0.052)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5205` → IC=-0.121 (n=344)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5205
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=701)

- **FILTRO** `ibs_20min` > `0.6272` → IC=-0.149 (n=186)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6272
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=560)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.156 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0043 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.5205` → IC=+0.160 (n=701)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5205 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.135` → IC=+0.157 (n=377)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.135 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.791` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.791 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.279 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=+0.041)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9861` → IC=+0.197 (n=295)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.9861 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.7577` → IC=+0.154 (n=212)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.7577 (IC base=+0.033)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.168 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0101 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.193 (n=552)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.2159` → IC=+0.150 (n=547)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2159 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.09` → IC=+0.234 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.09 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.1167` → IC=+0.192 (n=183)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.1167 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.1089` → IC=+0.176 (n=205)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1089 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `2.193` → IC=+0.130 (n=455)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.193 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `1.4591` → IC=+0.139 (n=516)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4591 (IC base=+0.100)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.329 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.300)

- **PATRÓN** `ibs_20min` > `0.6977` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6977 (IC base=+0.300)

- **PATRÓN** `dist_vwap_pct` > `0.4847` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4847 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.38` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.38 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.328` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.328 (IC base=+0.300)

- **PATRÓN** `volumen_regimen` < `0.9596` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9596 (IC base=+0.300)

- **PATRÓN** `volumen_regimen` > `0.6848` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6848 (IC base=+0.300)

- **PATRÓN** `volumen_pendiente_norm` < `0.0568` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0568 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` < `1.8927` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8927 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` > `2.1829` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1829 (IC base=+0.300)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `34.6896` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 34.6896 (IC base=+0.300)

- **PATRÓN** `sigma_h` < `0.0126` → IC=+0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0126 (IC base=+0.317)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.329 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.317)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.317)

- **PATRÓN** `ibs_20min` < `0.1481` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1481 (IC base=+0.317)

- **PATRÓN** `ibs_20min` > `0.3972` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3972 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` > `1.0585` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0585 (IC base=+0.317)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` < `1.5039` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5039 (IC base=+0.317)

- **PATRÓN** `libro_liquidez` > `39.7` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 39.7 (IC base=+0.317)

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

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.286 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=84)

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

- **FILTRO** `volumen_spike_ratio` > `2.5392` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.5392
  - _Potencial_: sin este filtro IC_bueno=-0.310 (n=77)

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
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.262 (n=372)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.203 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.8551` → IC=+0.324 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8551 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.414` → IC=+0.189 (n=191)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 10.414 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.407` → IC=+0.167 (n=835)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 8.407 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.195 (n=273)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6242 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` < `0.206` → IC=+0.186 (n=794)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.206 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4062` → IC=+0.212 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4062 (IC base=+0.167)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.159 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0065 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.7315` → IC=+0.137 (n=235)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7315 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.6628` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6628 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.242` → IC=+0.135 (n=433)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.242 (IC base=+0.074)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.137 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0045 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.181 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0071 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.139 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.177 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.7994` → IC=+0.186 (n=237)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7994 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.8076` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8076 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1088` → IC=+0.156 (n=216)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1088 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.169` → IC=+0.156 (n=274)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 9.169 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6229 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1834` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1834 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.0503` → IC=+0.189 (n=220)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0503 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.7116` → IC=+0.188 (n=158)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.7116 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=+0.003)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.15` → IC=-0.240 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=149)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.284 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.295 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` > `0.7508` → IC=+0.397 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7508 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` < `0.7943` → IC=+0.295 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7943 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.315 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.329 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.0543` → IC=+0.302 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0543 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.272 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.266)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=185)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.333)

- **PATRÓN** `elapsed_s` > `208.3` → IC=+0.380 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.3 (IC base=+0.333)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.6616` → IC=+0.380 (n=98)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6616 (IC base=+0.333)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.386 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `1046.0` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1046.0 (IC base=+0.333)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3507` → IC=+0.297 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3507 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `230.8` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.8 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.324 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.9468` → IC=+0.309 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9468 (IC base=+0.289)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1325.0` → IC=+0.375 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1325.0 (IC base=+0.289)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=185)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.333)

- **PATRÓN** `elapsed_s` > `208.3` → IC=+0.380 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.3 (IC base=+0.333)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.6616` → IC=+0.380 (n=98)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6616 (IC base=+0.333)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.386 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `1046.0` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1046.0 (IC base=+0.333)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3507` → IC=+0.297 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3507 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `230.8` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.8 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.324 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.9468` → IC=+0.309 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9468 (IC base=+0.289)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1325.0` → IC=+0.375 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1325.0 (IC base=+0.289)

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
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=1388)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4194)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1639)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1593)

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
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1125)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1125)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1502)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1502)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=348)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=348)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.138 (n=114)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=249)

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
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=422)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.126 (n=3440)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=8967)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=91)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.136 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=142)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=88)

- **FILTRO** `restante_min` < `3.99` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=72)

- **FILTRO** `lag_apertura_s` > `60.89` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.89
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.152 (n=409)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1003)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.151 (n=330)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=889)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.149 (n=425)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.51 (IC base=-0.006)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=194)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=441)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.120 (n=480)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=499)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=712)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=750)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.133 (n=330)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.51 (IC base=-0.020)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=354)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=748)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=765)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=399)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.129 (n=618)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9105)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=28347)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=9467)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=29286)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.199 (n=1696)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5287)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.144 (n=2319)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=4556)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1794)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.137 (n=3239)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.016)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.185 (n=1181)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=3946)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.176 (n=1334)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4090)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1722)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=5332)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.133 (n=2150)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7656` → IC=-0.152 (n=1254)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7656
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3765)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1364)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4162)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.162 (n=1733)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5269)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3283)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4235)

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

- **FILTRO** `libro_liquidez` < `2015.008` → IC=-0.137 (n=406)

  - _Acción_: SKIP cuando `libro_liquidez` < 2015.008
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=826)

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
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=57669)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=20221)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=62727)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=27265)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=55683)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.155 (n=27852)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=55096)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=25729)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=78056)

- **FILTRO** `ibs_7min` > `0.2785` → IC=-0.183 (n=25942)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2785
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=77843)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=3543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=11412)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.321 (n=3735)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=11220)

- **FILTRO** `ibs_7min` < `0.7087` → IC=-0.256 (n=4935)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7087
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=10020)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4359)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=13620)

- **FILTRO** `ibs_7min` > `0.7674` → IC=-0.211 (n=4494)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7674
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=13485)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.267 (n=3356)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=10332)

- **FILTRO** `ibs_7min` < `0.7112` → IC=-0.216 (n=3421)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7112
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=10267)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.205 (n=3415)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=10273)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=3189)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10817)

- **FILTRO** `ibs_7min` > `0.2646` → IC=-0.191 (n=3501)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2646
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10505)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.178 (n=3492)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10514)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3406)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=10928)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.330 (n=3426)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=10908)

- **FILTRO** `ibs_7min` < `0.2896` → IC=-0.255 (n=4730)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2896
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9604)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.174 (n=3447)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=10887)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.262 (n=4556)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=14455)

- **FILTRO** `ibs_7min` > `0.7222` → IC=-0.186 (n=4744)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=14267)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.278 (n=3036)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10333)

- **FILTRO** `ibs_7min` < `0.7119` → IC=-0.203 (n=3341)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7119
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=10028)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.200 (n=3226)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=10143)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3236)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=10639)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.179 (n=3468)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=10407)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.168 (n=3457)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10418)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=3219)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9979)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.235 (n=4338)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8860)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3265)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=9933)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.202 (n=4764)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=15330)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=3286)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=10118)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.232 (n=4400)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9004)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.196 (n=3332)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=10072)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.231 (n=4598)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=14222)

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
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=668)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=925)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.127 (n=234)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=463)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=593)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.124 (n=107)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=678)

- **FILTRO** `libro_liquidez` < `3306.8101` → IC=-0.146 (n=196)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.8101
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=589)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=554)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.144 (n=757)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.130 (n=609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `451.7672` → IC=+0.166 (n=555)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 451.7672 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3665.592` → IC=+0.131 (n=754)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3665.592 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.187 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `381.982` → IC=+0.165 (n=338)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 381.982 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.157 (n=266)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 9.0 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.130 (n=347)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.153 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.114)

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

- **FILTRO** `sigma_h` > `0.0074` → IC=-0.145 (n=336)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=654)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.157 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0047 (IC base=-0.026)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0059` → IC=-0.147 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0059
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=152)

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
- **FILTRO** `sigma_h` > `0.007` → IC=-0.241 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=143)

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

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.143 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=160)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.161 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=182)

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

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.306 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=118)

- **FILTRO** `sigma_h` < `0.0091` → IC=-0.261 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=134)

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
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.515 (IC base=-0.023)

- **PATRÓN** `streak_estiramiento` < `0.6467` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `streak_estiramiento` < 0.6467 (IC base=-0.005)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1321)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5453)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3267)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.184 (n=2119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.232` → IC=+0.158 (n=6357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.232 (IC base=+0.133)

- **PATRÓN** `drift_15min` |x|≤ `1.1201` → IC=+0.135 (n=6357)

  - _Acción_: Kelly boost +0.67€ cuando `drift_15min` |x|≤ 1.1201 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0645` → IC=+0.133 (n=6358)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0645 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0999` → IC=+0.143 (n=2000)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0999 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=5895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.5585` → IC=+0.210 (n=5679)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5585 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.166` → IC=+0.231 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.166 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3378)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4336.5815` → IC=+0.171 (n=2119)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4336.5815 (IC base=+0.133)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=2456)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.253 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.245 (n=383)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.205)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2678` → IC=+0.225 (n=289)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2678 (IC base=+0.205)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2264` → IC=+0.216 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2264 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.7058` → IC=+0.275 (n=867)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7058 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.3902` → IC=+0.224 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3902 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.547` → IC=+0.209 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.547 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.133` → IC=+0.299 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.133 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.224 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.205)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.161 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0047 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.146 (n=739)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0848` → IC=+0.137 (n=990)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.0848 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.144 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4837` → IC=+0.218 (n=1108)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4837 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1241` → IC=+0.144 (n=697)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1241 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.655` → IC=+0.135 (n=1259)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.655 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.04` → IC=+0.285 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.04 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6086.5636` → IC=+0.173 (n=503)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6086.5636 (IC base=+0.132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.84` → IC=+0.149 (n=651)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` > 0.84 (IC base=+0.046)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0139` → IC=+0.143 (n=709)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0139 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.144 (n=1611)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.012 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2382` → IC=+0.176 (n=1611)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2382 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.142 (n=1612)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0926` → IC=+0.191 (n=502)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0926 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=1477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.141 (n=1484)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.7` → IC=+0.235 (n=1079)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.2134` → IC=+0.151 (n=735)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2134 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.9149` → IC=+0.143 (n=1863)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.9149 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.332` → IC=+0.187 (n=369)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 17.332 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2946.9184` → IC=+0.182 (n=730)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2946.9184 (IC base=+0.139)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.363 (n=532)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1482` → IC=+0.376 (n=531)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1482 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.378 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.379 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.395 (n=797)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2675` → IC=+0.378 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2675 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.778` → IC=+0.395 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.778 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9610.6074` → IC=+0.379 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9610.6074 (IC base=+0.363)

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
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.364 (n=417)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.364 (n=278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1274` → IC=+0.379 (n=278)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1274 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.369 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.380 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.397 (n=417)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.375 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.364 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.857` → IC=+0.397 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.857 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `4304.5454` → IC=+0.374 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4304.5454 (IC base=+0.362)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.223 (n=2629)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3346)

- **FILTRO** `libro_liquidez` < `4366.1664` → IC=-0.173 (n=3943)

  - _Acción_: SKIP cuando `libro_liquidez` < 4366.1664
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=2032)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.215 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.090)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.278 (n=1314)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1154` → IC=+0.204 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1154 (IC base=-0.090)

- **PATRÓN** `dist_vwap_pct` < `0.5918` → IC=+0.199 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5918 (IC base=-0.090)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2285` → IC=+0.271 (n=1940)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2285 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.283 (n=5834)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.7038` → IC=+0.265 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7038 (IC base=+0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0737` → IC=-0.241 (n=1950)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0737
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=1953)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.213 (n=975)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=2928)

- **FILTRO** `sigma_ewma_delta_pct` > `22.279` → IC=-0.242 (n=553)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.279
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=3350)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.146 (n=360)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0032 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2678` → IC=+0.274 (n=157)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2678 (IC base=+0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.145` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.145 (IC base=+0.064)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.317 (n=469)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.281 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.5257` → IC=+0.284 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5257 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.8` → IC=+0.140 (n=237)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 21.8 (IC base=+0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.107` → IC=+0.236 (n=70)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.107 (IC base=-0.182)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0902` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0902 (IC base=-0.182)

- **PATRÓN** `ibs_15` < `0.6283` → IC=+0.290 (n=79)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6283 (IC base=-0.182)

- **PATRÓN** `dist_vwap_pct` < `0.0469` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0469 (IC base=-0.182)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.182)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=863)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.161 (n=661)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0066 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.176 (n=291)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3015` → IC=+0.190 (n=521)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3015 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.169 (n=475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.243 (n=660)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2791` → IC=+0.157 (n=269)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.2791 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.149 (n=505)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.266 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=863)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5128.1918` → IC=+0.161 (n=440)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5128.1918 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.259 (n=998)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4769` → IC=+0.242 (n=2269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4769 (IC base=+0.238)

- **PATRÓN** `drift_15min` |x|≤ `0.8208` → IC=+0.251 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8208 (IC base=+0.238)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2028` → IC=+0.258 (n=1028)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2028 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.240 (n=1543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.238)

- **PATRÓN** `ibs_15` < `0.3893` → IC=+0.270 (n=2268)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3893 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1649` → IC=+0.252 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1649 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.514` → IC=+0.245 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.514 (IC base=+0.238)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2013` → IC=-0.297 (n=357)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2013
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1076)

- **FILTRO** `drift_15min` |x|> `1.0081` → IC=-0.308 (n=358)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0081
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1075)

- **FILTRO** `sigma_ewma_delta_pct` > `5.969` → IC=-0.212 (n=314)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.969
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=1119)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.207)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.207)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.207)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.207)

- **PATRÓN** `ibs_15` < `0.3793` → IC=+0.297 (n=972)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3793 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.4661` → IC=+0.250 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4661 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0145` → IC=-0.252 (n=1130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0145
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=557)

- **FILTRO** `drift_60min` |x|> `0.1588` → IC=-0.252 (n=421)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1588
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=1266)

- **FILTRO** `drift_15min` |x|> `1.31` → IC=-0.282 (n=421)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.31
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1266)

- **FILTRO** `sigma_ewma_delta_pct` > `7.321` → IC=-0.226 (n=513)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.321
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1174)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=1666)

- **FILTRO** `libro_liquidez` < `2938.7935` → IC=-0.227 (n=1113)

  - _Acción_: SKIP cuando `libro_liquidez` < 2938.7935
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=574)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.222)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.283 (n=1217)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=-0.009)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.291 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.009)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=1374)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.324 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=-0.009)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0682` → IC=+0.284 (n=1466)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0682 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2201` → IC=+0.290 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2201 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8372` → IC=+0.310 (n=1467)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8372 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2747` → IC=+0.313 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2747 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.703` → IC=+0.384 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.703 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.284 (n=1741)

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
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.299 (n=306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0502` → IC=+0.321 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0502 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.293 (n=695)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1013` → IC=+0.308 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1013 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.289 (n=492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8452` → IC=+0.315 (n=695)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8452 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.312 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2918 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.914` → IC=+0.379 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.914 (IC base=+0.290)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5585 sube el IC de +0.133 a +0.210 en UPDOWN_GBM#15min (n=5679). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7058 sube el IC de +0.205 a +0.275 en UPDOWN_GBM#BTC#15min (n=867). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4837 sube el IC de +0.132 a +0.218 en UPDOWN_GBM#ETH#15min (n=1108). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.7 sube el IC de +0.139 a +0.235 en UPDOWN_GBM#XRP#15min (n=1079). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.090 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1314). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de +0.001 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=5834). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.064 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=469). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6283 sube el IC de -0.182 a +0.290 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=79). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de +0.147 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=660). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3893 sube el IC de +0.238 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2268). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.207 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3793 sube el IC de -0.026 a +0.297 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=972). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.222 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.009 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1374). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.085 a +0.300 en UPDOWN_GBM_ETH_15M_HORA7 (n=28). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.085 a +0.300 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=28). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8372 sube el IC de +0.284 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1467). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.278 a +0.302 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=772). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8452 sube el IC de +0.290 a +0.315 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=695). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.363 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=797). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.383 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.362 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=417). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2288 | +0.084 | +244.73€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2288 | +0.084 | +244.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1876 | +0.085 | +205.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1876 | +0.085 | +205.24€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1394 | -0.027 | +72.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1394 | -0.027 | +72.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1075 | -0.041 | +56.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1075 | -0.041 | +56.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 220 | +0.045 | +24.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 220 | +0.045 | +24.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 92 | -0.043 | -11.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 92 | -0.043 | -11.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 50951 | -0.087 | -6551.62€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3306 | +0.092 | -318.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 47645 | -0.100 | -6233.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5087 | -0.115 | -815.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5087 | -0.115 | -815.42€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3306 | +0.092 | -318.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3306 | +0.092 | -318.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5091 | -0.108 | -951.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5091 | -0.108 | -951.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14087 | -0.046 | -1353.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14087 | -0.046 | -1353.69€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14009 | -0.121 | -1572.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14009 | -0.121 | -1572.57€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9371 | -0.138 | -1540.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9371 | -0.138 | -1540.01€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 55538 | -0.012 | +2746.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 14306 | +0.003 | +1475.30€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 41232 | -0.017 | +1270.75€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 55538 | -0.012 | +2746.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 14306 | +0.003 | +1475.30€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 41232 | -0.017 | +1270.75€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 207746 | +0.113 | -8340.30€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 23053 | +0.179 | -757.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 969 | +0.018 | -76.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 171940 | +0.106 | -7088.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11784 | +0.095 | -417.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 28496 | +0.103 | -1996.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 83 | -0.182 | +13.02€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 28390 | +0.104 | -2006.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 8 | +0.040 | +8.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 38976 | +0.123 | -605.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5686 | +0.177 | -232.08€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 28461 | +0.120 | -179.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4787 | +0.082 | -171.70€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 28543 | +0.099 | -1982.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 97 | -0.116 | +14.79€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 28427 | +0.100 | -1987.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 44447 | +0.123 | -922.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11078 | +0.178 | -316.76€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 28919 | +0.106 | -521.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4438 | +0.103 | -75.54€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 38763 | +0.111 | -1647.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6012 | +0.199 | -248.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 872 | +0.042 | -22.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 29335 | +0.096 | -1193.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2544 | +0.106 | -183.58€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 28521 | +0.107 | -1186.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 97 | -0.136 | +11.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 28408 | +0.108 | -1200.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 33804 | +0.189 | -2519.20€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 33804 | +0.189 | -2519.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7662 | +0.162 | -896.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7662 | +0.162 | -896.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5049 | +0.194 | -214.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5049 | +0.194 | -214.82€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7483 | +0.172 | -691.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7483 | +0.172 | -691.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6196 | +0.252 | -220.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6196 | +0.252 | -220.79€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7335 | +0.184 | -509.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7335 | +0.184 | -509.98€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 119485 | +0.200 | -8667.57€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 119485 | +0.200 | -8667.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 20713 | +0.176 | -2430.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 20713 | +0.176 | -2430.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 19260 | +0.223 | -642.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 19260 | +0.223 | -642.10€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 20493 | +0.181 | -2127.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 20493 | +0.181 | -2127.60€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 19428 | +0.217 | -773.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 19428 | +0.217 | -773.48€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 19717 | +0.205 | -1158.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 19717 | +0.205 | -1158.99€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 19874 | +0.198 | -1534.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 19874 | +0.198 | -1534.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 46435 | +0.116 | +350.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 46435 | +0.116 | +350.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 23125 | +0.117 | +225.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 23125 | +0.117 | +225.92€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 23310 | +0.116 | +124.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 23310 | +0.116 | +124.96€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 600 | +0.435 | -7.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 606 | +0.441 | +0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 606 | +0.441 | +0.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2033 | +0.064 | -102.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1308 | +0.074 | -38.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1599 | +0.070 | -57.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1308 | +0.074 | -38.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 94747 | +0.101 | -1991.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7682 | +0.097 | +185.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 87065 | +0.101 | -2176.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 51728 | +0.105 | -435.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7682 | +0.097 | +185.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 44046 | +0.107 | -620.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 20340 | +0.110 | -48.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 20340 | +0.110 | -48.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 22679 | +0.083 | -1507.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 22679 | +0.083 | -1507.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 64528 | +0.102 | +36276.10€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 64528 | +0.102 | +36276.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10709 | +0.225 | +9198.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10709 | +0.225 | +9198.41€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 10072 | +0.176 | +8099.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10072 | +0.176 | +8099.25€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 11549 | +0.206 | +9099.68€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11549 | +0.206 | +9099.68€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 8532 | +0.062 | +2887.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8532 | +0.062 | +2887.30€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8941 | -0.026 | +2296.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8941 | -0.026 | +2296.40€ | 4 | 16 |
| ✅ GBM_LATE_15M#XRP | 14725 | -0.020 | +4695.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 14725 | -0.020 | +4695.06€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 68510 | +0.087 | +39995.58€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 68510 | +0.087 | +39995.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 13286 | -0.002 | +6942.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 13286 | -0.002 | +6942.53€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 14723 | +0.007 | +4076.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 14723 | +0.007 | +4076.35€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9213 | +0.295 | +10550.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9213 | +0.295 | +10550.92€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 13082 | +0.018 | +4189.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 13082 | +0.018 | +4189.61€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10441 | +0.049 | +4802.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10441 | +0.049 | +4802.42€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7765 | +0.313 | +9433.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7765 | +0.313 | +9433.76€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 50801 | +0.179 | +42218.65€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 50801 | +0.179 | +42218.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7682 | +0.240 | +7147.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7682 | +0.240 | +7147.08€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8085 | +0.141 | +6064.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8085 | +0.141 | +6064.48€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8183 | +0.224 | +7089.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8183 | +0.224 | +7089.00€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8693 | +0.130 | +6785.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8693 | +0.130 | +6785.10€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9582 | +0.123 | +7403.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9582 | +0.123 | +7403.22€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8576 | +0.232 | +7729.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8576 | +0.232 | +7729.77€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 13998 | +0.127 | +7163.55€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 13998 | +0.127 | +7163.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 677 | +0.163 | +447.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3604 | +0.126 | +1969.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3604 | +0.126 | +1969.04€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 509 | +0.156 | +286.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4109 | +0.128 | +2077.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4109 | +0.128 | +2077.37€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3839 | +0.104 | +1596.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3839 | +0.104 | +1596.14€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1260 | +0.167 | +786.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1260 | +0.167 | +786.94€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO | 64775 | +0.189 | +53919.45€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 64775 | +0.189 | +53919.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 10239 | +0.249 | +9872.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 10239 | +0.249 | +9872.64€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 10400 | +0.142 | +7521.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 10400 | +0.142 | +7521.82€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10985 | +0.234 | +9887.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10985 | +0.234 | +9887.52€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10719 | +0.144 | +8067.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10719 | +0.144 | +8067.65€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 11411 | +0.128 | +8349.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 11411 | +0.128 | +8349.00€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11021 | +0.240 | +10220.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11021 | +0.240 | +10220.82€ | 0 | 22 |
| ✅ GBM_LATE_5M | 16486 | +0.218 | +13889.00€ | 0 | 27 |
| ✅ GBM_LATE_5M#5min | 16486 | +0.218 | +13889.00€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1932 | +0.253 | +1880.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1932 | +0.253 | +1880.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3318 | +0.210 | +2853.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3318 | +0.210 | +2853.71€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1524 | +0.214 | +1243.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1524 | +0.214 | +1243.40€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 4698 | +0.209 | +3666.86€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4698 | +0.209 | +3666.86€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 2947 | +0.228 | +2611.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2947 | +0.228 | +2611.15€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 2067 | +0.210 | +1633.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2067 | +0.210 | +1633.69€ | 0 | 0 |
| ✅ GBM_LATE_60M | 6175 | +0.071 | +1936.15€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 6175 | +0.071 | +1936.15€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 110 | +0.259 | +109.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 110 | +0.259 | +109.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2004 | +0.060 | +578.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2004 | +0.060 | +578.77€ | 0 | 6 |
| ✅ GBM_LATE_60M#DOGE | 107 | +0.326 | +128.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 107 | +0.326 | +128.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 1861 | +0.054 | +593.76€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1861 | +0.054 | +593.76€ | 2 | 5 |
| ✅ GBM_LATE_60M#SOL | 1987 | +0.059 | +405.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1987 | +0.059 | +405.91€ | 0 | 10 |
| ✅ GBM_LATE_60M#XRP | 106 | +0.315 | +119.76€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 106 | +0.315 | +119.76€ | 0 | 22 |
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
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2349 | +0.090 | +597.24€ | 0 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2349 | +0.090 | +597.24€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 889 | +0.070 | +204.36€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 889 | +0.070 | +204.36€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 808 | +0.062 | +155.83€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 808 | +0.062 | +155.83€ | 0 | 15 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 649 | +0.153 | +236.24€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 649 | +0.153 | +236.24€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 397 | +0.312 | +482.97€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 397 | +0.312 | +482.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 397 | +0.312 | +482.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 397 | +0.312 | +482.97€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4825 | +0.094 | +1044.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4825 | +0.094 | +1044.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4825 | +0.094 | +1044.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4825 | +0.094 | +1044.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 1712 | +0.018 | +97.96€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1712 | +0.018 | +97.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 208 | +0.081 | +37.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 208 | +0.081 | +37.35€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 336 | -0.009 | +8.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 336 | -0.009 | +8.48€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 115 | +0.056 | +25.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 115 | +0.056 | +25.23€ | 2 | 3 |
| ✅ LIQUIDACIONES_15M#ETH | 386 | +0.026 | +21.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 386 | +0.026 | +21.80€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 350 | -0.014 | +2.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 350 | -0.014 | +2.82€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 317 | +0.017 | +2.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 317 | +0.017 | +2.27€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4535 | +0.017 | +181.80€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4535 | +0.017 | +181.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 860 | +0.015 | +47.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 860 | +0.015 | +47.72€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 334 | +0.062 | +80.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 334 | +0.062 | +80.07€ | 0 | 7 |
| ✅ LIQUIDACIONES_5M#ETH | 1691 | +0.020 | +31.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1691 | +0.020 | +31.17€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 789 | +0.015 | +5.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 789 | +0.015 | +5.57€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 620 | -0.006 | +23.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 620 | -0.006 | +23.43€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2722 | -0.034 | -6.14€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2722 | -0.034 | -6.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 832 | -0.034 | -13.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 832 | -0.034 | -13.44€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 981 | -0.015 | +18.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 981 | -0.015 | +18.43€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 898 | -0.054 | -10.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 898 | -0.054 | -10.73€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 8 | +0.000 | +0.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 8 | +0.000 | +0.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 20392 | -0.030 | -133.12€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 9863 | -0.033 | -124.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 10529 | -0.028 | -8.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 731 | -0.050 | -35.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 368 | -0.038 | -6.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 363 | -0.062 | -28.46€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 5479 | -0.025 | -9.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2604 | -0.023 | +10.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2875 | -0.027 | -19.10€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1864 | -0.032 | -2.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 952 | -0.044 | -30.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 912 | -0.020 | +28.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4662 | -0.031 | -51.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2246 | -0.030 | -20.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2416 | -0.032 | -30.75€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3892 | -0.023 | +55.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1896 | -0.030 | -6.09€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1996 | -0.016 | +61.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3764 | -0.041 | -90.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1797 | -0.048 | -70.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1967 | -0.034 | -19.89€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 76205 | -0.000 | +4147.99€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 76205 | -0.000 | +4147.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13858 | +0.027 | +1931.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13858 | +0.027 | +1931.97€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10551 | -0.038 | -139.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10551 | -0.038 | -139.99€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14013 | +0.026 | +1567.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14013 | +0.026 | +1567.84€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10545 | -0.054 | -274.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10545 | -0.054 | -274.13€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12992 | -0.004 | +369.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12992 | -0.004 | +369.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14246 | +0.019 | +692.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14246 | +0.019 | +692.46€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7405 | -0.053 | -108.28€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7405 | -0.053 | -108.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1270 | -0.002 | -14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2105 | -0.058 | -17.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2105 | -0.058 | -17.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 102 | -0.019 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 102 | -0.019 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 819 | -0.116 | -32.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 819 | -0.116 | -32.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2239 | -0.067 | -13.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2239 | -0.067 | -13.94€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 186733 | -0.078 | +2221.10€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 186733 | -0.078 | +2221.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 32934 | -0.076 | +1930.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 32934 | -0.076 | +1930.36€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 27694 | -0.102 | -1376.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 27694 | -0.102 | -1376.63€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33345 | -0.068 | +1609.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33345 | -0.068 | +1609.12€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 27244 | -0.100 | -950.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 27244 | -0.100 | -950.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33292 | -0.059 | +179.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33292 | -0.059 | +179.05€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32224 | -0.069 | +829.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32224 | -0.069 | +829.69€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9322 | -0.036 | -191.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9322 | -0.036 | -191.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1009 | -0.017 | -19.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1009 | -0.017 | -19.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2186 | -0.046 | -28.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2186 | -0.046 | -28.58€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2676 | -0.024 | -31.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2676 | -0.024 | -31.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1298 | -0.064 | -32.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1298 | -0.064 | -32.37€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1144 | -0.042 | -46.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1144 | -0.042 | -46.97€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2353 | +0.120 | +941.65€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2217 | +0.124 | +929.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 511 | +0.141 | +264.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 511 | +0.141 | +264.33€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 462 | +0.114 | +157.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 462 | +0.114 | +157.49€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 410 | +0.126 | +185.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 410 | +0.126 | +185.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 375 | +0.134 | +182.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 375 | +0.134 | +182.24€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 459 | +0.101 | +139.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 459 | +0.101 | +139.00€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2492 | -0.022 | -45.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2492 | -0.022 | -45.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 445 | +0.008 | +22.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 445 | +0.008 | +22.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 458 | -0.048 | -30.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 458 | -0.048 | -30.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 606 | -0.046 | -43.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 606 | -0.046 | -43.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 516 | -0.004 | -1.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 516 | -0.004 | -1.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 467 | -0.014 | +6.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 467 | -0.014 | +6.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1303 | -0.041 | +136.66€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 601 | -0.066 | +27.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 472 | -0.061 | +51.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 458 | -0.011 | +72.15€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 337 | +0.010 | +80.90€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 244 | -0.037 | +36.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 208 | -0.029 | +35.13€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1017 | -0.031 | +167.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1653 | -0.184 | -31.00€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 652 | -0.173 | -8.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 581 | -0.169 | -4.11€ | 2 | 0 |
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
| ✅ STREAK_FADE_5M | 3643 | -0.023 | -144.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3643 | -0.023 | -144.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 626 | -0.030 | -28.54€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 626 | -0.030 | -28.54€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 177 | -0.048 | -15.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 177 | -0.048 | -15.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1713 | -0.018 | -59.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1713 | -0.018 | -59.53€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 135 | -0.011 | -6.94€ | 0 | 2 |
| ✅ STREAK_FADE_60M#60min | 135 | -0.011 | -6.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 48 | -0.040 | -2.81€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 48 | -0.040 | -2.81€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 81 | -0.006 | -6.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 81 | -0.006 | -6.44€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11660 | +0.013 | +62.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11660 | +0.013 | +62.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3007 | +0.017 | +21.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3007 | +0.017 | +21.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3106 | +0.013 | +23.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3106 | +0.013 | +23.88€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2940 | +0.008 | -3.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2940 | +0.008 | -3.49€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2607 | +0.014 | +20.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2607 | +0.014 | +20.40€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 13569 | +0.019 | +11.78€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 13569 | +0.019 | +11.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5472 | +0.021 | +3.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5472 | +0.021 | +3.53€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4796 | +0.020 | +7.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4796 | +0.020 | +7.03€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3301 | +0.016 | +1.22€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3301 | +0.016 | +1.22€ | 1 | 0 |
| ✅ UPDOWN_GBM | 122944 | +0.060 | +11736.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 30553 | +0.078 | +6025.94€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3501 | -0.000 | +41.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 81189 | +0.062 | +5542.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7283 | -0.001 | +131.32€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10792 | +0.103 | +1987.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2021 | +0.166 | +953.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8681 | +0.090 | +1036.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 27726 | +0.057 | +2456.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4079 | +0.081 | +918.17€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1025 | -0.001 | +21.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 19191 | +0.066 | +1429.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3281 | -0.004 | +82.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 150 | -0.066 | +4.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 13782 | +0.074 | +1513.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2008 | +0.156 | +859.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11688 | +0.060 | +655.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 28731 | +0.049 | +2057.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7086 | +0.071 | +1111.50€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 992 | +0.005 | +15.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 17810 | +0.052 | +886.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2703 | -0.001 | +41.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 140 | -0.099 | +2.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 25539 | +0.041 | +1452.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8275 | +0.033 | +478.33€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 911 | -0.010 | +8.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14928 | +0.053 | +968.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1299 | +0.004 | +8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 126 | -0.141 | -10.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 16372 | +0.073 | +2269.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7084 | +0.089 | +1705.82€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8891 | +0.063 | +565.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 416 | -0.101 | -3.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1062 | +0.363 | +393.44€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1062 | +0.363 | +393.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 507 | +0.362 | +177.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 507 | +0.362 | +177.09€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 555 | +0.362 | +216.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 555 | +0.362 | +216.35€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 29058 | -0.017 | +7229.39€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 29058 | -0.017 | +7229.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2263 | -0.047 | +601.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2263 | -0.047 | +601.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5341 | -0.116 | +287.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5341 | -0.116 | +287.84€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1243 | +0.221 | +1034.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1243 | +0.221 | +1034.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3903 | +0.217 | +2464.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3903 | +0.217 | +2464.68€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8201 | -0.058 | +1214.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8201 | -0.058 | +1214.67€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8107 | -0.053 | +1626.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8107 | -0.053 | +1626.17€ | 6 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 362 | +0.060 | +31.26€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 362 | +0.060 | +31.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 362 | +0.060 | +31.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 362 | +0.060 | +31.26€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1955 | +0.284 | +1669.11€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1955 | +0.284 | +1669.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1029 | +0.278 | +828.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1029 | +0.278 | +828.29€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 926 | +0.290 | +840.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 926 | +0.290 | +840.82€ | 0 | 9 |
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