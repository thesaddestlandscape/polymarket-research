# Hipótesis automáticas — 2026-10-11 03:06 UTC
_Generado por shadow_postmortem.py sobre 845734 resoluciones (PNL=+105688.19€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.237 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.127)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.194 (n=243)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 68.0 (IC base=+0.127)

- **PATRÓN** `banda_hit_calibrado` > `0.618` → IC=+0.251 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.618 (IC base=+0.127)

- **PATRÓN** `banda_z` > `9.204` → IC=+0.199 (n=237)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 9.204 (IC base=+0.127)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.727` → IC=+0.127 (n=631)

  - _Acción_: Kelly boost +0.64€ cuando `ballenas_wallet_edge_medio` > 0.727 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=758)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.141 (n=369)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 100.0 (IC base=+0.127)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.234 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.211 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 74.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.8183` → IC=+0.298 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8183 (IC base=+0.132)

- **PATRÓN** `banda_z` > `9.732` → IC=+0.209 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.732 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=660)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.132)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=115)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=110)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.125)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `1362.9219` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1362.9219 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.000)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.154)

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
- **FILTRO** `restante_s_al_confirmar` < `143.96` → IC=-0.207 (n=9049)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.96
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=27148)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.91` → IC=-0.265 (n=1105)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.91
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3318)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.71` → IC=-0.303 (n=1028)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.71
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3086)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.58` → IC=-0.224 (n=2338)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.58
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7016)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.56` → IC=-0.300 (n=1757)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.56
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=5271)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.207 (n=19020)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=4043)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `9468.964` → IC=+0.181 (n=1804)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9468.964 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.134 (n=15883)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=19208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.229 (n=14637)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=6670)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7415.5891` → IC=+0.163 (n=2565)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 7415.5891 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=1937)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1895)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2381)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `16135.1594` → IC=+0.207 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16135.1594 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=1713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=1907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=2444)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `16044.722` → IC=+0.207 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16044.722 (IC base=+0.191)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=424)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `6926.0677` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 6926.0677 (IC base=+0.088)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.123 (n=475)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 7.0 (IC base=+0.086)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=1005)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `5815.7893` → IC=+0.125 (n=238)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 5815.7893 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.367 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.228 (n=1647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.362 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=1918)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=789)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.256 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=722)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2152.9973` → IC=+0.157 (n=400)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2152.9973 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.408 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=662)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=828)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.147)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.176 (n=334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.368 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3371.7925` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3371.7925 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.224 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.825` → IC=-0.340 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.825
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=15832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=13414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.230 (n=6654)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=3496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3495)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3568)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=1680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.226 (n=1670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.316 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=3635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=3469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=2877)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=3172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.349 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.243)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=3557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=2273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.189 (n=2716)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.71 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.198 (n=1256)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.428 (n=620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `2839.9084` → IC=+0.434 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2839.9084 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.446 (n=184)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.453 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `18111.1478` → IC=+0.436 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18111.1478 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.443 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3434.6605` → IC=+0.444 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3434.6605 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.409 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.408 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.411 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.406)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=20436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=20757)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.193 (n=3041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=6496)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=9050)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=4150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.284 (n=2999)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=8575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=6486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=8649)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=4291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.275 (n=2947)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.204 (n=7843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.203 (n=6243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3084)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=3399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=3578)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=7315)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.125 (n=6740)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.2 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=7118)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=8915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.45` → IC=+0.140 (n=6727)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.45 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=3622)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.127 (n=3340)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.144 (n=3585)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=4415)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `2.96` → IC=+0.148 (n=3338)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 2.96 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=3693)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=3898)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.137 (n=3383)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.304 (n=1476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=1455)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.383 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `4254.7258` → IC=+0.306 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4254.7258 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.297 (n=662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.358 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `5357.3376` → IC=+0.311 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5357.3376 (IC base=+0.286)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1451.8749` → IC=+0.309 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1451.8749 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.350)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.375 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.350)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.350)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.354 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.350)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.350)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.444 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.450 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.463 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.445)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.446 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.445)

- **PATRÓN** `libro_liquidez` > `2127.0131` → IC=+0.460 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2127.0131 (IC base=+0.445)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.385 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.396)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.396)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.396)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.296 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.241 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.296 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.241 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.3659` → IC=+0.136 (n=9963)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3659 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.9838` → IC=+0.244 (n=3773)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9838 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2129` → IC=+0.253 (n=2610)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2129 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.003` → IC=+0.186 (n=4281)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 6.003 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.8514` → IC=+0.250 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8514 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.255 (n=3183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.3018` → IC=+0.231 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3018 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.332` → IC=+0.221 (n=3610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.332 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.141 (n=13859)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5667 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.5638` → IC=+0.205 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5638 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1467` → IC=+0.185 (n=4805)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1467 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `1.1879` → IC=+0.183 (n=5179)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1879 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0529` → IC=+0.182 (n=2348)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0529 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.227 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4504` → IC=+0.203 (n=8874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4504 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.217 (n=8696)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.073)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.219 (n=838)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.203 (n=839)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.2794` → IC=+0.188 (n=2208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.2794 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.199 (n=1218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=1676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.208` → IC=+0.291 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.208 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.239 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.5923` → IC=+0.199 (n=794)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.5923 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=2618)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.235 (n=2050)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.243 (n=1828)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0875` → IC=+0.266 (n=683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0875 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0067` → IC=+0.284 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0067 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.41` → IC=+0.241 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.41 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.234 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.255 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6401` → IC=+0.250 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6401 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.232 (n=890)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1051` → IC=+0.257 (n=887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1051 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=2016)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.220 (n=2057)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.9714` → IC=+0.266 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9714 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.1308` → IC=+0.223 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1308 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.469` → IC=+0.258 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.469 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.2468` → IC=+0.221 (n=2014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2468 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6193` → IC=+0.224 (n=2014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6193 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.243 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7701` → IC=+0.221 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7701 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.4271` → IC=+0.247 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4271 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.185 (n=675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0739` → IC=+0.173 (n=671)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0739 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7275` → IC=+0.179 (n=2007)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7275 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1299` → IC=+0.159 (n=1831)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1299 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.208` → IC=+0.147 (n=324)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.208 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.301` → IC=+0.146 (n=1838)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.301 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.186` → IC=+0.148 (n=2007)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.186 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.163 (n=544)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4537` → IC=+0.150 (n=1891)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4537 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7854` → IC=+0.145 (n=1261)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7854 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `227.0` → IC=+0.175 (n=804)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 227.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.201 (n=2563)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=2695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.366` → IC=+0.262 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.366 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.195 (n=2253)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.202 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.1566` → IC=+0.202 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1566 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=3052)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.227 (n=1513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.1765` → IC=+0.231 (n=997)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1765 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=1051)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.0676` → IC=+0.236 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0676 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.632` → IC=+0.256 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.632 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.254 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.724` → IC=+0.217 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.724 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.712` → IC=+0.228 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.712 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.217 (n=2078)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.138 (n=136)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=3049)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.144 (n=624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0041 (IC base=+0.047)

- **PATRÓN** `ibs_20min` > `0.9584` → IC=+0.224 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9584 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.042` → IC=+0.182 (n=999)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.042 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.333 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.352 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.1796` → IC=+0.325 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1796 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.4113` → IC=+0.360 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4113 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `2.1967` → IC=+0.324 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1967 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.329 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 150.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.0987` → IC=+0.170 (n=797)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.0987 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.4516` → IC=+0.205 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4516 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.152 (n=877)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8504 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `1.1679` → IC=+0.145 (n=438)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1679 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2852` → IC=+0.209 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2852 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.5204` → IC=+0.163 (n=1121)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5204 (IC base=+0.033)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.179 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=476)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.188 (n=139)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=419)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.129 (n=3080)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=1521)

- **FILTRO** `sigma_ewma_delta_pct` > `8.696` → IC=-0.224 (n=473)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.696
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=4128)

- **PATRÓN** `ibs_20min` > `0.8077` → IC=+0.182 (n=190)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8077 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.9668` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9668 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.37` → IC=+0.126 (n=196)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 2.37 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.256 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8709 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.269 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `2.5152` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5152 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `1.5481` → IC=+0.259 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5481 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.260 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.144 (n=1521)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.2222 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2559` → IC=+0.275 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2559 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.704` → IC=+0.282 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.704 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.08` → IC=+0.294 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.08 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.38` → IC=+0.294 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.38 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.206 (n=958)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2245)

- **FILTRO** `ibs_20min` > `0.7628` → IC=-0.205 (n=1196)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7628
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=3589)

- **PATRÓN** `dist_vwap_pct` > `0.4566` → IC=+0.314 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4566 (IC base=-0.075)

- **PATRÓN** `dist_vwap_pct` < `0.193` → IC=+0.312 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.193 (IC base=-0.075)

- **PATRÓN** `volumen_regimen` < `0.9898` → IC=+0.299 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9898 (IC base=-0.075)

- **PATRÓN** `volumen_regimen` > `0.6377` → IC=+0.311 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6377 (IC base=-0.075)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.298 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.306 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.075)

- **PATRÓN** `volumen_spike_ratio` < `2.4712` → IC=+0.300 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4712 (IC base=-0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.305 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1732 (IC base=-0.075)

- **PATRÓN** `dist_vwap_pct` > `0.8008` → IC=+0.283 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8008 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `1.0786` → IC=+0.275 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0786 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1035` → IC=+0.275 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1035 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `2.1758` → IC=+0.258 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1758 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.260 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4309 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.203 (n=4985)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4639` → IC=+0.186 (n=13340)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4639 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.9224` → IC=+0.283 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9224 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.679` → IC=+0.156 (n=6718)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.679 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.1726` → IC=+0.251 (n=5479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1726 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.258 (n=4894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.264 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4629` → IC=+0.248 (n=2942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4629 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6328` → IC=+0.261 (n=2942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6328 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.282 (n=8387)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.161 (n=4798)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0089 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5405` → IC=+0.158 (n=12667)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5405 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.8744` → IC=+0.253 (n=2941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8744 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1948` → IC=+0.262 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1948 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.309 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5864` → IC=+0.281 (n=2728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5864 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.274` → IC=+0.273 (n=2809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.274 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.285 (n=6097)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2594` → IC=-0.174 (n=1038)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2594
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=3114)

- **FILTRO** `ibs_20min` > `0.758` → IC=-0.192 (n=856)

  - _Acción_: SKIP cuando `ibs_20min` > 0.758
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2569)

- **FILTRO** `sigma_ewma_delta_pct` > `4.593` → IC=-0.187 (n=756)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.593
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2669)

- **PATRÓN** `ibs_20min` > `0.914` → IC=+0.285 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.914 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.245` → IC=+0.204 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.245 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.286 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.219 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.2236` → IC=+0.251 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2236 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.246 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.038)

- **PATRÓN** `ibs_20min` < `0.1601` → IC=+0.150 (n=857)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1601 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0774` → IC=+0.421 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0774 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.5483` → IC=+0.408 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5483 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.5399` → IC=+0.408 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5399 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.411 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1147` → IC=+0.193 (n=760)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1147 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6779` → IC=+0.183 (n=1286)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6779 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.218 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.198 (n=472)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4225 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.196 (n=472)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.227 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 223.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1497` → IC=+0.231 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1497 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.234 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.0736` → IC=+0.228 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0736 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.296 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5482` → IC=+0.235 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5482 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1745` → IC=+0.245 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1745 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.277 (n=2235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.261 (n=2242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=1998)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.279` → IC=+0.287 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.279 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.269 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.1675` → IC=+0.265 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1675 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.267 (n=2643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.304 (n=1884)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.1791` → IC=+0.306 (n=828)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1791 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.3644` → IC=+0.292 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3644 (IC base=+0.288)

- **PATRÓN** `ibs_20min` > `0.1045` → IC=+0.289 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1045 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.305 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` < `0.1942` → IC=+0.286 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1942 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.3376` → IC=+0.299 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3376 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `1.5693` → IC=+0.304 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5693 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `2.0995` → IC=+0.289 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0995 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.289 (n=1540)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.288)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7574` → IC=-0.183 (n=875)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7574
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=2629)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.147 (n=1105)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.8 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0122` → IC=+0.236 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0122 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1042` → IC=+0.235 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1042 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.263 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.292 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.221 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.122 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.0403` → IC=+0.233 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0403 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.287 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.8412` → IC=+0.264 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8412 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.5032` → IC=+0.248 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5032 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.250 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7645` → IC=-0.195 (n=1583)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7645
  - _Potencial_: sin este filtro IC_bueno=+0.292 (n=1584)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.249 (n=763)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=2404)

- **FILTRO** `sigma_ewma_delta_pct` > `8.621` → IC=-0.231 (n=362)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.621
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=2805)

- **PATRÓN** `ibs_20min` > `0.7645` → IC=+0.292 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7645 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `1.0133` → IC=+0.334 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0133 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.658` → IC=+0.171 (n=493)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.658 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8517` → IC=+0.317 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8517 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.634` → IC=+0.311 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.634 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.308 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.339 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.329 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.329 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.136 (n=2091)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5588 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2689` → IC=+0.239 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2689 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.261 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7031 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `1.1832` → IC=+0.230 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1832 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.237 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.248 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4125` → IC=+0.251 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4125 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.265 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.025)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.337 (n=1558)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=826)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.325 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.320 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.315 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.953` → IC=+0.295 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.953 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` > `0.6259` → IC=+0.305 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6259 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.343 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `1.4307` → IC=+0.304 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4307 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.329 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.325 (n=1229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1853` → IC=+0.293 (n=811)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1853 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.302 (n=921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.3696` → IC=+0.319 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3696 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.3061` → IC=+0.295 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3061 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.513` → IC=+0.303 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.513 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.036` → IC=+0.294 (n=2201)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.036 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` < `0.8905` → IC=+0.294 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8905 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` > `1.2273` → IC=+0.323 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2273 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.2325` → IC=+0.342 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2325 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `1.4184` → IC=+0.298 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4184 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.296 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.293)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.187 (n=3684)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.215 (n=3675)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3462` → IC=+0.187 (n=9696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3462 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=11485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.563` → IC=+0.229 (n=11019)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.563 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1656` → IC=+0.202 (n=4611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1656 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.409` → IC=+0.252 (n=2202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.409 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1981` → IC=+0.169 (n=7313)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1981 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6274` → IC=+0.163 (n=7314)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6274 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.197 (n=1620)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4509` → IC=+0.177 (n=3551)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4509 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.5982` → IC=+0.184 (n=3550)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5982 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2535.6028` → IC=+0.180 (n=7345)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2535.6028 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.192 (n=9929)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 101.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.188 (n=7043)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0066 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.223 (n=3519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=3969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.4925` → IC=+0.232 (n=10553)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4925 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.221` → IC=+0.195 (n=1748)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.221 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.1807` → IC=+0.165 (n=7549)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1807 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.291` → IC=+0.221 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.291 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6109` → IC=+0.179 (n=3277)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6109 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.186 (n=9526)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 105.0 (IC base=+0.176)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.234 (n=621)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.220 (n=619)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.334` → IC=+0.223 (n=1852)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.334 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=1241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.918` → IC=+0.286 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.918 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.239` → IC=+0.331 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.239 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.260 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.8247` → IC=+0.196 (n=1162)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.8247 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.5397` → IC=+0.203 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5397 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.248 (n=1252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.245 (n=1420)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.294 (n=625)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=1281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.2632` → IC=+0.263 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2632 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.182` → IC=+0.241 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.182 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.239 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.281 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4302` → IC=+0.250 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4302 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.6447` → IC=+0.247 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6447 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.218 (n=552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.1622` → IC=+0.191 (n=1103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1622 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=1653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.3742` → IC=+0.225 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3742 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1392` → IC=+0.208 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1392 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.506` → IC=+0.233 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.506 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.6889` → IC=+0.169 (n=728)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6889 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.186 (n=262)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.180 (n=539)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.4856` → IC=+0.159 (n=538)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4856 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `232.0` → IC=+0.171 (n=697)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 232.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=1738)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2293` → IC=+0.175 (n=1531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2293 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6041` → IC=+0.201 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6041 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.719` → IC=+0.203 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.719 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.165 (n=1738)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2025 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.2281` → IC=+0.147 (n=1796)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.2281 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.158` → IC=+0.144 (n=532)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.158 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4919` → IC=+0.154 (n=1621)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4919 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.171 (n=521)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 207.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.231 (n=618)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.4018` → IC=+0.219 (n=1631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4018 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.539` → IC=+0.286 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.539 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.206 (n=1574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1999` → IC=+0.210 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1999 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.767` → IC=+0.211 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.767 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.6785` → IC=+0.213 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6785 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=2204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.249 (n=1059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1427` → IC=+0.265 (n=697)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1427 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.281 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.3529` → IC=+0.249 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3529 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.624` → IC=+0.258 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.624 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.265 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.7162` → IC=+0.242 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7162 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.712` → IC=+0.233 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.712 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.229 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.229)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.182 (n=1562)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0063 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0757` → IC=+0.203 (n=593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0757 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3221` → IC=+0.208 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3221 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1366` → IC=+0.188 (n=1119)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1366 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.969` → IC=+0.205 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.969 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.162 (n=1184)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.856 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1013` → IC=+0.175 (n=737)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1013 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4275` → IC=+0.167 (n=580)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4275 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.5102` → IC=+0.165 (n=580)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5102 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5128.1918` → IC=+0.200 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5128.1918 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.156 (n=1716)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 147.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.160 (n=1635)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0061 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3824` → IC=+0.148 (n=1857)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3824 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6805` → IC=+0.186 (n=1857)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6805 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.845` → IC=+0.153 (n=647)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.845 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.164 (n=1238)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.856 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.189 (n=281)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8095` → IC=+0.132 (n=1151)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8095 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4164` → IC=+0.132 (n=1725)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4164 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `4533.1494` → IC=+0.169 (n=1238)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4533.1494 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.127 (n=1672)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 146.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.163 (n=914)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0098 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4354` → IC=+0.130 (n=1772)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4354 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.216 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1944` → IC=+0.187 (n=1202)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1944 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.853` → IC=+0.266 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.853 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8684` → IC=+0.147 (n=1342)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8684 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `0.7151` → IC=+0.129 (n=1797)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.7151 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.137 (n=2035)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4402` → IC=+0.144 (n=650)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4402 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2097)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2392.0288` → IC=+0.191 (n=1341)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2392.0288 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.162 (n=622)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 21.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.141 (n=1797)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0091 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.169 (n=681)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5882` → IC=+0.216 (n=2042)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5882 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.269` → IC=+0.128 (n=616)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 5.269 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.132 (n=2041)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1756 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.151 (n=262)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4487` → IC=+0.137 (n=628)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4487 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4233` → IC=+0.124 (n=628)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.4233 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2170.0549` → IC=+0.173 (n=1360)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2170.0549 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.129 (n=1844)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 51.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.237 (n=1674)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.2837` → IC=+0.224 (n=1250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2837 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1946)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=1264)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.252 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1899` → IC=+0.217 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1899 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.2706` → IC=+0.215 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2706 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.596` → IC=+0.245 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.596 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.1814` → IC=+0.218 (n=1874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1814 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.222 (n=1874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.273 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.219 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.8029` → IC=+0.227 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8029 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2995.8059` → IC=+0.224 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2995.8059 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.231 (n=843)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.227 (n=869)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.252 (n=640)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.241 (n=935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.4225` → IC=+0.252 (n=1915)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4225 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `1.1501` → IC=+0.233 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1501 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.402` → IC=+0.248 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.402 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6394` → IC=+0.231 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6394 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.282 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.2006` → IC=+0.215 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2006 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.223 (n=1767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.222)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.206 (n=957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.33` → IC=+0.181 (n=2522)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.33 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=2595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.4837` → IC=+0.205 (n=2561)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4837 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.5779` → IC=+0.182 (n=558)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.5779 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.721` → IC=+0.195 (n=1227)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.721 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8639` → IC=+0.190 (n=1724)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8639 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.173 (n=2311)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6949 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1017` → IC=+0.182 (n=1028)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1017 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4359` → IC=+0.191 (n=929)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4359 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5174` → IC=+0.174 (n=929)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5174 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=2663)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `4101.9995` → IC=+0.172 (n=1911)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4101.9995 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.184 (n=2647)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 152.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.149 (n=982)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0036 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=2781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.0802` → IC=+0.198 (n=981)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0802 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6982` → IC=+0.121 (n=1180)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 0.6982 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.4318` → IC=+0.139 (n=952)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4318 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `4801.2164` → IC=+0.137 (n=1960)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 4801.2164 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.134 (n=960)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 21.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.205 (n=367)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.214 (n=365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.190 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.6361` → IC=+0.212 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6361 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.3049` → IC=+0.182 (n=259)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.3049 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.109` → IC=+0.179 (n=353)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.109 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.8772` → IC=+0.185 (n=553)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8772 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.166 (n=321)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.2256` → IC=+0.165 (n=714)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.2256 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.417` → IC=+0.159 (n=811)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.417 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `14731.9311` → IC=+0.169 (n=553)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 14731.9311 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.198 (n=356)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 152.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.189 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0027 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2647` → IC=+0.154 (n=843)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.2647 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.3757` → IC=+0.197 (n=639)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3757 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.177` → IC=+0.147 (n=868)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.177 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2002` → IC=+0.144 (n=958)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2002 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6971` → IC=+0.155 (n=856)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6971 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.186 (n=256)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.1178` → IC=+0.158 (n=833)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1178 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1242)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `355.0` → IC=+0.153 (n=926)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 355.0 (IC base=+0.142)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.243 (n=609)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.2019` → IC=+0.223 (n=607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2019 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.3605` → IC=+0.242 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3605 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.3567` → IC=+0.211 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3567 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2052` → IC=+0.210 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2052 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.222 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.836` → IC=+0.210 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.836 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `1.1816` → IC=+0.221 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1816 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.1597` → IC=+0.233 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1597 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.4106` → IC=+0.244 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4106 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.221 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4427 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.125 (n=587)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0048 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.0901` → IC=+0.172 (n=294)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.0901 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.139 (n=388)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6877 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `4005.7464` → IC=+0.129 (n=786)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4005.7464 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.129 (n=370)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.097)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.156 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0074 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.149 (n=220)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0104 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.5317` → IC=+0.148 (n=658)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.5317 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.180 (n=591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.9216` → IC=+0.213 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9216 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.288` → IC=+0.205 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.288 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.0661` → IC=+0.170 (n=579)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.0661 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.6526` → IC=+0.154 (n=658)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6526 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.174 (n=185)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4594` → IC=+0.154 (n=212)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4594 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.162 (n=288)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.154 (n=692)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2928.3958` → IC=+0.181 (n=299)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2928.3958 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.4615` → IC=+0.150 (n=556)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.4615 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `1.5684` → IC=+0.131 (n=266)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5684 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `2428.7532` → IC=+0.131 (n=421)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2428.7532 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.136 (n=385)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 22.0 (IC base=+0.064)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.170 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0238 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.186 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.007 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.167 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5556 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2393` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2393 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6182 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.2537` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2537 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.162 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0119 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.133 (n=213)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.025` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.025 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.128 (n=213)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6515 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.8124` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.8124 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.180 (n=4790)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.218 (n=4782)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=14969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5591` → IC=+0.237 (n=12793)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5591 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1612` → IC=+0.187 (n=5244)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1612 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.376` → IC=+0.250 (n=3517)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.376 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8777` → IC=+0.175 (n=6396)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8777 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.202 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.5996` → IC=+0.196 (n=4628)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5996 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2507.0533` → IC=+0.184 (n=9547)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2507.0533 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.205 (n=11418)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.196 (n=5680)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1449` → IC=+0.195 (n=5682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1449 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=4838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5745` → IC=+0.241 (n=12902)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5745 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.039` → IC=+0.208 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.039 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.694` → IC=+0.189 (n=12454)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.694 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.165 (n=3837)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.705 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.250 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2631` → IC=+0.195 (n=5492)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.2631 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.211 (n=7858)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.250 (n=789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.243 (n=789)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=1143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=1587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.704` → IC=+0.349 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.704 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.271 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.2492` → IC=+0.222 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2492 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.262 (n=1977)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.262 (n=1975)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.278 (n=660)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.265 (n=1793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.4897` → IC=+0.283 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4897 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.581` → IC=+0.265 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.581 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2845` → IC=+0.288 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2845 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.635` → IC=+0.280 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.635 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=2179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.197 (n=769)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1761` → IC=+0.167 (n=1535)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1761 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2731` → IC=+0.207 (n=2300)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2731 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1274` → IC=+0.187 (n=1255)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1274 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.71` → IC=+0.169 (n=388)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.71 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.186` → IC=+0.154 (n=2101)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.186 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6273` → IC=+0.175 (n=767)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6273 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.187 (n=327)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.157 (n=1973)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5282` → IC=+0.153 (n=2002)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5282 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `271.0` → IC=+0.180 (n=958)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 271.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.192 (n=637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0026 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3225` → IC=+0.161 (n=1902)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3225 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6942` → IC=+0.197 (n=1903)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6942 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.169 (n=1749)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.479` → IC=+0.157 (n=322)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.479 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.148 (n=1719)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.160 (n=1903)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1817 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1532` → IC=+0.191 (n=510)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1532 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4364` → IC=+0.156 (n=1800)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4364 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.161 (n=1200)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `255.0` → IC=+0.147 (n=573)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 255.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.240 (n=1581)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.436` → IC=+0.311 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.436 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.225 (n=2074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7673` → IC=+0.229 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7673 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2816)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.245 (n=1475)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.239 (n=1977)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1801` → IC=+0.257 (n=974)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1801 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=1032)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0185` → IC=+0.301 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0185 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.137` → IC=+0.289 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.137 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3403` → IC=+0.301 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3403 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7177` → IC=+0.239 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7177 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1275` → IC=+0.246 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1275 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.261 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.238)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.201 (n=1079)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1258` → IC=+0.167 (n=1079)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1258 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.2656` → IC=+0.192 (n=2451)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2656 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.5323` → IC=+0.167 (n=620)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.5323 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.201` → IC=+0.161 (n=1002)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.201 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8732` → IC=+0.165 (n=1635)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8732 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.172 (n=861)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.171 (n=1051)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.1733` → IC=+0.156 (n=1083)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1733 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `7279.5454` → IC=+0.240 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7279.5454 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.179 (n=779)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 68.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.197 (n=665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0032 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.339` → IC=+0.144 (n=1748)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.339 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7379` → IC=+0.189 (n=1987)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7379 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.285` → IC=+0.174 (n=305)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.285 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6239` → IC=+0.151 (n=663)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6239 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.228 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.144 (n=1905)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5380.0822` → IC=+0.204 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5380.0822 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.134 (n=1911)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 162.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.142 (n=1648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0079 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4485` → IC=+0.200 (n=2472)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4485 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0121` → IC=+0.211 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0121 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.978` → IC=+0.261 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.978 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8869` → IC=+0.150 (n=1648)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8869 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.128 (n=2559)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2796` → IC=+0.131 (n=326)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2796 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1865` → IC=+0.134 (n=1093)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.1865 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2522)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2937.8881` → IC=+0.252 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2937.8881 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.142 (n=771)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 26.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.177 (n=785)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0057 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1302` → IC=+0.161 (n=785)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1302 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=1106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6351` → IC=+0.214 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6351 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.138 (n=1992)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.557` → IC=+0.135 (n=2163)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.557 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.7132` → IC=+0.151 (n=1035)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.7132 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2218` → IC=+0.169 (n=388)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2218 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4342` → IC=+0.156 (n=728)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4342 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2808.5642` → IC=+0.210 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2808.5642 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.139 (n=1916)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 49.0 (IC base=+0.121)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.240 (n=2118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0133 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.228 (n=1710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.6038` → IC=+0.268 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6038 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1989` → IC=+0.236 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1989 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.623` → IC=+0.259 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.623 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.2301` → IC=+0.228 (n=2371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2301 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.224 (n=2371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.248 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.246 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2995.8059` → IC=+0.243 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2995.8059 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.224 (n=827)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.237 (n=1124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.229 (n=2323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.4167` → IC=+0.268 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4167 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.944` → IC=+0.257 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.944 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.251 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.292 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.224 (n=2285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.221)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=4229)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.235 (n=1440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.4945` → IC=+0.204 (n=4318)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4945 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=1583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=2964)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.9409` → IC=+0.244 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9409 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.1681` → IC=+0.196 (n=1613)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1681 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.2371` → IC=+0.197 (n=2657)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2371 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.189` → IC=+0.210 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.189 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.204 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7053 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `0.8869` → IC=+0.198 (n=2047)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.8869 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.1678` → IC=+0.217 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1678 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.202 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.6126` → IC=+0.200 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6126 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=3250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `3860.3379` → IC=+0.207 (n=2879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3860.3379 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.227 (n=1065)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.4827` → IC=+0.194 (n=3184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4827 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=1092)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=1450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.198 (n=1401)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.18 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.639` → IC=+0.187 (n=550)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.639 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.176` → IC=+0.182 (n=3186)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.176 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.2492` → IC=+0.182 (n=2990)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.2492 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.180 (n=2903)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.182 (n=1449)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `2.538` → IC=+0.179 (n=3139)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.538 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.8147` → IC=+0.183 (n=2092)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8147 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=4229)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.185 (n=1387)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 36.0 (IC base=+0.177)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.247 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.270 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.228 (n=255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.5099` → IC=+0.245 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5099 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.761` → IC=+0.223 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.761 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3158` → IC=+0.231 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3158 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.071` → IC=+0.241 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.071 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.566` → IC=+0.222 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.566 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.228 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.5968` → IC=+0.232 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5968 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.238 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `12570.0288` → IC=+0.246 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12570.0288 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.234 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.3657` → IC=+0.170 (n=1097)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3657 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.187 (n=417)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.1568` → IC=+0.184 (n=483)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1568 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.160 (n=498)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6091 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.6637` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6637 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.1568` → IC=+0.156 (n=1070)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1568 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.421` → IC=+0.172 (n=1079)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.421 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8813` → IC=+0.194 (n=732)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8813 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.194 (n=230)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4094` → IC=+0.162 (n=365)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4094 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.8136` → IC=+0.174 (n=729)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8136 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `14894.8693` → IC=+0.178 (n=498)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14894.8693 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.168 (n=1052)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 701.0 (IC base=+0.156)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.201 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.185 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.5794` → IC=+0.180 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.5794 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.51` → IC=+0.217 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.51 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.226 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `3.3854` → IC=+0.184 (n=232)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3854 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.2021` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2021 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.215 (n=1128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4566` → IC=+0.209 (n=1283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4566 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.519` → IC=+0.216 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.519 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.8798` → IC=+0.207 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8798 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.152` → IC=+0.209 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.152 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.8824` → IC=+0.206 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8824 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2441` → IC=+0.209 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2441 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1054` → IC=+0.204 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1054 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1639` → IC=+0.210 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1639 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.220 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.238 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.4878` → IC=+0.200 (n=1028)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4878 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.188 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 16.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.189 (n=699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 10.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.7599` → IC=+0.179 (n=1028)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7599 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.087` → IC=+0.178 (n=1028)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.087 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.6243` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6243 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.748` → IC=+0.179 (n=1052)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 6.748 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2459` → IC=+0.188 (n=1028)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2459 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.175 (n=918)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.7214 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.195 (n=434)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.183` → IC=+0.188 (n=886)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.183 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.7774` → IC=+0.178 (n=671)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.7774 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `7366.3592` → IC=+0.189 (n=1028)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7366.3592 (IC base=+0.174)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.218 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.190 (n=547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 4.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.246 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.1861` → IC=+0.185 (n=357)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1861 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.348` → IC=+0.202 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.348 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.6991` → IC=+0.203 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6991 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.1075` → IC=+0.166 (n=522)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1075 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.198 (n=180)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `2.5474` → IC=+0.207 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5474 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=687)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `3315.2471` → IC=+0.207 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3315.2471 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.175 (n=564)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 56.0 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.208 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.200 (n=378)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.3574` → IC=+0.232 (n=282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3574 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.223 (n=283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.250 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.7586` → IC=+0.219 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7586 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.997` → IC=+0.201 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.997 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.926` → IC=+0.199 (n=370)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 2.926 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.7541` → IC=+0.218 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7541 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.230 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.6178` → IC=+0.194 (n=181)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.6178 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.213 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3258.9665` → IC=+0.211 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3258.9665 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.225 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.192)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.155 (n=621)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0038 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.4182` → IC=+0.148 (n=1318)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.4182 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.1388` → IC=+0.139 (n=701)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1388 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.448` → IC=+0.178 (n=296)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.448 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.161 (n=178)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.1875` → IC=+0.248 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1875 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.0861` → IC=+0.127 (n=598)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.0861 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.179 (n=160)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.4666` → IC=+0.130 (n=241)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4666 (IC base=+0.054)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.134 (n=482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0056 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.140 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 18.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.5456` → IC=+0.193 (n=402)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5456 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.155 (n=233)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.0431` → IC=+0.272 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0431 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.1067` → IC=+0.134 (n=290)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1067 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.698` → IC=+0.137 (n=246)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.698 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.1532` → IC=+0.153 (n=73)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1532 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.127 (n=261)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.078)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.152 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0046 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6816` → IC=+0.210 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6816 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.123` → IC=+0.175 (n=229)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.123 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.742` → IC=+0.268 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.742 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.7779` → IC=+0.129 (n=251)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7779 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `1723.7312` → IC=+0.153 (n=142)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1723.7312 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.1058` → IC=+0.268 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1058 (IC base=+0.005)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0093` → IC=-0.183 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0093
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=178)

- **FILTRO** `ibs_20min` > `0.1429` → IC=-0.255 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1429
  - _Potencial_: sin este filtro IC_bueno=+0.247 (n=148)

- **PATRÓN** `ibs_20min` > `0.7609` → IC=+0.163 (n=292)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.7609 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `0.7076` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.7076 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2453` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2453 (IC base=+0.037)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.150 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0093 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.247 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1278` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1278 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.3549` → IC=+0.163 (n=161)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.3549 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.815` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.815 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `0.9765` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.9765 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1476` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1476 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.4883` → IC=+0.184 (n=112)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4883 (IC base=+0.067)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.194 (n=119)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.06 (IC base=+0.067)

- **PATRÓN** `libro_liquidez` > `774.2903` → IC=+0.174 (n=87)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 774.2903 (IC base=+0.067)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` < `5.0` → IC=-0.206 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=150)

- **FILTRO** `dist_vwap_pct` > `0.235` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.235
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=258)

- **FILTRO** `volumen_regimen` < `0.7553` → IC=-0.343 (n=68)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7553
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=206)

- **FILTRO** `volumen_spike_ratio` > `2.8909` → IC=-0.186 (n=49)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.8909
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=151)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.205 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=198)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.381 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=174)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.300 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=163)

- **FILTRO** `dist_vwap_pct` > `0.3328` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3328
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=198)

- **FILTRO** `sigma_ewma_delta_pct` > `10.779` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.779
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=208)

- **FILTRO** `volumen_pendiente_norm` > `0.0559` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0559
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=121)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.261 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=47)

- **FILTRO** `volumen_regimen` < `0.8417` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8417
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=69)

- **FILTRO** `volumen_spike_ratio` > `3.7984` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.7984
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=52)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=76)

- **FILTRO** `sigma_ewma_delta_pct` > `2.402` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.402
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=69)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.329 (n=33)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=35)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.438 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=67)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=57)

- **FILTRO** `dist_vwap_pct` > `0.1182` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1182
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=57)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=35)

- **FILTRO** `libro_liquidez` < `1258.6237` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 1258.6237
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=64)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.9583 (IC base=-0.156)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=76)

- **FILTRO** `volumen_spike_ratio` < `1.5614` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5614
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1684` → IC=-0.120 (n=227)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1684
  - _Potencial_: sin este filtro IC_bueno=+0.171 (n=442)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.170 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0057 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.144 (n=445)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6667 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.4724` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.4724 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.66` → IC=+0.147 (n=148)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.66 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` < `0.236` → IC=+0.135 (n=379)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.236 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `2.5521` → IC=+0.137 (n=342)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5521 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.1684` → IC=+0.171 (n=442)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1684 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.209` → IC=+0.192 (n=154)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.209 (IC base=+0.072)

- **PATRÓN** `libro_liquidez` > `2868.4937` → IC=+0.156 (n=335)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2868.4937 (IC base=+0.072)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6585` → IC=-0.245 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6585
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=136)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.214 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.004 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.162 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 12.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.154 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.1381` → IC=+0.206 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1381 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.0931` → IC=+0.162 (n=232)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.0931 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.678` → IC=+0.170 (n=177)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 4.678 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.6869` → IC=+0.172 (n=202)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.6869 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0772` → IC=+0.180 (n=173)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.0772 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.2594` → IC=+0.182 (n=171)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.2594 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.150)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1403` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1403
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=138)

- **FILTRO** `ibs_20min` > `0.3972` → IC=-0.156 (n=62)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3972
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=190)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.128 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0044 (IC base=+0.078)

- **PATRÓN** `ibs_20min` > `0.7141` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.7141 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.033` → IC=+0.136 (n=116)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.033 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.078)

- **PATRÓN** `libro_liquidez` > `1535.3678` → IC=+0.139 (n=153)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1535.3678 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.2634` → IC=+0.133 (n=167)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2634 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.061` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.061 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2212` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2212 (IC base=+0.047)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `dist_vwap_pct` > `0.2725` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=93)

- **FILTRO** `volumen_spike_ratio` > `1.8262` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.8262
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=40)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.300 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.285 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.239 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.7358` → IC=+0.243 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7358 (IC base=+0.240)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.252 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `0.6388` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6388 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` < `0.216` → IC=+0.240 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.216 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.294 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.292 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.2516` → IC=+0.295 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2516 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4189` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4189 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1062` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1062 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.245 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.076)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.286)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `1.0148` → IC=+0.333 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0148 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.286)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.212)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.212)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.263 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.212)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.212)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.286)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `1.0148` → IC=+0.333 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0148 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.286)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.212)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.212)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.263 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.212)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.212)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=163)

