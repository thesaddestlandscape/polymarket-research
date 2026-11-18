# Hipótesis automáticas — 2026-11-18 00:29 UTC
_Generado por shadow_postmortem.py sobre 1384928 resoluciones (PNL=+193018.14€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=729)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1057)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.172 (n=346)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8126` → IC=+0.268 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8126 (IC base=+0.122)

- **PATRÓN** `banda_z` > `8.346` → IC=+0.193 (n=333)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.346 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.129 (n=903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=1090)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=518)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=922)

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

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=616)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=990)

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
- **FILTRO** `restante_s_al_confirmar` < `131.33` → IC=-0.218 (n=12402)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.33
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=37208)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `124.11` → IC=-0.260 (n=1239)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.11
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3719)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.05` → IC=-0.282 (n=1256)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.05
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3768)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.68` → IC=-0.166 (n=3397)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.68
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=10192)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `152.11` → IC=-0.239 (n=3389)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.11
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=10169)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=29221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `8017.1924` → IC=+0.156 (n=2403)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8017.1924 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=25610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=30893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=23192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=8579)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6395.739` → IC=+0.141 (n=3334)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 6395.739 (IC base=+0.124)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=4717)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.379 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=2541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2959)

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

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=744)
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
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.133 (n=993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.252 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.121)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.201 (n=24242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=21514)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.228 (n=8114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=5830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.176 (n=5724)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.210 (n=2526)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.248 (n=1735)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.209)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=5398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4806)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=5826)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4477)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.258 (n=4512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=4002)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.364 (n=1545)

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
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=4703)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=4122)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.186)

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
- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **FILTRO** `libro_liquidez` < `4817.0959` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 4817.0959
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=27)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=28829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=33312)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=5025)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10689)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=15403)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=13979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.276 (n=6019)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.195 (n=4941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=11857)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=4698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=5353)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=5822)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4805)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=4792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.241 (n=6916)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=12041)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=12939)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.31` → IC=+0.141 (n=11223)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.31 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5874)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=5859)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=7388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.51` → IC=+0.143 (n=5569)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.51 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=6167)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.136 (n=7839)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.01` → IC=+0.137 (n=7396)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.01 (IC base=+0.116)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4952` → IC=+0.140 (n=19056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4952 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=19314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=13231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9756` → IC=+0.246 (n=6355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9756 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8262` → IC=+0.287 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8262 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.479` → IC=+0.190 (n=9557)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.479 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6969` → IC=+0.270 (n=5175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6969 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3043` → IC=+0.253 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3043 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7483` → IC=+0.233 (n=4592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7483 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=9332)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4748.6611` → IC=+0.152 (n=6352)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4748.6611 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.123 (n=12000)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0064 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.564` → IC=+0.145 (n=23987)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.564 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.8518` → IC=+0.188 (n=1184)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8518 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.1699` → IC=+0.194 (n=9735)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1699 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.8591` → IC=+0.195 (n=6618)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8591 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.235 (n=2422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `1.4548` → IC=+0.209 (n=16832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4548 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.229 (n=16752)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.086)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.244 (n=1353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3759` → IC=+0.213 (n=4048)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3759 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=1973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.274 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.454` → IC=+0.276 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.454 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2349` → IC=+0.255 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2349 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.8556` → IC=+0.208 (n=2590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8556 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4424` → IC=+0.210 (n=3884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4424 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2027.615` → IC=+0.210 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2027.615 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.219 (n=2510)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.248 (n=2419)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.274 (n=1209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=3779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=1661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0741` → IC=+0.281 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0741 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.966` → IC=+0.247 (n=3715)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.966 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.245 (n=3130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.253 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4477` → IC=+0.243 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4477 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.8636` → IC=+0.245 (n=2314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8636 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=4164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.240 (n=1545)

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

- **PATRÓN** `ibs_20min` > `0.897` → IC=+0.259 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.897 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1939` → IC=+0.233 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1939 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.777` → IC=+0.266 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.777 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6973` → IC=+0.231 (n=3073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6973 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.269 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4477` → IC=+0.248 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4477 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `15840.9937` → IC=+0.225 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15840.9937 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.152 (n=3740)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0067 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0808` → IC=+0.161 (n=1247)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0808 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=2674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.3606` → IC=+0.205 (n=2493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3606 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1457` → IC=+0.149 (n=3659)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1457 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.949` → IC=+0.140 (n=3417)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.949 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.151 (n=1247)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6279 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.157 (n=1371)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4453` → IC=+0.142 (n=3610)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4453 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4861)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `170.0` → IC=+0.184 (n=1193)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 170.0 (IC base=+0.134)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.202 (n=2865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.255 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.965` → IC=+0.282 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.965 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.194 (n=3848)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.226 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7284` → IC=+0.210 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7284 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=5209)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2004.2354` → IC=+0.205 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.2354 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.223 (n=3523)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.222 (n=2673)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.232 (n=1761)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=1523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.229 (n=1812)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0488` → IC=+0.272 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0488 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.771` → IC=+0.267 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.771 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.346` → IC=+0.256 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.346 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.232 (n=2572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1876.1163` → IC=+0.225 (n=1814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.1163 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.224 (n=3802)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.168 (n=227)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=5184)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.144 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.245 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1477` → IC=+0.347 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1477 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.5749` → IC=+0.343 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5749 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.19` → IC=+0.213 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.19 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.1152` → IC=+0.361 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1152 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.1677` → IC=+0.345 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1677 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.3054` → IC=+0.347 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3054 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.5458` → IC=+0.359 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5458 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `2.2831` → IC=+0.347 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2831 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.349 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.189 (n=1353)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0867 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.3493` → IC=+0.164 (n=662)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3493 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.1456` → IC=+0.158 (n=2500)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1456 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` < `1.0026` → IC=+0.161 (n=2317)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0026 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.208 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.4311` → IC=+0.172 (n=846)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.4311 (IC base=+0.057)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.192 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=835)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.131 (n=5032)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2565)

- **FILTRO** `sigma_ewma_delta_pct` > `8.302` → IC=-0.235 (n=820)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.302
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=6777)

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

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.159 (n=2565)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.2 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` > `0.2322` → IC=+0.287 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2322 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` < `0.3191` → IC=+0.288 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3191 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.294 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` > `1.0437` → IC=+0.292 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0437 (IC base=-0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.0778` → IC=+0.314 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0778 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.1243` → IC=+0.302 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1243 (IC base=-0.033)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7949` → IC=-0.158 (n=3905)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7949
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=2012)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.173 (n=1229)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4688)

- **FILTRO** `ibs_20min` > `0.7305` → IC=-0.191 (n=2044)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7305
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=6134)

