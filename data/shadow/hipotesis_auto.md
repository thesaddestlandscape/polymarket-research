# Hipótesis automáticas — 2026-09-11 19:47 UTC
_Generado por shadow_postmortem.py sobre 393329 resoluciones (PNL=+41370.02€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=185)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.249 (n=389)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=377)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.249 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.121)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.213 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.121)

- **PATRÓN** `banda_hit_calibrado` > `0.8071` → IC=+0.267 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8071 (IC base=+0.121)

- **PATRÓN** `banda_z` > `10.841` → IC=+0.233 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.841 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.138 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=453)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.123 (n=377)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `84.0` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 84.0 (IC base=+0.034)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.465` → IC=-0.121 (n=143)

  - _Acción_: SKIP cuando `py_entrada` < 0.465
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=296)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=274)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=299)

- **PATRÓN** `py_entrada` > `0.465` → IC=+0.255 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.465 (IC base=+0.133)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.203 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 58.0 (IC base=+0.133)

- **PATRÓN** `banda_hit_calibrado` > `0.806` → IC=+0.275 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.806 (IC base=+0.133)

- **PATRÓN** `banda_z` > `11.795` → IC=+0.268 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.795 (IC base=+0.133)

- **PATRÓN** `ballenas_wallet_edge_medio` > `3.159` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `ballenas_wallet_edge_medio` > 3.159 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=371)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 88.0 (IC base=+0.027)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=95)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=99)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.241 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.092)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.241 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.092)

- **PATRÓN** `banda_z` > `6.173` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `banda_z` > 6.173 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.092)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `148.13` → IC=-0.269 (n=5090)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 148.13
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=15273)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `143.19` → IC=-0.273 (n=708)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.19
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2125)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `131.47` → IC=-0.304 (n=657)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.47
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1974)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `146.53` → IC=-0.183 (n=1319)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.53
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=3960)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `155.51` → IC=-0.265 (n=1168)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 155.51
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3506)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `159.99` → IC=-0.339 (n=1265)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 159.99
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=2570)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.5` → IC=-0.254 (n=67)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=89)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.236 (n=51)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=77)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.52 (IC base=+0.022)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=19)

- **FILTRO** `py_entrada` > `0.29` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.29
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.197 (n=9607)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.7 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=2578)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `11109.7462` → IC=+0.192 (n=825)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11109.7462 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.144 (n=7654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=9113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.247 (n=6729)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.173 (n=5082)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4718.4515` → IC=+0.173 (n=2198)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4718.4515 (IC base=+0.136)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.354 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `14550.7486` → IC=+0.218 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14550.7486 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=1095)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.210 (n=1203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.268 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `12844.1642` → IC=+0.205 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12844.1642 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.172 (n=254)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.615 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=276)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `4737.5622` → IC=+0.156 (n=222)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4737.5622 (IC base=+0.108)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.190 (n=259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.165 (n=530)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.425 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `3919.7561` → IC=+0.163 (n=402)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3919.7561 (IC base=+0.137)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=1771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.328 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.240 (n=896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.296 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.234 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2381.1953` → IC=+0.239 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2381.1953 (IC base=+0.234)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.224 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=573)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `1517.6481` → IC=+0.150 (n=430)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1517.6481 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `4449.086` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4449.086 (IC base=+0.082)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 12.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.426 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.190 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.286 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.188 (n=1027)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.03 (IC base=+0.183)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.333 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3435.4625` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3435.4625 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.140 (n=631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.120)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.219 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=312)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.120)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=104)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=8002)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=6765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.216 (n=2839)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.336 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `3397.72` → IC=+0.332 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3397.72 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.180 (n=1932)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.182 (n=2030)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.390 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.332)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.356 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.332)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=1900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.185 (n=1686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=1925)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.188 (n=1283)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.72 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=1794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=1523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.327 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.322 (n=43)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1652)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.189 (n=1024)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.7 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.189 (n=812)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.73 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.446 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.447 (n=321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.484 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.441 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `9523.4542` → IC=+0.468 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9523.4542 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.445 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.440 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.456 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `11570.9911` → IC=+0.459 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11570.9911 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.454 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.440 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `3939.3842` → IC=+0.454 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3939.3842 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.418 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.429 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.425 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.932` → IC=+0.421 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.932 (IC base=+0.425)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=10)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.194 (n=23488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.226 (n=12869)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=4837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.165 (n=4612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 17.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4280)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.162)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=4151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.250 (n=3048)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=4275)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.165)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=2099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=1581)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.269 (n=1478)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=3893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=3844)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.233 (n=2584)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=1689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.190 (n=3140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.241 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.187)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=3488)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.07` → IC=+0.134 (n=3239)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.07 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.146 (n=3524)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.94 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.137 (n=4763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.41` → IC=+0.151 (n=3232)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.41 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.130)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.142 (n=1603)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` < 4.01 (IC base=+0.130)

- **PATRÓN** `restante_min` > `4.89` → IC=+0.145 (n=2236)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.89 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.149 (n=2349)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.130)

- **PATRÓN** `lag_apertura_s` < `6.47` → IC=+0.147 (n=2116)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 6.47 (IC base=+0.130)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=1752)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.125 (n=2157)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.149 (n=1770)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `3.06` → IC=+0.148 (n=1631)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 3.06 (IC base=+0.118)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1658.923` → IC=+0.298 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1658.923 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.298 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.327 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `5211.8636` → IC=+0.295 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5211.8636 (IC base=+0.276)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.337 (n=280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.384 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `1534.8677` → IC=+0.312 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1534.8677 (IC base=+0.296)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.335 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.328)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.357 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.328)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.328)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.366 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.328)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.434 (n=334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.431 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.428 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `1921.0334` → IC=+0.435 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1921.0334 (IC base=+0.426)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.432 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.434 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `5328.1568` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5328.1568 (IC base=+0.427)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.444 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.426 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.429 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `1841.4992` → IC=+0.450 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1841.4992 (IC base=+0.428)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.372)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.372)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.278 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.261)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.403 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.261)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.281 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `2203.2207` → IC=+0.294 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2203.2207 (IC base=+0.261)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.278 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.261)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.403 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.261)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.281 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `2203.2207` → IC=+0.294 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2203.2207 (IC base=+0.261)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9692` → IC=+0.227 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9692 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.1582` → IC=+0.242 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1582 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.829` → IC=+0.166 (n=2008)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.829 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.6193` → IC=+0.248 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6193 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `1.0731` → IC=+0.242 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0731 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.1087` → IC=+0.197 (n=1293)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1087 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `1.4617` → IC=+0.195 (n=3360)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4617 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.5814` → IC=+0.122 (n=6508)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.5814 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.1358` → IC=+0.163 (n=1881)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1358 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `0.8681` → IC=+0.165 (n=1322)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8681 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.1677` → IC=+0.227 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1677 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.4569` → IC=+0.193 (n=3279)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4569 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `174.0` → IC=+0.204 (n=3040)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 174.0 (IC base=+0.054)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.191 (n=393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.005 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.189 (n=394)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0076 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3237` → IC=+0.169 (n=1177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3237 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.889` → IC=+0.286 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.889 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2285` → IC=+0.201 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2285 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.5938` → IC=+0.157 (n=1072)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.5938 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.163 (n=1072)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.184 (n=1237)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.06 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.190 (n=830)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 65.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.262 (n=779)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.1962` → IC=+0.282 (n=581)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1962 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.250 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.242 (n=885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.065` → IC=+0.292 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.065 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.135` → IC=+0.250 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.135 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0678` → IC=+0.239 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0678 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.289 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.6417` → IC=+0.272 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6417 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.247 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1732.1248` → IC=+0.260 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1732.1248 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.237 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 68.0 (IC base=+0.242)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.241 (n=303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1979` → IC=+0.229 (n=600)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1979 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9263` → IC=+0.246 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9263 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.2233` → IC=+0.214 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2233 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.921` → IC=+0.229 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.921 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2628` → IC=+0.220 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2628 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.8804` → IC=+0.218 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8804 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.212 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2334` → IC=+0.218 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2334 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4807` → IC=+0.227 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4807 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.214 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `11927.4558` → IC=+0.233 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11927.4558 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.162 (n=858)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0049 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.079` → IC=+0.167 (n=325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.079 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6828` → IC=+0.174 (n=975)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6828 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.496` → IC=+0.200 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.496 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.148 (n=975)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1954 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6855` → IC=+0.141 (n=871)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6855 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1525` → IC=+0.211 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1525 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.3739` → IC=+0.152 (n=866)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.3739 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4094` → IC=+0.152 (n=866)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4094 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `12924.6533` → IC=+0.153 (n=650)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 12924.6533 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.173 (n=261)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 218.0 (IC base=+0.140)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.183 (n=999)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0089 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.192 (n=1137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.006 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.208 (n=426)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.58` → IC=+0.259 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.58 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.1057` → IC=+0.184 (n=955)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1057 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.3745` → IC=+0.180 (n=148)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.3745 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `3.5324` → IC=+0.176 (n=1049)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 3.5324 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.8619` → IC=+0.192 (n=937)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.8619 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=1263)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.205 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.217 (n=987)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.211 (n=885)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.1555` → IC=+0.211 (n=434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1555 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.3956` → IC=+0.233 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3956 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.68` → IC=+0.239 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.68 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3645` → IC=+0.274 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3645 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.2796` → IC=+0.219 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2796 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1875.0896` → IC=+0.222 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1875.0896 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.209 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.209)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.7828` → IC=-0.162 (n=386)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7828
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1162)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=85)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1463)

- **PATRÓN** `dist_vwap_pct` < `0.4679` → IC=+0.338 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4679 (IC base=+0.002)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.479` → IC=+0.128 (n=415)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 5.479 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` < `0.6055` → IC=+0.417 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6055 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `1.1808` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1808 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.362 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `1.8361` → IC=+0.332 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8361 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.333 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 173.0 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.1626` → IC=+0.179 (n=135)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1626 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` < `0.8572` → IC=+0.137 (n=279)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8572 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2145` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2145 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.5104` → IC=+0.166 (n=330)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5104 (IC base=-0.015)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=209)

- **FILTRO** `ibs_20min` < `0.3385` → IC=-0.163 (n=84)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3385
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=171)

- **FILTRO** `ibs_20min` > `0.2927` → IC=-0.127 (n=1523)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2927
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=755)

- **FILTRO** `sigma_ewma_delta_pct` > `8.582` → IC=-0.195 (n=254)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.582
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2024)

- **PATRÓN** `ibs_20min` > `0.7353` → IC=+0.185 (n=87)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7353 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` < `0.5471` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5471 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.6528` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6528 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `1.1564` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1564 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.0735` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0735 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.3618` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3618 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.3269` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3269 (IC base=-0.049)

- **PATRÓN** `volumen_regimen` < `1.1373` → IC=+0.178 (n=147)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1373 (IC base=-0.049)

- **PATRÓN** `volumen_regimen` > `0.735` → IC=+0.162 (n=149)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.735 (IC base=-0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.0964` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0964 (IC base=-0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.4205` → IC=+0.203 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4205 (IC base=-0.049)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.269 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=-0.049)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6623` → IC=-0.187 (n=365)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6623
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1106)

- **FILTRO** `ibs_20min` < `0.625` → IC=-0.159 (n=965)

  - _Acción_: SKIP cuando `ibs_20min` < 0.625
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=506)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.185 (n=281)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1190)

- **FILTRO** `ibs_20min` > `0.78` → IC=-0.197 (n=563)

  - _Acción_: SKIP cuando `ibs_20min` > 0.78
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1697)

- **PATRÓN** `dist_vwap_pct` > `0.941` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.941 (IC base=-0.093)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.280 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.093)

- **PATRÓN** `volumen_regimen` > `0.6141` → IC=+0.272 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6141 (IC base=-0.093)

- **PATRÓN** `volumen_pendiente_norm` < `0.1499` → IC=+0.247 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1499 (IC base=-0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.093)

- **PATRÓN** `volumen_spike_ratio` < `1.5219` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5219 (IC base=-0.093)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.266 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.093)

- **PATRÓN** `dist_vwap_pct` > `0.488` → IC=+0.256 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.488 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2715` → IC=+0.231 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2715 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.295 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1054` → IC=+0.246 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1054 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4871` → IC=+0.241 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4871 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.234 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.030)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.169 (n=2184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0092 (IC base=+0.084)

- **PATRÓN** `ibs_20min` > `0.4505` → IC=+0.172 (n=5848)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4505 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.7383` → IC=+0.272 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7383 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.464` → IC=+0.136 (n=3084)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.464 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `0.6792` → IC=+0.228 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6792 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2472` → IC=+0.256 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2472 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `1.4779` → IC=+0.235 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4779 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.7512` → IC=+0.237 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7512 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.283 (n=2884)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.084)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.140 (n=2248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0085 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.5636` → IC=+0.145 (n=5934)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5636 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.6823` → IC=+0.242 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6823 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.1632` → IC=+0.233 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1632 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.261 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1967 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.2502` → IC=+0.322 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2502 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` > `2.3535` → IC=+0.264 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3535 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.257 (n=2076)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.064)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3291` → IC=-0.133 (n=587)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3291
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=1194)

- **FILTRO** `sigma_ewma_delta_pct` > `2.501` → IC=-0.151 (n=431)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.501
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=979)