- **FILTRO** `libro_liquidez` < `2690.866` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 2690.866
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=135)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=58)

- **FILTRO** `libro_liquidez` < `11939.3802` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 11939.3802
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=53)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

### LIQUIDACIONES_15M#XRP#15min
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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3004)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=99)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=56)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=88)

- **FILTRO** `ballena_activa_n` > `124.0` → IC=-0.212 (n=57)

  - _Acción_: SKIP cuando `ballena_activa_n` > 124.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=119)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.128 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 13.0 (IC base=+0.036)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `libro_liquidez` < `15247.5472` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 15247.5472
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.135 (n=198)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.045)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1099)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1053)

- **FILTRO** `liq_usd_total` < `12056.79` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `liq_usd_total` < 12056.79
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=696)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=378)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=359)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.150 (n=141)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.495 (IC base=+0.020)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=789)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=789)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=623)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=634)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=634)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=180)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=158)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=182)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=192)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=314)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=314)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=223)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.145 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=164)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=1573)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1697)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` > `0.46` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `lag_apertura_s` > `70.72` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `lag_apertura_s` > 70.72
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.133 (n=213)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=114)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.138 (n=205)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.56 (IC base=+0.035)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=174)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.167 (n=97)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=114)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.58 (IC base=+0.042)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.141 (n=215)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=75)

- **FILTRO** `profundidad_ratio` < `37.6` → IC=-0.189 (n=72)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.6
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=218)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=229)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.46 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.127 (n=231)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=135)

- **FILTRO** `restante_min` < `3.33` → IC=-0.189 (n=120)

  - _Acción_: SKIP cuando `restante_min` < 3.33
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=246)

- **FILTRO** `lag_apertura_s` > `98.43` → IC=-0.198 (n=124)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.43
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=242)

- **FILTRO** `profundidad_ratio` < `22.7` → IC=-0.140 (n=98)

  - _Acción_: SKIP cuando `profundidad_ratio` < 22.7
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=200)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.141 (n=62)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=227)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.130 (n=98)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.5 (IC base=+0.002)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.137 (n=221)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=118)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.188 (n=94)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=326)

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

- **FILTRO** `libro_liquidez` < `15906.9303` → IC=-0.152 (n=268)

  - _Acción_: SKIP cuando `libro_liquidez` < 15906.9303
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=805)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.475` → IC=-0.160 (n=5173)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=15527)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.167 (n=5306)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=16086)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.186 (n=897)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=2804)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.157 (n=892)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2937)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=1775)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.151 (n=731)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=2379)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.173 (n=741)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=2340)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.172 (n=920)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2832)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.182 (n=967)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=2921)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2240)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2615)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3355)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `libro_liquidez` < `2574.706` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2574.706
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.192 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=288)

