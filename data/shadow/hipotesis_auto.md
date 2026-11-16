# Hipótesis automáticas — 2026-11-16 16:48 UTC
_Generado por shadow_postmortem.py sobre 1365536 resoluciones (PNL=+189668.94€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=729)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=1049)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.182 (n=331)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 62.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8127` → IC=+0.266 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8127 (IC base=+0.122)

- **PATRÓN** `banda_z` > `8.423` → IC=+0.194 (n=331)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.423 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=1083)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=518)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=914)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.181 (n=296)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 64.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8124` → IC=+0.269 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8124 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.629` → IC=+0.203 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.629 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.133 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=611)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=983)

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
- **FILTRO** `restante_s_al_confirmar` < `131.5` → IC=-0.218 (n=12305)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.5
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=36924)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `124.95` → IC=-0.256 (n=1224)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.95
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3674)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.11` → IC=-0.281 (n=1251)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.11
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3754)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.9` → IC=-0.167 (n=3376)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.9
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=10130)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.78` → IC=-0.239 (n=3358)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.78
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=10075)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.32` → IC=-0.268 (n=2316)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.32
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6951)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=28936)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `8081.2707` → IC=+0.155 (n=2383)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8081.2707 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=25068)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=30579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=22901)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8518)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6401.9564` → IC=+0.143 (n=3307)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 6401.9564 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2694)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `16274.6013` → IC=+0.181 (n=700)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 16274.6013 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2747)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16068.6951` → IC=+0.185 (n=709)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16068.6951 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=2297)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=634)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.150 (n=1489)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.44 (IC base=+0.087)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=5261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=4682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.374 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.206 (n=2508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.145 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.259 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=1148)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.250 (n=970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1443)
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
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=469)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.167 (n=469)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.55 (IC base=+0.050)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.133 (n=984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.255 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=25237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=21316)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.227 (n=7991)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=5753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.176 (n=5674)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.74 (IC base=+0.166)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.212 (n=3478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2310)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.248 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.207)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=5618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=5755)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4417)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=3973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1515)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=4659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1818)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=990)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4669.4566` → IC=+0.441 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4669.4566 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12510.8319` → IC=+0.445 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12510.8319 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.440 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `4774.0338` → IC=+0.425 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4774.0338 (IC base=+0.423)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.401 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.413 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.398)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=32928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=32954)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=4926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.205 (n=7026)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=13798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=4582)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.184 (n=13830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.198 (n=11698)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=5362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=5756)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=12561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.255 (n=4759)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=5481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.241 (n=6843)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=11883)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=12706)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.31` → IC=+0.140 (n=11022)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.31 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5793)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.142 (n=5750)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.53` → IC=+0.142 (n=5494)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.53 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=6090)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.136 (n=7704)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `3.06` → IC=+0.136 (n=7303)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.06 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.306 (n=1442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `4000.2748` → IC=+0.295 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4000.2748 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.294 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.370 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.282)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=1029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.394 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.296)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.438 (n=322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.433 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.450 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.440 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.440 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.442)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4926` → IC=+0.139 (n=18759)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4926 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=18989)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=13077)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.976` → IC=+0.246 (n=6252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.976 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8298` → IC=+0.286 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8298 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.49` → IC=+0.188 (n=9407)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.49 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.268 (n=5079)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6975 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3043` → IC=+0.251 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3043 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7479` → IC=+0.233 (n=4518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7479 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=9213)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4741.9684` → IC=+0.150 (n=6252)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4741.9684 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.124 (n=11833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0064 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.564` → IC=+0.146 (n=23612)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.564 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.1693` → IC=+0.194 (n=9571)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1693 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.859` → IC=+0.195 (n=6494)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.859 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.237 (n=2378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `1.4548` → IC=+0.209 (n=16520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4548 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=16437)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.086)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.248 (n=1329)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3747` → IC=+0.213 (n=3988)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3747 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2675)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9839` → IC=+0.276 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9839 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.471` → IC=+0.274 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.471 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.255 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4413` → IC=+0.211 (n=3825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4413 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=4400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.221 (n=3661)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.248 (n=2378)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0925` → IC=+0.277 (n=1188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0925 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.252 (n=1641)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.4805` → IC=+0.260 (n=3136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4805 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.983` → IC=+0.247 (n=3653)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.983 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0712` → IC=+0.245 (n=3067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0712 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.252 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4479` → IC=+0.243 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4479 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.8611` → IC=+0.246 (n=2272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8611 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.245 (n=2532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1781.8598` → IC=+0.245 (n=2375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.8598 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.244 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.242)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.236 (n=1132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1122` → IC=+0.247 (n=1489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1122 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.224 (n=2414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.8988` → IC=+0.257 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8988 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1921` → IC=+0.231 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1921 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.817` → IC=+0.262 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.817 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.229 (n=3384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.269 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4472` → IC=+0.247 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4472 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `15856.4389` → IC=+0.224 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15856.4389 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.153 (n=3672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0067 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.160 (n=1223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=2614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.3601` → IC=+0.206 (n=2446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3601 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.974` → IC=+0.141 (n=3355)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.974 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6285` → IC=+0.151 (n=1223)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6285 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.158 (n=1499)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4414` → IC=+0.142 (n=3541)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4414 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.786` → IC=+0.135 (n=2360)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.786 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4768)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.187 (n=1162)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 171.0 (IC base=+0.134)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.204 (n=2825)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.256 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.97` → IC=+0.282 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.97 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.194 (n=3797)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3517` → IC=+0.226 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3517 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7296` → IC=+0.211 (n=1875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7296 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5130)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1998.1898` → IC=+0.203 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1998.1898 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.224 (n=3468)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.222 (n=2627)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1787` → IC=+0.234 (n=1732)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1787 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.229 (n=1788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.274 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.776` → IC=+0.268 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.776 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3465` → IC=+0.258 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3465 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1568` → IC=+0.231 (n=2529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1568 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1938)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1875.32` → IC=+0.224 (n=1785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1875.32 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.226 (n=3764)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.171 (n=223)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=5114)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.145 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0039 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.239 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1477` → IC=+0.346 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1477 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.5765` → IC=+0.341 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5765 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.146` → IC=+0.209 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.146 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.1139` → IC=+0.358 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1139 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` < `0.1687` → IC=+0.343 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1687 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.3054` → IC=+0.345 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3054 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `1.5556` → IC=+0.356 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5556 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` > `2.2887` → IC=+0.344 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2887 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.346 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.0883` → IC=+0.187 (n=1335)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0883 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.3483` → IC=+0.161 (n=652)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3483 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.1445` → IC=+0.158 (n=2460)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1445 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `1.0024` → IC=+0.161 (n=2273)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0024 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.210 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.5054` → IC=+0.161 (n=2222)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5054 (IC base=+0.056)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.186 (n=151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=813)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.175 (n=241)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=723)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.130 (n=4969)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=2526)

- **FILTRO** `sigma_ewma_delta_pct` > `8.306` → IC=-0.232 (n=811)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.306
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=6684)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.180 (n=332)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.9803` → IC=+0.279 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9803 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.6326` → IC=+0.270 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6326 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.928` → IC=+0.146 (n=292)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 2.928 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.8516` → IC=+0.266 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8516 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6202` → IC=+0.287 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6202 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.281 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.288 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5342` → IC=+0.265 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5342 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.275 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.158 (n=2526)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.2 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` < `0.3228` → IC=+0.286 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3228 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.295 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` > `1.0437` → IC=+0.289 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0437 (IC base=-0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.0778` → IC=+0.313 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0778 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.4388` → IC=+0.298 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4388 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.4113` → IC=+0.293 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4113 (IC base=-0.033)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7937` → IC=-0.158 (n=3835)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7937
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=1977)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.175 (n=1215)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4597)

- **FILTRO** `ibs_20min` > `0.7333` → IC=-0.190 (n=2009)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=6044)