- **PATRÓN** `ibs_20min` > `0.7949` → IC=+0.141 (n=2012)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.7949 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `0.731` → IC=+0.341 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.731 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `0.7093` → IC=+0.322 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7093 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` < `0.1087` → IC=+0.302 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1087 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1716` → IC=+0.310 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1716 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.5188` → IC=+0.317 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5188 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` > `1.0657` → IC=+0.284 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0657 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.273 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.2078` → IC=+0.281 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2078 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2859` → IC=+0.287 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2859 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.4775` → IC=+0.266 (n=2287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4775 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4366` → IC=+0.271 (n=2287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4366 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.192 (n=8319)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0109 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8657` → IC=+0.284 (n=11299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8657 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6913` → IC=+0.296 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6913 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.464` → IC=+0.167 (n=11201)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.464 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.280 (n=8247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.297 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6418` → IC=+0.286 (n=4819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6418 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.309 (n=14094)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 88.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.161 (n=8065)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0105 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.5179` → IC=+0.172 (n=21281)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5179 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.2702` → IC=+0.282 (n=8453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2702 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.280 (n=3592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `1.1883` → IC=+0.286 (n=2720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1883 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.328 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.4514` → IC=+0.305 (n=4035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4514 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.2694` → IC=+0.303 (n=5488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2694 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.311 (n=12087)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.086)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8084` → IC=-0.141 (n=4418)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8084
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=2277)

- **FILTRO** `ibs_20min` > `0.7076` → IC=-0.236 (n=1497)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7076
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4493)

- **FILTRO** `sigma_ewma_delta_pct` > `4.065` → IC=-0.238 (n=1270)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.065
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=4720)

- **PATRÓN** `ibs_20min` > `0.8084` → IC=+0.306 (n=2277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8084 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.952` → IC=+0.184 (n=2234)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 2.952 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.330 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.289 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.2386` → IC=+0.308 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2386 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.310 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.011)

- **PATRÓN** `ibs_20min` < `0.1714` → IC=+0.170 (n=1500)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1714 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` < `0.1512` → IC=+0.390 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1512 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.5343` → IC=+0.409 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5343 (IC base=-0.017)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.381 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1735` → IC=+0.229 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1735 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6943` → IC=+0.223 (n=2171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6943 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.245 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4154` → IC=+0.234 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4154 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.4707` → IC=+0.216 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4707 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `256.0` → IC=+0.248 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 256.0 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.261 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.1631` → IC=+0.268 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1631 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.305 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.261 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.264 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.283 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 177.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.318 (n=2305)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=3465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.577` → IC=+0.305 (n=2330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.577 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1311` → IC=+0.293 (n=3210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1311 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2535` → IC=+0.299 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2535 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2006.7416` → IC=+0.298 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.7416 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.305 (n=2187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.334 (n=2125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.306)

- **PATRÓN** `drift_60min` |x|≤ `0.1837` → IC=+0.324 (n=1402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1837 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=1226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.306)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.311 (n=1441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` < `0.0263` → IC=+0.307 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0263 (IC base=+0.306)

- **PATRÓN** `ibs_20min` > `0.1509` → IC=+0.316 (n=2124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1509 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.315 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.412` → IC=+0.306 (n=3298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.412 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` < `0.1981` → IC=+0.306 (n=3159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1981 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.3441` → IC=+0.316 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3441 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` > `2.7444` → IC=+0.321 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7444 (IC base=+0.306)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.306)

- **PATRÓN** `libro_liquidez` > `1981.4084` → IC=+0.311 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.4084 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.310 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.306)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7153` → IC=-0.179 (n=1567)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7153
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=4707)

- **PATRÓN** `dist_vwap_pct` > `0.152` → IC=+0.237 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.152 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.365` → IC=+0.238 (n=2246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.365 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.164` → IC=+0.238 (n=2255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.164 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6735` → IC=+0.235 (n=2015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6735 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.237 (n=2366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.247 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4147` → IC=+0.243 (n=2189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4147 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.254 (n=2232)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.7772` → IC=+0.261 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7772 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.3678` → IC=+0.262 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3678 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `1.1864` → IC=+0.265 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1864 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6165` → IC=+0.259 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6165 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.299 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.7842` → IC=+0.289 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7842 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.280 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.285 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.010)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7451` → IC=-0.246 (n=2569)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7451
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=2574)

- **FILTRO** `ibs_20min` > `0.6111` → IC=-0.236 (n=1216)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6111
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=3655)

- **FILTRO** `sigma_ewma_delta_pct` > `8.26` → IC=-0.269 (n=556)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.26
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=4315)

- **PATRÓN** `ibs_20min` > `0.7451` → IC=+0.314 (n=2574)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7451 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.2252` → IC=+0.344 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2252 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.43` → IC=+0.157 (n=2094)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.43 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8417` → IC=+0.348 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8417 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6934` → IC=+0.336 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6934 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.366 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7756` → IC=+0.355 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7756 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.355 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6111` → IC=+0.160 (n=3655)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.6111 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` < `0.3221` → IC=+0.273 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3221 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.736` → IC=+0.130 (n=3819)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 4.736 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` < `0.6917` → IC=+0.281 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6917 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.297 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `2.1161` → IC=+0.280 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1161 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.290 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.061)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.356 (n=2379)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=2793)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` > `0.9015` → IC=+0.362 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9015 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `0.5415` → IC=+0.338 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5415 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.813` → IC=+0.337 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.813 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `0.6308` → IC=+0.326 (n=2662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6308 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.349 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `1.5345` → IC=+0.327 (n=2296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5345 (IC base=+0.314)

- **PATRÓN** `libro_liquidez` > `2662.7821` → IC=+0.323 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2662.7821 (IC base=+0.314)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.338 (n=2399)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.314)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.332 (n=2867)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=2871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.316 (n=2871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` < `0.3853` → IC=+0.331 (n=2866)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3853 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` < `0.2482` → IC=+0.317 (n=2819)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2482 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.299` → IC=+0.325 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.299 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` < `0.7184` → IC=+0.316 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7184 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.340 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2084 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.365 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.323 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `2.1456` → IC=+0.316 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1456 (IC base=+0.314)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.220 (n=6115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1246` → IC=+0.192 (n=8061)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1246 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=19051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.537` → IC=+0.229 (n=18318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.537 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1651` → IC=+0.206 (n=6918)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1651 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.761` → IC=+0.259 (n=3585)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.761 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1759` → IC=+0.152 (n=12215)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1759 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6222` → IC=+0.152 (n=12215)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6222 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.206 (n=2647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6002` → IC=+0.184 (n=5944)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6002 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=17247)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 85.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.192 (n=8005)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.006 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.188 (n=12119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0835` → IC=+0.221 (n=6065)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0835 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=8708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.248 (n=16013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1895` → IC=+0.180 (n=13272)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1895 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.491` → IC=+0.189 (n=2873)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.491 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.382` → IC=+0.191 (n=18860)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 5.382 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1877` → IC=+0.166 (n=12898)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1877 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.221 (n=2727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6294` → IC=+0.197 (n=5782)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6294 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.200 (n=17158)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.260 (n=1004)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.255 (n=1321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.9425` → IC=+0.290 (n=2001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9425 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.47` → IC=+0.325 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.47 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.279 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.8388` → IC=+0.227 (n=1912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8388 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4385` → IC=+0.224 (n=2868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4385 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2033.8453` → IC=+0.226 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2033.8453 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.257 (n=2503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.267 (n=1671)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0986` → IC=+0.308 (n=1103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0986 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.259 (n=2589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=2285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.0575` → IC=+0.302 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0575 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.261 (n=2794)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.257 (n=2206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.275 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4471` → IC=+0.270 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4471 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.6927` → IC=+0.261 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6927 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.263 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1785.4165` → IC=+0.257 (n=1669)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1785.4165 (IC base=+0.255)

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

- **PATRÓN** `ibs_20min` > `0.2583` → IC=+0.206 (n=2788)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2583 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1885` → IC=+0.213 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1885 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.579` → IC=+0.207 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.579 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6236` → IC=+0.136 (n=930)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6236 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `1.05` → IC=+0.134 (n=1264)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.05 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.171 (n=430)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.7742` → IC=+0.131 (n=1829)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.7742 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.145 (n=914)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.134 (n=2713)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 393.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.178 (n=2645)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0059 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.247` → IC=+0.174 (n=2640)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.247 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.4512` → IC=+0.225 (n=2640)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4512 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.87` → IC=+0.180 (n=561)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.87 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.022` → IC=+0.157 (n=2619)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.022 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.162 (n=3000)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.204 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2285` → IC=+0.155 (n=3194)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.2285 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4801` → IC=+0.156 (n=2873)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4801 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.197 (n=1238)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 205.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.222 (n=2071)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.406` → IC=+0.225 (n=2730)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.406 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.219 (n=2904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.063` → IC=+0.306 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.063 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.242 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.224 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3760)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1996.5606` → IC=+0.225 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1996.5606 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.246 (n=2442)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.2476` → IC=+0.269 (n=1850)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2476 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.274 (n=1061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0404` → IC=+0.295 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0404 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.896` → IC=+0.279 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.896 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3536` → IC=+0.287 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3536 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7668` → IC=+0.241 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7668 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.253 (n=1790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1968.96` → IC=+0.249 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1968.96 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.238 (n=1844)

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

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.161 (n=2844)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0069 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4179` → IC=+0.149 (n=3229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4179 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.67` → IC=+0.188 (n=3229)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.67 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1649` → IC=+0.157 (n=3298)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1649 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.534` → IC=+0.140 (n=1107)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.534 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6851` → IC=+0.157 (n=1422)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6851 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.177 (n=484)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.791` → IC=+0.134 (n=2048)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.791 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4097` → IC=+0.135 (n=3072)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4097 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6515.1715` → IC=+0.193 (n=1464)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 6515.1715 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.155 (n=1027)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.171 (n=1126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0128 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=3471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.5952` → IC=+0.224 (n=3013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5952 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.2025` → IC=+0.189 (n=1810)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2025 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.043` → IC=+0.286 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.043 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1661` → IC=+0.130 (n=3373)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1661 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.124 (n=3444)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.7824` → IC=+0.126 (n=2182)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.7824 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2692.6508` → IC=+0.200 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2692.6508 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=1133)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 16.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.143 (n=3524)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0121 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1172` → IC=+0.164 (n=1175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1172 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.4932` → IC=+0.239 (n=3101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4932 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.221` → IC=+0.147 (n=3494)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.221 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.239` → IC=+0.145 (n=3120)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.239 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1787` → IC=+0.130 (n=3524)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1787 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.8597` → IC=+0.128 (n=2349)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.8597 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1614` → IC=+0.127 (n=3476)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1614 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.147 (n=491)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4336` → IC=+0.144 (n=1114)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4336 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4393` → IC=+0.135 (n=1114)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4393 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2591.9948` → IC=+0.191 (n=1598)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2591.9948 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.131 (n=3355)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 44.0 (IC base=+0.124)

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

- **PATRÓN** `sigma_h` > `0.0169` → IC=+0.247 (n=2098)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0169 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.6026` → IC=+0.249 (n=3146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6026 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=1409)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.301 (n=1386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `1.1462` → IC=+0.252 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1462 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.109` → IC=+0.267 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.109 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.869` → IC=+0.242 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.869 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `1.0461` → IC=+0.244 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0461 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.295 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.8384` → IC=+0.239 (n=1984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8384 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.55` → IC=+0.240 (n=2659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.55 (IC base=+0.240)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.207 (n=1597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1404` → IC=+0.173 (n=2109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1404 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.421` → IC=+0.201 (n=4279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.421 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2287` → IC=+0.176 (n=1802)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2287 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.555` → IC=+0.212 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.555 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.167 (n=2892)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8615 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.1957` → IC=+0.164 (n=1446)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1957 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.174 (n=1254)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.5265` → IC=+0.160 (n=2056)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5265 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8062` → IC=+0.159 (n=3115)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8062 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=4064)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `7292.2926` → IC=+0.191 (n=2172)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7292.2926 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.3856` → IC=+0.176 (n=3493)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.3856 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.144 (n=2257)

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

- **PATRÓN** `ibs_20min` < `0.2123` → IC=+0.197 (n=642)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.2123 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.145 (n=955)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 234.0 (IC base=+0.075)

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

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.122 (n=979)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0055 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.0885` → IC=+0.209 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0885 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.6765` → IC=+0.139 (n=646)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6765 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `7843.9331` → IC=+0.150 (n=664)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7843.9331 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.142 (n=632)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 41.0 (IC base=+0.100)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.155 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0069 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=1201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.183 (n=1135)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5385 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.9866` → IC=+0.147 (n=222)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.9866 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.883` → IC=+0.224 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.883 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.0462` → IC=+0.127 (n=1118)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0462 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.143 (n=222)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.146 (n=410)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2991.1549` → IC=+0.157 (n=423)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2991.1549 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.3611` → IC=+0.193 (n=933)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3611 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2699.4473` → IC=+0.152 (n=634)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2699.4473 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.127 (n=631)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 13.0 (IC base=+0.085)

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
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.225 (n=8048)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=25196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9684` → IC=+0.303 (n=8046)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9684 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9055` → IC=+0.216 (n=2819)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9055 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.927` → IC=+0.261 (n=5909)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.927 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2141` → IC=+0.161 (n=16258)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2141 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.212 (n=4325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6226` → IC=+0.192 (n=7856)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6226 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.201 (n=22768)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.208 (n=7457)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1501` → IC=+0.202 (n=9835)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1501 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=8393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.253 (n=19670)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.1851` → IC=+0.182 (n=14246)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1851 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.513` → IC=+0.204 (n=20778)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.513 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0536` → IC=+0.174 (n=13199)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0536 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.256 (n=3073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6209` → IC=+0.212 (n=7155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6209 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=21234)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.273 (n=1286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3718` → IC=+0.235 (n=3850)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3718 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8625` → IC=+0.294 (n=2567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8625 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.835` → IC=+0.341 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.835 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.286 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4504` → IC=+0.233 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4504 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2926` → IC=+0.237 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2926 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2024.1081` → IC=+0.238 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.1081 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.246 (n=3098)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.267 (n=3487)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.269 (n=2326)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.294 (n=1537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.268 (n=3628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.272 (n=3144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.4663` → IC=+0.287 (n=3069)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4663 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.270 (n=3181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.286 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5653` → IC=+0.272 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5653 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6533` → IC=+0.278 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6533 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1786.007` → IC=+0.268 (n=2325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1786.007 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.275 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.176 (n=1321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0032 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.151 (n=1319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.3074` → IC=+0.204 (n=3533)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3074 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.3319` → IC=+0.202 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3319 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.274` → IC=+0.168 (n=827)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.274 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6339` → IC=+0.157 (n=1319)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6339 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.0679` → IC=+0.146 (n=1793)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0679 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.186 (n=556)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.1716` → IC=+0.145 (n=3421)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.1716 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.5192` → IC=+0.148 (n=3473)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5192 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.161 (n=1704)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 239.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.170 (n=3062)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.174 (n=1159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.3199` → IC=+0.234 (n=2318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3199 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1466` → IC=+0.159 (n=3415)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1466 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.981` → IC=+0.145 (n=3152)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.981 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.0421` → IC=+0.153 (n=3059)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0421 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2209` → IC=+0.196 (n=636)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2209 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4311` → IC=+0.148 (n=3365)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4311 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7742` → IC=+0.149 (n=2243)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7742 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=4519)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.172 (n=1095)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 215.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.237 (n=1342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=3581)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.985` → IC=+0.320 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.985 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.349` → IC=+0.231 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.349 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7479` → IC=+0.240 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7479 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=4866)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2003.6763` → IC=+0.241 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2003.6763 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.249 (n=3405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.246 (n=1289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.259 (n=1702)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=1758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.064` → IC=+0.302 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.064 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.02` → IC=+0.306 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.02 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.302 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1705` → IC=+0.257 (n=2492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1705 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1875.8832` → IC=+0.253 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1875.8832 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.249 (n=3252)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=1395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3461` → IC=+0.148 (n=3674)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3461 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8802` → IC=+0.271 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8802 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1443` → IC=+0.168 (n=2069)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1443 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.026` → IC=+0.163 (n=1643)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.026 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.154 (n=2784)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8577 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2793` → IC=+0.200 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2793 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5159` → IC=+0.158 (n=1797)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5159 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1528` → IC=+0.144 (n=1850)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1528 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5735.9649` → IC=+0.238 (n=1893)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5735.9649 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.147 (n=2723)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 86.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.170 (n=3522)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0081 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4524` → IC=+0.161 (n=3521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4524 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=1304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.7036` → IC=+0.202 (n=3521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7036 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1616` → IC=+0.164 (n=3327)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1616 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.019` → IC=+0.156 (n=3070)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.019 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8555` → IC=+0.162 (n=2348)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8555 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.208 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1943` → IC=+0.154 (n=3000)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1943 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5222` → IC=+0.158 (n=3044)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5222 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6698.9455` → IC=+0.218 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6698.9455 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.166 (n=2328)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 89.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.154 (n=1418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0129 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=3017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.255 (n=2839)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0319` → IC=+0.203 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0319 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.244` → IC=+0.272 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.244 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.133 (n=2834)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8745 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.121 (n=4041)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.4849` → IC=+0.124 (n=4149)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4849 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2457.5501` → IC=+0.222 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2457.5501 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.158 (n=3505)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0111 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1417` → IC=+0.153 (n=1325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1417 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=1882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.243 (n=3501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5417 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2216` → IC=+0.151 (n=3650)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2216 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.046` → IC=+0.158 (n=3855)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 3.046 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.141 (n=3973)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1917 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2283` → IC=+0.202 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2283 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4341` → IC=+0.164 (n=1264)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4341 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2643.337` → IC=+0.215 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2643.337 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.148 (n=3823)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 49.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.258 (n=3881)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=4060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=2590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.99` → IC=+0.307 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.99 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1986` → IC=+0.252 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1986 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.087` → IC=+0.293 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.087 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.219` → IC=+0.239 (n=3880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.219 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6448` → IC=+0.244 (n=3879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6448 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.0788` → IC=+0.255 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0788 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.5029` → IC=+0.256 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5029 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2620.9731` → IC=+0.245 (n=2586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.9731 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.269 (n=1344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=4049)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1364` → IC=+0.308 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1364 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.3068` → IC=+0.249 (n=4018)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3068 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.054` → IC=+0.276 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.054 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7157` → IC=+0.245 (n=1772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7157 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2152` → IC=+0.264 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2152 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.313 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4305` → IC=+0.248 (n=3817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4305 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2978.7347` → IC=+0.246 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2978.7347 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.232 (n=6232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.5348` → IC=+0.233 (n=7083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5348 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=7127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9295` → IC=+0.262 (n=2360)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9295 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.9426` → IC=+0.226 (n=5809)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9426 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.475` → IC=+0.233 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.475 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.707` → IC=+0.231 (n=2212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.707 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.8813` → IC=+0.225 (n=3352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8813 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1039` → IC=+0.225 (n=6623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1039 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.1647` → IC=+0.233 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1647 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.235 (n=2324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=5101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3733.119` → IC=+0.232 (n=4720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3733.119 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.231 (n=1650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.5284` → IC=+0.217 (n=4948)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5284 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.217 (n=1925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2207)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.7306` → IC=+0.214 (n=4948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7306 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.6997` → IC=+0.218 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6997 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.4377` → IC=+0.203 (n=4868)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4377 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.764` → IC=+0.221 (n=4481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.764 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.2534` → IC=+0.210 (n=4566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2534 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.210 (n=4571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.5307` → IC=+0.212 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5307 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.1857` → IC=+0.218 (n=2210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1857 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.233 (n=2153)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3869` → IC=+0.187 (n=1533)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3869 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.178 (n=572)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.195 (n=676)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1382 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.7` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.835` → IC=+0.186 (n=1773)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 10.835 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.0909` → IC=+0.187 (n=1349)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.0909 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` < `0.2713` → IC=+0.177 (n=1809)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.2713 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.189 (n=468)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.191 (n=509)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.178 (n=691)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `14600.5038` → IC=+0.174 (n=695)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 14600.5038 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `694.0` → IC=+0.188 (n=1487)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 694.0 (IC base=+0.174)

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

- **PATRÓN** `drift_60min` |x|≤ `0.4679` → IC=+0.219 (n=1913)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4679 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4724` → IC=+0.223 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4724 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.1451` → IC=+0.213 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1451 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.4062` → IC=+0.224 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4062 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.309` → IC=+0.219 (n=1944)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.309 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `0.8705` → IC=+0.219 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8705 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.215 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.212 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4017` → IC=+0.230 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4017 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4928` → IC=+0.213 (n=1669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4928 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=1916)

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

- **PATRÓN** `drift_60min` |x|≤ `0.6874` → IC=+0.258 (n=916)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6874 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.265 (n=632)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.7375` → IC=+0.268 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7375 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.2622` → IC=+0.257 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2622 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.985` → IC=+0.264 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.985 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.6707` → IC=+0.260 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6707 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.1033` → IC=+0.257 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1033 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1617` → IC=+0.267 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1617 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.246 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `3989.109` → IC=+0.272 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3989.109 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.277 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.245)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.153 (n=808)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0039 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.7446` → IC=+0.186 (n=1554)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7446 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.1527` → IC=+0.147 (n=1134)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1527 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.421` → IC=+0.138 (n=509)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.421 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.614` → IC=+0.140 (n=1685)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.614 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1476` → IC=+0.143 (n=455)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1476 (IC base=+0.056)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5412` → IC=-0.122 (n=321)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5412
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=653)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.121 (n=671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0055 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.161 (n=653)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5412 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.3052` → IC=+0.190 (n=227)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3052 (IC base=+0.067)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.125 (n=299)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0036 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.0689` → IC=+0.241 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0689 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2165` → IC=+0.157 (n=132)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2165 (IC base=+0.049)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.5317` → IC=-0.138 (n=238)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5317
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=464)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.155 (n=346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0043 (IC base=+0.070)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.9316` → IC=+0.262 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9316 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1321` → IC=+0.170 (n=362)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1321 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.646` → IC=+0.187 (n=164)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.646 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.105` → IC=+0.265 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.105 (IC base=+0.033)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9778` → IC=+0.196 (n=281)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.9778 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.7478` → IC=+0.160 (n=198)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.7478 (IC base=+0.033)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.163 (n=357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0099 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.1905` → IC=+0.246 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1905 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.29` → IC=+0.136 (n=523)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.29 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.967` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.967 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `1.1218` → IC=+0.194 (n=168)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.1218 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.167 (n=133)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4591` → IC=+0.130 (n=474)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4591 (IC base=+0.087)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.123 (n=255)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.03 (IC base=+0.087)

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

- **PATRÓN** `sigma_ewma_delta_pct` < `8.416` → IC=+0.158 (n=796)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 8.416 (IC base=+0.157)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=1508)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2859.5654` → IC=+0.127 (n=767)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2859.5654 (IC base=+0.097)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=1508)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2859.5654` → IC=+0.127 (n=767)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2859.5654 (IC base=+0.097)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=272)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=272)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1198)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `liq_n` > 2.0 (IC base=+0.073)

- **PATRÓN** `liq_usd_total` > `1195.31` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `liq_usd_total` > 1195.31 (IC base=+0.073)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.073)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=49)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=71)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.068)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.425` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

- **PATRÓN** `liq_usd_total` > `5066.14` → IC=+0.131 (n=147)

  - _Acción_: Kelly boost +0.65€ cuando `liq_usd_total` > 5066.14 (IC base=+0.056)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4145)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=205)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=162)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.295 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=189)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.167 (n=94)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=98)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 26.0 (IC base=-0.022)

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

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.179)

- **PATRÓN** `liq_usd_total` > `4024.55` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 4024.55 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.211 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.198 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 14.0 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 16.0 (IC base=+0.179)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=739)

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
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1089)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1089)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1425)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1425)

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
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=321)

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
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=405)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.170 (n=101)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=118)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.139 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=124)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.149 (n=363)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=892)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.152 (n=288)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=813)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.145 (n=387)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.51 (IC base=-0.008)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.127 (n=183)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=410)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.135 (n=324)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=683)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.124 (n=698)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=371)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.121 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=402)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.134 (n=572)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=654)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.177 (n=8673)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=27216)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=9029)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=28080)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.197 (n=1614)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5057)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.143 (n=2219)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=4366)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.134 (n=3087)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.176 (n=1210)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=3721)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1273)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3922)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.195 (n=1643)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=5107)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2054)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `1746.57` → IC=+0.126 (n=2266)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1746.57 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7666` → IC=-0.152 (n=1205)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7666
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3616)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1294)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4006)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.163 (n=1667)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=5035)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2449)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2373)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3186)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4138)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1136)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=24307)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=55261)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=19286)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=60282)

- **FILTRO** `ibs_7min` < `0.2121` → IC=-0.236 (n=19891)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2121
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=59677)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=26754)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=52814)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.246 (n=24668)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=74770)

- **FILTRO** `ibs_7min` > `0.2793` → IC=-0.183 (n=24856)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2793
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74582)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=3412)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10879)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=3547)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=10744)

- **FILTRO** `ibs_7min` < `0.7093` → IC=-0.255 (n=4716)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7093
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=9575)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.280 (n=4163)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=13039)