- **FILTRO** `drift_20min_pct` |x|> `0.1544` → IC=-0.157 (n=138)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1544
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=268)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=391)

- **FILTRO** `libro_liquidez` < `3705.3844` → IC=-0.173 (n=203)

  - _Acción_: SKIP cuando `libro_liquidez` < 3705.3844
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=203)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=813)

- **FILTRO** `libro_liquidez` < `2034.799` → IC=-0.164 (n=340)

  - _Acción_: SKIP cuando `libro_liquidez` < 2034.799
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=691)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `drift_7min_pct` |x|> `0.0331` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0331
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.037)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=14322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=32035)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.286 (n=11062)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=35295)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.233 (n=11498)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=34859)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=15404)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=30953)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=14230)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=44722)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.179 (n=14704)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=44248)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2312)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5637)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=3918)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4031)

- **FILTRO** `ibs_7min` < `0.7098` → IC=-0.249 (n=2623)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7098
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=5326)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.172 (n=1923)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=6026)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2498)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=7736)

- **FILTRO** `ibs_7min` > `0.777` → IC=-0.209 (n=2558)

  - _Acción_: SKIP cuando `ibs_7min` > 0.777
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=7676)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.129 (n=1886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=5999)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.247 (n=1964)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5921)

- **FILTRO** `ibs_7min` < `0.7375` → IC=-0.195 (n=1970)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7375
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5915)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.186 (n=1966)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=5919)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1931)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6120)

