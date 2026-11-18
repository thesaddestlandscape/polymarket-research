# Hipótesis automáticas — 2026-11-18 02:37 UTC
_Generado por shadow_postmortem.py sobre 1386365 resoluciones (PNL=+193402.73€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=729)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1058)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.172 (n=346)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8126` → IC=+0.268 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8126 (IC base=+0.122)

- **PATRÓN** `banda_z` > `8.339` → IC=+0.191 (n=334)

  - _Acción_: Kelly boost +0.95€ cuando `banda_z` > 8.339 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=719)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=1091)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=518)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=923)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.181 (n=296)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 64.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8183` → IC=+0.289 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8183 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.618` → IC=+0.200 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.618 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.133 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=991)

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
- **FILTRO** `ballenas_wallet_edge_medio` < `2.833` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballenas_wallet_edge_medio` < 2.833
  - _Potencial_: sin este filtro IC_bueno=+0.375 (n=6)

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
- **FILTRO** `restante_s_al_confirmar` < `131.29` → IC=-0.218 (n=12408)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.29
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=37227)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `124.12` → IC=-0.260 (n=1240)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.12
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3720)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.05` → IC=-0.282 (n=1256)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.05
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3768)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.67` → IC=-0.165 (n=3399)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.67
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=10199)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.93` → IC=-0.239 (n=3392)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.93
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=10178)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.77` → IC=-0.268 (n=2329)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.77
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=6988)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=29249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `8015.1256` → IC=+0.155 (n=2404)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8015.1256 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=25611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=30983)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=23222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=8582)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6388.5284` → IC=+0.141 (n=3336)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6388.5284 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2700)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `16274.6013` → IC=+0.180 (n=701)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 16274.6013 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.184 (n=1919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2753)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `16068.6951` → IC=+0.184 (n=710)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16068.6951 (IC base=+0.177)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=2324)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.169 (n=644)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.149 (n=1510)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.44 (IC base=+0.087)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=5317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=4721)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.379 (n=1777)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=2541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2961)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.146 (n=685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.256 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1164)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4420.281 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.250 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=745)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=471)

- **FILTRO** `libro_liquidez` < `955.8819` → IC=-0.121 (n=159)

  - _Acción_: SKIP cuando `libro_liquidez` < 955.8819
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=325)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.168 (n=471)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.55 (IC base=+0.051)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.134 (n=995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.253 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=25571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=21549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.227 (n=8121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=5830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.176 (n=5731)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.74 (IC base=+0.165)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.214 (n=3536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2348)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.248 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.208)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=5834)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4480)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.258 (n=4512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=4006)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.364 (n=1547)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=4711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=4126)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=1003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=994)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4712.9023` → IC=+0.441 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4712.9023 (IC base=+0.426)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=396)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `4814.8438` → IC=+0.432 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4814.8438 (IC base=+0.424)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=28829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=33333)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=5025)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=15416)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=13979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6024)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.195 (n=4941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=11867)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=4698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.260 (n=5825)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.216 (n=4762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4806)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=4792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5542)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.241 (n=6918)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=12058)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=12959)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.31` → IC=+0.141 (n=11236)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.31 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5884)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=5869)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=7410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.5` → IC=+0.144 (n=5559)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.5 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=6174)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=7849)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.0` → IC=+0.137 (n=7402)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.0 (IC base=+0.116)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4952` → IC=+0.140 (n=19075)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4952 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=19314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=13257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9754` → IC=+0.246 (n=6360)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9754 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.826` → IC=+0.287 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.826 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.479` → IC=+0.190 (n=9569)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.479 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6969` → IC=+0.270 (n=5181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6969 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3042` → IC=+0.252 (n=1976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3042 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7487` → IC=+0.233 (n=4599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7487 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=9338)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4748.6611` → IC=+0.152 (n=6359)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4748.6611 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.123 (n=12010)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0064 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.5638` → IC=+0.145 (n=24017)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5638 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.1702` → IC=+0.194 (n=9755)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1702 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.8591` → IC=+0.195 (n=6627)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8591 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.234 (n=2427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `1.455` → IC=+0.209 (n=16858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.455 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.229 (n=16778)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.086)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.244 (n=1353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.376` → IC=+0.213 (n=4052)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.376 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=1973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.273 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.45` → IC=+0.276 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.45 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.255 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.8555` → IC=+0.207 (n=2593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8555 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.210 (n=3888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4471)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2028.3692` → IC=+0.209 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2028.3692 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.218 (n=2515)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.248 (n=2425)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0931` → IC=+0.274 (n=1212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0931 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=3779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=1669)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0749` → IC=+0.281 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0749 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.961` → IC=+0.247 (n=3720)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.961 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.245 (n=3136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.252 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4479` → IC=+0.243 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4479 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.8636` → IC=+0.245 (n=2318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8636 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=4172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.240 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.241)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.236 (n=1156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.247 (n=1515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.8969` → IC=+0.259 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8969 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1939` → IC=+0.233 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1939 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.781` → IC=+0.266 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.781 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6973` → IC=+0.231 (n=3076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6973 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.269 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4483` → IC=+0.247 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4483 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `15840.975` → IC=+0.225 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15840.975 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.152 (n=3746)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0067 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.161 (n=1250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=2674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.3599` → IC=+0.206 (n=2498)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3599 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.149 (n=3669)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.588` → IC=+0.134 (n=599)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 10.588 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.944` → IC=+0.139 (n=3423)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.944 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.628` → IC=+0.151 (n=1249)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.628 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.157 (n=1375)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4467` → IC=+0.142 (n=3617)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4467 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4870)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `170.0` → IC=+0.185 (n=1197)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 170.0 (IC base=+0.134)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.202 (n=2867)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.255 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.96` → IC=+0.283 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.96 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.193 (n=3853)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.351` → IC=+0.226 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.351 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7284` → IC=+0.210 (n=1904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7284 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5216)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2005.4352` → IC=+0.202 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2005.4352 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.223 (n=3530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.222 (n=2677)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.3013` → IC=+0.229 (n=2673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3013 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=1523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.229 (n=1821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0488` → IC=+0.272 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0488 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.764` → IC=+0.265 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.764 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3463` → IC=+0.254 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3463 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.232 (n=2576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1958)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1876.9224` → IC=+0.225 (n=1817)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.9224 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.224 (n=3810)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.168 (n=227)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=5190)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.145 (n=702)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.245 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1477` → IC=+0.347 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1477 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.5691` → IC=+0.343 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5691 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.197` → IC=+0.214 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.197 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.1165` → IC=+0.361 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1165 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.1672` → IC=+0.346 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1672 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.3052` → IC=+0.348 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3052 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.5458` → IC=+0.359 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5458 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.347 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.349 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.0866` → IC=+0.188 (n=1355)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0866 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.3493` → IC=+0.164 (n=662)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3493 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.1457` → IC=+0.158 (n=2505)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1457 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` < `0.8296` → IC=+0.165 (n=1757)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8296 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.209 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.4311` → IC=+0.173 (n=847)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.4311 (IC base=+0.058)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.192 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=835)

- **FILTRO** `ibs_20min` > `0.1981` → IC=-0.128 (n=5094)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1981
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=2510)

- **FILTRO** `sigma_ewma_delta_pct` > `8.302` → IC=-0.235 (n=820)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.302
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=6784)

- **PATRÓN** `ibs_20min` > `0.7544` → IC=+0.175 (n=337)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7544 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.9658` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9658 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.6024` → IC=+0.268 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6024 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.917` → IC=+0.167 (n=232)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.917 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6181` → IC=+0.289 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6181 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0778` → IC=+0.286 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0778 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.293 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5342` → IC=+0.263 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5342 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.275 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.1981` → IC=+0.160 (n=2510)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1981 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` > `0.233` → IC=+0.287 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.233 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` < `0.3191` → IC=+0.288 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3191 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.294 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` > `1.043` → IC=+0.293 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.043 (IC base=-0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.1585` → IC=+0.319 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1585 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.134` → IC=+0.302 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.134 (IC base=-0.033)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7949` → IC=-0.157 (n=3909)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7949
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=2014)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.173 (n=1229)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4694)

- **FILTRO** `ibs_20min` > `0.7305` → IC=-0.190 (n=2046)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7305
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=6140)

- **PATRÓN** `ibs_20min` > `0.7949` → IC=+0.141 (n=2014)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.7949 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.73` → IC=+0.341 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.73 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.709` → IC=+0.323 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.709 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` < `0.1087` → IC=+0.302 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1087 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.314 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5191` → IC=+0.317 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5191 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.0649` → IC=+0.284 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0649 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.274 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.0613` → IC=+0.278 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0613 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2861` → IC=+0.288 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2861 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.4785` → IC=+0.265 (n=2290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4785 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.270 (n=2289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.192 (n=8325)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0109 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8657` → IC=+0.284 (n=11303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8657 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9563` → IC=+0.298 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9563 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.464` → IC=+0.167 (n=11216)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.464 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.280 (n=8251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.297 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6418` → IC=+0.286 (n=4823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6418 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=14103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.161 (n=8072)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0105 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.5172` → IC=+0.173 (n=21310)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5172 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.2707` → IC=+0.283 (n=8476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2707 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.6968` → IC=+0.281 (n=3597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6968 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `1.1879` → IC=+0.286 (n=2727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1879 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.327 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.4514` → IC=+0.306 (n=4044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4514 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.2694` → IC=+0.303 (n=5500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2694 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.311 (n=12115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.086)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8077` → IC=-0.141 (n=4423)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8077
  - _Potencial_: sin este filtro IC_bueno=+0.305 (n=2280)

- **FILTRO** `ibs_20min` > `0.7072` → IC=-0.237 (n=1499)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7072
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4499)

- **FILTRO** `sigma_ewma_delta_pct` > `4.063` → IC=-0.238 (n=1271)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.063
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=4727)

- **PATRÓN** `ibs_20min` > `0.8077` → IC=+0.305 (n=2280)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8077 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.95` → IC=+0.183 (n=2238)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 2.95 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.330 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.289 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.2386` → IC=+0.308 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2386 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.310 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.011)

- **PATRÓN** `ibs_20min` < `0.1707` → IC=+0.171 (n=1500)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1707 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` < `0.1514` → IC=+0.391 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1514 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` < `1.5356` → IC=+0.410 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5356 (IC base=-0.016)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.381 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1735` → IC=+0.229 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1735 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6943` → IC=+0.223 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6943 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.245 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4154` → IC=+0.234 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4154 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4708` → IC=+0.216 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4708 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `256.0` → IC=+0.248 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 256.0 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.262 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.1631` → IC=+0.269 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1631 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.306 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.262 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1523` → IC=+0.266 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1523 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `178.0` → IC=+0.282 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 178.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.318 (n=2306)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=3465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.577` → IC=+0.305 (n=2331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.577 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1311` → IC=+0.293 (n=3211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1311 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2535` → IC=+0.299 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2535 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2007.0492` → IC=+0.297 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.0492 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.305 (n=2187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.333 (n=2129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.306)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.324 (n=1405)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=1226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.306)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.311 (n=1449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` < `0.0272` → IC=+0.307 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0272 (IC base=+0.306)

- **PATRÓN** `ibs_20min` > `0.1513` → IC=+0.316 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1513 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.091` → IC=+0.315 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.091 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.407` → IC=+0.306 (n=3303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.407 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` < `0.1982` → IC=+0.306 (n=3166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1982 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.3444` → IC=+0.315 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3444 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` > `2.7489` → IC=+0.320 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7489 (IC base=+0.306)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.306)

- **PATRÓN** `libro_liquidez` > `1983.3` → IC=+0.313 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1983.3 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.310 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.306)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.715` → IC=-0.179 (n=1569)

  - _Acción_: SKIP cuando `ibs_20min` > 0.715
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=4713)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.237 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.365` → IC=+0.238 (n=2248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.365 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1652` → IC=+0.238 (n=2257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1652 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6735` → IC=+0.235 (n=2016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6735 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.237 (n=2368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.247 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4161` → IC=+0.243 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4161 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.254 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.7747` → IC=+0.262 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7747 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.3678` → IC=+0.263 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3678 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `1.1822` → IC=+0.267 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1822 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.299 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.7842` → IC=+0.289 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7842 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4239` → IC=+0.280 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4239 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.286 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.010)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7451` → IC=-0.245 (n=2572)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7451
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=2575)

- **FILTRO** `ibs_20min` > `0.6111` → IC=-0.236 (n=1216)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6111
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=3660)

- **FILTRO** `sigma_ewma_delta_pct` > `8.259` → IC=-0.267 (n=557)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.259
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=4319)

- **PATRÓN** `ibs_20min` > `0.7451` → IC=+0.315 (n=2575)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7451 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.2247` → IC=+0.344 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2247 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.43` → IC=+0.158 (n=2097)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.43 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.841` → IC=+0.348 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.841 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6934` → IC=+0.336 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6934 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.366 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7749` → IC=+0.355 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7749 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.355 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6111` → IC=+0.161 (n=3660)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.6111 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` < `0.3224` → IC=+0.273 (n=1942)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3224 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.728` → IC=+0.131 (n=3824)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 4.728 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` < `0.6916` → IC=+0.281 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6916 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.297 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` < `2.1161` → IC=+0.280 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1161 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.291 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.062)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.356 (n=2381)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=2797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` > `0.9014` → IC=+0.362 (n=1778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9014 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `0.2135` → IC=+0.334 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2135 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.81` → IC=+0.337 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.81 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `0.6307` → IC=+0.326 (n=2665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6307 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.349 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `1.5345` → IC=+0.327 (n=2299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5345 (IC base=+0.314)

- **PATRÓN** `libro_liquidez` > `2663.7` → IC=+0.322 (n=1777)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2663.7 (IC base=+0.314)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.337 (n=2402)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.314)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.332 (n=2872)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=2871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.315 (n=2877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` < `0.385` → IC=+0.330 (n=2871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.385 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` < `0.2488` → IC=+0.317 (n=2826)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2488 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.322 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` < `0.7184` → IC=+0.316 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7184 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.339 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2084 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.365 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.323 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `2.1452` → IC=+0.315 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1452 (IC base=+0.314)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.220 (n=6115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1246` → IC=+0.192 (n=8064)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1246 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=19051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.6533` → IC=+0.240 (n=16368)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6533 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1651` → IC=+0.206 (n=6918)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1651 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.759` → IC=+0.260 (n=3586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.759 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1757` → IC=+0.152 (n=12217)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1757 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6221` → IC=+0.152 (n=12217)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6221 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.206 (n=2647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5997` → IC=+0.184 (n=5946)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5997 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=17253)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 85.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.192 (n=8033)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.006 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.188 (n=12149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0836` → IC=+0.222 (n=6074)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0836 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=8708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.248 (n=16050)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.475` → IC=+0.189 (n=2878)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.475 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.499` → IC=+0.193 (n=16232)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.499 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1867` → IC=+0.167 (n=12922)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1867 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.220 (n=2731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6298` → IC=+0.197 (n=5794)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6298 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.201 (n=17198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.260 (n=1004)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.255 (n=1322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9423` → IC=+0.290 (n=2002)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9423 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.469` → IC=+0.324 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.469 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.278 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.8385` → IC=+0.226 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8385 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4385` → IC=+0.224 (n=2870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4385 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3331)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.258 (n=2513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.267 (n=1675)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0986` → IC=+0.308 (n=1104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0986 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.259 (n=2589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=2292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.0577` → IC=+0.301 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0577 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.277` → IC=+0.261 (n=2800)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.277 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.257 (n=2211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.273 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.269 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.6927` → IC=+0.260 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6927 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.263 (n=1793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1786.5108` → IC=+0.256 (n=1672)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1786.5108 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.195 (n=935)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0032 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0659` → IC=+0.174 (n=930)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0659 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.2579` → IC=+0.206 (n=2789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2579 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1885` → IC=+0.213 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1885 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.579` → IC=+0.207 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.579 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6236` → IC=+0.136 (n=930)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6236 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `1.05` → IC=+0.133 (n=1265)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.05 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.171 (n=430)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.7742` → IC=+0.131 (n=1829)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.7742 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.144 (n=915)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.134 (n=2714)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 393.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.178 (n=2647)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0059 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2474` → IC=+0.174 (n=2646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2474 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.4506` → IC=+0.225 (n=2644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4506 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.86` → IC=+0.181 (n=562)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.86 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.012` → IC=+0.158 (n=2623)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.012 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.163 (n=3005)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.204 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2286` → IC=+0.155 (n=3201)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.2286 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4807` → IC=+0.157 (n=2878)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4807 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.197 (n=1241)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 205.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.222 (n=2071)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.4051` → IC=+0.225 (n=2730)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4051 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.219 (n=2904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.063` → IC=+0.306 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.063 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.351` → IC=+0.242 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.351 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.224 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1996.9984` → IC=+0.224 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1996.9984 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.246 (n=2449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.2486` → IC=+0.269 (n=1855)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2486 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.274 (n=1061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0415` → IC=+0.295 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0415 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.888` → IC=+0.280 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.888 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3536` → IC=+0.285 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3536 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.242 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1786` → IC=+0.252 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1786 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1873.8054` → IC=+0.248 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1873.8054 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.238 (n=1849)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.195 (n=1014)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.180 (n=1009)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2442` → IC=+0.189 (n=3024)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2442 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1446` → IC=+0.188 (n=1711)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1446 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.187` → IC=+0.202 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.187 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.838` → IC=+0.139 (n=2016)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.838 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.176 (n=455)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5177` → IC=+0.128 (n=1305)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5177 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5013` → IC=+0.134 (n=988)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5013 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6924.3049` → IC=+0.198 (n=1371)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6924.3049 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.127 (n=2964)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 124.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.162 (n=2849)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0069 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4196` → IC=+0.150 (n=3235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4196 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.67` → IC=+0.189 (n=3235)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.67 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1653` → IC=+0.157 (n=3305)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1653 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.534` → IC=+0.141 (n=1108)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.534 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6847` → IC=+0.158 (n=1423)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6847 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.176 (n=485)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1878` → IC=+0.133 (n=2708)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1878 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.135 (n=3076)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6515.1715` → IC=+0.192 (n=1467)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6515.1715 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.156 (n=1030)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.171 (n=1126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0128 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=3084)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.5946` → IC=+0.225 (n=3015)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5946 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.202` → IC=+0.189 (n=1810)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.202 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.043` → IC=+0.286 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.043 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1661` → IC=+0.130 (n=3375)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1661 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1614` → IC=+0.124 (n=3446)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1614 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.7801` → IC=+0.126 (n=2183)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.7801 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2692.1276` → IC=+0.199 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2692.1276 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=1133)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 16.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.143 (n=3532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0121 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1173` → IC=+0.165 (n=1177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1173 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.4932` → IC=+0.239 (n=3107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4932 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2209` → IC=+0.147 (n=3503)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2209 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.232` → IC=+0.146 (n=3125)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.232 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1785` → IC=+0.130 (n=3531)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1785 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.8589` → IC=+0.127 (n=2354)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8589 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1614` → IC=+0.127 (n=3484)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1614 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.147 (n=491)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4333` → IC=+0.144 (n=1116)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4333 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4393` → IC=+0.136 (n=1116)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4393 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2591.9948` → IC=+0.191 (n=1601)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2591.9948 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.130 (n=3319)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 43.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.247 (n=3032)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1677` → IC=+0.240 (n=1334)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1677 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.233 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.797` → IC=+0.227 (n=3128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.797 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.527` → IC=+0.261 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.527 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.237 (n=3031)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.268 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4727` → IC=+0.229 (n=2959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4727 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8253` → IC=+0.230 (n=1972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8253 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2610.0476` → IC=+0.232 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2610.0476 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.249 (n=1430)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.022 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.6026` → IC=+0.249 (n=3153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6026 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=1418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.301 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `1.1432` → IC=+0.253 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1432 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.101` → IC=+0.268 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.101 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.8684` → IC=+0.242 (n=2102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8684 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `1.0453` → IC=+0.244 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0453 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.295 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.8399` → IC=+0.239 (n=1989)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8399 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.5501` → IC=+0.239 (n=2664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5501 (IC base=+0.240)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.207 (n=1607)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1404` → IC=+0.173 (n=2110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1404 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.4201` → IC=+0.201 (n=4280)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4201 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2286` → IC=+0.175 (n=1803)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2286 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.555` → IC=+0.212 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.555 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.167 (n=2894)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8615 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.1957` → IC=+0.164 (n=1446)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1957 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.174 (n=1254)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.5264` → IC=+0.160 (n=2057)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5264 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8061` → IC=+0.159 (n=3116)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8061 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=4065)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `7292.2926` → IC=+0.191 (n=2172)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7292.2926 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.177 (n=3501)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.3846 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.144 (n=2262)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 22.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.201 (n=1172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1037` → IC=+0.228 (n=516)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1037 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.223 (n=1059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.6198` → IC=+0.247 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6198 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.3136` → IC=+0.224 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3136 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.928` → IC=+0.220 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.928 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.753` → IC=+0.191 (n=1391)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 10.753 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.7034` → IC=+0.213 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7034 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1492` → IC=+0.191 (n=1235)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1492 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.0912` → IC=+0.205 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0912 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.1675` → IC=+0.203 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1675 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.4033` → IC=+0.191 (n=1151)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4033 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `13761.5829` → IC=+0.199 (n=781)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 13761.5829 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.159 (n=490)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0032 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.2123` → IC=+0.196 (n=643)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.2123 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.167 (n=632)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 168.0 (IC base=+0.075)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.232 (n=644)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1302` → IC=+0.161 (n=644)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1302 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=1516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.7791` → IC=+0.268 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7791 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.5931` → IC=+0.194 (n=312)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.5931 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.923` → IC=+0.203 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.923 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.171 (n=973)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8358 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.194 (n=263)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.7716` → IC=+0.174 (n=960)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.7716 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `7946.3404` → IC=+0.181 (n=662)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 7946.3404 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.123 (n=978)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0055 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.0884` → IC=+0.209 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0884 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.6764` → IC=+0.140 (n=646)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6764 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `7843.145` → IC=+0.151 (n=665)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7843.145 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.143 (n=634)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 41.0 (IC base=+0.100)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.155 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0069 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=1201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.183 (n=1135)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5385 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.9836` → IC=+0.147 (n=222)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.9836 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.88` → IC=+0.224 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.88 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.0461` → IC=+0.128 (n=1118)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0461 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.143 (n=222)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4112` → IC=+0.146 (n=411)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4112 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2991.1549` → IC=+0.157 (n=424)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2991.1549 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.3611` → IC=+0.194 (n=937)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3611 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2702.7324` → IC=+0.154 (n=636)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2702.7324 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.127 (n=633)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 13.0 (IC base=+0.085)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.238 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.211 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9524 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.93` → IC=+0.196 (n=110)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.93 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.559` → IC=+0.186 (n=434)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.559 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.495` → IC=+0.199 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.495 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` > `1.2169` → IC=+0.250 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2169 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.218 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `2.1215` → IC=+0.197 (n=361)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1215 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.199 (n=459)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.03 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2696.9888` → IC=+0.218 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2696.9888 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.169 (n=485)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0105 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.3406` → IC=+0.163 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3406 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.3415` → IC=+0.163 (n=324)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3415 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.157 (n=485)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.1 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.969` → IC=+0.153 (n=122)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.969 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.009` → IC=+0.153 (n=468)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.009 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2424` → IC=+0.172 (n=485)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2424 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.168 (n=450)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4792` → IC=+0.196 (n=156)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4792 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.169 (n=466)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 20.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.225 (n=8050)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=25196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9683` → IC=+0.303 (n=8050)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9683 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.905` → IC=+0.216 (n=2821)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.905 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.927` → IC=+0.261 (n=5915)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.927 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2144` → IC=+0.161 (n=16272)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2144 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.212 (n=4326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6231` → IC=+0.192 (n=7863)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6231 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.201 (n=22791)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.208 (n=7468)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1503` → IC=+0.202 (n=9855)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1503 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=8393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.253 (n=19710)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.1851` → IC=+0.182 (n=14278)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1851 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.512` → IC=+0.204 (n=20810)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.512 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0535` → IC=+0.174 (n=13219)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0535 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.256 (n=3079)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6211` → IC=+0.212 (n=7167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6211 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=21273)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.273 (n=1286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3719` → IC=+0.235 (n=3852)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3719 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8625` → IC=+0.294 (n=2569)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8625 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.835` → IC=+0.341 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.835 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.286 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4504` → IC=+0.233 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4504 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2926` → IC=+0.237 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2926 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2024.7696` → IC=+0.237 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.7696 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.245 (n=3102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.267 (n=3499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.269 (n=2329)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.294 (n=1538)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.268 (n=3628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=3152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.4663` → IC=+0.287 (n=3075)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4663 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.270 (n=3188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.286 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5656` → IC=+0.273 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5656 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6533` → IC=+0.277 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6533 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1786.645` → IC=+0.268 (n=2329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1786.645 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.275 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.176 (n=1321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0032 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.151 (n=1320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.3068` → IC=+0.204 (n=3536)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3068 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.3319` → IC=+0.202 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3319 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.274` → IC=+0.169 (n=828)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.274 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6339` → IC=+0.157 (n=1320)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6339 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.0679` → IC=+0.146 (n=1795)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0679 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2724` → IC=+0.187 (n=557)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2724 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.1719` → IC=+0.145 (n=3424)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.1719 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.5192` → IC=+0.149 (n=3476)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5192 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.161 (n=1706)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 239.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.170 (n=3065)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0817` → IC=+0.173 (n=1161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0817 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.3197` → IC=+0.235 (n=2322)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3197 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1466` → IC=+0.159 (n=3423)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1466 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.981` → IC=+0.146 (n=3157)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.981 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.043` → IC=+0.153 (n=3064)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.043 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2209` → IC=+0.196 (n=639)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2209 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.148 (n=3371)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7747` → IC=+0.149 (n=2247)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7747 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=4526)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.173 (n=1099)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 215.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.237 (n=1342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.224 (n=3587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.319 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2062` → IC=+0.230 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2062 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7479` → IC=+0.240 (n=1785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7479 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=4872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2004.4784` → IC=+0.239 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.4784 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.250 (n=3412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.245 (n=1296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1826` → IC=+0.259 (n=1706)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1826 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=1767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0641` → IC=+0.302 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0641 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.015` → IC=+0.305 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.015 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.300 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1705` → IC=+0.257 (n=2496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1705 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1978.4576` → IC=+0.254 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.4576 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.249 (n=3259)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=1395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3461` → IC=+0.148 (n=3676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3461 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8802` → IC=+0.271 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8802 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1446` → IC=+0.169 (n=2068)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1446 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.026` → IC=+0.163 (n=1645)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.026 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.153 (n=2786)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8577 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.200 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5155` → IC=+0.157 (n=1797)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5155 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1532` → IC=+0.144 (n=1851)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1532 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5747.5752` → IC=+0.238 (n=1894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5747.5752 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.147 (n=2726)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 86.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.170 (n=3529)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0081 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4524` → IC=+0.161 (n=3526)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4524 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=1304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.7033` → IC=+0.202 (n=3526)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7033 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1617` → IC=+0.164 (n=3336)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1617 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.02` → IC=+0.155 (n=3072)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.02 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8545` → IC=+0.163 (n=2351)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8545 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.206 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1935` → IC=+0.155 (n=3004)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1935 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5222` → IC=+0.158 (n=3049)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5222 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6697.0019` → IC=+0.218 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6697.0019 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.166 (n=2333)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 89.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.154 (n=1419)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0129 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=3017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.256 (n=2841)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0309` → IC=+0.203 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0309 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.242` → IC=+0.273 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.242 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.133 (n=2836)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8739 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.121 (n=4044)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.8171` → IC=+0.129 (n=2768)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8171 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2457.5501` → IC=+0.222 (n=1929)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2457.5501 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.158 (n=3510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0111 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1419` → IC=+0.153 (n=1328)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1419 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=1882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5413` → IC=+0.243 (n=3501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5413 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2215` → IC=+0.152 (n=3658)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2215 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.042` → IC=+0.158 (n=3860)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 3.042 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1905` → IC=+0.142 (n=3979)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1905 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2281` → IC=+0.201 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2281 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.164 (n=1264)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2640.7331` → IC=+0.215 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2640.7331 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.148 (n=3830)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 49.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.258 (n=3884)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=4060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.241 (n=2596)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.99` → IC=+0.307 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.99 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.252 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.085` → IC=+0.294 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.085 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.239 (n=3884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2177 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6439` → IC=+0.244 (n=3884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6439 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.254 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.5029` → IC=+0.256 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5029 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2622.0126` → IC=+0.244 (n=2589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2622.0126 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0252` → IC=+0.270 (n=1347)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0252 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=4058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1366` → IC=+0.308 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1366 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.3068` → IC=+0.249 (n=4027)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3068 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.048` → IC=+0.277 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.048 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.246 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2146` → IC=+0.264 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2146 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2859` → IC=+0.314 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2859 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.247 (n=3822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2979.4762` → IC=+0.245 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2979.4762 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.232 (n=6232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.5346` → IC=+0.233 (n=7081)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5346 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=7127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9295` → IC=+0.262 (n=2361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9295 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.9426` → IC=+0.226 (n=5810)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9426 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.473` → IC=+0.233 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.473 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.7071` → IC=+0.231 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7071 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.8815` → IC=+0.225 (n=3352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8815 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1039` → IC=+0.225 (n=6624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1039 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2362` → IC=+0.233 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2362 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.235 (n=2324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=5102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3733.119` → IC=+0.232 (n=4721)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3733.119 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.231 (n=1650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.4129` → IC=+0.220 (n=4356)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4129 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.217 (n=1925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.7306` → IC=+0.214 (n=4950)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7306 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.6996` → IC=+0.218 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6996 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.1872` → IC=+0.203 (n=4265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1872 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.764` → IC=+0.221 (n=4483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.764 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.2534` → IC=+0.210 (n=4567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2534 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.210 (n=4573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.5307` → IC=+0.212 (n=2146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5307 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.1859` → IC=+0.218 (n=2210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1859 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.233 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.208)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.278 (n=827)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0854` → IC=+0.301 (n=314)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0854 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.282 (n=480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.270 (n=945)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.1406` → IC=+0.294 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1406 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.274 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `0.8784` → IC=+0.290 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8784 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.346 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.277 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.1895` → IC=+0.270 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1895 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `12905.1815` → IC=+0.282 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12905.1815 (IC base=+0.270)

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

- **PATRÓN** `sigma_ewma_delta_pct` < `10.835` → IC=+0.185 (n=1774)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 10.835 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.187 (n=1350)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.091 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` < `0.2713` → IC=+0.177 (n=1810)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.2713 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.189 (n=468)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `2.4929` → IC=+0.180 (n=1525)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.4929 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.177 (n=692)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `14600.5038` → IC=+0.174 (n=695)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 14600.5038 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `695.0` → IC=+0.187 (n=1488)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 695.0 (IC base=+0.173)

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
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.223 (n=1914)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4679` → IC=+0.219 (n=1914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4679 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4724` → IC=+0.223 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4724 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.1451` → IC=+0.213 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1451 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.4059` → IC=+0.224 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4059 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.305` → IC=+0.219 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.305 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `0.8705` → IC=+0.219 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8705 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.215 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4017` → IC=+0.230 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4017 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4929` → IC=+0.213 (n=1669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4929 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.242 (n=510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.5091` → IC=+0.223 (n=1528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5091 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.210 (n=574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.217 (n=1092)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.0863` → IC=+0.212 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0863 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.6774` → IC=+0.215 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6774 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.422` → IC=+0.206 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.422 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.29` → IC=+0.210 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.29 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2637` → IC=+0.212 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2637 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.7215` → IC=+0.208 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7215 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.231 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.5091` → IC=+0.211 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5091 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.7739` → IC=+0.208 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7739 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `7821.1761` → IC=+0.215 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7821.1761 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.208 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.206)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.229 (n=836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.226 (n=568)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.237 (n=1267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.219 (n=1146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9863` → IC=+0.300 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9863 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.8423` → IC=+0.247 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8423 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.218` → IC=+0.253 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.218 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.6422` → IC=+0.248 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6422 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `1.2446` → IC=+0.221 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2446 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1054` → IC=+0.220 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1054 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.235 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.273 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `2.1535` → IC=+0.225 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1535 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.468` → IC=+0.218 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.468 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `4450.1082` → IC=+0.248 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4450.1082 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.256 (n=612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.6874` → IC=+0.258 (n=917)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6874 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.265 (n=633)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.7375` → IC=+0.268 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7375 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.3343` → IC=+0.256 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3343 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.985` → IC=+0.265 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.985 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.7517` → IC=+0.259 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7517 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.1033` → IC=+0.258 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1033 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1617` → IC=+0.267 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1617 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.246 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `3989.109` → IC=+0.272 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3989.109 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.277 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.245)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.153 (n=808)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0039 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.7446` → IC=+0.186 (n=1554)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7446 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.147 (n=1135)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.421` → IC=+0.138 (n=509)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.421 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.6111` → IC=+0.142 (n=1690)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.6111 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1476` → IC=+0.145 (n=457)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1476 (IC base=+0.057)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5412` → IC=-0.122 (n=321)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5412
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=654)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.121 (n=671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0055 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.160 (n=654)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5412 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.3052` → IC=+0.190 (n=227)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3052 (IC base=+0.067)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.125 (n=299)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0036 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.245 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2165` → IC=+0.157 (n=132)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2165 (IC base=+0.049)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.5298` → IC=-0.135 (n=239)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5298
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=464)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.157 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0043 (IC base=+0.070)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9316` → IC=+0.262 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9316 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1324` → IC=+0.170 (n=362)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1324 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.646` → IC=+0.187 (n=164)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.646 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.1037` → IC=+0.269 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1037 (IC base=+0.034)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9778` → IC=+0.196 (n=281)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.9778 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.7478` → IC=+0.160 (n=198)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.7478 (IC base=+0.033)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.164 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0099 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.1905` → IC=+0.247 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1905 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.29` → IC=+0.138 (n=525)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.29 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.928` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.928 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1167` → IC=+0.196 (n=169)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.1167 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.1084` → IC=+0.160 (n=189)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1084 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `1.4591` → IC=+0.131 (n=475)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4591 (IC base=+0.089)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.123 (n=255)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.03 (IC base=+0.089)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1888` → IC=-0.318 (n=97)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1888
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=294)

- **FILTRO** `dist_vwap_pct` > `0.2422` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2422
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=378)

- **FILTRO** `libro_liquidez` < `905.1558` → IC=-0.240 (n=98)

  - _Acción_: SKIP cuando `libro_liquidez` < 905.1558
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=295)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.304 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=188)

- **FILTRO** `dist_vwap_pct` > `0.4497` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4497
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=325)

- **FILTRO** `sigma_ewma_delta_pct` > `9.539` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.539
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=315)

- **FILTRO** `volumen_pendiente_norm` > `0.046` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.251 (n=223)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.300 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=65)

- **FILTRO** `ibs_20min` < `0.0864` → IC=-0.275 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0864
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=80)

- **FILTRO** `volumen_spike_ratio` < `1.6757` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6757
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=72)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=75)

- **FILTRO** `dist_vwap_pct` < `0.091` → IC=-0.282 (n=108)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.091
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

- **FILTRO** `libro_liquidez` < `5528.1887` → IC=-0.259 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 5528.1887
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.471 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=101)

- **FILTRO** `volumen_regimen` < `0.7435` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7435
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=101)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=101)

- **FILTRO** `volumen_spike_ratio` < `1.442` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.442
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=75)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.293 (n=119)

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

- **FILTRO** `sigma_ewma_delta_pct` > `4.649` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.649
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=47)

- **FILTRO** `volumen_regimen` < `0.9169` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9169
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=43)

- **FILTRO** `libro_spread` > `0.05` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.05
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=44)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2418` → IC=-0.147 (n=307)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2418
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=924)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.249 (n=356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.200 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.68` → IC=+0.193 (n=785)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.68 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.8305` → IC=+0.310 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8305 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.618` → IC=+0.173 (n=436)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.618 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.193 (n=262)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6249 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.186 (n=588)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.210 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.831` → IC=+0.126 (n=271)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 8.831 (IC base=+0.026)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7305` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7305
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=227)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.158 (n=77)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0065 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.7305` → IC=+0.129 (n=227)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.7305 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.6315` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6315 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.2471` → IC=+0.137 (n=425)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.2471 (IC base=+0.077)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.174 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.007 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.1059` → IC=+0.132 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.1059 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.170 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 18.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.140 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.7953` → IC=+0.170 (n=225)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.7953 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.157 (n=205)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.417` → IC=+0.146 (n=261)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 9.417 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6249 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.1935` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1935 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1848` → IC=+0.148 (n=268)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1848 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.7295` → IC=+0.175 (n=149)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.7295 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=217)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `1704.1785` → IC=+0.173 (n=252)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1704.1785 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.659` → IC=+0.167 (n=79)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.659 (IC base=+0.004)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2121` → IC=-0.254 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2121
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=166)

- **FILTRO** `volumen_regimen` < `0.9345` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9345
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=111)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.289 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.280 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` > `0.8571` → IC=+0.302 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8571 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` > `0.7508` → IC=+0.392 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7508 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.347 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.293 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.2102` → IC=+0.283 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2102 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.092` → IC=+0.309 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.092 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.485` → IC=+0.330 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.485 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.3472` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3472 (IC base=+0.259)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.343 (n=157)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3462` → IC=+0.340 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3462 (IC base=+0.337)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.417 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.337)

- **PATRÓN** `drift_15min` |x|≤ `2.3858` → IC=+0.365 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3858 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `1.0148` → IC=+0.381 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0148 (IC base=+0.337)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.384 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.337)

- **PATRÓN** `ballena_activa_n` < `1049.0` → IC=+0.409 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1049.0 (IC base=+0.337)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3492` → IC=+0.315 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3492 (IC base=+0.295)

- **PATRÓN** `elapsed_s` > `230.5` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.5 (IC base=+0.295)

- **PATRÓN** `drift_15min` |x|≤ `2.3232` → IC=+0.338 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3232 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.7123` → IC=+0.333 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7123 (IC base=+0.295)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.343 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.295)

- **PATRÓN** `ballena_activa_n` < `1335.0` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1335.0 (IC base=+0.295)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.343 (n=157)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3462` → IC=+0.340 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3462 (IC base=+0.337)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.417 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.337)

- **PATRÓN** `drift_15min` |x|≤ `2.3858` → IC=+0.365 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3858 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `1.0148` → IC=+0.381 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0148 (IC base=+0.337)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.384 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.337)

- **PATRÓN** `ballena_activa_n` < `1049.0` → IC=+0.409 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1049.0 (IC base=+0.337)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3492` → IC=+0.315 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3492 (IC base=+0.295)

- **PATRÓN** `elapsed_s` > `230.5` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 230.5 (IC base=+0.295)

- **PATRÓN** `drift_15min` |x|≤ `2.3232` → IC=+0.338 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3232 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.7123` → IC=+0.333 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7123 (IC base=+0.295)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.343 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.295)

- **PATRÓN** `ballena_activa_n` < `1335.0` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1335.0 (IC base=+0.295)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1511)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1511)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=272)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=272)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1211)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `liq_n` > 2.0 (IC base=+0.079)

- **PATRÓN** `liq_usd_total` > `1195.31` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `liq_usd_total` > 1195.31 (IC base=+0.079)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.204 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.079)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.079)

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

- **PATRÓN** `liq_usd_total` > `5066.14` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `liq_usd_total` > 5066.14 (IC base=+0.059)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.142 (n=93)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 46.0 (IC base=+0.059)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=24)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=269)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=4150)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=208)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=165)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.295 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=192)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.153 (n=96)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=99)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.193 (n=99)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 25.0 (IC base=-0.015)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=280)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.188)

- **PATRÓN** `liq_usd_total` > `4024.55` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 4024.55 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.211 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.208 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.188)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1629)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1583)

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
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1090)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1090)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1426)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1426)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=324)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=324)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.142 (n=107)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=232)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=394)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=443)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=322)

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
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=406)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.170 (n=101)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=120)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.139 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=126)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.148 (n=365)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=895)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.152 (n=288)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=815)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.145 (n=387)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.51 (IC base=-0.007)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.127 (n=183)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=411)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.136 (n=325)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=685)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.124 (n=701)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=373)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.124 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=402)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.134 (n=574)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=657)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.177 (n=8684)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=27226)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=9040)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=28117)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.197 (n=1617)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5060)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.142 (n=2222)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=4371)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.134 (n=3089)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.176 (n=1212)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=3721)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.176 (n=1276)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3927)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.195 (n=1645)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=5113)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2054)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `1746.57` → IC=+0.126 (n=2267)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1746.57 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7666` → IC=-0.152 (n=1205)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7666
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3617)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1296)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4013)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.163 (n=1669)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=5039)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2449)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2373)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3187)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4139)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1137)

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
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=980)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=24369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=55261)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.300 (n=19309)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=60321)

- **FILTRO** `ibs_7min` < `0.2119` → IC=-0.236 (n=19907)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2119
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=59723)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=26773)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=52857)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.246 (n=24701)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=74853)

- **FILTRO** `ibs_7min` > `0.2793` → IC=-0.183 (n=24883)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2793
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=74671)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.160 (n=3421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10879)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.320 (n=3552)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=10748)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.255 (n=4719)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=9581)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.280 (n=4169)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=13056)

- **FILTRO** `ibs_7min` > `0.7679` → IC=-0.211 (n=4305)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7679
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=12920)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.124 (n=3170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=9998)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3210)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=9958)

- **FILTRO** `ibs_7min` < `0.7124` → IC=-0.211 (n=3291)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7124
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=9877)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.202 (n=3275)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9893)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=3060)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10402)

- **FILTRO** `ibs_7min` > `0.2648` → IC=-0.192 (n=3365)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2648
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10097)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.177 (n=3354)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10108)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.168 (n=3280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10447)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.327 (n=3272)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=10455)

- **FILTRO** `ibs_7min` < `0.2895` → IC=-0.252 (n=4529)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2895
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9198)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.171 (n=3369)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10358)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=4373)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=13863)

- **FILTRO** `ibs_7min` > `0.7233` → IC=-0.185 (n=4558)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7233
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=13678)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=3201)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9634)

- **FILTRO** `ibs_7min` < `0.7126` → IC=-0.202 (n=3208)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7126
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9627)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.193 (n=3204)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=9631)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3093)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=10250)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.179 (n=3332)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10011)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.169 (n=3313)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=10030)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=3074)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=9634)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.234 (n=4172)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8536)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3118)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=9590)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.200 (n=4574)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=14713)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=4163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=8729)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=3143)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9749)

- **FILTRO** `ibs_7min` < `0.7243` → IC=-0.227 (n=4254)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7243
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8638)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.192 (n=3211)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=9681)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.230 (n=4429)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=13572)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1021)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1310)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.161 (n=178)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=639)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=920)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=342)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=459)

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
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.150 (n=729)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.131 (n=1451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 14.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `437.4823` → IC=+0.160 (n=536)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 437.4823 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3593.1498` → IC=+0.146 (n=729)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3593.1498 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.181 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 14.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `499.459` → IC=+0.155 (n=375)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 499.459 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.155 (n=256)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 9.0 (IC base=+0.139)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3993` → IC=+0.129 (n=335)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3993 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.133 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 14.0 (IC base=+0.114)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.175 (n=201)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `681.9263` → IC=+0.167 (n=265)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 681.9263 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.182 (n=108)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 59.0 (IC base=+0.130)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4187` → IC=+0.200 (n=181)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4187 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.182 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 5.0 (IC base=+0.143)