- **FILTRO** `ibs_7min` > `0.7679` → IC=-0.211 (n=4300)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7679
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=12902)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3207)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=9949)

- **FILTRO** `ibs_7min` < `0.7125` → IC=-0.211 (n=3288)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7125
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=9868)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.202 (n=3271)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9885)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=3057)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10391)

- **FILTRO** `ibs_7min` > `0.2649` → IC=-0.192 (n=3361)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2649
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=10087)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.177 (n=3351)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=10097)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.167 (n=3269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10447)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.327 (n=3267)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=10449)

- **FILTRO** `ibs_7min` < `0.29` → IC=-0.252 (n=4526)

  - _Acción_: SKIP cuando `ibs_7min` < 0.29
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9190)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.171 (n=3368)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10348)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=4370)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=13846)

- **FILTRO** `ibs_7min` > `0.7238` → IC=-0.185 (n=4553)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7238
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=13663)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=3197)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9628)

- **FILTRO** `ibs_7min` < `0.7128` → IC=-0.201 (n=3206)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7128
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9619)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.193 (n=3202)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9623)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=3087)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=10241)

- **FILTRO** `ibs_7min` > `0.2719` → IC=-0.179 (n=3329)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=9999)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.169 (n=3313)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=10015)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=3070)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=9629)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.234 (n=4166)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8533)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.217 (n=3117)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=9582)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.200 (n=4567)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=14697)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=4152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=8729)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=3140)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9741)