- **FILTRO** `ibs_7min` > `0.2665` → IC=-0.194 (n=2011)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2665
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6040)

- **FILTRO** `ballena_activa_n` > `146.0` → IC=-0.184 (n=2011)

  - _Acción_: SKIP cuando `ballena_activa_n` > 146.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6040)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=1866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=5704)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.321 (n=1812)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5758)

- **FILTRO** `ibs_7min` < `0.7022` → IC=-0.248 (n=2498)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7022
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=5072)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.223 (n=1644)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5926)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.247 (n=2457)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=8424)

- **FILTRO** `ibs_7min` > `0.7348` → IC=-0.174 (n=2720)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7348
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=8161)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=2468)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=5128)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1890)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=5706)

- **FILTRO** `ibs_7min` < `0.736` → IC=-0.186 (n=1899)

  - _Acción_: SKIP cuando `ibs_7min` < 0.736
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5697)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.189 (n=1844)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5752)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1950)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5925)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.180 (n=1967)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5908)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.178 (n=1944)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5931)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=1877)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5875)

- **FILTRO** `ibs_7min` < `0.2381` → IC=-0.236 (n=1938)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=5814)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.183 (n=2660)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=8585)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.281 (n=1847)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5758)

- **FILTRO** `ibs_7min` < `0.2326` → IC=-0.224 (n=1901)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2326
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5704)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.202 (n=1801)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5804)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.207 (n=2585)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=8081)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=973)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1257)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=628)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `libro_liquidez` < `7436.9678` → IC=-0.144 (n=265)

  - _Acción_: SKIP cuando `libro_liquidez` < 7436.9678
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=797)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=365)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.146 (n=156)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=311)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=419)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=600)