- **PATRÓN** `ibs_20min` > `0.8409` → IC=+0.239 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8409 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.942` → IC=+0.152 (n=455)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.942 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2595` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2595 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.5259` → IC=+0.199 (n=396)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.5259 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5565` → IC=+0.197 (n=354)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.5565 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.233 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1791` → IC=+0.470 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1791 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4617` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4617 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.3568` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3568 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.84` → IC=-0.159 (n=506)

  - _Acción_: SKIP cuando `ibs_20min` > 0.84
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1520)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.124 (n=264)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `0.6774` → IC=+0.129 (n=491)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6774 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2205` → IC=+0.201 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2205 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.159 (n=177)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `272.0` → IC=+0.175 (n=229)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 272.0 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.1336` → IC=+0.248 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1336 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.7442` → IC=+0.216 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7442 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1121` → IC=+0.236 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1121 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `517.0` → IC=+0.211 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 517.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.281 (n=691)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0996` → IC=+0.242 (n=347)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0996 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.265 (n=385)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` > `0.7179` → IC=+0.272 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7179 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.58` → IC=+0.297 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.58 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.1101` → IC=+0.255 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1101 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `3.0864` → IC=+0.256 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0864 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.302 (n=730)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.312 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` < `0.3433` → IC=+0.290 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3433 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.884` → IC=+0.313 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.884 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.3437` → IC=+0.320 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3437 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` < `3.352` → IC=+0.276 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.352 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `2.2015` → IC=+0.286 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2015 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `1866.5527` → IC=+0.293 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1866.5527 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.277 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.279)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.136 (n=245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=881)

- **FILTRO** `ibs_20min` < `0.2163` → IC=-0.207 (n=281)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2163
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=845)

- **FILTRO** `ibs_20min` > `0.8394` → IC=-0.180 (n=389)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8394
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1170)

- **PATRÓN** `ibs_20min` > `0.8012` → IC=+0.126 (n=383)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.8012 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.4846` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4846 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2436` → IC=+0.169 (n=158)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.2436 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` < `0.9175` → IC=+0.196 (n=189)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.9175 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` > `0.6073` → IC=+0.168 (n=191)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6073 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.5078` → IC=+0.250 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5078 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.3994` → IC=+0.219 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3994 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1085` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1085 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0571` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0571 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` > `1.4214` → IC=+0.210 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4214 (IC base=-0.037)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 165.0 (IC base=-0.037)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6471` → IC=-0.198 (n=714)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6471
  - _Potencial_: sin este filtro IC_bueno=+0.245 (n=716)

- **FILTRO** `ibs_20min` > `0.7273` → IC=-0.235 (n=383)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7273
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=1151)

- **FILTRO** `sigma_ewma_delta_pct` > `4.709` → IC=-0.159 (n=376)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.709
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1158)