- **FILTRO** `ibs_7min` < `0.7245` → IC=-0.226 (n=4250)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7245
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8631)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.192 (n=3208)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=9673)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.230 (n=4423)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=13557)

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
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=637)

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
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=919)

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
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.149 (n=728)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=1448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `441.7389` → IC=+0.160 (n=536)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 441.7389 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3591.1308` → IC=+0.144 (n=728)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3591.1308 (IC base=+0.126)

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
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.173 (n=200)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `866.7487` → IC=+0.157 (n=301)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 866.7487 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 59.0 (IC base=+0.129)

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
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.134 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=205)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.160 (n=148)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.105)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **FILTRO** `pct_vs_K` |x|> `3.395` → IC=-0.147 (n=318)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.395
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=623)

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
- **FILTRO** `T_h` > `48.8172` → IC=-0.221 (n=202)

  - _Acción_: SKIP cuando `T_h` > 48.8172
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=68)

- **FILTRO** `sigma_h` < `0.0074` → IC=-0.179 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=96)

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

- **FILTRO** `sigma_h` < `0.0088` → IC=-0.295 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=127)

- **FILTRO** `T_h` < `91.2587` → IC=-0.173 (n=111)

  - _Acción_: SKIP cuando `T_h` < 91.2587
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=58)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=460)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=507)

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
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=201)

- **PATRÓN** `streak_estiramiento` < `0.2429` → IC=+0.145 (n=74)

  - _Acción_: Kelly boost +0.72€ cuando `streak_estiramiento` < 0.2429 (IC base=+0.030)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5256)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3033)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.185 (n=1991)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0056 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2285` → IC=+0.157 (n=5965)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2285 (IC base=+0.135)