- **PATRÓN** `ibs_20min` > `0.7937` → IC=+0.137 (n=1977)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7937 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0349` → IC=+0.344 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0349 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.7079` → IC=+0.318 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7079 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.1089` → IC=+0.301 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1089 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.0787` → IC=+0.305 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0787 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.5875` → IC=+0.302 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5875 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.5155` → IC=+0.312 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5155 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0731` → IC=+0.281 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0731 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6418` → IC=+0.275 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6418 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.2057` → IC=+0.285 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2057 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2841` → IC=+0.293 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2841 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.4677` → IC=+0.266 (n=2238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4677 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4331` → IC=+0.273 (n=2238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4331 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.192 (n=8182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0109 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8659` → IC=+0.284 (n=11110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8659 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9596` → IC=+0.297 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9596 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.469` → IC=+0.167 (n=11000)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.469 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.278 (n=8111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.295 (n=2032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6418` → IC=+0.285 (n=4746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6418 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.308 (n=13879)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.160 (n=7948)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0105 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.5183` → IC=+0.173 (n=20929)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5183 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.6972` → IC=+0.280 (n=3517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6972 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `1.1883` → IC=+0.286 (n=2664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1883 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.330 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.4516` → IC=+0.305 (n=3953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4516 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.2707` → IC=+0.304 (n=5372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2707 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.312 (n=11821)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.086)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8052` → IC=-0.139 (n=4353)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8052
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=2243)

- **FILTRO** `ibs_20min` > `0.7085` → IC=-0.238 (n=1469)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=4409)

- **FILTRO** `sigma_ewma_delta_pct` > `4.078` → IC=-0.238 (n=1252)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.078
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=4626)

- **PATRÓN** `ibs_20min` > `0.8052` → IC=+0.304 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8052 (IC base=+0.012)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.966` → IC=+0.184 (n=2197)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 2.966 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.327 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4491` → IC=+0.283 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4491 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.2425` → IC=+0.305 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2425 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.317 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.012)

- **PATRÓN** `ibs_20min` < `0.1719` → IC=+0.175 (n=1470)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1719 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` < `0.1515` → IC=+0.391 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1515 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.6476` → IC=+0.395 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6476 (IC base=-0.017)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.382 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1729` → IC=+0.228 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1729 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.1971` → IC=+0.213 (n=2399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1971 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.218 (n=2399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.242 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4151` → IC=+0.234 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4151 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4647` → IC=+0.213 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4647 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `256.0` → IC=+0.246 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 256.0 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `0.6814` → IC=+0.251 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6814 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.1582` → IC=+0.269 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1582 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.309 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5262` → IC=+0.260 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5262 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1487` → IC=+0.265 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1487 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.283 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 179.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.321 (n=1543)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.582` → IC=+0.304 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.582 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1307` → IC=+0.295 (n=3162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1307 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2614` → IC=+0.298 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2614 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2000.3184` → IC=+0.294 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2000.3184 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.304 (n=2125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.333 (n=2093)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.306)

- **PATRÓN** `drift_60min` |x|≤ `0.1824` → IC=+0.323 (n=1379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1824 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=1196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.306)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` < `0.0254` → IC=+0.307 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0254 (IC base=+0.306)

- **PATRÓN** `ibs_20min` > `0.1497` → IC=+0.316 (n=2089)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1497 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.122` → IC=+0.316 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.122 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.409` → IC=+0.306 (n=3242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.409 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` < `0.1982` → IC=+0.307 (n=3105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1982 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.318 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` > `2.7501` → IC=+0.320 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7501 (IC base=+0.306)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.307 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.306)

- **PATRÓN** `libro_liquidez` > `1978.3798` → IC=+0.312 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.3798 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.311 (n=2696)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.306)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7162` → IC=-0.180 (n=1544)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7162
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=4635)

- **PATRÓN** `dist_vwap_pct` > `0.152` → IC=+0.236 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.152 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.3648` → IC=+0.237 (n=2209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3648 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.164` → IC=+0.237 (n=2220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.164 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.595` → IC=+0.233 (n=2220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.595 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.235 (n=2328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.247 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4189` → IC=+0.241 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4189 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.4958` → IC=+0.236 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4958 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.252 (n=2202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.0913` → IC=+0.154 (n=1545)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.0913 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.7781` → IC=+0.258 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7781 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.1622` → IC=+0.261 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1622 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `1.1877` → IC=+0.264 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1877 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.6161` → IC=+0.257 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6161 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.304 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.296 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.278 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.284 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.009)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7447` → IC=-0.248 (n=2528)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7447
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2529)

- **FILTRO** `ibs_20min` > `0.6129` → IC=-0.235 (n=1196)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6129
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=3605)

- **FILTRO** `sigma_ewma_delta_pct` > `8.264` → IC=-0.266 (n=550)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.264
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=4251)

- **PATRÓN** `ibs_20min` > `0.7447` → IC=+0.313 (n=2529)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7447 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.2247` → IC=+0.343 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2247 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.438` → IC=+0.156 (n=2052)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.438 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8371` → IC=+0.347 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8371 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.6909` → IC=+0.335 (n=1650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6909 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.335 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.364 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.4268` → IC=+0.362 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4268 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.353 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.6129` → IC=+0.159 (n=3605)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.6129 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` < `0.3243` → IC=+0.272 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3243 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.726` → IC=+0.130 (n=3761)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 4.726 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` < `0.6914` → IC=+0.281 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6914 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.0702` → IC=+0.296 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0702 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.7979` → IC=+0.282 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7979 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.289 (n=1823)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.061)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.356 (n=2336)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` > `0.6528` → IC=+0.340 (n=2615)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6528 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `0.5444` → IC=+0.338 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5444 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.823` → IC=+0.334 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.823 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.0501` → IC=+0.341 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0501 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.345 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `1.5317` → IC=+0.326 (n=2255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5317 (IC base=+0.314)

- **PATRÓN** `libro_liquidez` > `2994.9154` → IC=+0.326 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.9154 (IC base=+0.314)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.337 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.314)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.333 (n=2813)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.316 (n=2825)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.333 (n=2813)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3846 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.326 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.318 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `1.2077` → IC=+0.342 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2077 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.371 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` < `1.4109` → IC=+0.321 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4109 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `2.1399` → IC=+0.319 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1399 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2976.1495` → IC=+0.316 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2976.1495 (IC base=+0.316)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.221 (n=6019)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1241` → IC=+0.192 (n=7938)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1241 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=18748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5374` → IC=+0.229 (n=18039)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5374 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1643` → IC=+0.204 (n=6788)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1643 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.991` → IC=+0.253 (n=4721)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.991 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1763` → IC=+0.151 (n=12034)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1763 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6224` → IC=+0.151 (n=12035)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6224 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.205 (n=2615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5995` → IC=+0.184 (n=5853)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5995 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.191 (n=16974)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 86.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.192 (n=7903)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.006 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.188 (n=11954)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.222 (n=5976)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.249 (n=15792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.495` → IC=+0.191 (n=2839)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.495 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.506` → IC=+0.193 (n=15952)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.506 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.1867` → IC=+0.167 (n=12725)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1867 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.222 (n=2689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6297` → IC=+0.197 (n=5700)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6297 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.201 (n=16887)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.187)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.263 (n=988)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.105` → IC=+0.255 (n=1301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.105 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.226 (n=2008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.9425` → IC=+0.291 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9425 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.479` → IC=+0.324 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.479 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2317` → IC=+0.280 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2317 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.8356` → IC=+0.224 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8356 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4364` → IC=+0.226 (n=2825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4364 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.260 (n=2468)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.268 (n=1645)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.0986` → IC=+0.310 (n=1089)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0986 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.259 (n=2546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.263 (n=2254)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.4423` → IC=+0.274 (n=2469)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4423 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.955` → IC=+0.262 (n=2432)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.955 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.0731` → IC=+0.258 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0731 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.273 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.4468` → IC=+0.272 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4468 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6917` → IC=+0.260 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6917 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.264 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1781.7648` → IC=+0.261 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.7648 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.257 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.256)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.195 (n=919)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0032 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0651` → IC=+0.175 (n=917)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0651 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2877)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2602` → IC=+0.205 (n=2748)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2602 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1869` → IC=+0.213 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1869 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.618` → IC=+0.208 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.618 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6247` → IC=+0.133 (n=917)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6247 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.05` → IC=+0.133 (n=1246)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.05 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.169 (n=424)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.7741` → IC=+0.130 (n=1802)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.7741 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4652` → IC=+0.143 (n=901)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4652 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `394.0` → IC=+0.133 (n=2670)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 394.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.180 (n=2604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2465` → IC=+0.174 (n=2602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2465 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=1403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.455` → IC=+0.224 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.455 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.877` → IC=+0.178 (n=554)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.877 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.023` → IC=+0.158 (n=2579)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.023 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2017` → IC=+0.163 (n=2956)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2017 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2285` → IC=+0.155 (n=3145)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.2285 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4706` → IC=+0.156 (n=2830)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4706 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.200 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 206.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.223 (n=2035)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2519` → IC=+0.232 (n=2034)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2519 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.044` → IC=+0.306 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.044 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3513` → IC=+0.241 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3513 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7121` → IC=+0.224 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7121 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=3695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1991.8648` → IC=+0.220 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1991.8648 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.248 (n=2405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.2476` → IC=+0.270 (n=1822)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2476 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=1042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.04` → IC=+0.295 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.04 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.896` → IC=+0.280 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.896 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3537` → IC=+0.289 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3537 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.7676` → IC=+0.241 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7676 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1818` → IC=+0.252 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1818 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1965.4884` → IC=+0.249 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1965.4884 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.241 (n=1798)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.195 (n=995)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.180 (n=995)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.245` → IC=+0.188 (n=2983)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.245 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1434` → IC=+0.187 (n=1689)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1434 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.184` → IC=+0.203 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.184 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8387` → IC=+0.137 (n=1991)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8387 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.177 (n=450)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.126 (n=1286)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.137 (n=974)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6884.2177` → IC=+0.196 (n=1353)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6884.2177 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.125 (n=2935)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 125.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.165 (n=2807)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0069 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4141` → IC=+0.150 (n=3187)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4141 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6714` → IC=+0.189 (n=3187)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6714 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1641` → IC=+0.158 (n=3252)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1641 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.186` → IC=+0.141 (n=756)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.186 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.152 (n=2125)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.852 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.178 (n=477)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1879` → IC=+0.134 (n=2666)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1879 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.5144` → IC=+0.137 (n=2707)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.5144 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6451.777` → IC=+0.191 (n=1445)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6451.777 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.153 (n=1006)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.169 (n=1109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0127 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4719` → IC=+0.204 (n=3316)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4719 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.2029` → IC=+0.187 (n=1764)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2029 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.014` → IC=+0.286 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.014 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1651` → IC=+0.129 (n=3316)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1651 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1625` → IC=+0.122 (n=3382)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1625 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7825` → IC=+0.124 (n=2146)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7825 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2684.2871` → IC=+0.195 (n=1504)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2684.2871 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=1110)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 16.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.143 (n=3478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0121 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1164` → IC=+0.164 (n=1160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1164 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.4878` → IC=+0.240 (n=3062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4878 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.232` → IC=+0.146 (n=3074)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.232 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1798` → IC=+0.130 (n=3478)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1798 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.8605` → IC=+0.127 (n=2319)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.8605 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.162` → IC=+0.127 (n=3429)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.162 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.147 (n=486)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4339` → IC=+0.146 (n=1099)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4339 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4432` → IC=+0.136 (n=1099)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4432 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2587.6384` → IC=+0.192 (n=1577)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2587.6384 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.131 (n=3297)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 44.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.247 (n=2986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1668` → IC=+0.240 (n=1314)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1668 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6646` → IC=+0.256 (n=2986)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6646 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.231 (n=1826)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8044` → IC=+0.227 (n=3086)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8044 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.534` → IC=+0.257 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.534 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.235 (n=2986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6219 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.265 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4668` → IC=+0.228 (n=2914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4668 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4338` → IC=+0.229 (n=2914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4338 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2599.3337` → IC=+0.232 (n=1991)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2599.3337 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.244 (n=1368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0123 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.017` → IC=+0.247 (n=2072)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.017 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.6074` → IC=+0.250 (n=3103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6074 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1391)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0364` → IC=+0.301 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0364 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `1.1534` → IC=+0.250 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1534 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.103` → IC=+0.271 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.103 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` > `1.0469` → IC=+0.248 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0469 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.296 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `2.5167` → IC=+0.238 (n=2935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5167 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.5486` → IC=+0.242 (n=2622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5486 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `2960.0954` → IC=+0.242 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2960.0954 (IC base=+0.241)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.208 (n=1574)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1388` → IC=+0.171 (n=2072)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1388 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.4225` → IC=+0.200 (n=4206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4225 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2287` → IC=+0.175 (n=1757)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2287 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.54` → IC=+0.210 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.54 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.167 (n=2838)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8615 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.1975` → IC=+0.163 (n=1419)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1975 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.1568` → IC=+0.174 (n=1236)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1568 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.5271` → IC=+0.159 (n=2020)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5271 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.8074` → IC=+0.159 (n=3061)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8074 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=4012)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7289.8412` → IC=+0.189 (n=2135)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7289.8412 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.383` → IC=+0.177 (n=3429)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.383 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.141 (n=2253)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 23.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.198 (n=1161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0062 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1037` → IC=+0.226 (n=512)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1037 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.220 (n=1047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.6189` → IC=+0.245 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6189 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.3129` → IC=+0.222 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3129 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.946` → IC=+0.218 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.946 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.8772` → IC=+0.204 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8772 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.2151` → IC=+0.191 (n=1307)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.2151 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0909` → IC=+0.204 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0909 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.200 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.4026` → IC=+0.188 (n=1139)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4026 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `13747.0284` → IC=+0.195 (n=774)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 13747.0284 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.158 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0032 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.2095` → IC=+0.196 (n=639)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.2095 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.172 (n=626)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 167.0 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.234 (n=634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1291` → IC=+0.158 (n=630)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1291 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=1485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.7794` → IC=+0.267 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7794 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.5942` → IC=+0.192 (n=306)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.5942 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.911` → IC=+0.207 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.911 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8344` → IC=+0.168 (n=954)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8344 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1649` → IC=+0.155 (n=477)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.1649 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.199 (n=260)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.4732` → IC=+0.186 (n=470)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4732 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7912.0475` → IC=+0.179 (n=649)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7912.0475 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.126 (n=950)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0054 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.0884` → IC=+0.206 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0884 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `0.6769` → IC=+0.138 (n=627)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6769 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `7713.0144` → IC=+0.155 (n=645)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 7713.0144 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.132 (n=612)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 42.0 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.159 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0069 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.138 (n=1161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.186 (n=1097)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.5357 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.9836` → IC=+0.152 (n=208)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.9836 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.88` → IC=+0.220 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.88 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8679` → IC=+0.135 (n=819)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8679 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.142 (n=216)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4106` → IC=+0.147 (n=397)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4106 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2762.3879` → IC=+0.151 (n=557)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2762.3879 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.36` → IC=+0.194 (n=904)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.36 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2650.9565` → IC=+0.169 (n=615)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2650.9565 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.130 (n=603)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.085)

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
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.227 (n=7922)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=24797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9688` → IC=+0.303 (n=7923)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9688 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.9069` → IC=+0.216 (n=2774)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9069 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.936` → IC=+0.259 (n=5833)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.936 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8694` → IC=+0.163 (n=10675)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8694 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.212 (n=4274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.623` → IC=+0.192 (n=7736)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.623 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.200 (n=22430)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.198 (n=7361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0053 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.208 (n=7351)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1497` → IC=+0.202 (n=9688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1497 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=8203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.253 (n=19377)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.514` → IC=+0.204 (n=20436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.514 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0532` → IC=+0.173 (n=12997)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.0532 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.257 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.212 (n=7042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=20883)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.275 (n=1264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3702` → IC=+0.234 (n=3790)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3702 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8626` → IC=+0.296 (n=2526)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8626 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.863` → IC=+0.340 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.863 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.286 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4492` → IC=+0.233 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4492 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2926` → IC=+0.240 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2926 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=4170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2020.5186` → IC=+0.237 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2020.5186 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.248 (n=2390)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.268 (n=3433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.269 (n=2289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1246` → IC=+0.294 (n=1510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1246 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.267 (n=3564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=3107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.466` → IC=+0.288 (n=3020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.466 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.042` → IC=+0.269 (n=3575)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.042 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.1616` → IC=+0.269 (n=3470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1616 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.286 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.273 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6526` → IC=+0.279 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6526 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1781.7622` → IC=+0.271 (n=2288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.7622 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.279 (n=1106)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.175 (n=1306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0032 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.08` → IC=+0.150 (n=1300)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.08 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.1948` → IC=+0.188 (n=3894)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1948 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.33` → IC=+0.200 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.33 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.061` → IC=+0.168 (n=621)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.061 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6358` → IC=+0.156 (n=1300)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6358 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.0686` → IC=+0.144 (n=1766)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0686 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2718` → IC=+0.187 (n=550)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2718 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.144 (n=3368)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.146 (n=3420)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.155 (n=2526)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 295.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.171 (n=3013)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0814` → IC=+0.172 (n=1140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0814 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=1254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.6801` → IC=+0.190 (n=3419)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6801 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.986` → IC=+0.144 (n=3097)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.986 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.042` → IC=+0.152 (n=3010)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.042 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2207` → IC=+0.198 (n=624)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2207 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4295` → IC=+0.147 (n=3308)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4295 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7688` → IC=+0.149 (n=2206)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7688 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=4444)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.165 (n=1082)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 217.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.237 (n=1798)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=3545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.988` → IC=+0.320 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.988 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.225 (n=3755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.233 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7503` → IC=+0.241 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7503 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=4788)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1997.4956` → IC=+0.239 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1997.4956 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.250 (n=3356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1813` → IC=+0.259 (n=1677)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1813 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1737)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.303 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.032` → IC=+0.308 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.032 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.303 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.256 (n=2453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1971.805` → IC=+0.252 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1971.805 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.249 (n=3180)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.193 (n=1376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3444` → IC=+0.147 (n=3624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3444 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.8819` → IC=+0.270 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8819 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1435` → IC=+0.168 (n=2041)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1435 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.181` → IC=+0.166 (n=830)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.181 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8575` → IC=+0.152 (n=2745)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8575 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.200 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5166` → IC=+0.156 (n=1772)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5166 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.156` → IC=+0.143 (n=1824)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.156 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `5698.1383` → IC=+0.231 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5698.1383 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.145 (n=2669)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 86.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.168 (n=3469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.008 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4492` → IC=+0.160 (n=3467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4492 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=1273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.7038` → IC=+0.201 (n=3467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7038 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1612` → IC=+0.164 (n=3283)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1612 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.018` → IC=+0.154 (n=3026)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.018 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8555` → IC=+0.161 (n=2312)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8555 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.211 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1974` → IC=+0.154 (n=2952)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1974 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5242` → IC=+0.156 (n=2997)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5242 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `6658.8999` → IC=+0.221 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6658.8999 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.165 (n=2283)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 89.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.154 (n=1396)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0129 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=2953)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.254 (n=2795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0324` → IC=+0.202 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0324 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.244` → IC=+0.272 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.244 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.133 (n=2788)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8745 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.126 (n=525)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.4871` → IC=+0.121 (n=4080)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4871 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2744.6466` → IC=+0.235 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2744.6466 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.158 (n=3452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0111 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1416` → IC=+0.153 (n=1308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1416 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=1846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.242 (n=3450)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5417 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.054` → IC=+0.157 (n=3793)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 3.054 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6385` → IC=+0.153 (n=1306)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6385 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.199 (n=689)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4353` → IC=+0.165 (n=1243)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4353 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2637.4052` → IC=+0.212 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2637.4052 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.147 (n=3756)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 49.0 (IC base=+0.135)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.258 (n=3824)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=3997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=2560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.6154` → IC=+0.270 (n=3416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6154 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1989` → IC=+0.250 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1989 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.104` → IC=+0.290 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.104 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.239 (n=3822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2203 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6439` → IC=+0.242 (n=3822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6439 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.258 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.4955` → IC=+0.253 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4955 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2870.2949` → IC=+0.245 (n=1733)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2870.2949 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.268 (n=1324)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=3736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.1358` → IC=+0.309 (n=1746)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1358 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.056` → IC=+0.279 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.056 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2151` → IC=+0.265 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2151 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2837` → IC=+0.309 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2837 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4271` → IC=+0.248 (n=3755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4271 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `2970.944` → IC=+0.247 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2970.944 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.232 (n=6174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.5297` → IC=+0.233 (n=7011)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5297 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=7060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.261 (n=2344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.4455` → IC=+0.226 (n=4965)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4455 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.568` → IC=+0.231 (n=3489)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.568 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.231 (n=2184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.8785` → IC=+0.225 (n=3305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8785 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.225 (n=6557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.232 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4471` → IC=+0.235 (n=2300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4471 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=5039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `3698.5889` → IC=+0.231 (n=4674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3698.5889 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.235 (n=1620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.5197` → IC=+0.217 (n=4856)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5197 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.215 (n=1884)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=2186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.0908` → IC=+0.216 (n=1619)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0908 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.6936` → IC=+0.215 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6936 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.187` → IC=+0.202 (n=4197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.187 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.776` → IC=+0.220 (n=4395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.776 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2476` → IC=+0.209 (n=4474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2476 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.209 (n=4489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.207 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.5304` → IC=+0.209 (n=2105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5304 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.1904` → IC=+0.217 (n=2169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1904 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.232 (n=2130)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.206)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.277 (n=824)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.300 (n=313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.269 (n=940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.1406` → IC=+0.294 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1406 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `1.2303` → IC=+0.273 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2303 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `1.0873` → IC=+0.274 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0873 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.346 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.276 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.269 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `12881.3725` → IC=+0.281 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12881.3725 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.265 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3869` → IC=+0.188 (n=1531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3869 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=571)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.197 (n=674)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1382 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.7` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.835` → IC=+0.187 (n=1770)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 10.835 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.0909` → IC=+0.188 (n=1347)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0909 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.2705` → IC=+0.178 (n=1807)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.2705 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.193 (n=467)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.4122` → IC=+0.192 (n=508)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4122 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `1.8038` → IC=+0.179 (n=1015)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8038 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `14600.5038` → IC=+0.175 (n=694)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 14600.5038 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `694.0` → IC=+0.188 (n=1486)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 694.0 (IC base=+0.175)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.238 (n=345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.3088` → IC=+0.212 (n=688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3088 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.231 (n=943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.7126` → IC=+0.212 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7126 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.277` → IC=+0.246 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.277 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2042` → IC=+0.244 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2042 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.7931` → IC=+0.215 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7931 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2777.94` → IC=+0.240 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2777.94 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.221 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.224 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.228)

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

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.222 (n=1890)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.4639` → IC=+0.218 (n=1889)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4639 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.472` → IC=+0.221 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.472 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.1473` → IC=+0.212 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1473 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4059` → IC=+0.221 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4059 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.314` → IC=+0.217 (n=1918)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.314 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.217 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1013` → IC=+0.213 (n=1746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1013 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.210 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.3969` → IC=+0.230 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3969 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.245 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.5009` → IC=+0.221 (n=1499)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5009 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.209 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=1073)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.0864` → IC=+0.209 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0864 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.216 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.4177` → IC=+0.204 (n=1612)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4177 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.345` → IC=+0.209 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.345 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2546` → IC=+0.211 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2546 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.721` → IC=+0.204 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.721 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.072` → IC=+0.229 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.072 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.4044` → IC=+0.207 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4044 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.7747` → IC=+0.207 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7747 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `7795.6157` → IC=+0.213 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7795.6157 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.204 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.203)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.237 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.223 (n=551)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.239 (n=1225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9863` → IC=+0.296 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9863 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.8376` → IC=+0.253 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8376 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.251 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `0.6403` → IC=+0.251 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6403 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.222 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2737` → IC=+0.228 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2737 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `2.1635` → IC=+0.227 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1635 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `4156.0524` → IC=+0.246 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4156.0524 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.254 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.6597` → IC=+0.254 (n=856)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6597 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.244 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.262 (n=606)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.266 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.5875` → IC=+0.247 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5875 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.982` → IC=+0.264 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.982 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` < `0.6707` → IC=+0.257 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6707 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0816` → IC=+0.258 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0816 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.269 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.242 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `3933.4587` → IC=+0.271 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3933.4587 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.276 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.242)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.149 (n=794)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.7446` → IC=+0.183 (n=1526)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7446 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.152` → IC=+0.144 (n=1109)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.152 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.6174` → IC=+0.145 (n=1648)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6174 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.147 (n=449)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.059)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5385` → IC=-0.123 (n=316)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5385
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=644)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.123 (n=662)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0055 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.159 (n=644)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5385 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.301` → IC=+0.188 (n=222)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.301 (IC base=+0.066)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.125 (n=294)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0036 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.254 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.154 (n=131)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.051)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.5379` → IC=-0.136 (n=234)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5379
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=455)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.149 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0042 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.124 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.9304` → IC=+0.257 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9304 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1321` → IC=+0.166 (n=354)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1321 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.623` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.623 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.105` → IC=+0.265 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.105 (IC base=+0.036)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7196` → IC=+0.140 (n=553)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.7196 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.7456` → IC=+0.153 (n=191)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7456 (IC base=+0.029)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.172 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0098 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.1837` → IC=+0.252 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1837 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` > `1.1136` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1136 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `2.5364` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5364 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.136 (n=240)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.03 (IC base=+0.092)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.302 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=294)

- **FILTRO** `dist_vwap_pct` > `0.2422` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2422
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=373)

- **FILTRO** `volumen_regimen` < `0.8583` → IC=-0.308 (n=128)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8583
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=260)

- **FILTRO** `ibs_20min` > `0.6926` → IC=-0.312 (n=115)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6926
  - _Potencial_: sin este filtro IC_bueno=-0.253 (n=225)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=321)

- **FILTRO** `sigma_ewma_delta_pct` > `9.683` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.683
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=312)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=219)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `9.679` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.679
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=97)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.297 (n=57)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

- **FILTRO** `dist_vwap_pct` < `0.091` → IC=-0.282 (n=108)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.091
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `hora_utc` < `2.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=106)

- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.471 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=99)

- **FILTRO** `volumen_regimen` < `0.7435` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7435
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=99)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.368 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=95)

- **FILTRO** `ibs_20min` > `0.7557` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7557
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=99)

- **FILTRO** `volumen_spike_ratio` < `1.442` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.442
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=72)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=116)

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
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=46)

- **FILTRO** `volumen_regimen` < `0.9169` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9169
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=42)

- **FILTRO** `libro_spread` > `0.05` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.05
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=43)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2457` → IC=-0.148 (n=305)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2457
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=919)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.241 (n=350)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.195 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.6786` → IC=+0.188 (n=770)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.6786 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.8367` → IC=+0.306 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8367 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.4` → IC=+0.176 (n=183)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.4 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.195 (n=257)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6244 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.183 (n=576)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.204 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.855` → IC=+0.126 (n=271)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 8.855 (IC base=+0.029)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7302` → IC=-0.171 (n=74)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7302
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=225)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.162 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0066 (IC base=+0.048)

- **PATRÓN** `ibs_20min` > `0.7302` → IC=+0.121 (n=225)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.7302 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.6482` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6482 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.141 (n=424)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.251 (IC base=+0.080)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.15` → IC=-0.129 (n=149)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=291)

- **PATRÓN** `drift_60min` |x|≤ `0.199` → IC=+0.129 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.199 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.135 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.7163` → IC=+0.151 (n=247)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.7163 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.154 (n=203)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.429` → IC=+0.133 (n=227)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 6.429 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6249 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1915 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1814` → IC=+0.147 (n=264)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.1814 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7318` → IC=+0.176 (n=146)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.7318 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=213)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.689` → IC=+0.167 (n=79)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.689 (IC base=+0.007)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2308` → IC=-0.268 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2308
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=166)

- **FILTRO** `volumen_regimen` < `0.9345` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9345
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=110)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.284 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.277 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` > `0.8636` → IC=+0.301 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8636 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` > `0.4724` → IC=+0.378 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4724 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.344 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.255)

- **PATRÓN** `volumen_regimen` < `0.6106` → IC=+0.314 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6106 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.092` → IC=+0.305 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.092 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.331 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.255)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.338 (n=152)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.350 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.335)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.412 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.335)

- **PATRÓN** `drift_15min` |x|≤ `2.3371` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3371 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `1.0022` → IC=+0.383 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0022 (IC base=+0.335)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.384 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.335)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3492` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3492 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `2.3232` → IC=+0.333 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3232 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.8756` → IC=+0.316 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8756 (IC base=+0.289)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.338 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.386 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.289)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.338 (n=152)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.350 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.335)

- **PATRÓN** `elapsed_s` > `209.2` → IC=+0.412 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.2 (IC base=+0.335)

- **PATRÓN** `drift_15min` |x|≤ `2.3371` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3371 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `1.0022` → IC=+0.383 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0022 (IC base=+0.335)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.384 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.335)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3492` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3492 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `2.3232` → IC=+0.333 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3232 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.8756` → IC=+0.316 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8756 (IC base=+0.289)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.338 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.386 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.289)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1495)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2854.854` → IC=+0.134 (n=757)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2854.854 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1495)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2854.854` → IC=+0.134 (n=757)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2854.854 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=262)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=262)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1139)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `liq_n` > 2.0 (IC base=+0.078)

- **PATRÓN** `liq_usd_total` > `1200.92` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1200.92 (IC base=+0.078)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.078)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11521.8948` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 11521.8948
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=47)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=69)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.058)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `1802.5` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_usd_total` < 1802.5
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=45)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=263)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4097)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=196)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=153)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=183)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.167 (n=91)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=92)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 29.0 (IC base=-0.025)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=277)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.190)