- **FILTRO** `libro_liquidez` < `3312.3658` → IC=-0.151 (n=167)

  - _Acción_: SKIP cuando `libro_liquidez` < 3312.3658
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=501)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=334)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3979` → IC=+0.141 (n=999)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.3979 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.128 (n=372)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 4.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `442.3859` → IC=+0.157 (n=333)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 442.3859 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `4332.4017` → IC=+0.133 (n=333)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 4332.4017 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.149 (n=331)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 14.0 (IC base=+0.128)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.163 (n=78)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.224 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2631.6638` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2631.6638 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.196 (n=110)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 11.0 (IC base=+0.144)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.126 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 16.0 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.123 (n=237)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.160 (n=92)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 10.0 (IC base=+0.116)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4153` → IC=+0.186 (n=135)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio` |x|> 0.4153 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.152 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 4.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7230.8556` → IC=+0.134 (n=181)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7230.8556 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 73.0 (IC base=+0.129)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.189 (n=178)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.153)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.172 (n=178)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 8043.774 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3405.7473` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3405.7473 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 28.0 (IC base=+0.153)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.127 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 10.0 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=117)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `3657.3836` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3657.3836 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.269 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=289)

- **FILTRO** `T_h` > `129.8877` → IC=-0.219 (n=144)

  - _Acción_: SKIP cuando `T_h` > 129.8877
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=433)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.160 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0035 (IC base=-0.087)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.157 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=44)

- **FILTRO** `T_h` > `88.1896` → IC=-0.300 (n=43)

  - _Acción_: SKIP cuando `T_h` > 88.1896
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=130)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.304 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.037)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.037)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.128 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `pct_vs_K` |x|> `8.3214` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.3214
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0078` → IC=-0.217 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=53)

- **FILTRO** `T_h` < `87.9936` → IC=-0.148 (n=52)

  - _Acción_: SKIP cuando `T_h` < 87.9936
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=52)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.066)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.207 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=396)

- **FILTRO** `T_h` > `69.913` → IC=-0.172 (n=395)

  - _Acción_: SKIP cuando `T_h` > 69.913
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=132)

- **FILTRO** `pct_vs_K` |x|> `2.1826` → IC=-0.385 (n=224)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.1826
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=225)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=138)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.307 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=83)

- **FILTRO** `pct_vs_K` |x|> `2.0268` → IC=-0.392 (n=81)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0268
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=83)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0049` → IC=-0.280 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=100)

- **FILTRO** `T_h` > `135.9851` → IC=-0.257 (n=35)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=113)

- **FILTRO** `pct_vs_K` |x|> `2.6354` → IC=-0.400 (n=68)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6354
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=70)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0072` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=101)

- **FILTRO** `T_h` > `113.0501` → IC=-0.176 (n=66)

  - _Acción_: SKIP cuando `T_h` > 113.0501
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=68)

- **FILTRO** `sigma_h` > `0.0132` → IC=-0.348 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=62)

- **FILTRO** `T_h` > `46.6251` → IC=-0.391 (n=62)

  - _Acción_: SKIP cuando `T_h` > 46.6251
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=31)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.474 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.382 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.336)

- **PATRÓN** `T_h` < `0.9804` → IC=+0.353 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9804 (IC base=+0.336)

- **PATRÓN** `T_h` > `0.4186` → IC=+0.371 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4186 (IC base=+0.336)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.353 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.336)

- **PATRÓN** `edge` > `0.096` → IC=+0.445 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.427 (n=67)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.440 (n=132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.417)

- **PATRÓN** `T_h` < `1.014` → IC=+0.426 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.014 (IC base=+0.417)

- **PATRÓN** `T_h` > `1.4832` → IC=+0.441 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4832 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.3885` → IC=+0.465 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3885 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.429)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.417 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.429)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.458 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.429)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.429)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.429)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.429)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.439 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.429)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1885` → IC=+0.481 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1885 (IC base=+0.430)

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.462 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.430)

- **PATRÓN** `T_h` > `0.6729` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.6729 (IC base=+0.430)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.462 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.430)

- **PATRÓN** `edge` > `0.1961` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.477 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.2025` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2025 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.4455` → IC=+0.485 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4455 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=261)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=347)

- **PATRÓN** `streak_estiramiento` < `0.4396` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.4396 (IC base=+0.025)

- **PATRÓN** `streak_estiramiento` < `0.4159` → IC=+0.228 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4159 (IC base=+0.043)

- **PATRÓN** `libro_liquidez` > `2526.423` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2526.423 (IC base=+0.043)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `1831586.9` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `volumen_racha` > 1831586.9
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=66)

- **FILTRO** `streak_estiramiento` > `0.4782` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4782
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=61)

- **FILTRO** `ballena_activa_n` > `51.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 51.0
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=65)