- **PATRÓN** `drift_15min` |x|≤ `1.0881` → IC=+0.135 (n=5966)

  - _Acción_: Kelly boost +0.68€ cuando `drift_15min` |x|≤ 1.0881 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.147 (n=2469)

  - _Acción_: Kelly boost +0.74€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=5532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.566` → IC=+0.213 (n=5328)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.566 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.5514` → IC=+0.123 (n=5696)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.5514 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.251` → IC=+0.235 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.251 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3284)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4429.328` → IC=+0.172 (n=1988)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4429.328 (IC base=+0.135)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=2344)

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
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` > 0.8462 (IC base=+0.051)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0141` → IC=+0.145 (n=668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0141 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.150 (n=1518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.012 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2341` → IC=+0.177 (n=1518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2341 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0581` → IC=+0.143 (n=1518)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.0581 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0933` → IC=+0.196 (n=472)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0933 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=1395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1400)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.212 (n=1356)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.3566` → IC=+0.157 (n=517)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3566 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.612` → IC=+0.178 (n=343)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 17.612 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2942.7145` → IC=+0.185 (n=688)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2942.7145 (IC base=+0.142)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.365 (n=515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.380 (n=514)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1351` → IC=+0.378 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1351 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.374 (n=816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.395 (n=771)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1542` → IC=+0.380 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1542 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.922` → IC=+0.397 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.922 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3895.4216` → IC=+0.377 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3895.4216 (IC base=+0.365)

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

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.380 (n=182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.366)

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
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.204 (n=2872)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2874)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.219 (n=2473)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3273)

- **PATRÓN** `ibs_15` > `0.6324` → IC=+0.276 (n=1282)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6324 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1129` → IC=+0.203 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1129 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` < `0.5656` → IC=+0.200 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5656 (IC base=-0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.23` → IC=+0.271 (n=1806)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.23 (IC base=-0.001)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.285 (n=5436)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` > `0.6726` → IC=+0.271 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6726 (IC base=-0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` < `0.0039` → IC=-0.218 (n=931)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=2793)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.189 (n=1728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1996)

- **FILTRO** `sigma_ewma_delta_pct` > `22.161` → IC=-0.249 (n=528)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.161
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=3196)

- **FILTRO** `libro_liquidez` < `10228.5098` → IC=-0.195 (n=1228)

  - _Acción_: SKIP cuando `libro_liquidez` < 10228.5098
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2496)

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

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.259 (n=939)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.463` → IC=+0.243 (n=2134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.463 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.8022` → IC=+0.254 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8022 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2053` → IC=+0.264 (n=967)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2053 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.242 (n=1454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3866` → IC=+0.272 (n=2134)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3866 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.391` → IC=+0.264 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.391 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.423` → IC=+0.246 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.423 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1956` → IC=-0.286 (n=340)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1956
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=1024)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.274 (n=463)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=901)

- **FILTRO** `drift_15min` |x|> `0.9529` → IC=-0.292 (n=340)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9529
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1024)

- **FILTRO** `sigma_ewma_delta_pct` > `6.088` → IC=-0.203 (n=301)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.088
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=1063)

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

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.296 (n=928)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` < `0.4621` → IC=+0.252 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4621 (IC base=-0.027)

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

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.293 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.297 (n=1299)
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

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.293 (n=1487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

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
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0797` → IC=-0.152 (n=257)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0797
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=87)

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
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=166)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.566 sube el IC de +0.135 a +0.213 en UPDOWN_GBM#15min (n=5328). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7058 sube el IC de +0.202 a +0.271 en UPDOWN_GBM#BTC#15min (n=842). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4895 sube el IC de +0.132 a +0.218 en UPDOWN_GBM#ETH#15min (n=1068). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.142 a +0.212 en UPDOWN_GBM#XRP#15min (n=1356). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6324 sube el IC de -0.085 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1282). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.375 sube el IC de -0.001 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=5436). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.066 a +0.316 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=455). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.184 a +0.285 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=77). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.148 a +0.241 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=643). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3866 sube el IC de +0.241 a +0.272 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2134). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.202 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.027 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=928). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.011 a +0.297 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1299). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
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
| ✅ BALLENAS_CONFIRMADAS_15M | 2256 | +0.082 | +223.92€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2256 | +0.082 | +223.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1846 | +0.083 | +185.38€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1846 | +0.083 | +185.38€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 94 | +0.125 | +28.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 94 | +0.125 | +28.08€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1265 | -0.018 | +69.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1265 | -0.018 | +69.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 974 | -0.035 | +49.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 974 | -0.035 | +49.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 199 | +0.057 | +23.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 199 | +0.057 | +23.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 49610 | -0.085 | -6267.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3164 | +0.087 | -299.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 46446 | -0.097 | -5967.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4958 | -0.112 | -787.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4958 | -0.112 | -787.53€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3164 | +0.087 | -299.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3164 | +0.087 | -299.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5024 | -0.107 | -954.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5024 | -0.107 | -954.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13589 | -0.043 | -1299.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13589 | -0.043 | -1299.16€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13558 | -0.113 | -1381.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13558 | -0.113 | -1381.81€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9317 | -0.138 | -1544.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9317 | -0.138 | -1544.52€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 53047 | -0.012 | +2683.49€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13675 | +0.003 | +1467.61€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 39372 | -0.017 | +1215.88€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 53047 | -0.012 | +2683.49€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13675 | +0.003 | +1467.61€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 39372 | -0.017 | +1215.88€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 200251 | +0.112 | -8359.09€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22554 | +0.179 | -731.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 927 | +0.016 | -73.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 165391 | +0.105 | -7122.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11379 | +0.094 | -431.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 27408 | +0.102 | -1975.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 82 | -0.179 | +13.53€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 27311 | +0.103 | -1977.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 37700 | +0.123 | -641.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5644 | +0.177 | -245.31€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 27377 | +0.120 | -199.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4637 | +0.081 | -174.53€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 27458 | +0.098 | -1971.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 94 | -0.115 | +14.54€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 27349 | +0.099 | -1975.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 42814 | +0.123 | -888.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10702 | +0.178 | -275.26€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 27815 | +0.106 | -538.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4285 | +0.102 | -66.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 37434 | +0.110 | -1696.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5936 | +0.198 | -251.94€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 830 | +0.041 | -19.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 28211 | +0.095 | -1234.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2457 | +0.103 | -190.45€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 27437 | +0.107 | -1185.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 96 | -0.133 | +12.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 27328 | +0.108 | -1197.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 32531 | +0.191 | -2328.27€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 32531 | +0.191 | -2328.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7373 | +0.165 | -821.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7373 | +0.165 | -821.05€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4799 | +0.197 | -178.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4799 | +0.197 | -178.52€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7209 | +0.174 | -647.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7209 | +0.174 | -647.80€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5997 | +0.252 | -207.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5997 | +0.252 | -207.06€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7074 | +0.185 | -487.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7074 | +0.185 | -487.60€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 115009 | +0.200 | -8400.74€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 115009 | +0.200 | -8400.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 19923 | +0.177 | -2316.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 19923 | +0.177 | -2316.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 18543 | +0.224 | -623.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 18543 | +0.224 | -623.58€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19737 | +0.181 | -2063.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19737 | +0.181 | -2063.60€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18694 | +0.218 | -739.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18694 | +0.218 | -739.92€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18987 | +0.204 | -1151.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18987 | +0.204 | -1151.34€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 19125 | +0.197 | -1506.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 19125 | +0.197 | -1506.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 44611 | +0.116 | +338.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 44611 | +0.116 | +338.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 22209 | +0.117 | +202.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 22209 | +0.117 | +202.68€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 22402 | +0.116 | +135.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 22402 | +0.116 | +135.73€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1996 | +0.067 | -89.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1271 | +0.079 | -25.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1562 | +0.074 | -44.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1271 | +0.079 | -25.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 90808 | +0.100 | -2041.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7347 | +0.096 | +155.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 83461 | +0.101 | -2196.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 49592 | +0.105 | -468.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7347 | +0.096 | +155.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 42245 | +0.107 | -624.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 19432 | +0.109 | -72.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 19432 | +0.109 | -72.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 21784 | +0.082 | -1499.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 21784 | +0.082 | -1499.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ GBM_LATE_15M | 61745 | +0.102 | +34567.89€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 61745 | +0.102 | +34567.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10231 | +0.225 | +8798.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10231 | +0.225 | +8798.94€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 9571 | +0.177 | +7597.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9571 | +0.177 | +7597.54€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 11055 | +0.207 | +8733.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 11055 | +0.207 | +8733.77€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 8207 | +0.060 | +2733.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8207 | +0.060 | +2733.35€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8586 | -0.027 | +2219.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8586 | -0.027 | +2219.97€ | 3 | 16 |
| ✅ GBM_LATE_15M#XRP | 14095 | -0.020 | +4484.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 14095 | -0.020 | +4484.32€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 65452 | +0.087 | +38122.85€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 65452 | +0.087 | +38122.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12685 | -0.002 | +6683.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12685 | -0.002 | +6683.40€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 14061 | +0.006 | +3835.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 14061 | +0.006 | +3835.10€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8853 | +0.295 | +10118.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8853 | +0.295 | +10118.79€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12469 | +0.016 | +3933.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12469 | +0.016 | +3933.14€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 10014 | +0.048 | +4565.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 10014 | +0.048 | +4565.06€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7370 | +0.314 | +8987.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7370 | +0.314 | +8987.36€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 48654 | +0.179 | +40405.70€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 48654 | +0.179 | +40405.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7338 | +0.239 | +6814.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7338 | +0.239 | +6814.62€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7716 | +0.141 | +5772.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7716 | +0.141 | +5772.98€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7834 | +0.224 | +6799.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7834 | +0.224 | +6799.49€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8336 | +0.130 | +6501.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8336 | +0.130 | +6501.34€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9195 | +0.122 | +7049.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9195 | +0.122 | +7049.75€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8235 | +0.233 | +7467.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8235 | +0.233 | +7467.53€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 13371 | +0.127 | +6798.06€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 13371 | +0.127 | +6798.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 674 | +0.163 | +445.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 674 | +0.163 | +445.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3507 | +0.126 | +1893.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3507 | +0.126 | +1893.38€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 508 | +0.157 | +288.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 508 | +0.157 | +288.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3897 | +0.128 | +1966.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3897 | +0.128 | +1966.24€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3555 | +0.100 | +1435.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3555 | +0.100 | +1435.44€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1230 | +0.167 | +768.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1230 | +0.167 | +768.64€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 61961 | +0.189 | +51404.01€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 61961 | +0.189 | +51404.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9780 | +0.249 | +9438.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9780 | +0.249 | +9438.37€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9907 | +0.142 | +7037.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9907 | +0.142 | +7037.12€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10511 | +0.234 | +9489.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10511 | +0.234 | +9489.75€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10259 | +0.144 | +7704.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10259 | +0.144 | +7704.30€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10963 | +0.127 | +7915.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10963 | +0.127 | +7915.47€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10541 | +0.241 | +9819.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10541 | +0.241 | +9819.00€ | 0 | 22 |
| ✅ GBM_LATE_5M | 16037 | +0.218 | +13450.76€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 16037 | +0.218 | +13450.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1792 | +0.250 | +1722.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1792 | +0.250 | +1722.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3296 | +0.210 | +2822.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3296 | +0.210 | +2822.88€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 4587 | +0.209 | +3567.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4587 | +0.209 | +3567.09€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 2891 | +0.229 | +2588.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2891 | +0.229 | +2588.47€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5573 | +0.056 | +1518.80€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 5573 | +0.056 | +1518.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1917 | +0.059 | +555.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1917 | +0.059 | +555.34€ | 1 | 6 |
| ✅ GBM_LATE_60M#ETH | 1779 | +0.055 | +577.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1779 | +0.055 | +577.65€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1877 | +0.053 | +385.82€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1877 | +0.053 | +385.82€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 737 | -0.251 | -39.31€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 737 | -0.251 | -39.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 265 | -0.257 | -21.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 265 | -0.257 | -21.57€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 268 | -0.244 | -8.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 268 | -0.244 | -8.50€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 204 | -0.248 | -9.24€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 204 | -0.248 | -9.24€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2276 | +0.086 | +571.37€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2276 | +0.086 | +571.37€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 868 | +0.069 | +192.21€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 868 | +0.069 | +192.21€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 779 | +0.057 | +149.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 779 | +0.057 | +149.00€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 629 | +0.147 | +230.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 629 | +0.147 | +230.17€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 338 | +0.318 | +413.36€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 338 | +0.318 | +413.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 338 | +0.318 | +413.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 338 | +0.318 | +413.36€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4585 | +0.097 | +1030.22€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4585 | +0.097 | +1030.22€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4585 | +0.097 | +1030.22€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4585 | +0.097 | +1030.22€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 1507 | +0.011 | +64.17€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1507 | +0.011 | +64.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 156 | +0.070 | +22.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 156 | +0.070 | +22.13€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M#BTC | 309 | -0.011 | +7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 309 | -0.011 | +7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 96 | +0.020 | +10.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 96 | +0.020 | +10.22€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 354 | +0.025 | +22.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 354 | +0.025 | +22.07€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 340 | -0.018 | +0.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 340 | -0.018 | +0.82€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 252 | +0.016 | +1.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 252 | +0.016 | +1.59€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4456 | +0.015 | +153.02€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4456 | +0.015 | +153.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 832 | +0.017 | +44.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 832 | +0.017 | +44.31€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 304 | +0.049 | +57.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 304 | +0.049 | +57.67€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1681 | +0.019 | +29.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1681 | +0.019 | +29.77€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 780 | +0.011 | +2.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 780 | +0.011 | +2.98€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 620 | -0.006 | +23.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 620 | -0.006 | +23.43€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2609 | -0.033 | -4.34€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2609 | -0.033 | -4.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 797 | -0.033 | -13.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 797 | -0.033 | -13.39€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 933 | -0.011 | +20.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 933 | -0.011 | +20.14€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 879 | -0.055 | -11.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 879 | -0.055 | -11.09€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 18548 | -0.032 | -160.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 8961 | -0.035 | -140.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 9587 | -0.029 | -19.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 649 | -0.058 | -42.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 333 | -0.037 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 316 | -0.079 | -36.19€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4902 | -0.027 | -33.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2330 | -0.025 | -10.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2572 | -0.028 | -22.51€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1738 | -0.032 | +2.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 887 | -0.043 | -24.23€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 851 | -0.019 | +26.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4223 | -0.029 | -26.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2031 | -0.029 | -10.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2192 | -0.030 | -16.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3564 | -0.023 | +52.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1734 | -0.033 | -13.39€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1830 | -0.014 | +65.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3472 | -0.045 | -113.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1646 | -0.052 | -75.99€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1826 | -0.039 | -37.34€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 72998 | -0.000 | +3951.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 72998 | -0.000 | +3951.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13256 | +0.027 | +1842.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13256 | +0.027 | +1842.73€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10126 | -0.038 | -154.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10126 | -0.038 | -154.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 13413 | +0.025 | +1517.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 13413 | +0.025 | +1517.55€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 10121 | -0.052 | -266.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 10121 | -0.052 | -266.58€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12448 | -0.004 | +351.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12448 | -0.004 | +351.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13634 | +0.019 | +660.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13634 | +0.019 | +660.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7305 | -0.053 | -112.15€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7305 | -0.053 | -112.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2044 | -0.061 | -22.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2044 | -0.061 | -22.40€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 179006 | -0.077 | +2319.15€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 179006 | -0.077 | +2319.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 31493 | -0.076 | +1842.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 31493 | -0.076 | +1842.03€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 26604 | -0.101 | -1296.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 26604 | -0.101 | -1296.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 31932 | -0.067 | +1512.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 31932 | -0.067 | +1512.81€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 26153 | -0.100 | -900.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 26153 | -0.100 | -900.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 31963 | -0.059 | +279.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 31963 | -0.059 | +279.44€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 30861 | -0.069 | +882.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 30861 | -0.069 | +882.22€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9220 | -0.035 | -183.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9220 | -0.035 | -183.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2140 | -0.047 | -28.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2140 | -0.047 | -28.53€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2670 | -0.024 | -34.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2670 | -0.024 | -34.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1293 | -0.064 | -31.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1293 | -0.064 | -31.95€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1100 | -0.035 | -37.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1100 | -0.035 | -37.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2276 | +0.122 | +927.42€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2140 | +0.126 | +914.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 499 | +0.139 | +252.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 499 | +0.139 | +252.81€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 446 | +0.114 | +150.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 446 | +0.114 | +150.76€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 400 | +0.129 | +186.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 400 | +0.129 | +186.13€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 362 | +0.143 | +188.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 362 | +0.143 | +188.84€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 433 | +0.105 | +136.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 433 | +0.105 | +136.29€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2383 | -0.021 | -37.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2383 | -0.021 | -37.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 424 | +0.009 | +22.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 424 | +0.009 | +22.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 439 | -0.049 | -30.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 439 | -0.049 | -30.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 588 | -0.049 | -45.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 588 | -0.049 | -45.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 491 | +0.003 | +7.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 491 | +0.003 | +7.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 441 | -0.012 | +8.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 441 | -0.012 | +8.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1254 | -0.046 | +109.97€ | 2 | 1 |
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
| ✅ STREAK_FADE_15M | 1005 | +0.037 | +76.14€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 1005 | +0.037 | +76.14€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 77 | +0.019 | +0.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 77 | +0.019 | +0.67€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 85 | +0.029 | +7.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 85 | +0.029 | +7.61€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 484 | +0.058 | +65.52€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 484 | +0.058 | +65.52€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3616 | -0.023 | -143.70€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3616 | -0.023 | -143.70€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 623 | -0.028 | -27.00€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 623 | -0.028 | -27.00€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 174 | -0.045 | -15.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 174 | -0.045 | -15.30€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1692 | -0.019 | -61.19€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1692 | -0.019 | -61.19€ | 2 | 0 |
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
| ✅ STRUCT_NO_15M | 12860 | +0.018 | -3.05€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12860 | +0.018 | -3.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5275 | +0.020 | +2.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5275 | +0.020 | +2.09€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4518 | +0.018 | -1.95€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4518 | +0.018 | -1.95€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3067 | +0.014 | -3.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3067 | +0.014 | -3.20€ | 1 | 0 |
| ✅ UPDOWN_GBM | 117356 | +0.059 | +11058.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 28693 | +0.077 | +5623.94€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3372 | -0.000 | +40.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 77891 | +0.062 | +5269.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7002 | -0.001 | +133.99€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10233 | +0.101 | +1799.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1827 | +0.163 | +837.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8316 | +0.089 | +963.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 26542 | +0.057 | +2338.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3861 | +0.079 | +860.77€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 978 | -0.001 | +20.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 18446 | +0.066 | +1375.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3113 | -0.004 | +80.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 144 | -0.069 | +2.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 12952 | +0.074 | +1377.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1810 | +0.151 | +747.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 11056 | +0.061 | +630.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 27556 | +0.049 | +1969.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6754 | +0.071 | +1057.32€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 946 | +0.005 | +15.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 17133 | +0.052 | +850.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2590 | +0.001 | +45.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 133 | -0.107 | -0.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 24580 | +0.040 | +1405.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7795 | +0.033 | +474.39€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 875 | -0.010 | +9.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14492 | +0.052 | +924.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1299 | +0.004 | +8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 119 | -0.145 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 15491 | +0.073 | +2169.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6646 | +0.091 | +1645.97€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8448 | +0.062 | +525.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 396 | -0.105 | -8.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1028 | +0.365 | +386.24€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1028 | +0.365 | +386.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 494 | +0.363 | +173.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 494 | +0.363 | +173.68€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 534 | +0.366 | +212.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 534 | +0.366 | +212.56€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 27535 | -0.019 | +6799.43€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 27535 | -0.019 | +6799.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2042 | -0.048 | +575.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2042 | -0.048 | +575.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5120 | -0.116 | +260.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5120 | -0.116 | +260.46€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1102 | +0.217 | +904.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1102 | +0.217 | +904.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3701 | +0.219 | +2373.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3701 | +0.219 | +2373.58€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7839 | -0.057 | +1157.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7839 | -0.057 | +1157.19€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7731 | -0.056 | +1528.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7731 | -0.056 | +1528.31€ | 4 | 6 |
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
| ✅ UPDOWN_OU_5M | 885 | -0.117 | -90.85€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 885 | -0.117 | -90.85€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 283 | -0.083 | -21.49€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 283 | -0.083 | -21.49€ | 2 | 0 |
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