- **PATRÓN** `ibs_20min` > `0.6471` → IC=+0.245 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6471 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1881` → IC=+0.301 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1881 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.284 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.634` → IC=+0.263 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.634 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.269 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.279 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.304 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.314 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.129` → IC=+0.182 (n=385)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.129 (IC base=-0.003)

- **PATRÓN** `dist_vwap_pct` < `0.1586` → IC=+0.198 (n=233)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.1586 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `1.0891` → IC=+0.199 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0891 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` < `0.1023` → IC=+0.190 (n=224)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1023 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.22` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.22 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.5615` → IC=+0.206 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5615 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.5131` → IC=+0.185 (n=236)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.5131 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.232 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0143` → IC=+0.328 (n=626)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0143 (IC base=+0.263)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.276 (n=448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` > `0.9` → IC=+0.330 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9 (IC base=+0.263)

- **PATRÓN** `dist_vwap_pct` > `0.1804` → IC=+0.310 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1804 (IC base=+0.263)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.355` → IC=+0.288 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.355 (IC base=+0.263)

- **PATRÓN** `volumen_regimen` > `0.8542` → IC=+0.290 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8542 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` < `0.1103` → IC=+0.269 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1103 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.289 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` < `1.5515` → IC=+0.273 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5515 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `2.2094` → IC=+0.269 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2094 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.266 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `2448.2154` → IC=+0.269 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2448.2154 (IC base=+0.263)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.274 (n=343)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0202` → IC=+0.306 (n=466)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0202 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.284 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.302 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.5366` → IC=+0.288 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5366 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.281 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `1.2432` → IC=+0.312 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2432 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2419` → IC=+0.350 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2419 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `2.559` → IC=+0.267 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.559 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.1785` → IC=+0.268 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1785 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2568.9526` → IC=+0.277 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2568.9526 (IC base=+0.271)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.172 (n=1759)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0049 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.201 (n=1756)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3424` → IC=+0.177 (n=4627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3424 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=5521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.6957` → IC=+0.230 (n=4699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6957 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1685` → IC=+0.196 (n=2313)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1685 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.226` → IC=+0.250 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.226 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2184` → IC=+0.161 (n=3536)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2184 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6242` → IC=+0.159 (n=3534)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6242 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1056` → IC=+0.188 (n=2049)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1056 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.2869` → IC=+0.168 (n=4372)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.2869 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3902.0492` → IC=+0.175 (n=1752)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3902.0492 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.187 (n=4176)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 132.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.184 (n=3388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0064 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.203 (n=1691)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.199 (n=2441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4567` → IC=+0.226 (n=5069)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4567 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.731` → IC=+0.194 (n=2108)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.731 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.18` → IC=+0.154 (n=3725)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.18 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6256` → IC=+0.153 (n=3725)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6256 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.236 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.8646` → IC=+0.168 (n=2952)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.8646 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6113` → IC=+0.175 (n=1477)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6113 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.169 (n=4028)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 135.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.219 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.214 (n=403)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3147` → IC=+0.210 (n=878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3147 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.225 (n=431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.966` → IC=+0.312 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.966 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2249` → IC=+0.237 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2249 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.2336` → IC=+0.178 (n=693)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.2336 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.5413` → IC=+0.185 (n=703)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.5413 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.207 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.244 (n=549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.261 (n=559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1816` → IC=+0.301 (n=416)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1816 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.247 (n=627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.265 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.25 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.854` → IC=+0.252 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.854 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0683` → IC=+0.237 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0683 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.280 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.8606` → IC=+0.263 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8606 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.621` → IC=+0.231 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.621 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.262 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1731.6` → IC=+0.263 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1731.6 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.236 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 74.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.249 (n=257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.2743` → IC=+0.176 (n=675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2743 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.45` → IC=+0.220 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.45 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.2277` → IC=+0.217 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2277 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.757` → IC=+0.234 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.757 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6258` → IC=+0.195 (n=257)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6258 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.8827` → IC=+0.165 (n=511)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.8827 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2363` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2363 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.206 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `11289.7522` → IC=+0.187 (n=685)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 11289.7522 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `418.0` → IC=+0.161 (n=606)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 418.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.181 (n=775)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.209 (n=294)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.169 (n=808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.5111` → IC=+0.193 (n=881)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5111 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.118` → IC=+0.231 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.118 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.167 (n=881)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1856 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1573` → IC=+0.209 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1573 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.386` → IC=+0.163 (n=772)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.386 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4049` → IC=+0.152 (n=772)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4049 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.164 (n=233)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 239.0 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.210 (n=564)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1996` → IC=+0.207 (n=564)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1996 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.199 (n=387)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.541` → IC=+0.291 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.541 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.1322` → IC=+0.193 (n=324)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1322 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.6638` → IC=+0.191 (n=260)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.6638 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `3.5963` → IC=+0.202 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5963 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.232 (n=722)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.219)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.221 (n=481)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0922` → IC=+0.245 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0922 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.254 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.3611` → IC=+0.252 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3611 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.671` → IC=+0.279 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.671 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3598` → IC=+0.278 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3598 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.8282` → IC=+0.210 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8282 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.2354` → IC=+0.222 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2354 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1877.2368` → IC=+0.237 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1877.2368 (IC base=+0.219)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.217 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.4408` → IC=+0.172 (n=822)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4408 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.4092` → IC=+0.207 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4092 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.1409` → IC=+0.190 (n=547)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1409 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.407` → IC=+0.253 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.407 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.8664` → IC=+0.169 (n=548)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8664 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.2029` → IC=+0.177 (n=274)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2029 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.246 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4065` → IC=+0.174 (n=268)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4065 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.5584` → IC=+0.191 (n=267)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5584 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `7908.6344` → IC=+0.196 (n=548)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 7908.6344 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.167 (n=671)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 162.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.155 (n=776)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0061 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.3779` → IC=+0.140 (n=881)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3779 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.5951` → IC=+0.172 (n=881)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5951 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.142` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 12.142 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8664` → IC=+0.132 (n=588)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8664 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6141` → IC=+0.129 (n=881)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6141 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2869` → IC=+0.190 (n=127)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2869 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.127 (n=512)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `9877.5526` → IC=+0.149 (n=400)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 9877.5526 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.156 (n=454)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0099 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=1031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5156` → IC=+0.194 (n=1002)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5156 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0297` → IC=+0.220 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0297 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.383` → IC=+0.256 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.383 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.121 (n=1003)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2233 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `2.1433` → IC=+0.123 (n=847)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.1433 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=1014)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2922.6812` → IC=+0.200 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2922.6812 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.138 (n=721)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 50.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.147 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0054 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.5283` → IC=+0.207 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5283 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.191` → IC=+0.135 (n=878)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.191 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.23` → IC=+0.150 (n=204)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 7.23 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.0367` → IC=+0.128 (n=839)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0367 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.126` → IC=+0.140 (n=370)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.126 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3140.9562` → IC=+0.150 (n=318)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3140.9562 (IC base=+0.115)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.211 (n=631)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1667` → IC=+0.223 (n=416)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1667 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=850)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.253 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.72 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `1.2895` → IC=+0.238 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2895 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.346` → IC=+0.236 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.346 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `1.1991` → IC=+0.198 (n=946)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.1991 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `0.8509` → IC=+0.225 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8509 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0826` → IC=+0.241 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0826 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.1841` → IC=+0.215 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1841 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.8108` → IC=+0.204 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8108 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.198 (n=985)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.243 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0158` → IC=+0.209 (n=674)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0158 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0904` → IC=+0.220 (n=337)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0904 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.207 (n=1058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.4231` → IC=+0.243 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4231 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.952` → IC=+0.239 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.952 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6271` → IC=+0.219 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6271 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.312 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.224` → IC=+0.190 (n=772)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.224 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.8642` → IC=+0.190 (n=585)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.8642 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2539.7275` → IC=+0.213 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2539.7275 (IC base=+0.201)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.150 (n=555)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0073 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.4009` → IC=+0.163 (n=1218)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.4009 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.8094` → IC=+0.185 (n=160)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.8094 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.673` → IC=+0.167 (n=545)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.673 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.154 (n=688)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8646 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.2036` → IC=+0.133 (n=344)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.2036 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1661` → IC=+0.165 (n=335)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1661 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4339` → IC=+0.145 (n=387)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4339 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8208` → IC=+0.144 (n=773)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8208 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=1333)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `11954.2454` → IC=+0.176 (n=406)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 11954.2454 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.155 (n=450)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 27.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.133 (n=417)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0038 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.494` → IC=+0.141 (n=1101)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.494 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.29` → IC=+0.150 (n=261)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 8.29 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.146 (n=317)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.167 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.221` → IC=+0.128 (n=1044)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.221 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.138 (n=365)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 20.0 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.121 (n=262)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0025 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.147 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.3061` → IC=+0.139 (n=261)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.3061 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.3423` → IC=+0.194 (n=83)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3423 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.03` → IC=+0.175 (n=121)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.03 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6949` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6949 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `10126.7179` → IC=+0.154 (n=261)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10126.7179 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.199 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.2764` → IC=+0.136 (n=372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.2764 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.6193` → IC=+0.166 (n=372)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6193 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.02` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.02 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` > `0.7034` → IC=+0.129 (n=378)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.7034 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.213 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `2.3721` → IC=+0.131 (n=413)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.3721 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 155.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.236 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.224 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.244 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.2721` → IC=+0.248 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2721 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.964` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.964 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2237` → IC=+0.206 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2237 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.949` → IC=+0.239 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.949 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.235 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6877 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `1.168` → IC=+0.238 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.168 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2464` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2464 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.368` → IC=+0.226 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.368 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.0266` → IC=+0.256 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0266 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `12609.7071` → IC=+0.238 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12609.7071 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.3111` → IC=+0.136 (n=204)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.3111 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.985` → IC=+0.140 (n=112)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 3.985 (IC base=+0.078)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.7333` → IC=-0.140 (n=112)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=232)

- **FILTRO** `dist_vwap_pct` > `0.3844` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3844
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=261)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.207 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8947 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.239` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 5.239 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `2971.9929` → IC=+0.171 (n=86)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2971.9929 (IC base=+0.052)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 16.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.4478` → IC=+0.162 (n=208)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.4478 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.859` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.859 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.7466` → IC=+0.128 (n=92)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.7466 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` < `0.2091` → IC=+0.121 (n=225)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.2091 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `2.4885` → IC=+0.145 (n=187)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4885 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.167 (n=151)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 49.0 (IC base=+0.081)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0226` → IC=+0.146 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0226 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.174 (n=142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0061 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.31` → IC=+0.161 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.31 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 16.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.4 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.2912` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2912 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.6865` → IC=+0.142 (n=174)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.6865 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.9833` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.9833 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.6571` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6571 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.2672` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.2672 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.899` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.899 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4996` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4996 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.213 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.141 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 10.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.9736` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9736 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.507` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.507 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.149 (n=149)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6197 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.5677` → IC=+0.138 (n=136)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5677 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2567.2585` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2567.2585 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 16.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.193 (n=3001)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0087 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=6935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.475` → IC=+0.214 (n=6602)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.475 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.9235` → IC=+0.201 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9235 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.554` → IC=+0.225 (n=3216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.554 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8873` → IC=+0.164 (n=2999)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8873 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.1685` → IC=+0.186 (n=1804)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1685 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8603` → IC=+0.175 (n=4166)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8603 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.172 (n=7807)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `3845.8163` → IC=+0.173 (n=2201)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3845.8163 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.195 (n=4603)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 102.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.196 (n=4043)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0068 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.4838` → IC=+0.186 (n=6057)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.4838 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=2300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.187 (n=2774)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.5591` → IC=+0.238 (n=6057)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5591 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2352` → IC=+0.166 (n=3825)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2352 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.78` → IC=+0.208 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.78 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `1.2003` → IC=+0.164 (n=1397)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.2003 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2354` → IC=+0.249 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2354 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.2782` → IC=+0.190 (n=2420)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.2782 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.178 (n=4938)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 134.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.222 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.236 (n=501)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.210 (n=795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.975` → IC=+0.311 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.975 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.0933` → IC=+0.220 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0933 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `1.5533` → IC=+0.201 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5533 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.216 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.239 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.267 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.275 (n=864)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.2083` → IC=+0.291 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2083 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.273 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.264 (n=797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.3681` → IC=+0.297 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3681 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.595` → IC=+0.271 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.595 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2258` → IC=+0.317 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2258 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6706` → IC=+0.296 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6706 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.271 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1563.08` → IC=+0.270 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1563.08 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.266 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.196 (n=353)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1895` → IC=+0.157 (n=703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1895 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.695` → IC=+0.240 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.695 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3501` → IC=+0.202 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3501 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.858` → IC=+0.167 (n=244)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.858 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.33` → IC=+0.157 (n=935)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.33 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6306` → IC=+0.184 (n=352)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6306 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.184 (n=289)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.3936` → IC=+0.160 (n=1001)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.3936 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7464` → IC=+0.160 (n=668)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7464 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `10716.3301` → IC=+0.174 (n=941)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 10716.3301 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `504.0` → IC=+0.165 (n=929)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 504.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.176 (n=837)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.005 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3291` → IC=+0.173 (n=949)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3291 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.161 (n=680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.6459` → IC=+0.207 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6459 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.698` → IC=+0.207 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.698 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.1847` → IC=+0.168 (n=949)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1847 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.1486` → IC=+0.234 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1486 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.3652` → IC=+0.172 (n=852)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.3652 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.0672` → IC=+0.175 (n=386)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.0672 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `322.0` → IC=+0.172 (n=333)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 322.0 (IC base=+0.159)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.226 (n=1010)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.219 (n=1016)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.238 (n=491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6739` → IC=+0.258 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6739 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.82` → IC=+0.319 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.82 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2176` → IC=+0.224 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2176 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.6743` → IC=+0.224 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6743 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.252 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.248 (n=335)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.236 (n=668)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.237 (n=363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.3901` → IC=+0.266 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3901 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.647` → IC=+0.280 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.647 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.357` → IC=+0.293 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.357 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `2.9265` → IC=+0.215 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9265 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.2457` → IC=+0.216 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2457 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1880.9161` → IC=+0.232 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.9161 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.214 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.224)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.177 (n=491)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2291` → IC=+0.140 (n=745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2291 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.7134` → IC=+0.238 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7134 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.7656` → IC=+0.189 (n=226)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7656 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.376` → IC=+0.169 (n=484)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.376 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.165 (n=744)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8847 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.226 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7393` → IC=+0.166 (n=713)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7393 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=1210)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `9103.3274` → IC=+0.232 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9103.3274 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.147 (n=781)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0067 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4329` → IC=+0.143 (n=883)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4329 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6898` → IC=+0.177 (n=883)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6898 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1535` → IC=+0.130 (n=398)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.1535 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.2051` → IC=+0.129 (n=815)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.2051 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.137` → IC=+0.189 (n=133)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.137 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.129 (n=589)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.856 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.1735` → IC=+0.152 (n=294)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1735 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.262 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4511` → IC=+0.158 (n=273)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4511 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `11192.0569` → IC=+0.169 (n=294)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 11192.0569 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.129 (n=709)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 179.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.173 (n=1163)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4615 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `1.0168` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 1.0168 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.364` → IC=+0.220 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.364 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=801)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2949.3334` → IC=+0.244 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2949.3334 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.126 (n=834)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 54.0 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.202 (n=357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1259` → IC=+0.171 (n=357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1259 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6061` → IC=+0.214 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6061 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.4731` → IC=+0.143 (n=1051)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.4731 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.325` → IC=+0.128 (n=1031)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.325 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.6459` → IC=+0.157 (n=357)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6459 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.0726` → IC=+0.174 (n=378)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0726 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4637` → IC=+0.162 (n=306)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4637 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.1911` → IC=+0.134 (n=416)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.1911 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.130 (n=1169)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.03 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2988.1614` → IC=+0.157 (n=357)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2988.1614 (IC base=+0.122)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.221 (n=529)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.1816` → IC=+0.239 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1816 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.539` → IC=+0.237 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.539 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.2397` → IC=+0.205 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2397 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6218` → IC=+0.208 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6218 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.236` → IC=+0.226 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.236 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.5902` → IC=+0.232 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5902 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.249 (n=432)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.025` → IC=+0.228 (n=431)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.025 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.206 (n=1214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.206 (n=1368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.254 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1908` → IC=+0.205 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1908 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.584` → IC=+0.267 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.584 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.239 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.270 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.2192` → IC=+0.190 (n=981)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.2192 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.198 (n=1115)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2549.3704` → IC=+0.207 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2549.3704 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.183 (n=1030)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 37.0 (IC base=+0.202)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=2274)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.146 (n=1818)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0095 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.5388` → IC=+0.137 (n=2065)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.5388 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.162 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.136 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 4.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.9298` → IC=+0.202 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9298 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `1.1727` → IC=+0.134 (n=249)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 1.1727 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.247` → IC=+0.151 (n=328)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.247 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.8968` → IC=+0.127 (n=883)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.8968 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.1721` → IC=+0.150 (n=564)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1721 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.449` → IC=+0.151 (n=682)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.449 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.8762` → IC=+0.142 (n=1362)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8762 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=1370)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `8866.0493` → IC=+0.152 (n=937)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8866.0493 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.199 (n=573)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.161 (n=1717)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.157 (n=653)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.1857` → IC=+0.157 (n=756)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1857 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.7` → IC=+0.150 (n=287)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.7 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.241` → IC=+0.149 (n=1698)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.241 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1041` → IC=+0.147 (n=1432)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1041 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.156 (n=806)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.5273` → IC=+0.145 (n=1699)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5273 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.804` → IC=+0.153 (n=1133)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.804 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=2274)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `12052.6582` → IC=+0.158 (n=779)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12052.6582 (IC base=+0.140)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `5.24` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.24
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=327)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.158 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.006 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.158 (n=232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0036 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1007` → IC=+0.163 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1007 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.182 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 19.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.515` → IC=+0.186 (n=173)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.515 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.2459` → IC=+0.156 (n=120)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.2459 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.24` → IC=+0.160 (n=327)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 5.24 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.1808` → IC=+0.147 (n=259)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1808 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.8126` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8126 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.154 (n=290)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.409` → IC=+0.208 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.409 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.5548` → IC=+0.171 (n=86)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5548 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `12670.6541` → IC=+0.191 (n=231)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 12670.6541 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.207 (n=353)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.3723` → IC=+0.144 (n=802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3723 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.162 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.157` → IC=+0.159 (n=353)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.157 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.6124` → IC=+0.139 (n=364)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.6124 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.6099` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6099 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.052` → IC=+0.148 (n=877)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 9.052 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8763` → IC=+0.175 (n=536)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.8763 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0677` → IC=+0.160 (n=377)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0677 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.508` → IC=+0.139 (n=799)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.508 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.794` → IC=+0.146 (n=532)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.794 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `12052.6582` → IC=+0.148 (n=716)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 12052.6582 (IC base=+0.133)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.212 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.182 (n=196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0106 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.6204` → IC=+0.158 (n=431)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.6204 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.988` → IC=+0.226 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.988 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.285` → IC=+0.218 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.285 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2126` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2126 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.9185` → IC=+0.161 (n=378)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.9185 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.8333` → IC=+0.155 (n=384)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8333 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2307.5732` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2307.5732 (IC base=+0.153)

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

- **PATRÓN** `libro_liquidez` > `2362.106` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.106 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.148 (n=679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0088 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.142 (n=680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0046 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4946` → IC=+0.146 (n=679)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4946 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.138 (n=244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 4.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8027` → IC=+0.165 (n=308)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8027 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.9851` → IC=+0.182 (n=152)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.9851 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.4185` → IC=+0.148 (n=631)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.4185 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.796` → IC=+0.148 (n=679)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.796 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.113` → IC=+0.143 (n=598)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.113 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6442` → IC=+0.139 (n=679)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6442 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1741` → IC=+0.157 (n=205)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1741 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.158 (n=223)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=623)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `8379.1781` → IC=+0.149 (n=679)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8379.1781 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.177 (n=472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0072 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.5091` → IC=+0.199 (n=537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5091 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.168 (n=362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 10.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.1042` → IC=+0.172 (n=537)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.1042 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1508` → IC=+0.167 (n=253)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1508 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.3605` → IC=+0.164 (n=540)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.3605 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.041` → IC=+0.169 (n=255)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.041 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.6549` → IC=+0.191 (n=179)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6549 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.7364` → IC=+0.160 (n=480)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.7364 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.188 (n=235)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.176 (n=464)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.4479` → IC=+0.173 (n=527)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.4479 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `8306.7713` → IC=+0.172 (n=537)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8306.7713 (IC base=+0.158)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=120)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=-0.016)

- **PATRÓN** `dist_vwap_pct` > `0.7139` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.7139 (IC base=+0.018)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.121 (n=196)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.220 (n=405)

- **FILTRO** `sigma_h` > `0.0071` → IC=-0.225 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=213)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.210 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=215)

- **FILTRO** `dist_vwap_pct` > `0.1621` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1621
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=163)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.179 (n=363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0053 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.155 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.220 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.141` → IC=+0.141 (n=235)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.141 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.411` → IC=+0.177 (n=283)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.411 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `2.0655` → IC=+0.151 (n=305)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.0655 (IC base=+0.090)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=366)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `2513.2372` → IC=+0.158 (n=194)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2513.2372 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.1111` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1111 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` < `2.4035` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.4035 (IC base=-0.056)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=118)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=-0.056)

- **PATRÓN** `libro_liquidez` > `2678.2434` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2678.2434 (IC base=-0.056)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.199 (n=164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0049 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.5857` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5857 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1435` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1435 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.734` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.734 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2494` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2494 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.9335` → IC=+0.179 (n=104)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.9335 (IC base=+0.096)

- **PATRÓN** `drift_60min` |x|≤ `0.0945` → IC=+0.192 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0945 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.739` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.739 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.914` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 5.914 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.9736` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.9736 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0796` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0796 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.1936` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1936 (IC base=+0.025)

- **PATRÓN** `libro_liquidez` > `2755.8716` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2755.8716 (IC base=+0.025)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6175` → IC=-0.179 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6175
  - _Potencial_: sin este filtro IC_bueno=+0.235 (n=164)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=73)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.258 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=65)

- **FILTRO** `ibs_20min` > `0.6928` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6928
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=51)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.167 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0049 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.133 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.6175` → IC=+0.235 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6175 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.1208` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1208 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.2873` → IC=+0.139 (n=153)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2873 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.649` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.649 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.7864` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.7864 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.144 (n=147)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.6214 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.2987` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2987 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.3908 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=170)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2086.7151` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2086.7151 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.204 (n=25)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1103 (IC base=-0.082)

- **PATRÓN** `ibs_20min` < `0.2452` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.2452 (IC base=-0.082)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.211` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.211 (IC base=-0.082)

- **PATRÓN** `volumen_spike_ratio` > `2.5683` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5683 (IC base=-0.082)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0094` → IC=-0.241 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=54)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.289 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=70)

- **FILTRO** `volumen_regimen` > `1.0255` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0255
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.167 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.060)

- **PATRÓN** `ibs_20min` > `0.6744` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.6744 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `1.0643` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0643 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `2.468` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.468 (IC base=+0.060)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.124 (n=91)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.07 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `330.3847` → IC=+0.141 (n=126)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 330.3847 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.0208` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0208 (IC base=-0.120)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1654` → IC=-0.382 (n=32)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1654
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=98)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.466 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=105)

- **FILTRO** `dist_vwap_pct` > `0.2348` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=116)

- **FILTRO** `volumen_pendiente_norm` > `0.1113` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1113
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=39)