- **PATRÓN** `liq_usd_total` > `345.52` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 345.52 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.228 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.190)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1623)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1577)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=735)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=555)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=536)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.137 (n=224)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.004)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1066)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1066)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1392)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1392)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=314)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=314)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.132 (n=104)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=225)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=386)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=435)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=317)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=420)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=420)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=392)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.125 (n=3045)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=7966)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.170 (n=101)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=118)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.139 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=124)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=48)

- **FILTRO** `restante_min` < `3.99` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=29)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.145 (n=347)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=865)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.120 (n=488)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=580)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.140 (n=376)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.51 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.130 (n=182)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=407)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=620)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=670)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.137 (n=315)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=676)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=680)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=367)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.123 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=387)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.133 (n=564)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=642)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.177 (n=8501)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=26819)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=8929)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=27676)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.191 (n=1640)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=4922)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.142 (n=2193)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=4307)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.135 (n=1688)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.134 (n=3038)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.176 (n=1186)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=3674)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1261)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3868)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1620)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=5031)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.136 (n=2016)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `1742.072` → IC=+0.125 (n=2229)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1742.072 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1280)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=3945)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.162 (n=1630)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=4960)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2448)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2372)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3161)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4113)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1119)

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
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=366)

- **FILTRO** `drift_20min_pct` |x|> `0.2022` → IC=-0.136 (n=119)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2022
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=360)