- **PATRÓN** `total_vol_5m` < `6013.826` → IC=+0.168 (n=239)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 6013.826 (IC base=+0.143)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.137 (n=298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=205)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `3589.693` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3589.693 (IC base=+0.106)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.155 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0046 (IC base=-0.032)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.283 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=-0.002)

- **PATRÓN** `pct_vs_K` |x|≤ `1.8236` → IC=+0.201 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.8236 (IC base=-0.002)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `6.4329` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.4329
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `96.5959` → IC=-0.159 (n=89)

  - _Acción_: SKIP cuando `T_h` < 96.5959
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=89)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0116` → IC=-0.246 (n=621)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0116
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=207)

- **FILTRO** `T_h` > `65.0572` → IC=-0.236 (n=554)

  - _Acción_: SKIP cuando `T_h` > 65.0572
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=274)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.191 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=570)

- **FILTRO** `T_h` > `142.427` → IC=-0.181 (n=189)

  - _Acción_: SKIP cuando `T_h` > 142.427
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=570)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.395 (n=188)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=571)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.009` → IC=-0.213 (n=176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.009
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=94)

- **FILTRO** `T_h` > `48.8172` → IC=-0.221 (n=202)

  - _Acción_: SKIP cuando `T_h` > 48.8172
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=68)