- **PATRÓN** `volumen_racha` < `945898.4` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_racha` < 945898.4 (IC base=+0.028)

- **PATRÓN** `streak_estiramiento` < `0.4782` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.4782 (IC base=+0.028)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.131 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.091)

- **PATRÓN** `streak_estiramiento` < `0.3252` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `streak_estiramiento` < 0.3252 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.154 (n=105)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 46.0 (IC base=+0.091)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `streak_estiramiento` > `0.5544` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.5544
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=666)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `volumen_racha` > `9229.0178` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 9229.0178
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.050)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=871)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1321)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1007)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1022)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3634)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1935)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.201 (n=982)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.232 (n=982)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1643` → IC=+0.200 (n=2592)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1643 (IC base=+0.192)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2275` → IC=+0.192 (n=982)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2275 (IC base=+0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3513` → IC=+0.205 (n=2611)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3513 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=2727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=2690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `ibs_15` > `0.5909` → IC=+0.266 (n=2946)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5909 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1207` → IC=+0.185 (n=1390)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1207 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.3015` → IC=+0.180 (n=2223)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.3015 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.676` → IC=+0.269 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.676 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `5725.1044` → IC=+0.199 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5725.1044 (IC base=+0.192)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1167)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.234 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.264 (n=176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.214)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.251 (n=175)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.214)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1462` → IC=+0.235 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1462 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.276 (n=525)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.247 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.290 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `16272.4583` → IC=+0.246 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16272.4583 (IC base=+0.214)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=669)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.183 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0033 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0671` → IC=+0.155 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0671 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.155 (n=392)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.164 (n=227)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.153 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.151 (n=414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.5773` → IC=+0.241 (n=588)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5773 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1541` → IC=+0.145 (n=325)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1541 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.914` → IC=+0.279 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.914 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3532.4883` → IC=+0.150 (n=526)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3532.4883 (IC base=+0.144)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `19.505` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=239)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.152 (n=176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0054 (IC base=+0.124)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.149 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0085 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.2298` → IC=+0.153 (n=528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.2298 (IC base=+0.124)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0632` → IC=+0.132 (n=528)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0632 (IC base=+0.124)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3414` → IC=+0.148 (n=478)

  - _Acción_: Kelly boost +0.74€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3414 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.134 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 11.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.131 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 15.0 (IC base=+0.124)

- **PATRÓN** `ibs_15` > `0.9149` → IC=+0.303 (n=176)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9149 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1879` → IC=+0.146 (n=470)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1879 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.367` → IC=+0.192 (n=105)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 17.367 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=305)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.124)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.015)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.257 (n=611)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0133 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1653` → IC=+0.225 (n=602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1653 (IC base=+0.218)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1105` → IC=+0.223 (n=456)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1105 (IC base=+0.218)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3236` → IC=+0.248 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3236 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.218)

- **PATRÓN** `ibs_15` > `0.5758` → IC=+0.300 (n=684)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5758 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1917` → IC=+0.235 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1917 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.872` → IC=+0.264 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.872 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2938.7046` → IC=+0.282 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2938.7046 (IC base=+0.218)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.160 (n=713)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.363 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.369 (n=565)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.381 (n=376)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1386` → IC=+0.392 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1386 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.376 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.396 (n=565)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.4137` → IC=+0.382 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4137 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.671` → IC=+0.378 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.671 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `3836.614` → IC=+0.370 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3836.614 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `429.0` → IC=+0.379 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 429.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.358 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.374 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.358)

- **PATRÓN** `drift_15min` |x|≤ `0.5078` → IC=+0.357 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5078 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2146` → IC=+0.384 (n=136)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2146 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.390 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.379 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.384 (n=300)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.742` → IC=+0.367 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.742 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.822` → IC=+0.358 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.822 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `15252.9657` → IC=+0.384 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15252.9657 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.406 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.358)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.373 (n=265)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.366 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0903` → IC=+0.374 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0903 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.391 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.406 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.361 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.406 (n=265)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.4366` → IC=+0.362 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4366 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` < `0.2765` → IC=+0.368 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2765 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.352` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.352 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `4305.62` → IC=+0.379 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4305.62 (IC base=+0.362)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.218 (n=969)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2914)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.205 (n=1502)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2381)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1416` → IC=+0.186 (n=619)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.1416 (IC base=-0.067)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.223 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.281 (n=929)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.199 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2619` → IC=+0.198 (n=780)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2619 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1326` → IC=+0.263 (n=2091)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1326 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3518` → IC=+0.280 (n=3136)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3518 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.8592` → IC=+0.295 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8592 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.203 (n=537)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1613)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.224 (n=537)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1613)

- **FILTRO** `sigma_ewma_delta_pct` > `23.61` → IC=-0.258 (n=308)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.61
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1842)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.200 (n=58)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=2092)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.171 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0027 (IC base=+0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2118` → IC=+0.298 (n=127)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2118 (IC base=+0.089)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1042` → IC=+0.293 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1042 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.134 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.089)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.329 (n=279)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.289 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.3659` → IC=+0.291 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3659 (IC base=+0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.236 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.189)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.189)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.311 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.189)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=606)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.159 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.160 (n=468)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0033 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1111` → IC=+0.181 (n=312)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1111 (IC base=+0.151)

- **PATRÓN** `drift_15min` |x|≤ `0.4036` → IC=+0.158 (n=156)

  - _Acción_: Kelly boost +0.79€ cuando `drift_15min` |x|≤ 0.4036 (IC base=+0.151)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1402` → IC=+0.156 (n=312)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1402 (IC base=+0.151)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.198 (n=352)

  - _Acción_: Kelly boost +0.99€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.6307` → IC=+0.253 (n=468)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6307 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.5656` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.5656 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.2658` → IC=+0.158 (n=440)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2658 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.508` → IC=+0.253 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.508 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=606)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `10849.734` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 10849.734 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.257 (n=472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.345` → IC=+0.243 (n=944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.345 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.7472` → IC=+0.252 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7472 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1556` → IC=+0.257 (n=715)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1556 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.246 (n=416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.269 (n=1073)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.76` → IC=+0.298 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.76 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.569` → IC=+0.261 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.569 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.584` → IC=+0.243 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.584 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1716` → IC=-0.252 (n=304)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1716
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=591)

- **FILTRO** `drift_15min` |x|> `0.8765` → IC=-0.269 (n=223)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8765
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=672)

- **FILTRO** `sigma_ewma_delta_pct` > `6.65` → IC=-0.194 (n=217)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.65
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=678)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.248 (n=109)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=786)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.179)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.179)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.179)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.179)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0646` → IC=+0.246 (n=486)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0646 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.3455` → IC=+0.287 (n=487)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3455 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.246 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.248 (n=542)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=544)

- **FILTRO** `drift_15min` |x|> `1.2315` → IC=-0.262 (n=271)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2315
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=815)

- **FILTRO** `libro_liquidez` < `2985.1852` → IC=-0.212 (n=814)

  - _Acción_: SKIP cuando `libro_liquidez` < 2985.1852
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=272)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.200)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.200)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.273 (n=681)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1713` → IC=+0.294 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1713 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=764)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `1.0282` → IC=+0.359 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0282 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.028)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.028)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.294 (n=624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.322 (n=312)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2427` → IC=+0.296 (n=312)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2427 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2257` → IC=+0.309 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2257 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.320 (n=936)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2663` → IC=+0.318 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2663 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.359 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `12818.9858` → IC=+0.305 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12818.9858 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.304 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.313 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.258` → IC=+0.306 (n=168)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.258 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.310 (n=504)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2573` → IC=+0.325 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2573 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.367 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `16341.0554` → IC=+0.318 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16341.0554 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.300 (n=288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.297 (n=432)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.322 (n=144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1516` → IC=+0.297 (n=288)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1516 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.317 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.313 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.332 (n=432)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.5893` → IC=+0.319 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5893 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.343 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0867` → IC=-0.260 (n=77)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0867
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=233)

- **FILTRO** `sigma_h` > `0.0042` → IC=-0.248 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=205)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.196 (n=67)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=137)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0682` → IC=-0.145 (n=60)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0682
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.174 (n=44)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=135)

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1941` → IC=-0.231 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.297` → IC=-0.139 (n=34)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.297
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.296` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.235 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.138` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.138
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1195` → IC=-0.206 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1195
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.3593` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3593
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3119` → IC=-0.184 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3119
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `81.6471` → IC=+0.209 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6471 (IC base=+0.197)

- **PATRÓN** `ratio` < `0.9753` → IC=+0.433 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9753 (IC base=+0.197)

- **PATRÓN** `T_h` > `145.7372` → IC=+0.386 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7372 (IC base=+0.338)

- **PATRÓN** `ratio` > `1.0088` → IC=+0.318 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0088 (IC base=+0.338)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.196 (n=169)

  - _Acción_: Kelly boost +0.98€ cuando `T_h` > 103.3918 (IC base=+0.176)

- **PATRÓN** `ratio` < `0.972` → IC=+0.420 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.176)

- **PATRÓN** `T_h` > `106.964` → IC=+0.301 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 106.964 (IC base=+0.292)

- **PATRÓN** `ratio` > `1.0467` → IC=+0.397 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0467 (IC base=+0.292)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `82.5234` → IC=+0.245 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 82.5234 (IC base=+0.230)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.404 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.230)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.351 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.326)