- **FILTRO** `drift_60min` |x|> `0.2275` → IC=-0.344 (n=30)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2275
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=94)

- **FILTRO** `ibs_20min` > `0.641` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `ibs_20min` > 0.641
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=66)

- **FILTRO** `dist_vwap_pct` > `0.3507` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3507
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=105)

- **FILTRO** `volumen_pendiente_norm` > `0.0765` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0765
  - _Potencial_: sin este filtro IC_bueno=-0.324 (n=32)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.6138` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6138
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `ibs_20min` > `0.3962` → IC=-0.300 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3962
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `volumen_regimen` > `0.9309` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9309
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=35)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `3.452` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.452
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

- **FILTRO** `ibs_20min` > `0.791` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.791
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `volumen_regimen` < `1.0152` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0152
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.420 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.641` → IC=-0.242 (n=60)

  - _Acción_: SKIP cuando `ibs_20min` < 0.641
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=181)

- **FILTRO** `ibs_20min` > `0.375` → IC=-0.161 (n=60)

  - _Acción_: SKIP cuando `ibs_20min` > 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=184)

- **PATRÓN** `ibs_20min` > `0.641` → IC=+0.139 (n=181)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.641 (IC base=+0.043)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.140 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 15.0 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.2727` → IC=+0.134 (n=162)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2727 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.672` → IC=+0.120 (n=77)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` > 5.672 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.0687` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0687 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `3787.1326` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3787.1326 (IC base=+0.045)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=60)

- **FILTRO** `volumen_regimen` < `0.7102` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7102
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.149 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0028 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1622 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.217` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 14.217 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.1293` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1293 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `3.3907` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 3.3907 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `1.5879` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5879 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `3644.5187` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3644.5187 (IC base=+0.116)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0036` → IC=-0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=41)

- **FILTRO** `ibs_20min` < `0.6061` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6061
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=46)

- **FILTRO** `ibs_20min` > `0.3236` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3236
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=48)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.056)

- **PATRÓN** `drift_60min` |x|≤ `0.111` → IC=+0.136 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.111 (IC base=+0.056)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.6061` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.6061 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.1167` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1167 (IC base=+0.056)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.000)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.5556` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5556
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=47)

- **FILTRO** `dist_vwap_pct` > `0.1813` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1813
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

- **FILTRO** `volumen_regimen` < `0.6649` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6649
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.179 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0047 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.9714` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.9714 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.7917 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.06 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=339)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2833.2535` → IC=+0.174 (n=127)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2833.2535 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.124 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2309.0554` → IC=+0.137 (n=428)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2309.0554 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=339)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2833.2535` → IC=+0.174 (n=127)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2833.2535 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.124 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2309.0554` → IC=+0.137 (n=428)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2309.0554 (IC base=+0.105)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `11.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=71)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=116)

- **FILTRO** `libro_liquidez` < `2359.8786` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 2359.8786
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=99)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=178)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.124 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=100)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=164)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `libro_liquidez` < `12409.8631` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 12409.8631
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `libro_liquidez` < `14445.5423` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 14445.5423
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1240)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=48)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=80)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `libro_liquidez` < `10665.27` → IC=-0.233 (n=84)

  - _Acción_: SKIP cuando `libro_liquidez` < 10665.27
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=28)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `31327.3` → IC=-0.136 (n=42)

  - _Acción_: SKIP cuando `liq_usd_total` < 31327.3
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **PATRÓN** `liq_usd_total` > `54982.77` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `liq_usd_total` > 54982.77 (IC base=+0.019)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=73)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=498)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=418)

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
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=67)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=67)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.425` → IC=-0.140 (n=145)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=446)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=200)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=200)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=172)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=150)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=150)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=90)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.151 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=124)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=40)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9979` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9979
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=205)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=205)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=67)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=5319)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.3878` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.3878
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=127)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=885)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1028)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.181 (n=2095)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=6740)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.175 (n=2143)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=7026)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.211 (n=355)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1109)

- **FILTRO** `ibs_20min` < `0.75` → IC=-0.177 (n=366)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=1098)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.202 (n=374)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=1149)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.215 (n=388)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1214)

- **FILTRO** `ibs_20min` > `0.2894` → IC=-0.184 (n=400)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2894
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1202)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.201 (n=342)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=1076)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.188 (n=399)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1216)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1745)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1596)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1602)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=152)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=87)

- **FILTRO** `drift_20min_pct` |x|> `0.1544` → IC=-0.221 (n=41)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1544
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=125)

- **FILTRO** `ibs_20min` > `0.981` → IC=-0.198 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.981
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=125)

- **FILTRO** `libro_liquidez` < `2918.5053` → IC=-0.221 (n=41)

  - _Acción_: SKIP cuando `libro_liquidez` < 2918.5053
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=125)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=510)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 16.0 (IC base=+0.033)

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
- **FILTRO** `py_entrada` < `0.35` → IC=-0.273 (n=5214)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=15914)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.234 (n=5280)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=15848)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.167 (n=7083)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=14045)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.219 (n=6570)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=19894)

- **FILTRO** `ibs_7min` > `0.2991` → IC=-0.176 (n=6613)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2991
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=19851)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=779)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=2488)

- **FILTRO** `ibs_7min` < `0.7063` → IC=-0.257 (n=1077)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7063
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2190)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.206 (n=764)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=2503)

- **FILTRO** `py_entrada` > `0.51` → IC=-0.150 (n=3045)

  - _Acción_: SKIP cuando `py_entrada` > 0.51
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=1535)

- **FILTRO** `drift_7min_pct` |x|> `0.1121` → IC=-0.129 (n=1557)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1121
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=3023)

- **FILTRO** `ibs_7min` > `0.8044` → IC=-0.205 (n=1144)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8044
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3436)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.143 (n=856)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=2900)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.251 (n=931)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=2825)

- **FILTRO** `ibs_7min` < `0.7617` → IC=-0.185 (n=939)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7617
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=2817)

- **FILTRO** `ballena_activa_n` > `163.0` → IC=-0.174 (n=936)

  - _Acción_: SKIP cuando `ballena_activa_n` > 163.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=2820)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.260 (n=873)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2910)

- **FILTRO** `ibs_7min` > `0.2503` → IC=-0.173 (n=943)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2503
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=2840)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.179 (n=940)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=2843)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.175 (n=753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=2347)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.319 (n=732)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=2368)

- **FILTRO** `ibs_7min` < `0.21` → IC=-0.274 (n=775)

  - _Acción_: SKIP cuando `ibs_7min` < 0.21
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=2325)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.215 (n=756)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=2344)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.226 (n=1109)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=3729)

- **FILTRO** `ibs_7min` > `0.2674` → IC=-0.155 (n=1643)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2674
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3195)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=1079)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=2415)

- **FILTRO** `ibs_7min` < `0.7509` → IC=-0.186 (n=873)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7509
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=2621)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.172 (n=1146)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=2348)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=879)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2679)

- **FILTRO** `ibs_7min` > `0.277` → IC=-0.176 (n=889)

  - _Acción_: SKIP cuando `ibs_7min` > 0.277
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=2669)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.179 (n=881)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=2677)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.235 (n=967)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2996)

- **FILTRO** `ibs_7min` < `0.7381` → IC=-0.198 (n=990)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7381
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2973)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.170 (n=1194)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3809)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.283 (n=856)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2692)

- **FILTRO** `ibs_7min` < `0.7315` → IC=-0.223 (n=887)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7315
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2661)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.209 (n=865)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=2683)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.191 (n=1138)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=3564)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=903)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=462)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=507)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.137 (n=615)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.139 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `130067.0` → IC=+0.144 (n=521)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 130067.0 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.126 (n=508)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 78.0 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.131)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.203 (n=72)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.146 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `498.2784` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `total_vol_5m` < 498.2784 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `9989.5319` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 9989.5319 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.116)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3997` → IC=+0.214 (n=96)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.3997 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.265 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.167)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `total_vol_5m` < 6300.756 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3155.1686` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3155.1686 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.190 (n=85)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 78.0 (IC base=+0.167)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.139 (n=95)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.108)

- **PATRÓN** `total_vol_5m` < `370723.7` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 370723.7 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `3294.4346` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3294.4346 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 41.0 (IC base=+0.108)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.275` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.275
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=68)