- **FILTRO** `libro_liquidez` < `3246.2924` → IC=-0.181 (n=158)

  - _Acción_: SKIP cuando `libro_liquidez` < 3246.2924
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=321)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=979)

- **FILTRO** `libro_liquidez` < `1991.6564` → IC=-0.139 (n=397)

  - _Acción_: SKIP cuando `libro_liquidez` < 1991.6564
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=809)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.133 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 17.0 (IC base=+0.029)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=24026)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=54326)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=18945)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=59407)

- **FILTRO** `ibs_7min` < `0.2138` → IC=-0.235 (n=19587)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2138
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=58765)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=26393)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=51959)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.245 (n=24345)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=73670)

- **FILTRO** `ibs_7min` > `0.28` → IC=-0.183 (n=24414)

  - _Acción_: SKIP cuando `ibs_7min` > 0.28
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=73601)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=3368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10663)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.320 (n=3476)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=10555)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.256 (n=4627)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=9404)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4116)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=12840)

- **FILTRO** `ibs_7min` > `0.7698` → IC=-0.210 (n=4238)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7698
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=12718)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=3148)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9830)

- **FILTRO** `ibs_7min` < `0.713` → IC=-0.210 (n=3243)

  - _Acción_: SKIP cuando `ibs_7min` < 0.713
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9735)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.201 (n=3239)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9739)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=3022)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10242)