- **FILTRO** `T_h` > `143.1485` → IC=-0.194 (n=70)

  - _Acción_: SKIP cuando `T_h` > 143.1485
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=211)

- **FILTRO** `pct_vs_K` |x|> `2.3742` → IC=-0.325 (n=95)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3742
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=186)

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
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=119)

- **FILTRO** `T_h` < `67.921` → IC=-0.300 (n=78)

  - _Acción_: SKIP cuando `T_h` < 67.921
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=160)

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.195 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=173)

- **FILTRO** `pct_vs_K` |x|> `2.0379` → IC=-0.376 (n=111)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0379
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=119)

- **PATRÓN** `pct_vs_K` |x|≤ `2.0379` → IC=+0.128 (n=119)

  - _Acción_: Kelly boost +0.64€ cuando `pct_vs_K` |x|≤ 2.0379 (IC base=-0.116)

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
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=155)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.247 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=157)

- **FILTRO** `T_h` > `69.913` → IC=-0.222 (n=156)

  - _Acción_: SKIP cuando `T_h` > 69.913
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=78)

- **FILTRO** `sigma_h` > `0.0152` → IC=-0.318 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0152
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=127)

- **FILTRO** `sigma_h` < `0.0088` → IC=-0.295 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=127)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=463)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=507)