- **FILTRO** `pct_vs_K` |x|> `3.7615` → IC=-0.339 (n=60)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7615
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=181)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.194 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0029 (IC base=-0.123)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `63.9544` → IC=-0.397 (n=37)

  - _Acción_: SKIP cuando `T_h` > 63.9544
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=39)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.340 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=-0.091)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `291.9853` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `T_h` < 291.9853
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `4.085` → IC=-0.256 (n=84)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.085
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=166)

- **FILTRO** `T_h` > `144.6658` → IC=-0.361 (n=70)

  - _Acción_: SKIP cuando `T_h` > 144.6658
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=137)

- **FILTRO** `pct_vs_K` |x|> `3.96` → IC=-0.431 (n=70)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.96
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=137)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0036` → IC=-0.260 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

- **FILTRO** `T_h` > `63.9866` → IC=-0.153 (n=70)

  - _Acción_: SKIP cuando `T_h` > 63.9866
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=24)

- **FILTRO** `T_h` > `144.5878` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `T_h` > 144.5878
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=49)

- **FILTRO** `pct_vs_K` |x|> `2.2737` → IC=-0.447 (n=36)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.2737
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=38)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9851` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=50)

- **FILTRO** `pct_vs_K` |x|> `4.5365` → IC=-0.444 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.5365
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=50)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.380 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

- **FILTRO** `T_h` > `71.1632` → IC=-0.318 (n=53)

  - _Acción_: SKIP cuando `T_h` > 71.1632
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0109` → IC=-0.190 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0109
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `sigma_h` < `0.0142` → IC=-0.357 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `T_h` > `87.8116` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `T_h` > 87.8116
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### RESOLUTION_SNIPER
- **PATRÓN** `dist_50` > `0.4444` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.343)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.447 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.343)

- **PATRÓN** `edge` > `0.1043` → IC=+0.440 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1043 (IC base=+0.402)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.467 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.402)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.402)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.485 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.439 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.402)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1327` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1327 (IC base=+0.486)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.476 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.486)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.476 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.486)

- **PATRÓN** `T_h` > `1.1323` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1323 (IC base=+0.486)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.486)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.478 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.486)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=101)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=194)

- **PATRÓN** `streak_estiramiento` < `0.5801` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `streak_estiramiento` < 0.5801 (IC base=+0.021)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `libro_liquidez` < `2191.3335` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 2191.3335
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=65)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=80)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=394)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=400)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=270)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=390)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=772)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=431)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=497)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2037)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1091)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1099)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.187 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0039 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.197 (n=295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0083 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.177 (n=295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.168)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0592` → IC=+0.171 (n=883)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.0592 (IC base=+0.168)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0905` → IC=+0.228 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0905 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.168)

- **PATRÓN** `ibs_15` > `0.6173` → IC=+0.245 (n=883)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6173 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.1047` → IC=+0.176 (n=593)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1047 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.825` → IC=+0.248 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.825 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=824)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `3038.6807` → IC=+0.184 (n=589)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3038.6807 (IC base=+0.168)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=230)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.5998` → IC=-0.131 (n=120)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.5998
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=234)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.234 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.203 (n=234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0023 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.1873` → IC=+0.217 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1873 (IC base=+0.200)

- **PATRÓN** `drift_15min` |x|≤ `0.3761` → IC=+0.212 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3761 (IC base=+0.200)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2265` → IC=+0.212 (n=78)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2265 (IC base=+0.200)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1084` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1084 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.217 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_15` > `0.7061` → IC=+0.254 (n=234)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7061 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.1129` → IC=+0.221 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1129 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.624` → IC=+0.264 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.624 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `8560.6622` → IC=+0.225 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8560.6622 (IC base=+0.200)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `14.615` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.615
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=157)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.153 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0062 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.163 (n=93)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2448` → IC=+0.185 (n=71)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio_macro` |x|> 0.2448 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.266` → IC=+0.161 (n=125)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.266 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.140 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.6973` → IC=+0.259 (n=189)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6973 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1449` → IC=+0.169 (n=170)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1449 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.024` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.024 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=248)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `12005.5439` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 12005.5439 (IC base=+0.136)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `dist_vwap_pct` > `0.2708` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2708
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=366)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.1983` → IC=-0.231 (n=24)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1983
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=25)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.55` → IC=-0.204 (n=42)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.234 (n=126)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.182 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0081 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1325` → IC=+0.155 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1325 (IC base=+0.123)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.161 (n=113)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.123)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3249` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3249 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.139 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 8.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.141 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 4.0 (IC base=+0.123)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.234 (n=126)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.55 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.1491` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1491 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.367` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.367 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2978.7992` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2978.7992 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.123)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `dist_vwap_pct` > `0.992` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.992
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=131)

- **FILTRO** `sigma_ewma_delta_pct` < `12.892` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 12.892
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0219` → IC=+0.238 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0219 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0899` → IC=+0.182 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0899 (IC base=+0.163)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0485` → IC=+0.185 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.0485 (IC base=+0.163)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1082` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1082 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.206 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_15` > `0.5075` → IC=+0.250 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5075 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.1542` → IC=+0.181 (n=133)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1542 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.09` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.09 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.092` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 7.092 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2728.3216` → IC=+0.202 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2728.3216 (IC base=+0.163)

- **PATRÓN** `ibs_15` < `0.1091` → IC=+0.169 (n=276)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.1091 (IC base=+0.044)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.336 (n=181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.393 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.338)

- **PATRÓN** `drift_60min` |x|≤ `0.1153` → IC=+0.352 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1153 (IC base=+0.338)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.343 (n=271)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.338)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.350 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.338)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.386 (n=271)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.338)

- **PATRÓN** `dist_vwap_pct` > `0.424` → IC=+0.353 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.424 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.994` → IC=+0.356 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.994 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` < `24.027` → IC=+0.337 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 24.027 (IC base=+0.338)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.345 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.338)

- **PATRÓN** `libro_liquidez` > `3987.1822` → IC=+0.352 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3987.1822 (IC base=+0.338)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1118` → IC=+0.354 (n=53)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1118 (IC base=+0.333)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.336 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.352 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.343 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.333)

- **PATRÓN** `drift_15min` |x|≤ `0.4089` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4089 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0919` → IC=+0.338 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0919 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.361 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.333)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.331 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.373 (n=156)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.2458` → IC=+0.373 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2458 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.561` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.561 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.292` → IC=+0.345 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.292 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `8997.0825` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8997.0825 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `613.0` → IC=+0.400 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 613.0 (IC base=+0.333)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.391 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.339)

- **PATRÓN** `drift_60min` |x|≤ `0.0771` → IC=+0.387 (n=51)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0771 (IC base=+0.339)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0624` → IC=+0.363 (n=115)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0624 (IC base=+0.339)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.349 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.339)

- **PATRÓN** `ibs_15` > `0.7785` → IC=+0.406 (n=115)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7785 (IC base=+0.339)

- **PATRÓN** `dist_vwap_pct` < `0.2966` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2966 (IC base=+0.339)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.292` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.292 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.358 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `3553.0968` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3553.0968 (IC base=+0.339)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.375 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.339)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.012` → IC=-0.207 (n=473)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.012
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1421)

- **FILTRO** `ibs_15` < `0.5753` → IC=-0.189 (n=159)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5753
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=479)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=558)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.214 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.056)

- **PATRÓN** `ibs_15` > `0.5753` → IC=+0.244 (n=479)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5753 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.171 (n=372)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.056)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1192` → IC=+0.230 (n=590)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1192 (IC base=-0.051)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1809` → IC=+0.232 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1809 (IC base=-0.051)

- **PATRÓN** `ibs_15` < `0.3659` → IC=+0.271 (n=886)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3659 (IC base=-0.051)

- **PATRÓN** `dist_vwap_pct` > `0.6445` → IC=+0.256 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6445 (IC base=-0.051)

- **PATRÓN** `dist_vwap_pct` < `0.2256` → IC=+0.220 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2256 (IC base=-0.051)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.214 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=865)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.228 (n=380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=773)

- **FILTRO** `sigma_ewma_delta_pct` > `20.172` → IC=-0.250 (n=210)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.172
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=943)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.177 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.217` → IC=+0.265 (n=32)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.217 (IC base=+0.070)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.070)

- **PATRÓN** `ibs_15` > `0.7648` → IC=+0.364 (n=86)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7648 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.284 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.070)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6314` → IC=-0.256 (n=76)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6314
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=230)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=289)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.129 (n=230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0066 (IC base=+0.123)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.164 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.004 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.222 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.123)

- **PATRÓN** `drift_15min` |x|≤ `0.4223` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.4223 (IC base=+0.123)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1288` → IC=+0.132 (n=153)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.1288 (IC base=+0.123)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.216 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.123)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.250 (n=230)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6314 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.1621` → IC=+0.158 (n=179)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1621 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.094` → IC=+0.139 (n=181)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 7.094 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=289)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `10544.7398` → IC=+0.210 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10544.7398 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.225 (n=329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3509` → IC=+0.225 (n=329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3509 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `0.4628` → IC=+0.225 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4628 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2036` → IC=+0.237 (n=169)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2036 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.213 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.229 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.260 (n=373)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.7277` → IC=+0.250 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7277 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.993` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.993 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.572` → IC=+0.217 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.572 (IC base=+0.211)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1655` → IC=-0.214 (n=159)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1655
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=309)