- **FILTRO** `ibs_7min` > `0.2649` → IC=-0.192 (n=3314)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2649
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=9950)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.179 (n=3298)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9966)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=3232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10254)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.325 (n=3204)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=10282)

- **FILTRO** `ibs_7min` < `0.29` → IC=-0.251 (n=4450)

  - _Acción_: SKIP cuando `ibs_7min` < 0.29
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9036)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.170 (n=3346)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10140)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=4309)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=13639)

- **FILTRO** `ibs_7min` > `0.7248` → IC=-0.184 (n=4486)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7248
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=13462)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=3150)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9495)

- **FILTRO** `ibs_7min` < `0.7132` → IC=-0.200 (n=3161)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7132
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9484)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.192 (n=3160)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9485)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=3046)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=10100)

- **FILTRO** `ibs_7min` > `0.2721` → IC=-0.178 (n=3283)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2721
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=9863)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.168 (n=3270)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=9876)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=3019)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=9498)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.234 (n=4130)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8387)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3066)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9451)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.200 (n=4508)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=14476)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=4103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=8592)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=3084)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=9611)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.224 (n=4176)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8519)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.191 (n=3170)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=9525)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.229 (n=4357)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=13360)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1016)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1305)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.161 (n=172)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=636)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=918)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=334)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=451)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=589)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.150 (n=195)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=586)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.147 (n=721)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `729.2318` → IC=+0.155 (n=699)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 729.2318 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3572.803` → IC=+0.141 (n=720)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3572.803 (IC base=+0.126)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.182 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `377.422` → IC=+0.161 (n=328)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 377.422 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2527.6661` → IC=+0.230 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2527.6661 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 6.0 (IC base=+0.139)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.133 (n=330)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.134 (n=293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.175 (n=198)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `657.7094` → IC=+0.162 (n=261)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 657.7094 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.189 (n=104)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 59.0 (IC base=+0.132)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.418` → IC=+0.196 (n=179)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio` |x|> 0.418 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.176 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 5.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `5947.939` → IC=+0.168 (n=236)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 5947.939 (IC base=+0.138)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.133 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 14.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=204)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3578.603` → IC=+0.149 (n=146)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3578.603 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **FILTRO** `pct_vs_K` |x|> `3.3889` → IC=-0.170 (n=310)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3889
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=605)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.151 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0045 (IC base=-0.040)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.205` → IC=-0.229 (n=68)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.205
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=207)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.296 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.002)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.002)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` < `0.0107` → IC=-0.136 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=25)

- **FILTRO** `T_h` < `243.9505` → IC=-0.182 (n=64)

  - _Acción_: SKIP cuando `T_h` < 243.9505
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=25)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `96.5959` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `T_h` < 96.5959
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=87)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `87.9882` → IC=-0.246 (n=408)

  - _Acción_: SKIP cuando `T_h` < 87.9882
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=409)

- **FILTRO** `sigma_h` < `0.0077` → IC=-0.186 (n=364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0077
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=365)

- **FILTRO** `T_h` > `142.6336` → IC=-0.210 (n=181)

  - _Acción_: SKIP cuando `T_h` > 142.6336
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=548)

- **FILTRO** `pct_vs_K` |x|> `3.0033` → IC=-0.400 (n=178)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0033
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=551)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.009` → IC=-0.210 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.009
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `T_h` < `60.8769` → IC=-0.219 (n=87)

  - _Acción_: SKIP cuando `T_h` < 60.8769
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=179)

- **FILTRO** `sigma_h` < `0.008` → IC=-0.185 (n=201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `T_h` > `143.1632` → IC=-0.210 (n=67)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=202)

- **FILTRO** `pct_vs_K` |x|> `1.0921` → IC=-0.234 (n=201)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.0921
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=68)

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
- **FILTRO** `sigma_h` < `0.0092` → IC=-0.324 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0092
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=117)

- **FILTRO** `T_h` < `87.9956` → IC=-0.297 (n=116)

  - _Acción_: SKIP cuando `T_h` < 87.9956
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=118)

- **FILTRO** `sigma_h` < `0.0056` → IC=-0.202 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=165)

- **FILTRO** `pct_vs_K` |x|> `2.0379` → IC=-0.383 (n=109)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0379
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=111)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0948` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `pct_vs_K` |x|≤ 1.0948 (IC base=-0.131)

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
- **FILTRO** `sigma_h` > `0.013` → IC=-0.212 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=153)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.244 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=155)

- **FILTRO** `T_h` > `70.1154` → IC=-0.218 (n=154)

  - _Acción_: SKIP cuando `T_h` > 70.1154
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=77)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.286 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=121)

- **FILTRO** `pct_vs_K` |x|> `2.975` → IC=-0.429 (n=54)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.975
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=107)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1186` → IC=+0.454 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1186 (IC base=+0.335)

- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.357 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.335)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.335)

- **PATRÓN** `T_h` > `0.4704` → IC=+0.361 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4704 (IC base=+0.335)

- **PATRÓN** `dist_50` > `0.4679` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4679 (IC base=+0.335)

- **PATRÓN** `edge` > `0.1` → IC=+0.430 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.393)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.396 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.393)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.412 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.393)

- **PATRÓN** `T_h` > `1.484` → IC=+0.399 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.393)

- **PATRÓN** `dist_50` > `0.3717` → IC=+0.444 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3717 (IC base=+0.393)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.393)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.195)

- **PATRÓN** `T_h` > `1.4764` → IC=+0.256 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4764 (IC base=+0.195)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.234 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.195)

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
- **PATRÓN** `edge` > `0.1745` → IC=+0.486 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1745 (IC base=+0.438)

- **PATRÓN** `sigma_h` < `0.0163` → IC=+0.458 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0163 (IC base=+0.438)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.458 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.438)

- **PATRÓN** `dist_50` > `0.3553` → IC=+0.472 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3553 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.438)

- **PATRÓN** `edge` > `0.1954` → IC=+0.471 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1954 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.474 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.464)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4578` → IC=+0.493 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4578 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=459)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=499)

- **PATRÓN** `streak_estiramiento` < `0.829` → IC=+0.124 (n=344)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.829 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 14.0 (IC base=+0.055)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=24)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.037)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `regimen_ma_toques` < `2.0` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `regimen_ma_toques` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=200)

- **PATRÓN** `streak_estiramiento` < `0.2031` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.2031 (IC base=+0.028)

- **PATRÓN** `streak_estiramiento` < `0.5801` → IC=+0.163 (n=170)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.5801 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.083)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=93)

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
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=20)

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
- **PATRÓN** `streak_estiramiento` < `0.6439` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.6439 (IC base=+0.017)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1089)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5170)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2991)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.179 (n=2559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2267` → IC=+0.157 (n=5816)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2267 (IC base=+0.135)

- **PATRÓN** `drift_15min` |x|≤ `1.077` → IC=+0.136 (n=5816)

  - _Acción_: Kelly boost +0.68€ cuando `drift_15min` |x|≤ 1.077 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1327` → IC=+0.148 (n=2402)

  - _Acción_: Kelly boost +0.74€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1327 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=5377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.5679` → IC=+0.215 (n=5196)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5679 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.139` → IC=+0.124 (n=2714)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.139 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.5446` → IC=+0.122 (n=5578)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.5446 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.281` → IC=+0.237 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.281 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3231)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4436.4712` → IC=+0.171 (n=1939)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4436.4712 (IC base=+0.135)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=2294)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.250 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.254 (n=278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2672` → IC=+0.231 (n=277)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2672 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.273 (n=831)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.3824` → IC=+0.226 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3824 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.5302` → IC=+0.205 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5302 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.343` → IC=+0.300 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.343 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `14141.7548` → IC=+0.226 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14141.7548 (IC base=+0.203)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.143 (n=1046)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0072 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.147 (n=698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.138 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.4895` → IC=+0.217 (n=1046)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4895 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.150 (n=653)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.6132` → IC=+0.131 (n=1188)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6132 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.055` → IC=+0.284 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.055 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6037.827` → IC=+0.170 (n=474)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6037.827 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.7619` → IC=+0.132 (n=780)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.66€ cuando `ibs_15` > 0.7619 (IC base=+0.050)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0144` → IC=+0.147 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0144 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.150 (n=1480)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0124 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2321` → IC=+0.176 (n=1480)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2321 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.144 (n=1480)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.197 (n=460)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.151 (n=1360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.214 (n=1323)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2046` → IC=+0.158 (n=671)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.2046 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.616` → IC=+0.182 (n=338)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 17.616 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2933.0749` → IC=+0.190 (n=671)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2933.0749 (IC base=+0.143)

- **PATRÓN** `ibs_15` < `0.1143` → IC=+0.149 (n=1135)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1143 (IC base=+0.069)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.365 (n=511)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.379 (n=510)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.380 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.374 (n=808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7906` → IC=+0.394 (n=765)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7906 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.382 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.396 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3887.2465` → IC=+0.376 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3887.2465 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.404 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.365 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.376 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.399 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.384 (n=369)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2485` → IC=+0.388 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2485 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.163` → IC=+0.392 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.163 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8157.6321` → IC=+0.384 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8157.6321 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.402 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.370 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.385 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.366)

- **PATRÓN** `drift_60min` |x|≤ `0.1066` → IC=+0.369 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1066 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1293` → IC=+0.384 (n=264)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1293 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.374 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.372 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.8152` → IC=+0.399 (n=354)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8152 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.376 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` < `0.6408` → IC=+0.368 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6408 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.392 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `4202.8422` → IC=+0.379 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4202.8422 (IC base=+0.366)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.205 (n=2819)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2821)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2405)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3235)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.216 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.086)