- **PATRÓN** `streak_estiramiento` < `0.293` → IC=+0.139 (n=117)

  - _Acción_: Kelly boost +0.69€ cuando `streak_estiramiento` < 0.293 (IC base=+0.015)

- **PATRÓN** `streak_estiramiento` < `0.5567` → IC=+0.178 (n=234)

  - _Acción_: Kelly boost +0.89€ cuando `streak_estiramiento` < 0.5567 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.141 (n=129)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 14.0 (IC base=+0.056)

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
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=204)

- **PATRÓN** `streak_estiramiento` < `0.2033` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.2033 (IC base=+0.028)

- **PATRÓN** `streak_estiramiento` < `0.5959` → IC=+0.155 (n=175)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.5959 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 30.0 (IC base=+0.081)

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
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

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

- **FILTRO** `streak_estiramiento` > `0.6439` → IC=-0.123 (n=59)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6439
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=21)

- **PATRÓN** `streak_estiramiento` < `0.6439` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `streak_estiramiento` < 0.6439 (IC base=-0.023)

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
- **PATRÓN** `streak_estiramiento` < `0.6279` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6279 (IC base=+0.025)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1090)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1307)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5259)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3036)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.185 (n=1991)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0056 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.2286` → IC=+0.157 (n=5969)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2286 (IC base=+0.134)

- **PATRÓN** `drift_15min` |x|≤ `1.0877` → IC=+0.135 (n=5969)

  - _Acción_: Kelly boost +0.68€ cuando `drift_15min` |x|≤ 1.0877 (IC base=+0.134)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.147 (n=2471)

  - _Acción_: Kelly boost +0.73€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=5532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.212 (n=5332)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.5513` → IC=+0.123 (n=5699)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.5513 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.241` → IC=+0.235 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.241 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3284)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4429.208` → IC=+0.172 (n=1990)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4429.208 (IC base=+0.134)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=2346)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.225 (n=741)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.245 (n=371)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2678` → IC=+0.228 (n=281)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2678 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2266` → IC=+0.211 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2266 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.231 (n=779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7058` → IC=+0.271 (n=842)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7058 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.221 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.242` → IC=+0.298 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.242 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `11825.4597` → IC=+0.218 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11825.4597 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.144 (n=1068)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0073 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.148 (n=712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0863` → IC=+0.133 (n=954)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0863 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.144 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4895` → IC=+0.218 (n=1068)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4895 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1217` → IC=+0.145 (n=669)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1217 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.6301` → IC=+0.133 (n=1213)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6301 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.075` → IC=+0.290 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.075 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6086.5636` → IC=+0.173 (n=484)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6086.5636 (IC base=+0.132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8462` → IC=+0.148 (n=598)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` > 0.8462 (IC base=+0.050)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.150 (n=1518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.012 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2345` → IC=+0.177 (n=1519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2345 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0581` → IC=+0.143 (n=1518)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.0581 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0933` → IC=+0.195 (n=473)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0933 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=1395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.5328` → IC=+0.212 (n=1357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5328 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.3571` → IC=+0.156 (n=516)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3571 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.543` → IC=+0.178 (n=343)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 17.543 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2942.7145` → IC=+0.184 (n=689)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2942.7145 (IC base=+0.142)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.365 (n=515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.380 (n=514)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1351` → IC=+0.378 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1351 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.374 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.395 (n=771)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1542` → IC=+0.380 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1542 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.922` → IC=+0.397 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.922 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `9553.1781` → IC=+0.381 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9553.1781 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.413 (n=124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1523` → IC=+0.363 (n=327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1523 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.377 (n=168)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.399 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.382 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.385 (n=371)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.3751` → IC=+0.393 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3751 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.163` → IC=+0.392 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.163 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `8157.6321` → IC=+0.385 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8157.6321 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.402 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.371 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.366)

- **PATRÓN** `drift_60min` |x|≤ `0.1066` → IC=+0.367 (n=268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1066 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1288` → IC=+0.385 (n=267)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1288 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.373 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.372 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.7632` → IC=+0.396 (n=401)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7632 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.372 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.889` → IC=+0.396 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.889 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `4207.8495` → IC=+0.380 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4207.8495 (IC base=+0.366)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.204 (n=2873)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2875)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.219 (n=2475)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3273)

- **PATRÓN** `ibs_15` > `0.6324` → IC=+0.276 (n=1282)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6324 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1129` → IC=+0.203 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1129 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` < `0.5656` → IC=+0.200 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5656 (IC base=-0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.23` → IC=+0.271 (n=1813)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.23 (IC base=-0.001)

- **PATRÓN** `ibs_15` < `0.3737` → IC=+0.285 (n=5433)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3737 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` > `0.6721` → IC=+0.271 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6721 (IC base=-0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0722` → IC=-0.246 (n=1861)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0722
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=1865)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.218 (n=931)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=2795)

- **FILTRO** `sigma_ewma_delta_pct` > `22.161` → IC=-0.249 (n=529)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.161
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=3197)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.148 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0031 (IC base=+0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2675` → IC=+0.286 (n=152)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2675 (IC base=+0.066)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.273 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.066)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.316 (n=455)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1043` → IC=+0.274 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1043 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.281 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.961` → IC=+0.142 (n=230)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 21.961 (IC base=+0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.107` → IC=+0.232 (n=69)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.107 (IC base=-0.184)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.184)

- **PATRÓN** `ibs_15` < `0.6221` → IC=+0.285 (n=77)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6221 (IC base=-0.184)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.184)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.308 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.184)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=840)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.162 (n=566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.006 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1591` → IC=+0.164 (n=566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1591 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3015` → IC=+0.195 (n=506)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3015 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.176 (n=297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.5749` → IC=+0.241 (n=643)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5749 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6363` → IC=+0.159 (n=121)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6363 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.454` → IC=+0.149 (n=682)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.454 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.264 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=840)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5050.7283` → IC=+0.168 (n=429)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5050.7283 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.259 (n=941)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.4622` → IC=+0.243 (n=2137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4622 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.8022` → IC=+0.254 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8022 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.264 (n=969)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.243 (n=1459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3855` → IC=+0.272 (n=2137)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3855 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.3906` → IC=+0.264 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3906 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.399` → IC=+0.247 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.399 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1955` → IC=-0.287 (n=341)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1955
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1024)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.275 (n=464)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=901)

- **FILTRO** `drift_15min` |x|> `0.9529` → IC=-0.293 (n=341)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9529
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1024)

- **FILTRO** `sigma_ewma_delta_pct` > `6.067` → IC=-0.203 (n=301)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.067
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.202)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.202)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.202)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.202)

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.296 (n=930)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.4621` → IC=+0.252 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4621 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1198` → IC=-0.266 (n=817)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1198
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=818)

- **FILTRO** `sigma_h` > `0.0123` → IC=-0.242 (n=1226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=409)

- **FILTRO** `drift_15min` |x|> `1.2899` → IC=-0.281 (n=408)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2899
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=1227)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1614)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0721` → IC=+0.281 (n=1154)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0721 (IC base=-0.011)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.291 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.296 (n=1300)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.7589` → IC=+0.335 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7589 (IC base=-0.011)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.144 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0068 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.150 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.286 (n=26)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 116.0 (IC base=+0.097)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.144 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0068 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.150 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.286 (n=26)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 116.0 (IC base=+0.097)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.297 (n=477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.310 (n=478)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1514` → IC=+0.283 (n=952)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1514 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2214` → IC=+0.288 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2214 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.298 (n=1298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.8372` → IC=+0.309 (n=1428)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8372 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2719` → IC=+0.311 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2719 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.806` → IC=+0.385 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.806 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `13088.9696` → IC=+0.295 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13088.9696 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.305 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.299 (n=331)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.275)

- **PATRÓN** `drift_15min` |x|≤ `0.3847` → IC=+0.275 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3847 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2702` → IC=+0.279 (n=251)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2702 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2298` → IC=+0.282 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2298 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.301 (n=695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.301 (n=753)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.309 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` < `0.559` → IC=+0.275 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.559 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.54` → IC=+0.393 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.54 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `15684.0606` → IC=+0.314 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15684.0606 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.293 (n=676)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0502` → IC=+0.320 (n=226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0502 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0654` → IC=+0.292 (n=676)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0654 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.307 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.296 (n=650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.287 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8447` → IC=+0.313 (n=676)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8447 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.309 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` < `0.6412` → IC=+0.287 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6412 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.379 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.287)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1148` → IC=-0.157 (n=231)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1148
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=114)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.143 (n=236)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=119)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.175 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=375)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.222 (n=77)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=161)

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
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

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

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
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
- **PATRÓN** `ratio` < `0.987` → IC=+0.267 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.987 (IC base=+0.134)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.356 (n=3105)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0182` → IC=+0.387 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0182 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.184 (n=273)

  - _Acción_: Kelly boost +0.92€ cuando `ratio` < 0.9922 (IC base=+0.081)

- **PATRÓN** `T_h` > `109.838` → IC=+0.324 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.838 (IC base=+0.306)

- **PATRÓN** `ratio` > `1.0155` → IC=+0.380 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0155 (IC base=+0.306)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9826` → IC=+0.371 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9826 (IC base=+0.191)

- **PATRÓN** `T_h` > `111.9922` → IC=+0.355 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9922 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0259` → IC=+0.407 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0259 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0398` → IC=+0.416 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0398 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de +0.134 a +0.212 en UPDOWN_GBM#15min (n=5332). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7058 sube el IC de +0.202 a +0.271 en UPDOWN_GBM#BTC#15min (n=842). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4895 sube el IC de +0.132 a +0.218 en UPDOWN_GBM#ETH#15min (n=1068). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5328 sube el IC de +0.142 a +0.212 en UPDOWN_GBM#XRP#15min (n=1357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6324 sube el IC de -0.085 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1282). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3737 sube el IC de -0.001 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=5433). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.066 a +0.316 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=455). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.184 a +0.285 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=77). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.148 a +0.241 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=643). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3855 sube el IC de +0.241 a +0.272 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2137). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.202 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.026 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=930). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.011 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1300). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.097 a +0.286 en UPDOWN_GBM_ETH_15M_HORA7 (n=26). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.097 a +0.286 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=26). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8372 sube el IC de +0.281 a +0.309 en UPDOWN_GBM_IBS_ALTO (n=1428). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.275 a +0.301 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=753). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8447 sube el IC de +0.287 a +0.313 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=676). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.365 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=771). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.363 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=371). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7632 sube el IC de +0.366 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=401). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2257 | +0.083 | +225.62€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2257 | +0.083 | +225.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1847 | +0.083 | +187.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1847 | +0.083 | +187.08€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 94 | +0.125 | +28.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 94 | +0.125 | +28.08€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1267 | -0.018 | +70.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1267 | -0.018 | +70.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 976 | -0.035 | +50.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 976 | -0.035 | +50.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 199 | +0.057 | +23.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 199 | +0.057 | +23.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 49635 | -0.085 | -6267.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3166 | +0.087 | -300.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 46469 | -0.097 | -5967.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4960 | -0.113 | -789.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4960 | -0.113 | -789.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3166 | +0.087 | -300.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3166 | +0.087 | -300.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5024 | -0.107 | -954.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5024 | -0.107 | -954.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13598 | -0.043 | -1302.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13598 | -0.043 | -1302.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13570 | -0.114 | -1375.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13570 | -0.114 | -1375.50€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9317 | -0.138 | -1544.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9317 | -0.138 | -1544.52€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 53108 | -0.012 | +2672.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13689 | +0.004 | +1472.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 39419 | -0.017 | +1200.74€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 53108 | -0.012 | +2672.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13689 | +0.004 | +1472.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 39419 | -0.017 | +1200.74€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 200421 | +0.112 | -8334.89€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22564 | +0.179 | -730.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 928 | +0.016 | -73.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 165545 | +0.105 | -7106.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11384 | +0.094 | -424.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 27434 | +0.102 | -1973.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 82 | -0.179 | +13.53€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 27337 | +0.103 | -1974.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 37726 | +0.123 | -641.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5644 | +0.177 | -245.31€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 27403 | +0.120 | -199.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4637 | +0.081 | -174.53€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 27483 | +0.098 | -1971.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 94 | -0.115 | +14.54€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 27374 | +0.099 | -1974.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 42850 | +0.123 | -882.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10710 | +0.178 | -274.70€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 27841 | +0.106 | -534.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4287 | +0.103 | -65.17€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 37464 | +0.111 | -1690.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5938 | +0.198 | -251.57€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 831 | +0.041 | -19.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 28236 | +0.095 | -1231.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2459 | +0.104 | -188.59€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 27464 | +0.107 | -1174.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 96 | -0.133 | +12.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 27354 | +0.108 | -1191.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 32566 | +0.191 | -2345.35€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 32566 | +0.191 | -2345.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7381 | +0.165 | -825.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7381 | +0.165 | -825.24€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4806 | +0.197 | -181.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4806 | +0.197 | -181.62€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7217 | +0.173 | -653.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7217 | +0.173 | -653.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6001 | +0.252 | -207.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6001 | +0.252 | -207.18€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7082 | +0.184 | -491.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7082 | +0.184 | -491.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1293 | +0.426 | -46.68€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1293 | +0.426 | -46.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 541 | +0.439 | -4.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 541 | +0.439 | -4.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 524 | +0.424 | -19.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 524 | +0.424 | -19.86€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 214 | +0.398 | -18.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 214 | +0.398 | -18.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 115109 | +0.200 | -8429.04€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 115109 | +0.200 | -8429.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 19941 | +0.177 | -2323.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 19941 | +0.177 | -2323.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 18559 | +0.224 | -626.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 18559 | +0.224 | -626.08€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19754 | +0.181 | -2072.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19754 | +0.181 | -2072.01€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18709 | +0.217 | -744.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18709 | +0.217 | -744.52€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 19002 | +0.204 | -1151.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 19002 | +0.204 | -1151.35€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 19144 | +0.197 | -1512.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 19144 | +0.197 | -1512.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 44654 | +0.116 | +350.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 44654 | +0.116 | +350.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 22231 | +0.117 | +209.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 22231 | +0.117 | +209.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 22423 | +0.116 | +140.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 22423 | +0.116 | +140.90€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1997 | +0.067 | -90.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1272 | +0.079 | -26.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1563 | +0.074 | -45.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1272 | +0.079 | -26.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 90903 | +0.101 | -2035.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7355 | +0.096 | +157.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 83548 | +0.101 | -2193.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 49645 | +0.105 | -468.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7355 | +0.096 | +157.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 42290 | +0.107 | -626.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 19453 | +0.110 | -63.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 19453 | +0.110 | -63.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 21805 | +0.082 | -1503.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 21805 | +0.082 | -1503.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ GBM_LATE_15M | 61818 | +0.102 | +34647.17€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 61818 | +0.102 | +34647.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10244 | +0.225 | +8804.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10244 | +0.225 | +8804.30€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 9584 | +0.177 | +7615.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9584 | +0.177 | +7615.93€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 11071 | +0.207 | +8733.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11071 | +0.207 | +8733.09€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 8217 | +0.060 | +2760.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8217 | +0.060 | +2760.16€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8593 | -0.026 | +2225.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8593 | -0.026 | +2225.59€ | 3 | 16 |
| ✅ GBM_LATE_15M#XRP | 14109 | -0.020 | +4508.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 14109 | -0.020 | +4508.10€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 65527 | +0.087 | +38199.38€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 65527 | +0.087 | +38199.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12701 | -0.002 | +6701.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12701 | -0.002 | +6701.40€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 14076 | +0.006 | +3846.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 14076 | +0.006 | +3846.58€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8863 | +0.295 | +10126.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8863 | +0.295 | +10126.35€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12484 | +0.016 | +3953.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12484 | +0.016 | +3953.13€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10023 | +0.048 | +4581.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10023 | +0.048 | +4581.04€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7380 | +0.314 | +8990.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7380 | +0.314 | +8990.89€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 48709 | +0.179 | +40446.77€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 48709 | +0.179 | +40446.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7348 | +0.239 | +6818.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7348 | +0.239 | +6818.10€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7724 | +0.141 | +5775.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7724 | +0.141 | +5775.44€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7844 | +0.224 | +6807.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7844 | +0.224 | +6807.01€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8343 | +0.130 | +6510.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8343 | +0.130 | +6510.19€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9206 | +0.122 | +7062.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9206 | +0.122 | +7062.82€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8244 | +0.233 | +7473.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8244 | +0.233 | +7473.21€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 13383 | +0.127 | +6812.49€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 13383 | +0.127 | +6812.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 674 | +0.163 | +445.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 674 | +0.163 | +445.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3509 | +0.126 | +1902.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3509 | +0.126 | +1902.98€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 508 | +0.157 | +288.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 508 | +0.157 | +288.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3900 | +0.128 | +1967.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3900 | +0.128 | +1967.16€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3562 | +0.100 | +1439.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3562 | +0.100 | +1439.34€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1230 | +0.167 | +768.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1230 | +0.167 | +768.64€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 62038 | +0.189 | +51510.77€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 62038 | +0.189 | +51510.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9792 | +0.249 | +9445.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9792 | +0.249 | +9445.78€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9919 | +0.142 | +7073.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9919 | +0.142 | +7073.56€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10526 | +0.234 | +9491.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10526 | +0.234 | +9491.11€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10270 | +0.145 | +7737.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10270 | +0.145 | +7737.99€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10975 | +0.127 | +7941.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10975 | +0.127 | +7941.89€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10556 | +0.241 | +9820.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10556 | +0.241 | +9820.44€ | 0 | 22 |
| ✅ GBM_LATE_5M | 16040 | +0.218 | +13449.89€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 16040 | +0.218 | +13449.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1792 | +0.250 | +1722.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1792 | +0.250 | +1722.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3297 | +0.210 | +2820.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3297 | +0.210 | +2820.84€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 4588 | +0.209 | +3567.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4588 | +0.209 | +3567.81€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 2892 | +0.229 | +2588.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2892 | +0.229 | +2588.92€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5582 | +0.056 | +1524.00€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 5582 | +0.056 | +1524.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1919 | +0.059 | +554.09€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1919 | +0.059 | +554.09€ | 1 | 6 |
| ✅ GBM_LATE_60M#ETH | 1781 | +0.055 | +577.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1781 | +0.055 | +577.03€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1879 | +0.054 | +389.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1879 | +0.054 | +389.16€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 737 | -0.251 | -39.31€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 737 | -0.251 | -39.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 265 | -0.257 | -21.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 265 | -0.257 | -21.57€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 268 | -0.244 | -8.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 268 | -0.244 | -8.50€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 204 | -0.248 | -9.24€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 204 | -0.248 | -9.24€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2276 | +0.086 | +571.37€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2276 | +0.086 | +571.37€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 868 | +0.069 | +192.21€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 868 | +0.069 | +192.21€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 779 | +0.057 | +149.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 779 | +0.057 | +149.00€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 629 | +0.147 | +230.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 629 | +0.147 | +230.17€ | 2 | 10 |
| ✅ LATE_WINDOW_5MIN | 338 | +0.318 | +413.36€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 338 | +0.318 | +413.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 338 | +0.318 | +413.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 338 | +0.318 | +413.36€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4592 | +0.096 | +1025.85€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4592 | +0.096 | +1025.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4592 | +0.096 | +1025.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4592 | +0.096 | +1025.85€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1520 | +0.013 | +71.93€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1520 | +0.013 | +71.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 158 | +0.075 | +24.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 158 | +0.075 | +24.35€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 309 | -0.011 | +7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 309 | -0.011 | +7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 98 | +0.030 | +13.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 98 | +0.030 | +13.56€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#ETH | 358 | +0.028 | +23.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 358 | +0.028 | +23.83€ | 1 | 3 |
| ✅ LIQUIDACIONES_15M#SOL | 340 | -0.018 | +0.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 340 | -0.018 | +0.82€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 257 | +0.017 | +2.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 257 | +0.017 | +2.02€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4464 | +0.015 | +156.31€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4464 | +0.015 | +156.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 240 | +0.004 | -5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 240 | +0.004 | -5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 835 | +0.015 | +42.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 835 | +0.015 | +42.78€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 307 | +0.053 | +63.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 307 | +0.053 | +63.51€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1681 | +0.019 | +29.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1681 | +0.019 | +29.77€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 781 | +0.011 | +2.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 781 | +0.011 | +2.47€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 620 | -0.006 | +23.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 620 | -0.006 | +23.43€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2611 | -0.033 | -4.30€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2611 | -0.033 | -4.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 797 | -0.033 | -13.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 797 | -0.033 | -13.39€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 934 | -0.012 | +19.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 934 | -0.012 | +19.63€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 880 | -0.054 | -10.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 880 | -0.054 | -10.53€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 18603 | -0.032 | -168.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 8988 | -0.035 | -140.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 9615 | -0.029 | -27.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 652 | -0.057 | -40.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 334 | -0.036 | -4.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 318 | -0.078 | -36.09€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4916 | -0.027 | -31.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2338 | -0.025 | -10.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2578 | -0.028 | -21.49€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1742 | -0.032 | +0.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 889 | -0.044 | -26.38€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 853 | -0.019 | +27.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4231 | -0.030 | -29.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2036 | -0.029 | -10.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2195 | -0.030 | -19.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3578 | -0.024 | +47.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1739 | -0.033 | -11.60€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1839 | -0.015 | +59.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3484 | -0.045 | -114.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1652 | -0.052 | -77.88€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1832 | -0.039 | -36.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 73067 | -0.000 | +3979.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 73067 | -0.000 | +3979.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13270 | +0.027 | +1848.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13270 | +0.027 | +1848.56€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10136 | -0.038 | -153.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10136 | -0.038 | -153.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 13423 | +0.026 | +1528.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 13423 | +0.026 | +1528.98€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10131 | -0.052 | -264.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10131 | -0.052 | -264.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12459 | -0.004 | +352.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12459 | -0.004 | +352.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13648 | +0.019 | +667.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13648 | +0.019 | +667.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7306 | -0.053 | -111.61€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7306 | -0.053 | -111.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2045 | -0.061 | -21.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2045 | -0.061 | -21.86€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 94 | -0.021 | -0.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 94 | -0.021 | -0.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 817 | -0.117 | -33.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 817 | -0.117 | -33.11€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2213 | -0.068 | -14.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2213 | -0.068 | -14.56€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 179184 | -0.077 | +2299.29€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 179184 | -0.077 | +2299.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 31525 | -0.076 | +1842.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 31525 | -0.076 | +1842.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 26630 | -0.101 | -1310.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 26630 | -0.101 | -1310.08€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 31963 | -0.067 | +1518.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 31963 | -0.067 | +1518.07€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 26178 | -0.100 | -906.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 26178 | -0.100 | -906.55€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 31995 | -0.059 | +276.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 31995 | -0.059 | +276.96€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 30893 | -0.069 | +878.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 30893 | -0.069 | +878.72€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9223 | -0.035 | -181.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9223 | -0.035 | -181.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2142 | -0.046 | -27.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2142 | -0.046 | -27.40€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2671 | -0.024 | -33.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2671 | -0.024 | -33.78€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1293 | -0.064 | -31.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1293 | -0.064 | -31.95€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1100 | -0.035 | -37.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1100 | -0.035 | -37.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2279 | +0.122 | +933.24€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2143 | +0.127 | +920.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 499 | +0.139 | +252.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 499 | +0.139 | +252.81€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 446 | +0.114 | +150.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 446 | +0.114 | +150.76€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 401 | +0.130 | +188.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 401 | +0.130 | +188.13€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 362 | +0.143 | +188.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 362 | +0.143 | +188.84€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 435 | +0.106 | +140.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 435 | +0.106 | +140.11€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2385 | -0.021 | -37.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2385 | -0.021 | -37.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 424 | +0.009 | +22.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 424 | +0.009 | +22.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 440 | -0.050 | -31.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 440 | -0.050 | -31.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 589 | -0.048 | -44.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 589 | -0.048 | -44.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 491 | +0.003 | +7.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 491 | +0.003 | +7.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 441 | -0.012 | +8.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 441 | -0.012 | +8.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1254 | -0.046 | +109.97€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 582 | -0.075 | +11.32€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 453 | -0.074 | +35.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 440 | -0.016 | +62.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 319 | +0.005 | +71.63€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 232 | -0.030 | +35.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 196 | -0.020 | +33.93€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 968 | -0.037 | +140.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1587 | -0.187 | -40.03€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 622 | -0.176 | -13.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 551 | -0.173 | -9.94€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 71 | -0.199 | -3.91€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 531 | -0.198 | -32.05€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 468 | -0.206 | -38.69€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 63 | -0.131 | +6.63€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 434 | -0.188 | +5.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 403 | -0.184 | +4.23€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 31 | -0.227 | +1.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1422 | -0.188 | -44.40€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 1008 | +0.037 | +75.60€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1008 | +0.037 | +75.60€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 77 | +0.019 | +0.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 77 | +0.019 | +0.67€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 487 | +0.056 | +64.98€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 487 | +0.056 | +64.98€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3618 | -0.023 | -142.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3618 | -0.023 | -142.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 623 | -0.028 | -27.00€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 623 | -0.028 | -27.00€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 174 | -0.045 | -15.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 174 | -0.045 | -15.30€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1694 | -0.019 | -60.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1694 | -0.019 | -60.17€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 126 | -0.031 | -11.46€ | 3 | 1 |
| ✅ STREAK_FADE_60M#60min | 126 | -0.031 | -11.46€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 46 | -0.062 | -3.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 46 | -0.062 | -3.71€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 80 | -0.012 | -7.74€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 80 | -0.012 | -7.74€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11598 | +0.013 | +66.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11598 | +0.013 | +66.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2997 | +0.018 | +23.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2997 | +0.018 | +23.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3071 | +0.014 | +28.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3071 | +0.014 | +28.23€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2937 | +0.008 | -4.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2937 | +0.008 | -4.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2593 | +0.014 | +19.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2593 | +0.014 | +19.31€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12870 | +0.018 | +0.68€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12870 | +0.018 | +0.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5278 | +0.021 | +3.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5278 | +0.021 | +3.53€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4522 | +0.019 | -0.10€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4522 | +0.019 | -0.10€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3070 | +0.014 | -2.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3070 | +0.014 | -2.75€ | 1 | 0 |
| ✅ UPDOWN_GBM | 117555 | +0.059 | +11082.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 28744 | +0.077 | +5635.70€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3378 | -0.000 | +40.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 78027 | +0.062 | +5283.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7008 | -0.001 | +132.83€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10260 | +0.101 | +1802.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1837 | +0.163 | +842.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8333 | +0.088 | +962.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 26574 | +0.057 | +2340.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3863 | +0.079 | +859.75€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 980 | -0.001 | +20.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 18471 | +0.066 | +1378.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3116 | -0.004 | +79.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 144 | -0.069 | +2.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 12987 | +0.074 | +1388.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1819 | +0.152 | +753.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11082 | +0.062 | +635.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 27598 | +0.050 | +1973.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6762 | +0.072 | +1059.48€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 948 | +0.005 | +15.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 17162 | +0.052 | +853.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2593 | +0.001 | +45.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 133 | -0.107 | -0.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 24616 | +0.040 | +1408.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7807 | +0.033 | +474.64€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 877 | -0.010 | +9.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14514 | +0.052 | +926.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1299 | +0.004 | +8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 119 | -0.145 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 15518 | +0.073 | +2170.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6656 | +0.091 | +1645.15€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8465 | +0.062 | +527.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 396 | -0.105 | -8.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1028 | +0.365 | +386.24€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1028 | +0.365 | +386.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 494 | +0.363 | +173.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 494 | +0.363 | +173.68€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 534 | +0.366 | +212.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 534 | +0.366 | +212.56€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 27579 | -0.019 | +6831.14€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 27579 | -0.019 | +6831.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2052 | -0.048 | +578.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2052 | -0.048 | +578.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5122 | -0.116 | +267.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5122 | -0.116 | +267.07€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1111 | +0.218 | +913.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1111 | +0.218 | +913.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3706 | +0.220 | +2377.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3706 | +0.220 | +2377.95€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7848 | -0.057 | +1158.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7848 | -0.057 | +1158.60€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7740 | -0.055 | +1535.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7740 | -0.055 | +1535.00€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 342 | +0.058 | +32.99€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 342 | +0.058 | +32.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 342 | +0.058 | +32.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 342 | +0.058 | +32.99€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1904 | +0.281 | +1610.71€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1904 | +0.281 | +1610.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1003 | +0.275 | +799.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1003 | +0.275 | +799.08€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 901 | +0.287 | +811.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 901 | +0.287 | +811.64€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 886 | -0.117 | -91.36€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 886 | -0.117 | -91.36€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 284 | -0.084 | -22.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 284 | -0.084 | -22.00€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 103 | -0.195 | -15.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 103 | -0.195 | -15.02€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 116 | -0.178 | -4.99€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 116 | -0.178 | -4.99€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 5094 | +0.295 | +2244.31€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1966 | +0.251 | +262.08€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1973 | +0.289 | +827.16€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1155 | +0.382 | +1155.07€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.022 n=1440 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1440 IC=+0.022 PNL=+69.52€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 840 celda(s) pasan gate riguroso completo de 3008 evaluadas (n>=40) y 4117 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=7803 IC=+0.033 PNL=+474.68€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1973/15 IC=+0.289 PNL=+827.16€ | BTC: n=1966/15 IC=+0.251 PNL=+262.08€ | SOL: n=1155/15 IC=+0.382 PNL=+1155.07€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.135 n=1105/60 | contraria IC=+0.183 n=1167 | gap=-0.049 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=626, boost estimado=+0.010. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2591/40 IC=+0.001 PNL=+45.36€ | BTC#60min: n=3114/40 IC=-0.004 PNL=+79.58€ | SOL#60min: n=1299/40 IC=+0.004 PNL=+8.03€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=788475 | tras_1loss IC=+0.102 n=596996 | tras_2loss IC=+0.072 n=237757/40 | gap=-0.028 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.154 > 0.08 con n=1171 PNL=+679.20€
  - _Datos_: n=1171 IC=+0.154 PNL=+679.20€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.08 con n=1410 PNL=+646.23€
  - _Datos_: n=1410 IC=+0.128 PNL=+646.23€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.08 con n=90 PNL=+34.62€
  - _Datos_: n=90 IC=+0.120 PNL=+34.62€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=4154 PNL=+2347.31€
  - _Datos_: n=4154 IC=+0.335 PNL=+2347.31€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1189 IC=+0.063 PNL=+115.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1189 IC=+0.063 PNL=+115.28€

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
  - _Estado_: n=4606 IC=-0.003 PNL=-33.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4606 IC=-0.003 PNL=-33.44€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2398 IC=+0.003 PNL=+166.40€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2398 IC=+0.003 PNL=+166.40€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1440 IC=+0.022 PNL=+69.52€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1440 IC=+0.022 PNL=+69.52€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.134 > 0.1 con n=7957 PNL=+3829.86€
  - _Datos_: n=7957 IC=+0.134 PNL=+3829.86€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3862 IC=+0.079 PNL=+860.26€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3862 IC=+0.079 PNL=+860.26€

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
  - _Estado_: n=1553 IC=+0.043 PNL=+130.93€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1553 IC=+0.043 PNL=+130.93€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=195 IC=-0.028 PNL=-6.26€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=195 IC=-0.028 PNL=-6.26€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.318 n=338) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=338 IC=+0.318 PNL=+413.36€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.02 con n=1333 PNL=+551.13€
  - _Datos_: n=1333 IC=+0.121 PNL=+551.13€

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
  - _Estado_: n=48266 IC=+0.070 PNL=+6441.14€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=48266 IC=+0.070 PNL=+6441.14€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=800 PNL=+115.80€
  - _Datos_: n=800 IC=-0.137 PNL=+115.80€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4628 IC=+0.068 PNL=+575.24€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4628 IC=+0.068 PNL=+575.24€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=201 IC=-0.081 PNL=+2.01€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=201 IC=-0.081 PNL=+2.01€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1245 IC=+0.095 PNL=+302.66€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1245 IC=+0.095 PNL=+302.66€

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
  - _Estado_: n=46907 IC=-0.137 PNL=+2889.08€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=46907 IC=-0.137 PNL=+2889.08€

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
  - _Estado_: n=4990 IC=+0.134 PNL=+3385.06€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4990 IC=+0.134 PNL=+3385.06€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=12179 IC=+0.057 PNL=+1032.36€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12179 IC=+0.057 PNL=+1032.36€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=5050 PNL=+2851.05€
  - _Datos_: n=5050 IC=+0.102 PNL=+2851.05€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.221 < -0.1 con n=5108 PNL=-430.38€
  - _Datos_: n=5108 IC=-0.221 PNL=-430.38€

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
  - _Estado_: n=127 IC=+0.066 PNL=+22.07€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=127 IC=+0.066 PNL=+22.07€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2331) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2331 IC=+0.096 PNL=+465.57€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.415 n=692) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=692 IC=+0.415 PNL=+1016.23€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=19931 IC=+0.177 PNL=-2318.16€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=19931 IC=+0.177 PNL=-2318.16€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.233 > 0.1 con n=327 PNL=+228.95€
  - _Datos_: n=327 IC=+0.233 PNL=+228.95€