- **FILTRO** `drift_15min` |x|> `0.8627` → IC=-0.229 (n=116)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8627
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=352)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.202 (n=166)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=302)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1145` → IC=+0.212 (n=130)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1145 (IC base=-0.043)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.194` → IC=+0.177 (n=125)

  - _Acción_: Kelly boost +0.89€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.194 (IC base=-0.043)

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.242 (n=196)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` < `0.143` → IC=+0.196 (n=179)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.143 (IC base=-0.043)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0185` → IC=-0.253 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0185
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=274)

- **FILTRO** `drift_60min` |x|> `0.1593` → IC=-0.181 (n=136)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1593
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=411)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0991` → IC=+0.380 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0991 (IC base=-0.049)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.299 (n=247)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.049)

- **PATRÓN** `dist_vwap_pct` > `0.498` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.498 (IC base=-0.049)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.4249` → IC=+0.154 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4249 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.588` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.588 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1147` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1147 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.088)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.4249` → IC=+0.154 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4249 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.588` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.588 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1147` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1147 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.088)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.300 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.291 (n=462)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.340 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.226` → IC=+0.333 (n=154)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.226 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1069` → IC=+0.318 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1069 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8341` → IC=+0.332 (n=462)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8341 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.318 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.501` → IC=+0.310 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.501 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `12476.4494` → IC=+0.316 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12476.4494 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.300 (n=173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0625` → IC=+0.309 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0625 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2286` → IC=+0.332 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2286 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.340 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8545` → IC=+0.325 (n=232)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8545 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.447` → IC=+0.338 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.447 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.523` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.523 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `15220.5605` → IC=+0.332 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15220.5605 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.301 (n=179)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.300 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0037 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.343 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1898` → IC=+0.330 (n=92)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1898 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2248` → IC=+0.347 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2248 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.318 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.339 (n=203)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` < `0.1631` → IC=+0.301 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1631 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.579` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.579 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.310 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `11977.5569` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11977.5569 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `170.0` → IC=+0.303 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 170.0 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0876` → IC=-0.271 (n=59)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0876
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=178)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.244 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=157)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1209` → IC=-0.157 (n=106)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1209
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=320)

- **FILTRO** `drift_15min` |x|> `0.5291` → IC=-0.130 (n=106)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5291
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=320)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2192` → IC=-0.162 (n=63)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2192
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=64)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.167 (n=43)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=88)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2312` → IC=-0.204 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2312
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1977` → IC=-0.143 (n=26)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1977
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1979` → IC=-0.382 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1979
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.1352` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1352
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **FILTRO** `ratio` > `0.9937` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `ratio` > 0.9937
  - _Potencial_: sin este filtro IC_bueno=+0.337 (n=127)

- **PATRÓN** `T_h` < `83.3501` → IC=+0.128 (n=84)

  - _Acción_: Kelly boost +0.64€ cuando `T_h` < 83.3501 (IC base=+0.122)

- **PATRÓN** `T_h` > `63.9922` → IC=+0.124 (n=187)

  - _Acción_: Kelly boost +0.62€ cuando `T_h` > 63.9922 (IC base=+0.122)

- **PATRÓN** `ratio` < `0.9937` → IC=+0.337 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9937 (IC base=+0.122)

- **PATRÓN** `T_h` > `145.9123` → IC=+0.408 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.9123 (IC base=+0.347)

- **PATRÓN** `ratio` > `1.012` → IC=+0.356 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.347)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9997` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `T_h` > 111.9997 (IC base=+0.090)

- **PATRÓN** `ratio` < `0.9956` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9956 (IC base=+0.090)

- **PATRÓN** `T_h` > `87.9882` → IC=+0.296 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9882 (IC base=+0.293)