- **PATRÓN** `ibs_15` > `0.6307` → IC=+0.276 (n=1265)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6307 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.201 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` < `0.5648` → IC=+0.198 (n=1341)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.5648 (IC base=-0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2304` → IC=+0.273 (n=1763)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2304 (IC base=-0.001)

- **PATRÓN** `ibs_15` < `0.371` → IC=+0.286 (n=5281)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.371 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` > `0.6758` → IC=+0.274 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6758 (IC base=-0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0437` → IC=-0.227 (n=2453)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0437
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=1212)

- **FILTRO** `sigma_ewma_delta_pct` > `22.099` → IC=-0.252 (n=519)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.099
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=3146)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.145 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0031 (IC base=+0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.283 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.145` → IC=+0.270 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.145 (IC base=+0.068)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.316 (n=450)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1043` → IC=+0.277 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1043 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.282 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.961` → IC=+0.151 (n=227)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 21.961 (IC base=+0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.224 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.184)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.184)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.289 (n=74)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.184)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.184)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.184)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=824)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.160 (n=556)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.006 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.163 (n=556)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3014` → IC=+0.195 (n=496)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3014 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.162 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5684` → IC=+0.239 (n=631)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5684 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.6301` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6301 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.147 (n=587)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2675 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.262 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=824)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7310.985` → IC=+0.160 (n=286)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7310.985 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.259 (n=919)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.4598` → IC=+0.245 (n=2087)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4598 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7999` → IC=+0.255 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7999 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2073` → IC=+0.268 (n=946)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2073 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.244 (n=1432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3858` → IC=+0.273 (n=2087)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3858 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.391` → IC=+0.265 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.391 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.392` → IC=+0.247 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.392 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1917` → IC=-0.279 (n=333)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1917
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=1002)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.274 (n=453)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=882)

- **FILTRO** `drift_15min` |x|> `0.9462` → IC=-0.297 (n=333)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9462
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1002)

- **FILTRO** `sigma_ewma_delta_pct` > `6.094` → IC=-0.205 (n=296)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.094
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=1039)

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

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.296 (n=911)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.257 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.199 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1191` → IC=-0.264 (n=803)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1191
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=806)

- **FILTRO** `sigma_h` > `0.0125` → IC=-0.242 (n=1206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0125
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=403)

- **FILTRO** `drift_15min` |x|> `1.2845` → IC=-0.277 (n=402)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2845
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1207)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1588)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0719` → IC=+0.283 (n=1126)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0719 (IC base=-0.011)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.297 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3289` → IC=+0.297 (n=1260)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3289 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.7684` → IC=+0.337 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7684 (IC base=-0.011)

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

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.049)

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

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.049)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.297 (n=471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.282 (n=471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.312 (n=471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1507` → IC=+0.281 (n=940)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1507 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2211` → IC=+0.289 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2211 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.294 (n=1466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8378` → IC=+0.309 (n=1410)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8378 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.312 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.386 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13088.9696` → IC=+0.299 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13088.9696 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.303 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.304 (n=329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.276)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2692` → IC=+0.284 (n=248)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2692 (IC base=+0.276)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.282 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.301 (n=686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.276)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.300 (n=745)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.312 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.686` → IC=+0.391 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.686 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `15684.0606` → IC=+0.316 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15684.0606 (IC base=+0.276)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.294 (n=667)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0501` → IC=+0.318 (n=223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0501 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0654` → IC=+0.290 (n=666)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0654 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.309 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.297 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.287 (n=473)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.846` → IC=+0.317 (n=666)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.846 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2797` → IC=+0.315 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2797 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` < `0.6422` → IC=+0.287 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6422 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.128` → IC=+0.376 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.128 (IC base=+0.288)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.156 (n=94)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=289)

- **FILTRO** `ballena_activa_n` > `46.0` → IC=-0.137 (n=235)

  - _Acción_: SKIP cuando `ballena_activa_n` > 46.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=116)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.212 (n=123)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=373)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.180 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=373)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1387` → IC=-0.143 (n=54)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1387
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=165)

- **FILTRO** `sigma_h` < `0.0064` → IC=-0.160 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1257` → IC=-0.214 (n=19)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1257
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=41)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1177` → IC=-0.167 (n=16)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1177
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `sigma_h` < `0.0054` → IC=-0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0773` → IC=-0.243 (n=33)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0773
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

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
- **PATRÓN** `ratio` < `0.9696` → IC=+0.337 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9696 (IC base=+0.143)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.356 (n=3056)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0189` → IC=+0.390 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0189 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.206 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.095)

- **PATRÓN** `T_h` > `110.2068` → IC=+0.321 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.2068 (IC base=+0.302)

- **PATRÓN** `ratio` > `1.0159` → IC=+0.376 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0159 (IC base=+0.302)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9833` → IC=+0.378 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9833 (IC base=+0.195)