- **PATRÓN** `ratio` > `1.0112` → IC=+0.363 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0112 (IC base=+0.326)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1062` → IC=+0.450 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1062 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5909 sube el IC de +0.192 a +0.266 en UPDOWN_GBM#15min (n=2946). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.214 a +0.276 en UPDOWN_GBM#BTC#15min (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5773 sube el IC de +0.144 a +0.241 en UPDOWN_GBM#ETH#15min (n=588). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9149 sube el IC de +0.124 a +0.303 en UPDOWN_GBM#SOL#15min (n=176). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5758 sube el IC de +0.218 a +0.300 en UPDOWN_GBM#XRP#15min (n=684). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.160 en UPDOWN_GBM#XRP#15min (n=713). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.067 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=929). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3518 sube el IC de -0.012 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=3136). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.089 a +0.329 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=279). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.189 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6307 sube el IC de +0.151 a +0.253 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=468). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.242 a +0.269 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1073). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.179 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3455 sube el IC de -0.038 a +0.287 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=487). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.200 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=764). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.289 a +0.320 en UPDOWN_GBM_IBS_ALTO (n=936). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.283 a +0.310 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=504). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.294 a +0.332 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=432). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.361 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=565). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.358 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=300). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.362 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=265). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1676 | +0.089 | +193.35€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1676 | +0.089 | +193.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1305 | +0.094 | +166.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1305 | +0.094 | +166.31€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 268 | +0.067 | +11.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 268 | +0.067 | +11.32€ | 3 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 373 | +0.001 | +73.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 373 | +0.001 | +73.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 270 | -0.004 | +50.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 270 | -0.004 | +50.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 80 | +0.037 | +21.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 80 | +0.037 | +21.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 36197 | -0.084 | -4716.99€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1879 | -0.004 | -244.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 34318 | -0.088 | -4472.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4423 | -0.116 | -760.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4423 | -0.116 | -760.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1879 | -0.004 | -244.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1879 | -0.004 | -244.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4114 | -0.113 | -841.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4114 | -0.113 | -841.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9399 | +0.005 | -886.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9399 | +0.005 | -886.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9354 | -0.109 | -714.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9354 | -0.109 | -714.59€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7028 | -0.152 | -1268.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7028 | -0.152 | -1268.86€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 29077 | -0.018 | +3597.01€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7512 | +0.003 | +1757.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 21565 | -0.026 | +1839.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 29077 | -0.018 | +3597.01€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7512 | +0.003 | +1757.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 21565 | -0.026 | +1839.91€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 126232 | +0.114 | -5437.33€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17096 | +0.182 | -517.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 544 | -0.037 | -65.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 100857 | +0.104 | -4570.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7735 | +0.103 | -283.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 16740 | +0.105 | -1098.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 57 | -0.144 | +12.20€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 16668 | +0.106 | -1099.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 24793 | +0.129 | -392.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4982 | +0.194 | -145.54€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 16722 | +0.118 | -137.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3047 | +0.087 | -87.52€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 16791 | +0.096 | -1263.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 67 | -0.109 | -4.71€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 16709 | +0.097 | -1247.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 26832 | +0.123 | -487.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7075 | +0.176 | -114.54€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 16929 | +0.106 | -311.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2816 | +0.100 | -52.54€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 24320 | +0.113 | -1342.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4856 | +0.190 | -273.30€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 447 | -0.001 | -11.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 17145 | +0.093 | -914.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1872 | +0.132 | -143.21€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 16756 | +0.104 | -853.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 59 | -0.057 | +7.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 16684 | +0.104 | -861.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 20238 | +0.194 | -1285.80€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 20238 | +0.194 | -1285.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4663 | +0.175 | -426.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4663 | +0.175 | -426.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2335 | +0.198 | -58.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2335 | +0.198 | -58.26€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4600 | +0.180 | -378.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4600 | +0.180 | -378.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4024 | +0.243 | -141.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4024 | +0.243 | -141.62€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4537 | +0.189 | -294.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4537 | +0.189 | -294.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 919 | +0.427 | -31.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 919 | +0.427 | -31.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 363 | +0.434 | -6.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 363 | +0.434 | -6.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 355 | +0.430 | -9.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 355 | +0.430 | -9.26€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 189 | +0.406 | -12.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 189 | +0.406 | -12.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 70338 | +0.200 | -5191.14€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 70338 | +0.200 | -5191.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12098 | +0.184 | -1262.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12098 | +0.184 | -1262.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 11334 | +0.224 | -390.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 11334 | +0.224 | -390.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12067 | +0.178 | -1331.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12067 | +0.178 | -1331.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 11403 | +0.220 | -432.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 11403 | +0.220 | -432.54€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11660 | +0.201 | -793.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11660 | +0.201 | -793.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 11776 | +0.195 | -980.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 11776 | +0.195 | -980.48€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 26842 | +0.118 | +233.28€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 26842 | +0.118 | +233.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 13336 | +0.121 | +197.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 13336 | +0.121 | +197.88€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 13506 | +0.114 | +35.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 13506 | +0.114 | +35.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1851 | +0.293 | -0.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1851 | +0.293 | -0.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 838 | +0.286 | -5.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 838 | +0.286 | -5.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 895 | +0.291 | +0.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 895 | +0.291 | +0.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 118 | +0.350 | +4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 118 | +0.350 | +4.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 850 | +0.443 | +6.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 850 | +0.443 | +6.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 409 | +0.442 | +1.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 409 | +0.442 | +1.62€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 395 | +0.445 | +4.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 395 | +0.445 | +4.25€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1436 | +0.070 | -64.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 534 | +0.060 | -39.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 902 | +0.075 | -25.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 69 | +0.106 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 69 | +0.106 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1113 | +0.076 | -31.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 211 | +0.077 | -5.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 902 | +0.075 | -25.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 254 | +0.031 | -36.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 254 | +0.031 | -36.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 52071 | +0.100 | -1317.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4218 | +0.094 | +69.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 47853 | +0.101 | -1387.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 28781 | +0.105 | -288.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4218 | +0.094 | +69.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 24563 | +0.107 | -357.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 10479 | +0.109 | -34.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 10479 | +0.109 | -34.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 12811 | +0.081 | -995.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 12811 | +0.081 | -995.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 875 | +0.200 | -103.20€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 875 | +0.200 | -103.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 875 | +0.200 | -103.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 875 | +0.200 | -103.20€ | 2 | 4 |
| ✅ GBM_LATE_15M | 36084 | +0.090 | +18185.02€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 36084 | +0.090 | +18185.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6071 | +0.206 | +4759.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6071 | +0.206 | +4759.51€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 5360 | +0.179 | +3925.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5360 | +0.179 | +3925.66€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 6431 | +0.202 | +4916.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6431 | +0.202 | +4916.82€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5075 | +0.038 | +1335.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5075 | +0.038 | +1335.19€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 5159 | -0.031 | +1115.68€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5159 | -0.031 | +1115.68€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 7988 | -0.037 | +2132.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7988 | -0.037 | +2132.16€ | 2 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 39099 | +0.087 | +20826.83€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 39099 | +0.087 | +20826.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7577 | +0.008 | +3806.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7577 | +0.008 | +3806.61€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8171 | +0.013 | +1790.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8171 | +0.013 | +1790.50€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5488 | +0.271 | +5729.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5488 | +0.271 | +5729.16€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6753 | +0.013 | +1543.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6753 | +0.013 | +1543.91€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6334 | +0.037 | +2536.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6334 | +0.037 | +2536.18€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4776 | +0.293 | +5420.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4776 | +0.293 | +5420.47€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 28759 | +0.177 | +22691.85€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 28759 | +0.177 | +22691.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4362 | +0.219 | +3688.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4362 | +0.219 | +3688.56€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4521 | +0.151 | +3315.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4521 | +0.151 | +3315.27€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4583 | +0.218 | +3833.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4583 | +0.218 | +3833.82€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4841 | +0.139 | +3630.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4841 | +0.139 | +3630.22€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5402 | +0.124 | +3953.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5402 | +0.124 | +3953.08€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5050 | +0.218 | +4270.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5050 | +0.218 | +4270.90€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7741 | +0.139 | +3761.61€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7741 | +0.139 | +3761.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 342 | +0.142 | +200.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 342 | +0.142 | +200.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2382 | +0.149 | +1354.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2382 | +0.149 | +1354.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 377 | +0.139 | +171.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 377 | +0.139 | +171.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2383 | +0.151 | +1178.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2383 | +0.151 | +1178.18€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1719 | +0.107 | +614.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1719 | +0.107 | +614.85€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 538 | +0.135 | +242.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 538 | +0.135 | +242.32€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 36296 | +0.183 | +28357.34€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 36296 | +0.183 | +28357.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5781 | +0.233 | +5201.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5781 | +0.233 | +5201.81€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5601 | +0.149 | +3718.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5601 | +0.149 | +3718.37€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6103 | +0.230 | +5379.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6103 | +0.230 | +5379.31€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5916 | +0.139 | +4179.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5916 | +0.139 | +4179.96€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6431 | +0.123 | +4380.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6431 | +0.123 | +4380.07€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6464 | +0.222 | +5497.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6464 | +0.222 | +5497.82€ | 0 | 20 |
| ✅ GBM_LATE_5M | 10001 | +0.187 | +7156.96€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 10001 | +0.187 | +7156.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2200 | +0.178 | +1647.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2200 | +0.178 | +1647.59€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 1002 | +0.176 | +657.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1002 | +0.176 | +657.98€ | 0 | 16 |
| ✅ GBM_LATE_5M#ETH | 3079 | +0.189 | +2122.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3079 | +0.189 | +2122.51€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1339 | +0.175 | +930.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1339 | +0.175 | +930.78€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1462 | +0.183 | +984.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1462 | +0.183 | +984.11€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2794 | +0.068 | +956.28€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 2794 | +0.068 | +956.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1051 | +0.086 | +375.04€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1051 | +0.086 | +375.04€ | 0 | 9 |
| ✅ GBM_LATE_60M#ETH | 883 | +0.067 | +351.57€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 883 | +0.067 | +351.57€ | 0 | 9 |
| ✅ GBM_LATE_60M#SOL | 860 | +0.045 | +229.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 860 | +0.045 | +229.67€ | 2 | 13 |
| 🚫 GBM_LATE_60M_FADE | 505 | -0.240 | -15.81€ | 10 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 505 | -0.240 | -15.81€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 192 | -0.232 | -10.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 192 | -0.232 | -10.05€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 176 | -0.219 | +0.69€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 176 | -0.219 | +0.69€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 137 | -0.270 | -6.45€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 137 | -0.270 | -6.45€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1260 | +0.086 | +316.93€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1260 | +0.086 | +316.93€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 482 | +0.083 | +100.01€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 482 | +0.083 | +100.01€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 456 | +0.061 | +74.18€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 456 | +0.061 | +74.18€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 322 | +0.127 | +142.74€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 322 | +0.127 | +142.74€ | 2 | 15 |
| ✅ LATE_WINDOW_5MIN | 139 | +0.252 | +118.97€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 139 | +0.252 | +118.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 139 | +0.252 | +118.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 139 | +0.252 | +118.97€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3008 | +0.099 | +756.21€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3008 | +0.099 | +756.21€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3008 | +0.099 | +756.21€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3008 | +0.099 | +756.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 446 | -0.069 | -32.31€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 446 | -0.069 | -32.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 127 | -0.027 | -0.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 127 | -0.027 | -0.72€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 70 | -0.097 | -8.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 70 | -0.097 | -8.98€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3209 | +0.020 | +85.82€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3209 | +0.020 | +85.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 155 | +0.022 | -2.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 155 | +0.022 | -2.00€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 558 | +0.030 | +40.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 558 | +0.030 | +40.78€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1149 | +0.030 | +32.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1149 | +0.030 | +32.00€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 737 | +0.011 | +0.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 737 | +0.011 | +0.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 407 | +0.013 | +19.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 407 | +0.013 | +19.13€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1518 | -0.043 | -28.64€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1518 | -0.043 | -28.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 430 | -0.037 | -12.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 430 | -0.037 | -12.53€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 506 | -0.020 | +2.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 506 | -0.020 | +2.58€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 582 | -0.067 | -18.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 582 | -0.067 | -18.70€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 5996 | -0.020 | +74.72€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2848 | -0.025 | +3.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3148 | -0.016 | +70.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 170 | +0.000 | +9.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 83 | +0.041 | +11.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 87 | -0.039 | -2.30€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1504 | -0.009 | +40.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 718 | -0.011 | +11.71€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 786 | -0.006 | +28.90€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 664 | -0.027 | +2.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 335 | -0.040 | -7.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 329 | -0.014 | +10.16€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1232 | -0.033 | -28.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 568 | -0.047 | -35.32€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 664 | -0.021 | +7.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1174 | -0.013 | +40.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 567 | -0.013 | +24.24€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 607 | -0.012 | +15.97€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1252 | -0.028 | +10.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 577 | -0.032 | -0.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 675 | -0.024 | +10.98€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 42092 | -0.002 | +2006.60€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 42092 | -0.002 | +2006.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7530 | +0.025 | +984.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7530 | +0.025 | +984.64€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6191 | -0.034 | -115.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6191 | -0.034 | -115.61€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7640 | +0.022 | +763.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7640 | +0.022 | +763.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6019 | -0.051 | -181.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6019 | -0.051 | -181.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7105 | -0.007 | +219.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7105 | -0.007 | +219.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7607 | +0.014 | +336.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7607 | +0.014 | +336.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6313 | -0.059 | -149.62€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6313 | -0.059 | -149.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1221 | +0.000 | -14.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1221 | +0.000 | -14.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1580 | -0.076 | -34.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1580 | -0.076 | -34.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 740 | -0.123 | -33.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 740 | -0.123 | -33.74€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1863 | -0.079 | -39.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1863 | -0.079 | -39.42€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3358 | +0.004 | -2.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3358 | +0.004 | -2.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 138 | +0.000 | -1.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 138 | +0.000 | -1.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1322 | +0.005 | +5.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1322 | +0.005 | +5.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1389 | +0.007 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1389 | +0.007 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 105309 | -0.074 | +1688.55€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 105309 | -0.074 | +1688.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 18183 | -0.074 | +969.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 18183 | -0.074 | +969.64€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 15936 | -0.098 | -875.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 15936 | -0.098 | -875.97€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 18451 | -0.066 | +1024.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 18451 | -0.066 | +1024.66€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 15471 | -0.095 | -467.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 15471 | -0.095 | -467.63€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 18997 | -0.052 | +379.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 18997 | -0.052 | +379.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 18271 | -0.065 | +658.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 18271 | -0.065 | +658.44€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8522 | -0.033 | -182.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8522 | -0.033 | -182.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1950 | -0.045 | -22.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1950 | -0.045 | -22.16€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2553 | -0.028 | -49.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2553 | -0.028 | -49.47€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1136 | -0.051 | -25.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1136 | -0.051 | -25.77€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 879 | -0.029 | -32.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 879 | -0.029 | -32.75€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1466 | +0.122 | +585.69€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1330 | +0.128 | +573.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 310 | +0.144 | +163.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 310 | +0.144 | +163.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 261 | +0.116 | +86.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 261 | +0.116 | +86.15€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 270 | +0.129 | +122.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 270 | +0.129 | +122.23€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 237 | +0.153 | +130.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 237 | +0.153 | +130.93€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 252 | +0.095 | +69.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 252 | +0.095 | +69.81€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1108 | -0.022 | -26.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1108 | -0.022 | -26.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 213 | -0.007 | +4.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 213 | -0.007 | +4.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 184 | -0.016 | +0.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 184 | -0.016 | +0.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 288 | -0.038 | -18.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 288 | -0.038 | -18.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 234 | +0.000 | -0.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 234 | +0.000 | -0.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 189 | -0.044 | -13.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 189 | -0.044 | -13.15€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 806 | -0.069 | -30.55€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 369 | -0.123 | -74.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 289 | -0.156 | -67.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 286 | -0.028 | +30.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 207 | -0.021 | +29.77€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 151 | -0.016 | +13.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 618 | -0.086 | -29.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 976 | -0.204 | -47.28€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 400 | -0.202 | -34.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 345 | -0.206 | -34.88€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 330 | -0.214 | -27.36€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 286 | -0.222 | -32.94€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 246 | -0.194 | +14.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 227 | -0.190 | +11.03€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 858 | -0.208 | -56.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 408 | +0.395 | +375.02€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 102 | +0.375 | +92.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 102 | +0.375 | +92.55€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 253 | +0.457 | +236.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 253 | +0.457 | +236.35€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 408 | +0.395 | +375.02€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 646 | +0.035 | +35.73€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 646 | +0.035 | +35.73€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 49 | +0.010 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 49 | +0.010 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 67 | -0.007 | -0.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 67 | -0.007 | -0.79€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 234 | +0.068 | +35.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 234 | +0.068 | +35.36€ | 3 | 5 |
| ✅ STREAK_FADE_5M | 3340 | -0.020 | -126.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3340 | -0.020 | -126.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 585 | -0.026 | -25.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 585 | -0.026 | -25.65€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 158 | -0.037 | -13.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 158 | -0.037 | -13.35€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1546 | -0.015 | -50.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1546 | -0.015 | -50.26€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 93 | -0.047 | -8.86€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 93 | -0.047 | -8.86€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 39 | -0.085 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 39 | -0.085 | -3.98€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 54 | -0.018 | -4.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 54 | -0.018 | -4.88€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10114 | +0.019 | +110.89€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10114 | +0.019 | +110.89€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2523 | +0.026 | +51.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2523 | +0.026 | +51.56€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2872 | +0.009 | -2.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2872 | +0.009 | -2.23€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2071 | +0.022 | +34.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2071 | +0.022 | +34.28€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9214 | +0.013 | -46.73€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 9214 | +0.013 | -46.73€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3653 | +0.019 | -2.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3653 | +0.019 | -2.47€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3592 | +0.010 | -31.73€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3592 | +0.010 | -31.73€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1969 | +0.009 | -12.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1969 | +0.009 | -12.53€ | 1 | 0 |
| ✅ UPDOWN_GBM | 66036 | +0.051 | +5652.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 16504 | +0.085 | +3725.34€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2174 | +0.007 | +12.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 43395 | +0.045 | +1855.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3740 | +0.008 | +61.31€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6744 | +0.088 | +1043.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1512 | +0.158 | +677.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5155 | +0.069 | +367.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 13010 | +0.052 | +1063.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2037 | +0.089 | +484.87€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 555 | +0.012 | +6.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 8661 | +0.056 | +525.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1676 | +0.006 | +44.87€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 81 | -0.078 | +2.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 7986 | +0.066 | +826.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1504 | +0.147 | +592.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6404 | +0.047 | +235.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 14475 | +0.041 | +868.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3792 | +0.060 | +516.59€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 549 | +0.008 | +8.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 8786 | +0.041 | +333.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1274 | +0.009 | +7.29€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 74 | -0.105 | +2.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 14504 | +0.028 | +620.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3923 | +0.036 | +353.38€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 538 | -0.002 | +0.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9187 | +0.029 | +263.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 790 | +0.010 | +9.14€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 66 | -0.147 | -5.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9315 | +0.060 | +1231.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3736 | +0.103 | +1100.51€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 377 | +0.012 | +0.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5202 | +0.032 | +130.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 221 | -0.110 | -0.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 753 | +0.361 | +262.73€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 753 | +0.361 | +262.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 400 | +0.358 | +131.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 400 | +0.358 | +131.98€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 353 | +0.362 | +130.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 353 | +0.362 | +130.75€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 17800 | -0.024 | +4345.90€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 17800 | -0.024 | +4345.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1637 | -0.056 | +491.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1637 | -0.056 | +491.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3017 | -0.109 | +155.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3017 | -0.109 | +155.40€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 911 | +0.218 | +750.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 911 | +0.218 | +750.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2053 | +0.214 | +1314.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2053 | +0.214 | +1314.43€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5060 | -0.063 | +689.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5060 | -0.063 | +689.27€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5122 | -0.063 | +944.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5122 | -0.063 | +944.32€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 195 | +0.033 | +5.53€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 195 | +0.033 | +5.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 195 | +0.033 | +5.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 195 | +0.033 | +5.53€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1247 | +0.289 | +1032.29€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1247 | +0.289 | +1032.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 672 | +0.283 | +521.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 672 | +0.283 | +521.62€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 575 | +0.294 | +510.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 575 | +0.294 | +510.67€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 775 | -0.114 | -83.64€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 775 | -0.114 | -83.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 228 | -0.087 | -18.28€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 228 | -0.087 | -18.28€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 82 | -0.155 | -7.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 82 | -0.155 | -7.67€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 86 | -0.193 | -7.63€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 86 | -0.193 | -7.63€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 3156 | +0.306 | +1549.01€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1136 | +0.259 | +169.54€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1207 | +0.299 | +535.76€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 813 | +0.379 | +843.70€ | 0 | 1 |