- **PATRÓN** `ratio` > `1.0349` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0349 (IC base=+0.293)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9922` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `T_h` > 111.9922 (IC base=+0.179)

- **PATRÓN** `ratio` < `0.9911` → IC=+0.415 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9911 (IC base=+0.179)

- **PATRÓN** `T_h` > `87.9955` → IC=+0.347 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9955 (IC base=+0.326)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.326)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.406)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6173 sube el IC de +0.168 a +0.245 en UPDOWN_GBM#15min (n=883). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7061 sube el IC de +0.200 a +0.254 en UPDOWN_GBM#BTC#15min (n=234). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6973 sube el IC de +0.136 a +0.259 en UPDOWN_GBM#ETH#15min (n=189). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.123 a +0.234 en UPDOWN_GBM#SOL#15min (n=126). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5075 sube el IC de +0.163 a +0.250 en UPDOWN_GBM#XRP#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1091 sube el IC de +0.044 a +0.169 en UPDOWN_GBM#XRP#15min (n=276). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5753 sube el IC de -0.056 a +0.244 en UPDOWN_GBM_15M_TARDIO (n=479). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3659 sube el IC de -0.051 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=886). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7648 sube el IC de +0.070 a +0.364 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=86). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6314 sube el IC de +0.123 a +0.250 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=230). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3605 sube el IC de +0.211 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=373). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.143 a +0.333 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.043 a +0.242 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=196). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.049 a +0.299 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=247). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8341 sube el IC de +0.291 a +0.332 en UPDOWN_GBM_IBS_ALTO (n=462). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8545 sube el IC de +0.287 a +0.325 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=232). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.294 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=203). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.338 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=271). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.333 a +0.373 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=156). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7785 sube el IC de +0.339 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=115). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH#sniper` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1063 | +0.081 | +105.63€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1063 | +0.081 | +105.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 765 | +0.088 | +84.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 765 | +0.088 | +84.73€ | 3 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 224 | +0.040 | +1.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 224 | +0.040 | +1.71€ | 3 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 48 | +0.180 | +20.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 48 | +0.180 | +20.69€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS | 20363 | -0.108 | -3135.29€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1111 | -0.031 | -190.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 19252 | -0.113 | -2944.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 2833 | -0.108 | -522.11€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 2833 | -0.108 | -522.11€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1111 | -0.031 | -190.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1111 | -0.031 | -190.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 2631 | -0.099 | -616.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 2631 | -0.099 | -616.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5279 | -0.070 | -487.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5279 | -0.070 | -487.01€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 4674 | -0.121 | -368.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 4674 | -0.121 | -368.22€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 3835 | -0.175 | -950.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 3835 | -0.175 | -950.70€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 9089 | -0.055 | +3728.70€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 2510 | -0.011 | +1636.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 6579 | -0.071 | +2092.40€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 9089 | -0.055 | +3728.70€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 2510 | -0.011 | +1636.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 6579 | -0.071 | +2092.40€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 284 | -0.094 | -46.40€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 5 | +0.018 | +0.75€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 279 | -0.098 | -47.15€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 15 | -0.066 | +0.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 15 | -0.066 | +0.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 190 | -0.036 | -15.97€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 190 | -0.036 | -15.97€ | 1 | 1 |
| 🚫 CANDIDATA9_BOT_CONSENSO#ETH | 70 | -0.208 | -22.80€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 5 | +0.018 | +0.75€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#ETH#5min | 65 | -0.231 | -23.55€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 6 | -0.113 | -6.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 6 | -0.113 | -6.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 64401 | +0.112 | -3631.55€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 10344 | +0.182 | -325.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 245 | -0.111 | -47.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 49460 | +0.099 | -3179.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 4352 | +0.116 | -79.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 8256 | +0.092 | -873.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 34 | -0.167 | -0.75€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 8207 | +0.094 | -860.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 12766 | +0.132 | -255.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3113 | +0.203 | -88.57€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 8196 | +0.108 | -183.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1415 | +0.120 | +38.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 8293 | +0.086 | -886.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 39 | -0.037 | -2.52€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 8239 | +0.088 | -872.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 13882 | +0.126 | -260.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 3948 | +0.169 | -81.91€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 8248 | +0.111 | -127.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1674 | +0.099 | -41.76€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 12931 | +0.116 | -798.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3178 | +0.186 | -157.56€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 148 | -0.053 | +6.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 8342 | +0.090 | -570.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1263 | +0.136 | -76.23€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 8273 | +0.100 | -558.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 32 | +0.000 | +6.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 8228 | +0.101 | -564.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 10061 | +0.184 | -728.10€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 10061 | +0.184 | -728.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2568 | +0.168 | -274.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2568 | +0.168 | -274.58€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 149 | -0.136 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 149 | -0.136 | -0.83€ | 4 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2524 | +0.178 | -231.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2524 | +0.178 | -231.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2272 | +0.239 | -55.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2272 | +0.239 | -55.53€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2469 | +0.187 | -179.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2469 | +0.187 | -179.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 484 | +0.442 | -0.23€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 484 | +0.442 | -0.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 189 | +0.442 | +0.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 189 | +0.442 | +0.84€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 184 | +0.441 | +0.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 184 | +0.441 | +0.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 105 | +0.425 | -2.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 105 | +0.425 | -2.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 34874 | +0.191 | -3078.17€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 34874 | +0.191 | -3078.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 6123 | +0.162 | -844.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 6123 | +0.162 | -844.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 5485 | +0.221 | -220.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 5485 | +0.221 | -220.22€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 6044 | +0.165 | -796.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 6044 | +0.165 | -796.95€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 5587 | +0.219 | -219.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 5587 | +0.219 | -219.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 5769 | +0.198 | -428.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 5769 | +0.198 | -428.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 5866 | +0.187 | -569.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 5866 | +0.187 | -569.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 12919 | +0.124 | +274.78€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 12919 | +0.124 | +274.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 6400 | +0.130 | +202.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 6400 | +0.130 | +202.75€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 6519 | +0.118 | +72.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 6519 | +0.118 | +72.03€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1133 | +0.291 | -14.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1133 | +0.291 | -14.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 499 | +0.276 | -14.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 499 | +0.276 | -14.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 537 | +0.296 | +1.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 537 | +0.296 | +1.70€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 97 | +0.328 | -1.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 97 | +0.328 | -1.32€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 500 | +0.426 | -10.96€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 500 | +0.426 | -10.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 230 | +0.427 | -4.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 230 | +0.427 | -4.87€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 233 | +0.428 | -5.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 233 | +0.428 | -5.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 37 | +0.372 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 37 | +0.372 | -0.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 714 | +0.075 | -28.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 253 | +0.069 | -16.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 461 | +0.079 | -12.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 47 | +0.092 | +0.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 47 | +0.092 | +0.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 555 | +0.087 | -6.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 94 | +0.125 | +5.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 461 | +0.079 | -12.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 112 | +0.009 | -21.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 112 | +0.009 | -21.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 21928 | +0.095 | -755.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1879 | +0.088 | +14.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 20049 | +0.096 | -769.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 12673 | +0.100 | -229.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1879 | +0.088 | +14.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 10794 | +0.102 | -243.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 3550 | +0.111 | +14.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 3550 | +0.111 | +14.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 5705 | +0.075 | -539.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 5705 | +0.075 | -539.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 651 | +0.261 | -77.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 651 | +0.261 | -77.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 651 | +0.261 | -77.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 651 | +0.261 | -77.30€ | 0 | 4 |
| ✅ GBM_LATE_15M | 16865 | +0.071 | +7538.51€ | 0 | 13 |
| ✅ GBM_LATE_15M#15min | 16865 | +0.071 | +7538.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 2729 | +0.199 | +2038.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 2729 | +0.199 | +2038.77€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 2498 | +0.174 | +1681.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2498 | +0.174 | +1681.25€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 2828 | +0.195 | +2059.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 2828 | +0.195 | +2059.11€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 2546 | -0.009 | +324.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2546 | -0.009 | +324.86€ | 2 | 12 |
| ✅ GBM_LATE_15M#SOL | 2533 | -0.041 | +569.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2533 | -0.041 | +569.57€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 3731 | -0.055 | +864.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 3731 | -0.055 | +864.94€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 17715 | +0.074 | +8990.20€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 17715 | +0.074 | +8990.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3191 | +0.009 | +1873.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3191 | +0.009 | +1873.04€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 3784 | -0.001 | +692.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 3784 | -0.001 | +692.39€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2471 | +0.258 | +2446.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2471 | +0.258 | +2446.46€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2685 | -0.032 | +208.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2685 | -0.032 | +208.72€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2964 | +0.010 | +1064.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2964 | +0.010 | +1064.21€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2620 | +0.267 | +2705.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2620 | +0.267 | +2705.37€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 13766 | +0.169 | +9924.08€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 13766 | +0.169 | +9924.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2001 | +0.211 | +1624.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2001 | +0.211 | +1624.88€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2196 | +0.158 | +1542.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2196 | +0.158 | +1542.93€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2087 | +0.205 | +1637.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2087 | +0.205 | +1637.84€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2269 | +0.140 | +1466.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2269 | +0.140 | +1466.05€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2606 | +0.113 | +1624.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2606 | +0.113 | +1624.42€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2607 | +0.200 | +2027.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2607 | +0.200 | +2027.95€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 3291 | +0.118 | +1194.68€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 3291 | +0.118 | +1194.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 105 | +0.107 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 105 | +0.107 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 910 | +0.107 | +322.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 910 | +0.107 | +322.85€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 900 | +0.147 | +372.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 900 | +0.147 | +372.58€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 621 | +0.065 | +125.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 621 | +0.065 | +125.21€ | 2 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 387 | +0.130 | +151.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 387 | +0.130 | +151.73€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO | 16876 | +0.174 | +12143.66€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 16876 | +0.174 | +12143.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 2613 | +0.225 | +2244.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 2613 | +0.225 | +2244.73€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2668 | +0.154 | +1784.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2668 | +0.154 | +1784.97€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 2681 | +0.221 | +2258.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 2681 | +0.221 | +2258.96€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 2662 | +0.134 | +1670.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 2662 | +0.134 | +1670.66€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2976 | +0.107 | +1633.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2976 | +0.107 | +1633.75€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3276 | +0.203 | +2550.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3276 | +0.203 | +2550.59€ | 0 | 24 |
| ✅ GBM_LATE_5M | 5042 | +0.134 | +2594.18€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 5042 | +0.134 | +2594.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 474 | +0.176 | +313.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 474 | +0.176 | +313.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1412 | +0.135 | +821.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1412 | +0.135 | +821.53€ | 1 | 26 |
| ✅ GBM_LATE_5M#DOGE | 633 | +0.163 | +380.44€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 633 | +0.163 | +380.44€ | 0 | 21 |
| ✅ GBM_LATE_5M#ETH | 1620 | +0.147 | +867.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1620 | +0.147 | +867.97€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 261 | -0.002 | +11.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 261 | -0.002 | +11.37€ | 2 | 2 |
| ✅ GBM_LATE_5M#XRP | 642 | +0.096 | +199.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 642 | +0.096 | +199.29€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1043 | +0.045 | +347.66€ | 4 | 14 |
| ✅ GBM_LATE_60M#60min | 1043 | +0.045 | +347.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 366 | +0.073 | +124.17€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 366 | +0.073 | +124.17€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 355 | +0.057 | +132.84€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 355 | +0.057 | +132.84€ | 4 | 17 |
| ✅ GBM_LATE_60M#SOL | 322 | +0.000 | +90.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 322 | +0.000 | +90.65€ | 3 | 9 |
| 🚫 GBM_LATE_60M_FADE | 262 | -0.280 | -32.64€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 262 | -0.280 | -32.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 100 | -0.235 | -8.55€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 100 | -0.235 | -8.55€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 87 | -0.332 | -20.74€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 87 | -0.332 | -20.74€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 75 | -0.266 | -3.34€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 75 | -0.266 | -3.34€ | 2 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 485 | +0.044 | +69.36€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 485 | +0.044 | +69.36€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 189 | +0.050 | +25.61€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 189 | +0.050 | +25.61€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 133 | +0.026 | -9.21€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 133 | +0.026 | -9.21€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 163 | +0.051 | +52.96€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 163 | +0.051 | +52.96€ | 3 | 6 |
| ✅ LATE_WINDOW_5MIN | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1076 | +0.108 | +323.21€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1076 | +0.108 | +323.21€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1076 | +0.108 | +323.21€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1076 | +0.108 | +323.21€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M | 331 | -0.095 | -37.20€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 331 | -0.095 | -37.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 78 | -0.100 | -9.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 78 | -0.100 | -9.01€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 106 | -0.028 | -4.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 106 | -0.028 | -4.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1437 | -0.007 | -12.06€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1437 | -0.007 | -12.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 163 | -0.021 | +0.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 163 | -0.021 | +0.58€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 101 | -0.053 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 101 | -0.053 | -6.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 544 | +0.020 | +13.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 544 | +0.020 | +13.24€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 458 | -0.006 | -8.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 458 | -0.006 | -8.22€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 96 | -0.061 | -5.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 96 | -0.061 | -5.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 806 | -0.041 | -19.81€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 806 | -0.041 | -19.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 236 | -0.063 | -16.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 236 | -0.063 | -16.45€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 253 | -0.014 | +1.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 253 | -0.014 | +1.76€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 317 | -0.045 | -5.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 317 | -0.045 | -5.12€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 11155 | -0.009 | -146.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 11155 | -0.009 | -146.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 577 | -0.009 | +0.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 577 | -0.009 | +0.01€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 1821 | -0.020 | -36.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 1821 | -0.020 | -36.71€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2555 | +0.008 | -16.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2555 | +0.008 | -16.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2118 | -0.012 | -3.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2118 | -0.012 | -3.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 2598 | -0.018 | -60.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 2598 | -0.018 | -60.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1486 | -0.005 | -30.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1486 | -0.005 | -30.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 18004 | -0.017 | +878.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 18004 | -0.017 | +878.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3095 | +0.005 | +475.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3095 | +0.005 | +475.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 2919 | -0.029 | -22.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 2919 | -0.029 | -22.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3125 | -0.004 | +257.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3125 | -0.004 | +257.62€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 2797 | -0.046 | -54.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 2797 | -0.046 | -54.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3035 | -0.022 | +127.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3035 | -0.022 | +127.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3033 | -0.012 | +95.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3033 | -0.012 | +95.06€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 3442 | -0.029 | -72.34€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 3442 | -0.029 | -72.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 625 | +0.001 | -11.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 625 | +0.001 | -11.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 555 | -0.046 | -16.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 555 | -0.046 | -16.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 40 | -0.119 | -5.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 40 | -0.119 | -5.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 333 | -0.103 | -4.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 333 | -0.103 | -4.90€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1113 | -0.022 | -11.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1113 | -0.022 | -11.98€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 776 | -0.014 | -22.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 776 | -0.014 | -22.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M | 3186 | +0.004 | -3.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3186 | +0.004 | -3.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1387 | +0.007 | -0.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1387 | +0.007 | -0.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 47592 | -0.074 | +928.72€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 47592 | -0.074 | +928.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 7847 | -0.085 | +436.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 7847 | -0.085 | +436.68€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 7539 | -0.087 | -278.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 7539 | -0.087 | -278.21€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 7938 | -0.072 | +397.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 7938 | -0.072 | +397.87€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 7052 | -0.096 | -268.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 7052 | -0.096 | -268.97€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 8966 | -0.046 | +256.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 8966 | -0.046 | +256.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 8250 | -0.063 | +384.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 8250 | -0.063 | +384.97€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6542 | -0.018 | -112.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6542 | -0.018 | -112.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1423 | -0.017 | -15.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1423 | -0.017 | -15.53€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1431 | -0.011 | -10.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1431 | -0.011 | -10.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 953 | -0.029 | -12.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 953 | -0.029 | -12.59€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 858 | +0.113 | +292.98€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 722 | +0.123 | +280.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 166 | +0.131 | +77.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 166 | +0.131 | +77.19€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 144 | +0.089 | +30.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 144 | +0.089 | +30.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 144 | +0.116 | +56.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 144 | +0.116 | +56.74€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 127 | +0.167 | +73.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 127 | +0.167 | +73.67€ | 0 | 7 |
| ✅ ORDER_FLOW_5M#XRP | 141 | +0.108 | +42.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 141 | +0.108 | +42.70€ | 0 | 5 |
| ✅ PRICE_TARGET_GBM | 410 | -0.100 | -12.69€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 180 | -0.154 | -36.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 146 | -0.196 | -37.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 34 | +0.028 | +0.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 148 | -0.087 | +4.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 110 | -0.098 | -1.87€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 38 | -0.050 | +6.62€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 82 | +0.000 | +19.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 63 | -0.023 | +12.47€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 19 | +0.068 | +6.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 319 | -0.129 | -26.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 91 | +0.005 | +14.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 457 | -0.219 | -30.11€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 194 | -0.199 | -26.68€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 168 | -0.188 | -24.38€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 26 | -0.250 | -2.30€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 160 | -0.247 | -19.85€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 137 | -0.255 | -23.72€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 23 | -0.180 | +3.88€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 103 | -0.205 | +16.41€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 89 | -0.203 | +13.35€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 394 | -0.217 | -34.75€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 63 | -0.223 | +4.64€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 159 | +0.388 | +106.60€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#BTC | 21 | -0.022 | -5.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 21 | -0.022 | -5.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 37 | +0.321 | +34.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 37 | +0.321 | +34.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 101 | +0.490 | +77.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 101 | +0.490 | +77.58€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#sniper | 159 | +0.388 | +106.60€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 333 | +0.016 | -5.30€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 333 | +0.016 | -5.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 148 | +0.040 | +2.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 148 | +0.040 | +2.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 22 | +0.042 | +1.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 22 | +0.042 | +1.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 34 | -0.056 | -6.55€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 34 | -0.056 | -6.55€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 129 | +0.004 | -2.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 129 | +0.004 | -2.50€ | 1 | 0 |
| ✅ STREAK_FADE_5M | 2233 | -0.024 | -99.50€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2233 | -0.024 | -99.50€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 559 | -0.024 | -23.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 559 | -0.024 | -23.97€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 146 | -0.041 | -13.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 146 | -0.041 | -13.44€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 724 | -0.028 | -35.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 724 | -0.028 | -35.15€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 48 | +0.020 | +0.80€ | 1 | 0 |
| ✅ STREAK_FADE_60M#60min | 48 | +0.020 | +0.80€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 29 | -0.048 | -1.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 29 | -0.048 | -1.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 5450 | +0.022 | +79.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 5450 | +0.022 | +79.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1774 | +0.025 | +24.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1774 | +0.025 | +24.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1127 | +0.037 | +37.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1127 | +0.037 | +37.69€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1579 | +0.008 | -5.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1579 | +0.008 | -5.71€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 970 | +0.024 | +22.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 970 | +0.024 | +22.27€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5301 | +0.013 | -23.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5301 | +0.013 | -23.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2056 | +0.020 | +1.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2056 | +0.020 | +1.91€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2122 | +0.016 | -3.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2122 | +0.016 | -3.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1123 | -0.004 | -21.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1123 | -0.004 | -21.66€ | 2 | 0 |
| ✅ UPDOWN_GBM | 18819 | +0.024 | +959.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 5554 | +0.053 | +826.94€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 736 | +0.003 | +7.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 11312 | +0.016 | +134.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1130 | -0.004 | -12.85€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 1469 | +0.064 | +127.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 238 | +0.121 | +68.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 17 | -0.022 | -0.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1214 | +0.054 | +59.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 3210 | +0.030 | +230.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 665 | +0.086 | +162.24€ | 1 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 215 | +0.030 | +7.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1810 | +0.019 | +60.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 488 | +0.000 | -2.77€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 32 | -0.118 | +2.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 2250 | +0.019 | +47.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 196 | +0.106 | +50.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 12 | +0.000 | -0.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2042 | +0.011 | -2.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 3779 | +0.011 | +140.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1537 | +0.035 | +147.04€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 203 | +0.007 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 1585 | -0.004 | -13.90€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 425 | -0.008 | -4.97€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 29 | -0.145 | +4.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 5097 | +0.015 | +109.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1489 | +0.021 | +78.84€ | 1 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 197 | -0.007 | -2.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 3170 | +0.016 | +38.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 217 | -0.007 | -5.11€ | 2 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 24 | -0.154 | -0.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3012 | +0.035 | +305.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1429 | +0.072 | +319.62€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 92 | -0.043 | -5.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1491 | +0.005 | -8.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 85 | -0.144 | +5.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 361 | +0.338 | +98.07€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 361 | +0.338 | +98.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 208 | +0.333 | +50.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 208 | +0.333 | +50.71€ | 0 | 15 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 153 | +0.339 | +47.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 153 | +0.339 | +47.35€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO | 7780 | -0.053 | +1615.50€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 7780 | -0.053 | +1615.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 359 | -0.046 | +350.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 359 | -0.046 | +350.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1539 | -0.133 | -67.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1539 | -0.133 | -67.86€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 124 | +0.095 | +37.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 124 | +0.095 | +37.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 803 | +0.178 | +436.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 803 | +0.178 | +436.50€ | 2 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2520 | -0.061 | +426.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2520 | -0.061 | +426.83€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2435 | -0.078 | +432.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2435 | -0.078 | +432.17€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 83 | +0.065 | +8.06€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 83 | +0.065 | +8.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 83 | +0.065 | +8.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 83 | +0.065 | +8.06€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 615 | +0.291 | +503.84€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 615 | +0.291 | +503.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 345 | +0.287 | +269.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 345 | +0.287 | +269.17€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 270 | +0.294 | +234.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 270 | +0.294 | +234.68€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 663 | -0.104 | -76.42€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 663 | -0.104 | -76.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 169 | -0.061 | -11.14€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 169 | -0.061 | -11.14€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 64 | -0.182 | -10.25€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 64 | -0.182 | -10.25€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 52 | -0.167 | -5.48€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 52 | -0.167 | -5.48€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1696 | +0.300 | +841.58€ | 1 | 5 |
| ✅ WEEKLY_PRICE#BTC | 557 | +0.235 | +67.93€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 585 | +0.289 | +222.97€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 554 | +0.374 | +550.68€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.067) — sin ventaja clara. oversold(IBS<0.3): IC=+0.038 n=6583 | neutral: IC=+0.023 n=7223 | overbought(IBS>0.7): IC=+0.090 n=7052
  - _Datos_: n=21583 IC=+0.051 PNL=+2543.15€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 383 celda(s) pasan gate riguroso completo de 1898 evaluadas (n>=40) y 2847 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.021 < 0.08 — monitorear
  - _Datos_: n=1487 IC=+0.021 PNL=+79.86€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=585/15 IC=+0.289 PNL=+222.97€ | BTC: n=557/15 IC=+0.235 PNL=+67.93€ | SOL: n=554/15 IC=+0.374 PNL=+550.68€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 27 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 18717 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.049 n=131/60 | contraria IC=+0.114 n=125 | gap=-0.065 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=199, boost estimado=-0.002. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 127 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=424/40 IC=-0.007 PNL=-4.46€ | BTC#60min: n=487/40 IC=+0.001 PNL=-2.26€ | SOL#60min: n=217/40 IC=-0.007 PNL=-5.11€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.057 n=219862 | tras_1loss IC=+0.065 n=172700 | tras_2loss IC=+0.032 n=75147/40 | gap=+0.025 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.000 n=1732 | contrario_BTC IC=+0.018 n=1624/40 | gap=+0.018 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.08 con n=166 PNL=+108.29€
  - _Datos_: n=166 IC=+0.196 PNL=+108.29€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.185 > 0.08 con n=217 PNL=+118.76€
  - _Datos_: n=217 IC=+0.185 PNL=+118.76€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.242 > 0.08 con n=29 PNL=+21.27€
  - _Datos_: n=29 IC=+0.242 PNL=+21.27€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.340 > 0.1 con n=1425 PNL=+834.71€
  - _Datos_: n=1425 IC=+0.340 PNL=+834.71€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=138 IC=+0.071 PNL=+19.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=138 IC=+0.071 PNL=+19.45€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=39 IC=+0.183 PNL=+24.69€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=39 IC=+0.183 PNL=+24.69€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=18250 IC=+0.023 PNL=+876.64€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=18250 IC=+0.023 PNL=+876.64€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 2/15 ops en el filtro definido (IC actual=+0.025 PNL=+3.18€)
  - _Datos_: n=2 IC=+0.025 PNL=+3.18€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=844 IC=+0.000 PNL=-8.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=844 IC=+0.000 PNL=-8.81€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=284 IC=-0.014 PNL=-3.02€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=284 IC=-0.014 PNL=-3.02€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=295 IC=+0.025 PNL=+18.62€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=295 IC=+0.025 PNL=+18.62€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.1 con n=1171 PNL=+609.15€
  - _Datos_: n=1171 IC=+0.167 PNL=+609.15€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=337 IC=+0.049 PNL=+46.89€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=337 IC=+0.049 PNL=+46.89€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=663 IC=+0.086 PNL=+162.17€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=663 IC=+0.086 PNL=+162.17€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=3184 IC=+0.055 PNL=+525.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3184 IC=+0.055 PNL=+525.32€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=86 IC=-0.216 PNL=-2.94€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=86 IC=-0.216 PNL=-2.94€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=157 IC=-0.016 PNL=+15.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=157 IC=-0.016 PNL=+15.57€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=268 IC=+0.018 PNL=+19.23€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=268 IC=+0.018 PNL=+19.23€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=17 IC=-0.022 PNL=-1.11€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=17 IC=-0.022 PNL=-1.11€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2938 IC=-0.009 PNL=-29.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2938 IC=-0.009 PNL=-29.43€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.156 > 0.08 con n=59 PNL=+12.92€
  - _Datos_: n=59 IC=+0.156 PNL=+12.92€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.227 n=53) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=53 IC=+0.227 PNL=+25.89€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=3988 IC=+0.024 PNL=+194.60€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3988 IC=+0.024 PNL=+194.60€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=1307 IC=+0.050 PNL=+131.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1307 IC=+0.050 PNL=+131.46€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=258 PNL=+64.56€
  - _Datos_: n=258 IC=+0.100 PNL=+64.56€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.152 > 0.08 con n=334 PNL=+71.82€
  - _Datos_: n=334 IC=+0.152 PNL=+71.82€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=271 PNL=+138.63€
  - _Datos_: n=271 IC=+0.126 PNL=+138.63€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=27153 IC=+0.103 PNL=+8552.65€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=27153 IC=+0.103 PNL=+8552.65€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=1792 IC=+0.109 PNL=+195.82€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=1792 IC=+0.109 PNL=+195.82€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=2599 IC=+0.033 PNL=+163.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2599 IC=+0.033 PNL=+163.04€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=482 PNL=+178.53€
  - _Datos_: n=482 IC=+0.124 PNL=+178.53€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=131 IC=-0.049 PNL=+33.33€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=131 IC=-0.049 PNL=+33.33€