- **PATRÓN** `T_h` > `111.9957` → IC=+0.353 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9957 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0277` → IC=+0.404 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0277 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.417 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5679 sube el IC de +0.135 a +0.215 en UPDOWN_GBM#15min (n=5196). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.203 a +0.273 en UPDOWN_GBM#BTC#15min (n=831). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4895 sube el IC de +0.131 a +0.217 en UPDOWN_GBM#ETH#15min (n=1046). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.143 a +0.214 en UPDOWN_GBM#XRP#15min (n=1323). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6307 sube el IC de -0.086 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1265). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.371 sube el IC de -0.001 a +0.286 en UPDOWN_GBM_15M_TARDIO (n=5281). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.068 a +0.316 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=450). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.184 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5684 sube el IC de +0.145 a +0.239 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=631). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3858 sube el IC de +0.243 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2087). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.204 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.026 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=911). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3289 sube el IC de -0.011 a +0.297 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1260). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.097 a +0.286 en UPDOWN_GBM_ETH_15M_HORA7 (n=26). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.097 a +0.286 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=26). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8378 sube el IC de +0.282 a +0.309 en UPDOWN_GBM_IBS_ALTO (n=1410). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.276 a +0.300 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=745). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.846 sube el IC de +0.288 a +0.317 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=666). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7906 sube el IC de +0.365 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=765). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8152 sube el IC de +0.366 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=354). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2248 | +0.082 | +220.95€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2248 | +0.082 | +220.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1838 | +0.083 | +182.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1838 | +0.083 | +182.41€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 94 | +0.125 | +28.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 94 | +0.125 | +28.08€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1251 | -0.017 | +70.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1251 | -0.017 | +70.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 960 | -0.033 | +50.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 960 | -0.033 | +50.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 199 | +0.057 | +23.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 199 | +0.057 | +23.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 49229 | -0.085 | -6321.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3120 | +0.084 | -304.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 46109 | -0.097 | -6017.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4898 | -0.110 | -822.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4898 | -0.110 | -822.70€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3120 | +0.084 | -304.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3120 | +0.084 | -304.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5005 | -0.106 | -938.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5005 | -0.106 | -938.19€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13506 | -0.043 | -1331.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13506 | -0.043 | -1331.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13433 | -0.114 | -1391.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13433 | -0.114 | -1391.29€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9267 | -0.137 | -1533.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9267 | -0.137 | -1533.27€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 52254 | -0.012 | +2737.21€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13475 | +0.004 | +1472.55€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 38779 | -0.017 | +1264.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 52254 | -0.012 | +2737.21€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13475 | +0.004 | +1472.55€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 38779 | -0.017 | +1264.66€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 197791 | +0.112 | -8305.31€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22401 | +0.180 | -711.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 913 | +0.015 | -73.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 163231 | +0.105 | -7111.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11246 | +0.094 | -408.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 27051 | +0.102 | -1956.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 81 | -0.175 | +14.04€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 26955 | +0.103 | -1958.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 37280 | +0.123 | -642.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5632 | +0.178 | -234.99€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 27021 | +0.119 | -213.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4585 | +0.081 | -171.63€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 27098 | +0.097 | -1977.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 91 | -0.113 | +13.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 26992 | +0.098 | -1980.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 42286 | +0.123 | -898.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10591 | +0.178 | -268.84€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 27452 | +0.105 | -558.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4231 | +0.103 | -62.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 36997 | +0.111 | -1660.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5912 | +0.198 | -249.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 816 | +0.040 | -19.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 27839 | +0.095 | -1217.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2430 | +0.105 | -174.56€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 27079 | +0.107 | -1168.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 94 | -0.125 | +13.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 26972 | +0.108 | -1181.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 32128 | +0.191 | -2320.30€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 32128 | +0.191 | -2320.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7279 | +0.165 | -802.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7279 | +0.165 | -802.95€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4724 | +0.196 | -186.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4724 | +0.196 | -186.08€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7123 | +0.173 | -644.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7123 | +0.173 | -644.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5935 | +0.251 | -209.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5935 | +0.251 | -209.30€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6988 | +0.184 | -490.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6988 | +0.184 | -490.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1286 | +0.425 | -47.61€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1286 | +0.425 | -47.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 538 | +0.439 | -5.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 538 | +0.439 | -5.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 521 | +0.423 | -20.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 521 | +0.423 | -20.27€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 113577 | +0.199 | -8364.88€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 113577 | +0.199 | -8364.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 19666 | +0.177 | -2287.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 19666 | +0.177 | -2287.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 18314 | +0.223 | -621.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 18314 | +0.223 | -621.98€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19498 | +0.180 | -2057.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19498 | +0.180 | -2057.02€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18463 | +0.217 | -741.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18463 | +0.217 | -741.00€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18748 | +0.204 | -1160.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18748 | +0.204 | -1160.40€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18888 | +0.197 | -1496.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18888 | +0.197 | -1496.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 44020 | +0.116 | +312.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 44020 | +0.116 | +312.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 21914 | +0.116 | +193.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 21914 | +0.116 | +193.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 22106 | +0.115 | +119.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 22106 | +0.115 | +119.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2688 | +0.293 | -14.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2688 | +0.293 | -14.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1228 | +0.282 | -29.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1228 | +0.282 | -29.06€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1318 | +0.296 | +8.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1318 | +0.296 | +8.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1239 | +0.438 | -5.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1239 | +0.438 | -5.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 591 | +0.434 | -8.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 591 | +0.434 | -8.35€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 596 | +0.442 | +1.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 596 | +0.442 | +1.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1983 | +0.067 | -91.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1258 | +0.079 | -26.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1549 | +0.074 | -45.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1258 | +0.079 | -26.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 89491 | +0.100 | -2051.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7232 | +0.096 | +159.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 82259 | +0.101 | -2210.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 48879 | +0.105 | -462.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7232 | +0.096 | +159.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 41647 | +0.107 | -622.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 19129 | +0.109 | -82.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 19129 | +0.109 | -82.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 21483 | +0.082 | -1505.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 21483 | +0.082 | -1505.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 60782 | +0.101 | +34027.83€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 60782 | +0.101 | +34027.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10066 | +0.225 | +8680.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10066 | +0.225 | +8680.03€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 9403 | +0.177 | +7437.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9403 | +0.177 | +7437.35€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 10889 | +0.207 | +8609.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10889 | +0.207 | +8609.30€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 8100 | +0.059 | +2674.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8100 | +0.059 | +2674.33€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8459 | -0.027 | +2206.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8459 | -0.027 | +2206.55€ | 4 | 17 |
| ✅ GBM_LATE_15M#XRP | 13865 | -0.020 | +4420.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13865 | -0.020 | +4420.26€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 64385 | +0.086 | +37472.79€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 64385 | +0.086 | +37472.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12474 | -0.002 | +6594.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12474 | -0.002 | +6594.41€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13837 | +0.006 | +3762.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13837 | +0.006 | +3762.13€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8715 | +0.295 | +9969.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8715 | +0.295 | +9969.21€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12267 | +0.016 | +3859.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12267 | +0.016 | +3859.98€ | 1 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9858 | +0.046 | +4447.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9858 | +0.046 | +4447.58€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7234 | +0.315 | +8839.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7234 | +0.315 | +8839.48€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 47945 | +0.179 | +39778.29€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 47945 | +0.179 | +39778.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7230 | +0.240 | +6742.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7230 | +0.240 | +6742.18€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7605 | +0.141 | +5663.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7605 | +0.141 | +5663.77€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7709 | +0.225 | +6714.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7709 | +0.225 | +6714.20€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8225 | +0.130 | +6372.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8225 | +0.130 | +6372.27€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9058 | +0.121 | +6901.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9058 | +0.121 | +6901.56€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8118 | +0.234 | +7384.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8118 | +0.234 | +7384.31€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 13134 | +0.126 | +6666.51€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 13134 | +0.126 | +6666.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 670 | +0.162 | +441.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 670 | +0.162 | +441.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3480 | +0.126 | +1882.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3480 | +0.126 | +1882.76€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3804 | +0.126 | +1894.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3804 | +0.126 | +1894.35€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3443 | +0.100 | +1388.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3443 | +0.100 | +1388.18€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1230 | +0.167 | +768.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1230 | +0.167 | +768.64€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 61019 | +0.189 | +50487.30€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 61019 | +0.189 | +50487.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9627 | +0.250 | +9298.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9627 | +0.250 | +9298.26€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9750 | +0.141 | +6869.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9750 | +0.141 | +6869.58€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10353 | +0.234 | +9348.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10353 | +0.234 | +9348.97€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10110 | +0.143 | +7543.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10110 | +0.143 | +7543.94€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10796 | +0.126 | +7754.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10796 | +0.126 | +7754.41€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10383 | +0.241 | +9672.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10383 | +0.241 | +9672.15€ | 0 | 19 |
| ✅ GBM_LATE_5M | 15821 | +0.217 | +13222.79€ | 0 | 27 |
| ✅ GBM_LATE_5M#5min | 15821 | +0.217 | +13222.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1792 | +0.250 | +1722.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1792 | +0.250 | +1722.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3288 | +0.211 | +2826.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3288 | +0.211 | +2826.97€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4516 | +0.207 | +3464.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4516 | +0.207 | +3464.66€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 2754 | +0.228 | +2458.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2754 | +0.228 | +2458.84€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5472 | +0.056 | +1471.79€ | 0 | 5 |
| ✅ GBM_LATE_60M#60min | 5472 | +0.056 | +1471.79€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1887 | +0.059 | +550.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1887 | +0.059 | +550.26€ | 1 | 6 |
| ✅ GBM_LATE_60M#ETH | 1745 | +0.055 | +541.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1745 | +0.055 | +541.91€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1840 | +0.053 | +379.62€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1840 | +0.053 | +379.62€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 728 | -0.251 | -37.07€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 728 | -0.251 | -37.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 262 | -0.254 | -20.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 262 | -0.254 | -20.04€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 263 | -0.243 | -7.19€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 263 | -0.243 | -7.19€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 203 | -0.251 | -9.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 203 | -0.251 | -9.85€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2250 | +0.085 | +570.27€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2250 | +0.085 | +570.27€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 863 | +0.069 | +194.25€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 863 | +0.069 | +194.25€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 769 | +0.056 | +148.28€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 769 | +0.056 | +148.28€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 618 | +0.143 | +227.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 618 | +0.143 | +227.73€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 325 | +0.314 | +391.78€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 325 | +0.314 | +391.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 325 | +0.314 | +391.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 325 | +0.314 | +391.78€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4512 | +0.097 | +1027.24€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4512 | +0.097 | +1027.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4512 | +0.097 | +1027.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4512 | +0.097 | +1027.24€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 1438 | +0.013 | +64.75€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1438 | +0.013 | +64.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 146 | +0.074 | +24.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 146 | +0.074 | +24.35€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M#BTC | 296 | -0.003 | +9.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 296 | -0.003 | +9.41€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 94 | +0.010 | +7.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 94 | +0.010 | +7.08€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 340 | +0.021 | +19.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 340 | +0.021 | +19.13€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 334 | -0.009 | +3.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 334 | -0.009 | +3.88€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 228 | +0.013 | +0.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 228 | +0.013 | +0.90€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4399 | +0.016 | +152.64€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4399 | +0.016 | +152.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 829 | +0.016 | +43.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 829 | +0.016 | +43.09€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 295 | +0.049 | +56.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 295 | +0.049 | +56.07€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1675 | +0.019 | +29.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1675 | +0.019 | +29.76€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 776 | +0.013 | +3.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 776 | +0.013 | +3.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 585 | -0.001 | +24.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 585 | -0.001 | +24.87€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2553 | -0.032 | -4.26€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2553 | -0.032 | -4.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 779 | -0.031 | -11.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 779 | -0.031 | -11.94€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 917 | -0.010 | +20.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 917 | -0.010 | +20.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 857 | -0.057 | -12.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 857 | -0.057 | -12.67€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 18094 | -0.033 | -205.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 8723 | -0.034 | -133.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 9371 | -0.031 | -72.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 642 | -0.056 | -39.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 329 | -0.035 | -3.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 313 | -0.078 | -35.74€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4756 | -0.028 | -47.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2255 | -0.025 | -4.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2501 | -0.031 | -42.53€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1718 | -0.031 | +3.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 876 | -0.042 | -22.06€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 842 | -0.020 | +25.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4107 | -0.031 | -44.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1969 | -0.029 | -11.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2138 | -0.033 | -33.50€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3476 | -0.023 | +47.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1687 | -0.030 | -4.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1789 | -0.016 | +52.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3395 | -0.047 | -125.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1607 | -0.054 | -86.58€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1788 | -0.040 | -38.98€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 71925 | +0.000 | +3950.61€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 71925 | +0.000 | +3950.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13062 | +0.027 | +1834.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13062 | +0.027 | +1834.97€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9989 | -0.038 | -140.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9989 | -0.038 | -140.84€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 13206 | +0.026 | +1499.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 13206 | +0.026 | +1499.45€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9973 | -0.053 | -263.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9973 | -0.053 | -263.05€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12271 | -0.004 | +353.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12271 | -0.004 | +353.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13424 | +0.019 | +666.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13424 | +0.019 | +666.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7279 | -0.053 | -112.40€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7279 | -0.053 | -112.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2027 | -0.061 | -22.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2027 | -0.061 | -22.68€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 813 | -0.118 | -34.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 813 | -0.118 | -34.55€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2209 | -0.068 | -13.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2209 | -0.068 | -13.60€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 868 | -0.018 | -27.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 868 | -0.018 | -27.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3382 | +0.004 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3382 | +0.004 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 198 | +0.010 | -0.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 198 | +0.010 | -0.55€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 176367 | -0.077 | +2512.92€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 176367 | -0.077 | +2512.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 30987 | -0.077 | +1850.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 30987 | -0.077 | +1850.83€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 26242 | -0.101 | -1235.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 26242 | -0.101 | -1235.54€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 31434 | -0.067 | +1531.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 31434 | -0.067 | +1531.02€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 25791 | -0.099 | -842.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 25791 | -0.099 | -842.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 31501 | -0.058 | +289.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 31501 | -0.058 | +289.56€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 30412 | -0.069 | +919.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 30412 | -0.069 | +919.60€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9159 | -0.035 | -179.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9159 | -0.035 | -179.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2128 | -0.046 | -28.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2128 | -0.046 | -28.35€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2669 | -0.024 | -33.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2669 | -0.024 | -33.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1282 | -0.062 | -29.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1282 | -0.062 | -29.57€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1063 | -0.034 | -35.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1063 | -0.034 | -35.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2252 | +0.122 | +916.10€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2116 | +0.126 | +903.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 496 | +0.139 | +250.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 496 | +0.139 | +250.97€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 440 | +0.118 | +154.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 440 | +0.118 | +154.79€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 395 | +0.132 | +187.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 395 | +0.132 | +187.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 357 | +0.138 | +178.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 357 | +0.138 | +178.57€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 428 | +0.102 | +131.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 428 | +0.102 | +131.20€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2347 | -0.020 | -31.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2347 | -0.020 | -31.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 421 | +0.011 | +23.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 421 | +0.011 | +23.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 435 | -0.049 | -29.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 435 | -0.049 | -29.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 576 | -0.045 | -39.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 576 | -0.045 | -39.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 479 | +0.003 | +7.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 479 | +0.003 | +7.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 436 | -0.014 | +7.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 436 | -0.014 | +7.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1228 | -0.052 | +65.56€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 570 | -0.086 | -18.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 441 | -0.087 | +5.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 430 | -0.016 | +54.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 309 | +0.005 | +63.47€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 228 | -0.035 | +29.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 192 | -0.026 | +27.55€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 942 | -0.044 | +96.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1546 | -0.194 | -57.75€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 606 | -0.186 | -23.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 535 | -0.183 | -19.98€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 71 | -0.199 | -3.91€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 517 | -0.203 | -36.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 454 | -0.213 | -42.69€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 63 | -0.131 | +6.63€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 423 | -0.194 | +2.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 392 | -0.190 | +0.56€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 31 | -0.227 | +1.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1381 | -0.196 | -62.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 165 | -0.183 | +4.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 567 | +0.377 | +521.66€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 124 | +0.167 | +98.87€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 124 | +0.167 | +98.87€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 130 | +0.371 | +107.64€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 130 | +0.371 | +107.64€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 313 | +0.459 | +315.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 313 | +0.459 | +315.15€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 567 | +0.377 | +521.66€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 996 | +0.036 | +75.46€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 996 | +0.036 | +75.46€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 76 | +0.013 | +0.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 76 | +0.013 | +0.02€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 84 | +0.023 | +7.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 84 | +0.023 | +7.13€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 477 | +0.057 | +65.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 477 | +0.057 | +65.97€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3613 | -0.023 | -142.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3613 | -0.023 | -142.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 621 | -0.026 | -25.98€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 621 | -0.026 | -25.98€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 174 | -0.045 | -15.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 174 | -0.045 | -15.30€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1691 | -0.019 | -60.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1691 | -0.019 | -60.68€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 125 | -0.035 | -12.61€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 125 | -0.035 | -12.61€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 46 | -0.062 | -3.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 46 | -0.062 | -3.71€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 79 | -0.018 | -8.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 79 | -0.018 | -8.89€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11587 | +0.014 | +70.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11587 | +0.014 | +70.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3063 | +0.015 | +30.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3063 | +0.015 | +30.24€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2936 | +0.008 | -3.55€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2936 | +0.008 | -3.55€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2593 | +0.014 | +19.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2593 | +0.014 | +19.31€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12642 | +0.018 | -0.04€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12642 | +0.018 | -0.04€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5189 | +0.021 | +3.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5189 | +0.021 | +3.90€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4428 | +0.018 | -1.37€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4428 | +0.018 | -1.37€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3025 | +0.014 | -2.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3025 | +0.014 | -2.57€ | 1 | 0 |
| ✅ UPDOWN_GBM | 115259 | +0.060 | +10868.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 28084 | +0.078 | +5521.99€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 3326 | -0.000 | +39.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 76592 | +0.062 | +5195.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6871 | -0.002 | +122.32€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10001 | +0.102 | +1763.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1782 | +0.163 | +818.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8129 | +0.089 | +946.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 26111 | +0.057 | +2311.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3786 | +0.079 | +848.53€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 962 | -0.001 | +19.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 18168 | +0.067 | +1364.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3055 | -0.005 | +77.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 140 | -0.070 | +2.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 12641 | +0.074 | +1355.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1763 | +0.154 | +737.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 10792 | +0.062 | +618.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 27120 | +0.050 | +1915.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6629 | +0.072 | +1021.03€ | 0 | 8 |
| ✅ UPDOWN_GBM#ETH#240min | 930 | +0.005 | +15.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16892 | +0.052 | +837.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2540 | +0.000 | +40.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 129 | -0.111 | -0.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 24220 | +0.041 | +1383.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7635 | +0.033 | +463.47€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 861 | -0.010 | +8.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14333 | +0.053 | +917.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1276 | +0.001 | +4.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 115 | -0.150 | -10.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 15164 | +0.073 | +2141.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6489 | +0.092 | +1632.43€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8278 | +0.062 | +510.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 384 | -0.109 | -8.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1020 | +0.365 | +380.98€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1020 | +0.365 | +380.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 492 | +0.362 | +172.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 492 | +0.362 | +172.46€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 528 | +0.366 | +208.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 528 | +0.366 | +208.53€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 27022 | -0.019 | +6723.99€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 27022 | -0.019 | +6723.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5040 | -0.115 | +274.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5040 | -0.115 | +274.28€ | 2 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1072 | +0.223 | +901.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1072 | +0.223 | +901.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3623 | +0.220 | +2321.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3623 | +0.220 | +2321.37€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7711 | -0.057 | +1145.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7711 | -0.057 | +1145.26€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7595 | -0.056 | +1520.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7595 | -0.056 | +1520.07€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 339 | +0.060 | +34.14€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 339 | +0.060 | +34.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 339 | +0.060 | +34.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 339 | +0.060 | +34.14€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1880 | +0.282 | +1585.30€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1880 | +0.282 | +1585.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 992 | +0.276 | +788.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 992 | +0.276 | +788.89€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 888 | +0.288 | +796.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 888 | +0.288 | +796.41€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 879 | -0.115 | -89.28€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 879 | -0.115 | -89.28€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 279 | -0.080 | -20.94€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 279 | -0.080 | -20.94€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 101 | -0.189 | -14.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 101 | -0.189 | -14.00€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 116 | -0.178 | -4.99€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 116 | -0.178 | -4.99€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4989 | +0.297 | +2212.94€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1923 | +0.252 | +252.54€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1929 | +0.291 | +816.22€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1137 | +0.382 | +1144.18€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.020 n=1405 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1405 IC=+0.020 PNL=+63.96€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 842 celda(s) pasan gate riguroso completo de 2985 evaluadas (n>=40) y 4101 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=7630 IC=+0.033 PNL=+461.34€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1929/15 IC=+0.291 PNL=+816.22€ | BTC: n=1922/15 IC=+0.252 PNL=+250.69€ | SOL: n=1137/15 IC=+0.382 PNL=+1144.18€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.135 n=1094/60 | contraria IC=+0.182 n=1151 | gap=-0.047 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=615, boost estimado=+0.010. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2539/40 IC=+0.000 PNL=+40.68€ | BTC#60min: n=3054/40 IC=-0.005 PNL=+78.26€ | SOL#60min: n=1274/40 IC=+0.001 PNL=+4.47€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=776486 | tras_1loss IC=+0.101 n=588202 | tras_2loss IC=+0.072 n=234504/40 | gap=-0.027 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.157 > 0.08 con n=1151 PNL=+674.90€
  - _Datos_: n=1151 IC=+0.157 PNL=+674.90€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.08 con n=1369 PNL=+645.10€
  - _Datos_: n=1369 IC=+0.132 PNL=+645.10€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=89 PNL=+36.54€
  - _Datos_: n=89 IC=+0.126 PNL=+36.54€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=4070 PNL=+2285.72€
  - _Datos_: n=4070 IC=+0.334 PNL=+2285.72€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1160 IC=+0.065 PNL=+115.25€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1160 IC=+0.065 PNL=+115.25€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=109 IC=+0.176 PNL=+69.98€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=109 IC=+0.176 PNL=+69.98€

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
  - _Estado_: n=4520 IC=-0.004 PNL=-40.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4520 IC=-0.004 PNL=-40.90€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2347 IC=+0.003 PNL=+164.31€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2347 IC=+0.003 PNL=+164.31€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1405 IC=+0.020 PNL=+63.96€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1405 IC=+0.020 PNL=+63.96€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.135 > 0.1 con n=7751 PNL=+3726.23€
  - _Datos_: n=7751 IC=+0.135 PNL=+3726.23€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3783 IC=+0.079 PNL=+849.05€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3783 IC=+0.079 PNL=+849.05€

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
  - _Estado_: n=1526 IC=+0.043 PNL=+129.66€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1526 IC=+0.043 PNL=+129.66€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=193 IC=-0.023 PNL=-5.24€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=193 IC=-0.023 PNL=-5.24€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.312 n=322) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=322 IC=+0.312 PNL=+386.62€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=1311 PNL=+528.33€
  - _Datos_: n=1311 IC=+0.118 PNL=+528.33€

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
  - _Estado_: n=47268 IC=+0.070 PNL=+6306.07€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=47268 IC=+0.070 PNL=+6306.07€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.138 < -0.1 con n=790 PNL=+113.34€
  - _Datos_: n=790 IC=-0.138 PNL=+113.34€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4512 IC=+0.070 PNL=+579.29€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4512 IC=+0.070 PNL=+579.29€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=195 IC=-0.084 PNL=+1.76€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=195 IC=-0.084 PNL=+1.76€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1206 IC=+0.098 PNL=+301.15€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1206 IC=+0.098 PNL=+301.15€

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
  - _Estado_: n=46117 IC=-0.138 PNL=+2797.92€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=46117 IC=-0.138 PNL=+2797.92€

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
  - _Estado_: n=4888 IC=+0.134 PNL=+3306.08€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4888 IC=+0.134 PNL=+3306.08€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=11981 IC=+0.057 PNL=+1014.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11981 IC=+0.057 PNL=+1014.99€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=4982 PNL=+2817.72€
  - _Datos_: n=4982 IC=+0.102 PNL=+2817.72€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.222 < -0.1 con n=5014 PNL=-449.75€
  - _Datos_: n=5014 IC=-0.222 PNL=-449.75€

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
  - _Estado_: n=122 IC=+0.057 PNL=+20.50€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=122 IC=+0.057 PNL=+20.50€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=2287) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2287 IC=+0.097 PNL=+461.17€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.415 n=690) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=690 IC=+0.415 PNL=+1010.73€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=19658 IC=+0.177 PNL=-2284.28€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=19658 IC=+0.177 PNL=-2284.28€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.234 > 0.1 con n=318 PNL=+224.12€
  - _Datos_: n=318 IC=+0.234 PNL=+224.12€