**〰️ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: n≥25 y IC<-0.10 para confirmar (evidencia inicial es de solo 3 ops)
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: n=81 IC=-0.030 PNL=+3.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=81 IC=-0.030 PNL=+3.88€

**🟡 H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: n≥25 y IC>+0.10 para confirmar
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.450 > 0.1 con n=870 PNL=+849.21€
  - _Datos_: n=870 IC=+0.450 PNL=+849.21€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=5546 IC=+0.048 PNL=+654.77€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=5546 IC=+0.048 PNL=+654.77€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.188 > 0.1 con n=1840 PNL=+906.70€
  - _Datos_: n=1840 IC=+0.188 PNL=+906.70€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.125 < -0.1 con n=126 PNL=+17.90€
  - _Datos_: n=126 IC=-0.125 PNL=+17.90€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1100 IC=+0.044 PNL=+124.95€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1100 IC=+0.044 PNL=+124.95€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=49 IC=-0.108 PNL=+7.40€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=49 IC=-0.108 PNL=+7.40€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.143 > 0.1 con n=208 PNL=+67.53€
  - _Datos_: n=208 IC=+0.143 PNL=+67.53€

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
  - _Estado_: n=11477 IC=-0.141 PNL=+583.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11477 IC=-0.141 PNL=+583.49€

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
  - _Estado_: n=1298 IC=+0.140 PNL=+690.42€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1298 IC=+0.140 PNL=+690.42€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.169 > 0.08 con n=1132 PNL=+596.52€
  - _Datos_: n=1132 IC=+0.169 PNL=+596.52€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=1901 IC=+0.015 PNL=+38.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1901 IC=+0.015 PNL=+38.24€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.080 > 0.08 con n=1339 PNL=+727.67€
  - _Datos_: n=1339 IC=+0.080 PNL=+727.67€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.08 con n=309 PNL=+148.77€
  - _Datos_: n=309 IC=+0.198 PNL=+148.77€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.241 < -0.1 con n=1186 PNL=-166.39€
  - _Datos_: n=1186 IC=-0.241 PNL=-166.39€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=3305 IC=+0.140 PNL=+1941.40€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=3305 IC=+0.140 PNL=+1941.40€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.08 con n=57 PNL=+24.53€
  - _Datos_: n=57 IC=+0.127 PNL=+24.53€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=1321 IC=+0.034 PNL=+260.92€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1321 IC=+0.034 PNL=+260.92€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.185 > 0.08 con n=1191 PNL=+813.51€
  - _Datos_: n=1191 IC=+0.185 PNL=+813.51€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1955 IC=-0.043 PNL=+460.20€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1955 IC=-0.043 PNL=+460.20€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.097 > 0.08 con n=420 PNL=-42.58€
  - _Datos_: n=420 IC=+0.097 PNL=-42.58€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.08 con n=2457 PNL=-252.92€
  - _Datos_: n=2457 IC=+0.227 PNL=-252.92€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 24/40 ops en el filtro definido (IC actual=+0.038 PNL=+7.24€)
  - _Datos_: n=24 IC=+0.038 PNL=+7.24€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.105 n=568) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=568 IC=+0.105 PNL=+166.55€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.329 > 0.08 con n=156 PNL=+68.28€
  - _Datos_: n=156 IC=+0.329 PNL=+68.28€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.418 n=350) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=350 IC=+0.418 PNL=+491.48€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=6116 IC=+0.162 PNL=-845.43€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=6116 IC=+0.162 PNL=-845.43€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.208 > 0.1 con n=87 PNL=+52.98€
  - _Datos_: n=87 IC=+0.208 PNL=+52.98€
