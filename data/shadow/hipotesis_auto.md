# Hipótesis automáticas — 2026-10-14 06:08 UTC
_Generado por shadow_postmortem.py sobre 890350 resoluciones (PNL=+113860.79€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.258 (n=163)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=601)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.238 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.195 (n=254)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 68.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.268 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.131)

- **PATRÓN** `banda_z` > `9.563` → IC=+0.217 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.563 (IC base=+0.131)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.734` → IC=+0.130 (n=668)

  - _Acción_: Kelly boost +0.65€ cuando `ballenas_wallet_edge_medio` > 0.734 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=802)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.131)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.235 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.211 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.6169` → IC=+0.261 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6169 (IC base=+0.136)

- **PATRÓN** `banda_z` > `10.179` → IC=+0.231 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.179 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=704)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.136)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.234 (n=107)

- **FILTRO** `banda_hit_calibrado` < `0.8019` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8019
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=96)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=115)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=98)

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

- **PATRÓN** `libro_liquidez` > `906.0197` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 906.0197 (IC base=+0.125)

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
- **FILTRO** `restante_s_al_confirmar` < `143.96` → IC=-0.207 (n=9348)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.96
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=28047)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.76` → IC=-0.265 (n=1107)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.76
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3322)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.47` → IC=-0.301 (n=1031)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.47
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3094)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.08` → IC=-0.218 (n=2430)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.08
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7290)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.51` → IC=-0.292 (n=1809)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.51
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=5430)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=19843)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=4136)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `9345.8788` → IC=+0.178 (n=1853)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9345.8788 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=16769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=20266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=15471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=6859)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7290.0547` → IC=+0.160 (n=2642)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7290.0547 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=1969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1928)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2419)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `16195.2715` → IC=+0.207 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16195.2715 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.194 (n=1737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=1939)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=2484)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `16078.4757` → IC=+0.198 (n=640)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 16078.4757 (IC base=+0.188)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=441)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `6891.1913` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6891.1913 (IC base=+0.087)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.136 (n=1043)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.44 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `5856.6213` → IC=+0.124 (n=240)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 5856.6213 (IC base=+0.085)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=3857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.366 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.224 (n=1721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.359 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=2014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=964)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=826)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.256 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=755)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2155.5298` → IC=+0.153 (n=419)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2155.5298 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.409 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=835)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.175 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.350 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `3371.7925` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3371.7925 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.236 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=16594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=14124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.232 (n=6937)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=3860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.179 (n=3655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=3739)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=1821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.233 (n=1217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.313 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.225)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=3794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=3638)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.187 (n=2075)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=3304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.246)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.350 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.246)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=3720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=2382)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=2742)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.431 (n=649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.427 (n=642)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `7517.3335` → IC=+0.442 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7517.3335 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.448 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `18171.404` → IC=+0.439 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18171.404 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.444 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `4010.0754` → IC=+0.429 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4010.0754 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.403)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.403)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.403)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=21461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=21789)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=3194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=6853)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=9571)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.228 (n=4395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3158)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=3673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.179 (n=6840)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=9134)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=4514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.277 (n=3086)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=8228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.262 (n=3234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=3566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.196 (n=3111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=3735)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=7755)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.21` → IC=+0.125 (n=7110)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.21 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=7581)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=9436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.43` → IC=+0.138 (n=7101)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.43 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3839)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.18` → IC=+0.126 (n=3530)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.18 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=3828)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.132 (n=4680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.86` → IC=+0.146 (n=3523)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.86 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=3916)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=4148)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.136 (n=3570)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.311 (n=1029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.294 (n=1516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `4306.4231` → IC=+0.297 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4306.4231 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.286 (n=596)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `5376.6669` → IC=+0.297 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5376.6669 (IC base=+0.284)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2071.3908` → IC=+0.304 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2071.3908 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.351)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.377 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.351)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.356 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.351)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.441 (n=589)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.442 (n=293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.448 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.449 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.445 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `2103.8839` → IC=+0.452 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2103.8839 (IC base=+0.444)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=87)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=73)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=87)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=73)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4759` → IC=+0.134 (n=11975)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.4759 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.9838` → IC=+0.245 (n=3992)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9838 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.7743` → IC=+0.258 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7743 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.3726` → IC=+0.254 (n=3231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3726 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.965` → IC=+0.185 (n=4516)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.965 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.253 (n=3410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2089 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6189` → IC=+0.258 (n=3408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6189 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.3021` → IC=+0.234 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3021 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.3424` → IC=+0.224 (n=3836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3424 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.5668` → IC=+0.141 (n=14700)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5668 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.5751` → IC=+0.187 (n=1029)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5751 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1495` → IC=+0.186 (n=5152)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1495 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `1.1939` → IC=+0.181 (n=5595)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1939 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.053` → IC=+0.183 (n=2537)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.053 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.230 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.6792` → IC=+0.209 (n=3179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6792 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.219 (n=9382)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 111.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.215 (n=879)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.347` → IC=+0.196 (n=2635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.347 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=1280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=1762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.9736` → IC=+0.274 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9736 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.096` → IC=+0.278 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.096 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.243 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.2732` → IC=+0.208 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2732 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.204 (n=2761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2096.16` → IC=+0.210 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2096.16 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.204 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.236 (n=1448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.239 (n=986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0875` → IC=+0.263 (n=724)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0875 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5093` → IC=+0.254 (n=2173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5093 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0942` → IC=+0.236 (n=1926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0942 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.250 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.232 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.245 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2391)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1585.6447` → IC=+0.244 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1585.6447 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.231 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.235 (n=940)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.223 (n=972)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.258 (n=940)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=2237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=2175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.967` → IC=+0.269 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.967 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.228 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.260 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.2417` → IC=+0.225 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2417 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.229 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6219 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.247 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.5126` → IC=+0.224 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5126 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.4379` → IC=+0.249 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4379 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.184 (n=719)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0745` → IC=+0.173 (n=719)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0745 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5867` → IC=+0.183 (n=1893)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5867 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1271` → IC=+0.157 (n=1960)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1271 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.165` → IC=+0.151 (n=348)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.165 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.236` → IC=+0.143 (n=1971)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.236 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.145 (n=2152)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1954 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.164 (n=787)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4576` → IC=+0.145 (n=2034)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4576 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4228` → IC=+0.142 (n=2034)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4228 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.171 (n=863)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 222.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.212 (n=905)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.262 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.195 (n=2391)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.213 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.1546` → IC=+0.204 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1546 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=3204)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2000.041` → IC=+0.201 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2000.041 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.223 (n=2113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.217 (n=2144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1763` → IC=+0.227 (n=1057)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1763 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0712` → IC=+0.236 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0712 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.539` → IC=+0.258 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.539 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3469` → IC=+0.256 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3469 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.724` → IC=+0.218 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.724 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7264` → IC=+0.231 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7264 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2075.512` → IC=+0.231 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2075.512 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.219 (n=2211)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.145 (n=139)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=3252)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.121 (n=991)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0054 (IC base=+0.051)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.222 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.1857` → IC=+0.332 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1857 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.068` → IC=+0.183 (n=1051)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.068 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.332 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.350 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` < `0.1771` → IC=+0.324 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1771 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.345 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `1.4113` → IC=+0.351 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4113 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` > `2.2172` → IC=+0.326 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2172 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.334 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.0951` → IC=+0.166 (n=848)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.0951 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.6631` → IC=+0.158 (n=217)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6631 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.146 (n=965)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8504 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.203 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.5196` → IC=+0.152 (n=1235)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5196 (IC base=+0.033)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=501)

- **FILTRO** `ibs_20min` < `0.2909` → IC=-0.198 (n=147)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2909
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=443)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.131 (n=3235)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=1615)

- **FILTRO** `sigma_ewma_delta_pct` > `8.654` → IC=-0.227 (n=500)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.654
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=4350)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.176 (n=202)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7857 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.9864` → IC=+0.286 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9864 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.5952` → IC=+0.255 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5952 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.125 (n=206)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.257 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.871 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.0006` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0006 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1558` → IC=+0.270 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1558 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.286 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.259 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.151 (n=1615)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2222 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2634` → IC=+0.277 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2634 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.7102` → IC=+0.287 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7102 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.301 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.3955` → IC=+0.298 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3955 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6268` → IC=-0.179 (n=858)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6268
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2575)

- **FILTRO** `ibs_20min` < `0.728` → IC=-0.153 (n=2265)

  - _Acción_: SKIP cuando `ibs_20min` < 0.728
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1168)

- **FILTRO** `ibs_20min` > `0.76` → IC=-0.204 (n=1260)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=3808)

- **PATRÓN** `dist_vwap_pct` > `0.4495` → IC=+0.322 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4495 (IC base=-0.072)

- **PATRÓN** `dist_vwap_pct` < `0.193` → IC=+0.300 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.193 (IC base=-0.072)

- **PATRÓN** `volumen_regimen` < `1.1432` → IC=+0.294 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1432 (IC base=-0.072)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.310 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.072)

- **PATRÓN** `volumen_pendiente_norm` < `0.1029` → IC=+0.301 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1029 (IC base=-0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.295 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=-0.072)

- **PATRÓN** `volumen_spike_ratio` < `1.4371` → IC=+0.323 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4371 (IC base=-0.072)

- **PATRÓN** `volumen_spike_ratio` > `1.8611` → IC=+0.299 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8611 (IC base=-0.072)

- **PATRÓN** `dist_vwap_pct` > `0.8005` → IC=+0.275 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8005 (IC base=-0.008)

- **PATRÓN** `volumen_regimen` > `1.0811` → IC=+0.284 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0811 (IC base=-0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1041` → IC=+0.281 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1041 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.1777` → IC=+0.260 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1777 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.264 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=-0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.204 (n=5263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.886` → IC=+0.277 (n=7158)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.886 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.9472` → IC=+0.293 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9472 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.644` → IC=+0.157 (n=7063)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.644 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.1757` → IC=+0.255 (n=5802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1757 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6894` → IC=+0.261 (n=5183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6894 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.270 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6389` → IC=+0.265 (n=3102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6389 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.286 (n=8859)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.161 (n=5072)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.009 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5368` → IC=+0.160 (n=13380)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5368 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2375` → IC=+0.260 (n=4611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2375 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1951` → IC=+0.265 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1951 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.313 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5835` → IC=+0.284 (n=2945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5835 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2717` → IC=+0.278 (n=3034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2717 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.288 (n=6604)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3694` → IC=-0.163 (n=1440)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3694
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=2926)

- **FILTRO** `ibs_20min` > `0.7526` → IC=-0.201 (n=903)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7526
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=2713)

- **FILTRO** `sigma_ewma_delta_pct` > `4.567` → IC=-0.196 (n=791)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.567
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=2825)

- **PATRÓN** `ibs_20min` > `0.9142` → IC=+0.295 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9142 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.136` → IC=+0.207 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.136 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.293 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4486` → IC=+0.224 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4486 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.2415` → IC=+0.260 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2415 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.260 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.1596` → IC=+0.156 (n=905)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1596 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0728` → IC=+0.420 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0728 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.4828` → IC=+0.409 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4828 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.5212` → IC=+0.401 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5212 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.399 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1123` → IC=+0.205 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1123 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.197` → IC=+0.180 (n=1528)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.197 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6809` → IC=+0.190 (n=1365)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.6809 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.221 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.204 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.4786` → IC=+0.193 (n=502)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4786 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `193.0` → IC=+0.236 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 193.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1497` → IC=+0.232 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1497 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6209` → IC=+0.236 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6209 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0745` → IC=+0.229 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0745 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.298 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5491` → IC=+0.237 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5491 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1745` → IC=+0.250 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1745 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.292 (n=1563)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=2460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=2097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.267` → IC=+0.292 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.267 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.271 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.6122` → IC=+0.266 (n=2253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6122 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.271 (n=2750)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1987.3384` → IC=+0.284 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1987.3384 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.330 (n=903)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.1806` → IC=+0.305 (n=877)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1806 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.327 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.3631` → IC=+0.292 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3631 (IC base=+0.290)

- **PATRÓN** `ibs_20min` > `0.1081` → IC=+0.292 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1081 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.72` → IC=+0.306 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.72 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.1951` → IC=+0.288 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1951 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.3387` → IC=+0.304 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3387 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.7162` → IC=+0.303 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7162 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` > `2.6391` → IC=+0.299 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6391 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `2070.398` → IC=+0.315 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2070.398 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.292 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.290)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7478` → IC=-0.183 (n=935)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7478
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=2812)

- **PATRÓN** `ibs_20min` > `0.8878` → IC=+0.172 (n=878)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8878 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3676` → IC=+0.227 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3676 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0157` → IC=+0.241 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0157 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.164` → IC=+0.232 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.164 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.244 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.256 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.260 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1885` → IC=+0.224 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1885 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.226 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1942 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.103` → IC=+0.237 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.103 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.289 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.8189` → IC=+0.263 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8189 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4671` → IC=+0.252 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4671 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.251 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 129.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7632` → IC=-0.200 (n=1669)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7632
  - _Potencial_: sin este filtro IC_bueno=+0.296 (n=1673)

- **FILTRO** `ibs_20min` > `0.6545` → IC=-0.233 (n=830)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6545
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=2491)

- **FILTRO** `sigma_ewma_delta_pct` > `8.558` → IC=-0.234 (n=377)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.558
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2944)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.296 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.2124` → IC=+0.331 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2124 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.168 (n=522)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8488` → IC=+0.325 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8488 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6316` → IC=+0.315 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6316 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.312 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.343 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.335 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.339 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.140 (n=2204)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5556 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2075` → IC=+0.243 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2075 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.7096` → IC=+0.258 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7096 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `1.1845` → IC=+0.234 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1845 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.2188` → IC=+0.240 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2188 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.246 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.252 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4232 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.270 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.030)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.341 (n=1618)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=865)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.295)

- **PATRÓN** `ibs_20min` > `0.6516` → IC=+0.327 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6516 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.325 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.315 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.295)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.305 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.295)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.342 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.295)

- **PATRÓN** `volumen_spike_ratio` > `1.43` → IC=+0.307 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.43 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `2474.544` → IC=+0.308 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.544 (IC base=+0.295)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.330 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.329 (n=1275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.299 (n=843)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.305 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.297)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.322 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.3069` → IC=+0.297 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3069 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.518` → IC=+0.305 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.518 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.01` → IC=+0.298 (n=2279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.01 (IC base=+0.297)

- **PATRÓN** `volumen_regimen` < `0.719` → IC=+0.297 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.719 (IC base=+0.297)

- **PATRÓN** `volumen_regimen` > `1.2282` → IC=+0.327 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2282 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.347 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` < `1.4172` → IC=+0.304 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4172 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` > `2.1396` → IC=+0.300 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1396 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2433.3002` → IC=+0.302 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2433.3002 (IC base=+0.297)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.186 (n=3891)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0048 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.220 (n=3886)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3457` → IC=+0.188 (n=10249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3457 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=12085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.561` → IC=+0.231 (n=11646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.561 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1668` → IC=+0.207 (n=4880)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1668 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.354` → IC=+0.254 (n=2306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.354 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1978` → IC=+0.169 (n=7727)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1978 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6273` → IC=+0.163 (n=7729)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6273 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.201 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6045` → IC=+0.188 (n=3759)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6045 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2014.5756` → IC=+0.183 (n=10404)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2014.5756 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.195 (n=10565)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 99.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.187 (n=7450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.225 (n=3724)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=4203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.4951` → IC=+0.235 (n=11169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4951 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.144` → IC=+0.197 (n=1845)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.144 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1819` → IC=+0.166 (n=7982)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1819 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.225 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.626` → IC=+0.187 (n=3480)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.626 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.195 (n=8928)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 67.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.233 (n=654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.3322` → IC=+0.227 (n=1954)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3322 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.214 (n=1315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9216` → IC=+0.290 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9216 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.146` → IC=+0.329 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.146 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.267 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.2511` → IC=+0.220 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2511 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.219 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2097.1285` → IC=+0.219 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2097.1285 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.244 (n=1012)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.242 (n=685)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0691` → IC=+0.299 (n=506)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0691 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=1363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.005` → IC=+0.296 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.005 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.243 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.276 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4284` → IC=+0.259 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4284 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.6706` → IC=+0.246 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6706 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=1668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1567.34` → IC=+0.254 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1567.34 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.244 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.219 (n=586)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1623` → IC=+0.185 (n=1169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1623 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=1843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.3545` → IC=+0.221 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3545 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.214 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.468` → IC=+0.228 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.468 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.168 (n=772)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6895 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.0696` → IC=+0.156 (n=795)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0696 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.186 (n=278)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.5138` → IC=+0.173 (n=756)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5138 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.4971` → IC=+0.160 (n=572)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4971 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `424.0` → IC=+0.161 (n=1675)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 424.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=1835)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.176 (n=1614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6083` → IC=+0.205 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6083 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.655` → IC=+0.205 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.655 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.164 (n=1834)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2032 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0703` → IC=+0.146 (n=1466)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0703 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.150 (n=563)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.152 (n=1715)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4963 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7847` → IC=+0.149 (n=1143)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7847 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.169 (n=724)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 233.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.235 (n=659)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3997` → IC=+0.223 (n=1730)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3997 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=2037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.5` → IC=+0.292 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.5 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3513` → IC=+0.228 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3513 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.7734` → IC=+0.214 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7734 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7037` → IC=+0.225 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7037 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1990.6681` → IC=+0.220 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1990.6681 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.246 (n=1477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.269 (n=560)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.288 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.3543` → IC=+0.251 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3543 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.632` → IC=+0.273 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.632 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.274 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7224` → IC=+0.241 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7224 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.7272` → IC=+0.243 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7272 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2070.8434` → IC=+0.250 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2070.8434 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.227 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.233)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.176 (n=1878)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0074 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.4028` → IC=+0.168 (n=1878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4028 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3144` → IC=+0.210 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3144 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1388` → IC=+0.194 (n=1189)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1388 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.969` → IC=+0.202 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.969 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.163 (n=1252)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8553 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.177 (n=775)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4237` → IC=+0.158 (n=614)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4237 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.5013` → IC=+0.166 (n=614)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5013 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `4707.8067` → IC=+0.195 (n=1252)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 4707.8067 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.162 (n=1818)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 144.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.157 (n=1973)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.007 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3872` → IC=+0.147 (n=1972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3872 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6818` → IC=+0.188 (n=1972)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6818 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1506` → IC=+0.156 (n=1942)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1506 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.878` → IC=+0.156 (n=696)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.878 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8571` → IC=+0.161 (n=1315)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8571 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.197 (n=298)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8092` → IC=+0.134 (n=1226)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8092 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4213` → IC=+0.132 (n=1838)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4213 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `4434.3207` → IC=+0.169 (n=1315)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4434.3207 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.143 (n=598)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 59.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.130 (n=709)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0059 (IC base=+0.127)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.168 (n=965)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.01 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.5652` → IC=+0.128 (n=2126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.5652 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.4889` → IC=+0.215 (n=2126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4889 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.190 (n=1273)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.679` → IC=+0.265 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.679 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1891` → IC=+0.141 (n=2126)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1891 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1608` → IC=+0.136 (n=2152)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1608 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4387` → IC=+0.145 (n=688)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4387 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2853.6473` → IC=+0.210 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2853.6473 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.156 (n=682)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 21.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.144 (n=1907)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0092 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1069` → IC=+0.170 (n=722)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1069 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.220 (n=2170)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1974` → IC=+0.149 (n=2005)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1974 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.524` → IC=+0.130 (n=439)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 7.524 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.536` → IC=+0.124 (n=1911)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 2.536 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.132 (n=2166)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1776 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1651` → IC=+0.122 (n=2083)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1651 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.151 (n=282)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4527` → IC=+0.133 (n=669)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4527 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.132 (n=669)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2700.5187` → IC=+0.190 (n=982)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2700.5187 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.129 (n=1989)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 51.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.242 (n=1761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.2814` → IC=+0.226 (n=1315)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2814 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=2041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.222 (n=1778)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.6552` → IC=+0.254 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6552 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.1917` → IC=+0.225 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1917 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.247 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.183` → IC=+0.219 (n=1972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.183 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.225 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.267 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `2.1548` → IC=+0.220 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1548 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `1.8081` → IC=+0.230 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8081 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.219 (n=2562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2645.421` → IC=+0.227 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.421 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.236 (n=886)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0122 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.233 (n=913)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.261 (n=671)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` < `0.4226` → IC=+0.257 (n=2012)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4226 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `1.1533` → IC=+0.237 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1533 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.249 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6418` → IC=+0.236 (n=2012)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6418 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.286 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.228 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2408.8526` → IC=+0.233 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2408.8526 (IC base=+0.227)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.205 (n=1320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.177 (n=1000)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0085 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3359` → IC=+0.185 (n=2635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3359 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=1490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.7276` → IC=+0.225 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7276 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.7807` → IC=+0.192 (n=466)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.7807 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.689` → IC=+0.202 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.689 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.0578` → IC=+0.188 (n=2357)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0578 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.178 (n=2392)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6955 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1013` → IC=+0.186 (n=1078)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1013 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4339` → IC=+0.193 (n=970)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4339 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.5152` → IC=+0.179 (n=970)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.5152 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.178 (n=3399)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `2746.5037` → IC=+0.179 (n=2674)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2746.5037 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.188 (n=2773)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 151.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.144 (n=1046)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0036 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.3688` → IC=+0.161 (n=2082)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3688 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.433` → IC=+0.129 (n=1011)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.433 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.133 (n=1315)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 29.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.208 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.0997` → IC=+0.216 (n=375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0997 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.194 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.6473` → IC=+0.219 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6473 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.3049` → IC=+0.190 (n=269)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3049 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.137` → IC=+0.188 (n=363)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.137 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.834` → IC=+0.165 (n=904)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.834 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.193 (n=568)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8753 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.175 (n=336)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.2167` → IC=+0.174 (n=734)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.2167 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.4164` → IC=+0.166 (n=834)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4164 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `14845.767` → IC=+0.177 (n=568)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14845.767 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.200 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.194 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0027 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.141 (n=992)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6298` → IC=+0.170 (n=873)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6298 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.715` → IC=+0.141 (n=190)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 8.715 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.155` → IC=+0.129 (n=901)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.155 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0611` → IC=+0.157 (n=450)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.0611 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0982` → IC=+0.172 (n=346)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0982 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.139 (n=862)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=1286)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.161 (n=644)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 216.0 (IC base=+0.127)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.250 (n=618)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.224 (n=618)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.6787` → IC=+0.268 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6787 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.3567` → IC=+0.223 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3567 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.213 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.989` → IC=+0.230 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.989 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8392` → IC=+0.213 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8392 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.182` → IC=+0.227 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.182 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.241 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4109` → IC=+0.249 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4109 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.4387` → IC=+0.226 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4387 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.0987` → IC=+0.170 (n=307)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.0987 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `7277.3315` → IC=+0.135 (n=612)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 7277.3315 (IC base=+0.080)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.151 (n=709)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0106 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.154 (n=322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0093 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.5366` → IC=+0.151 (n=709)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.5366 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.9449` → IC=+0.219 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9449 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.112` → IC=+0.215 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.112 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0551` → IC=+0.172 (n=624)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.0551 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.6503` → IC=+0.157 (n=709)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6503 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.179 (n=104)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4582` → IC=+0.158 (n=229)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4582 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.1881` → IC=+0.161 (n=311)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1881 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=733)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.190 (n=237)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.150 (n=630)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` < `1.5655` → IC=+0.127 (n=298)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5655 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `2774.6938` → IC=+0.156 (n=321)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2774.6938 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.139 (n=441)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 22.0 (IC base=+0.063)

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

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.158 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0119 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.134 (n=214)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.61 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.1471` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1471 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.969` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 4.969 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6529` → IC=+0.120 (n=214)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` > 0.6529 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.134 (n=173)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 17.0 (IC base=+0.113)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.181 (n=5058)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0046 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.221 (n=5055)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=15777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.5584` → IC=+0.239 (n=13527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5584 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1624` → IC=+0.192 (n=5574)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1624 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.343` → IC=+0.252 (n=3708)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.343 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2258` → IC=+0.168 (n=10141)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2258 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.204 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6075` → IC=+0.196 (n=4899)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6075 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1829.0184` → IC=+0.185 (n=15141)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1829.0184 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.201 (n=13767)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.194 (n=6037)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0053 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3793` → IC=+0.192 (n=12043)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3793 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=5122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5766` → IC=+0.242 (n=13685)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5766 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.1738` → IC=+0.172 (n=8182)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1738 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.923` → IC=+0.209 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.923 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.666` → IC=+0.190 (n=13213)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.666 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6352` → IC=+0.162 (n=3087)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6352 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.251 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.6126` → IC=+0.199 (n=4295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6126 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `1766.2984` → IC=+0.188 (n=13685)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1766.2984 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.214 (n=8497)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.239 (n=834)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.3478` → IC=+0.220 (n=2487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3478 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=1206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.221 (n=1670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.349 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.279 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.265` → IC=+0.233 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.265 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=2590)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2017.79` → IC=+0.231 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2017.79 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.233 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.263 (n=2094)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.2011` → IC=+0.271 (n=1397)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2011 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=1904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.4947` → IC=+0.283 (n=2094)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4947 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.392` → IC=+0.261 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.392 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.258 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.280 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6396` → IC=+0.273 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6396 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1584.8284` → IC=+0.268 (n=2094)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1584.8284 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.261 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.201 (n=817)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1767` → IC=+0.164 (n=1628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1767 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2626` → IC=+0.207 (n=2441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2626 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1244` → IC=+0.193 (n=1331)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1244 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.666` → IC=+0.162 (n=406)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.666 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.156 (n=2232)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.629` → IC=+0.173 (n=815)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.629 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0712` → IC=+0.154 (n=2179)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0712 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.173 (n=347)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1781` → IC=+0.160 (n=2096)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1781 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5299` → IC=+0.155 (n=2128)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5299 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `10332.5429` → IC=+0.153 (n=2441)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 10332.5429 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.180 (n=1023)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 268.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=2032)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.187 (n=679)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6969` → IC=+0.198 (n=2031)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6969 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.169 (n=1863)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.255` → IC=+0.161 (n=452)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.255 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1835` → IC=+0.156 (n=2031)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1835 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.154` → IC=+0.192 (n=544)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.154 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.151 (n=1927)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7762` → IC=+0.162 (n=1285)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7762 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `250.0` → IC=+0.150 (n=612)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 250.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.249 (n=839)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.391` → IC=+0.314 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.391 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2094` → IC=+0.224 (n=2557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2094 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.6938` → IC=+0.238 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6938 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=2963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2000.58` → IC=+0.239 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2000.58 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.246 (n=2064)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.243 (n=2099)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.256 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.268 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0217` → IC=+0.303 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0217 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.074` → IC=+0.290 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.074 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.343` → IC=+0.292 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.343 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.723` → IC=+0.240 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.723 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.13` → IC=+0.247 (n=1478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.13 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2071.1599` → IC=+0.265 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2071.1599 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.245 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.203 (n=1141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4158` → IC=+0.157 (n=2590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4158 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2558` → IC=+0.194 (n=2591)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2558 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.5539` → IC=+0.176 (n=675)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5539 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.174` → IC=+0.162 (n=1049)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.174 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.166 (n=1728)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8725 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.184 (n=340)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.172 (n=1112)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1733` → IC=+0.158 (n=1145)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1733 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6973.6067` → IC=+0.238 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6973.6067 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.175 (n=1084)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 77.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.189 (n=716)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0032 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4319` → IC=+0.142 (n=2132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4319 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.74` → IC=+0.187 (n=2132)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.74 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.146` → IC=+0.146 (n=1889)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.146 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.258` → IC=+0.174 (n=326)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.258 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8743` → IC=+0.141 (n=1422)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8743 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.232 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4325` → IC=+0.141 (n=2046)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4325 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `7613.0669` → IC=+0.210 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7613.0669 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.145 (n=1745)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0082 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4481` → IC=+0.198 (n=2616)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4481 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0494` → IC=+0.206 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0494 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.907` → IC=+0.266 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.907 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8869` → IC=+0.148 (n=1744)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8869 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.126 (n=2460)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.136 (n=339)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `2.4754` → IC=+0.124 (n=2552)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4754 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.4651` → IC=+0.126 (n=2552)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4651 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2672)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2883.9504` → IC=+0.251 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2883.9504 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.136 (n=798)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.143 (n=2494)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0109 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1331` → IC=+0.161 (n=833)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1331 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=2564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.216 (n=2494)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.139 (n=2103)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.375` → IC=+0.135 (n=2403)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.375 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6439` → IC=+0.144 (n=832)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6439 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.169 (n=418)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4358` → IC=+0.150 (n=775)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4358 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2725.786` → IC=+0.212 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2725.786 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.140 (n=2031)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 48.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.243 (n=2229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.232 (n=1802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.607` → IC=+0.269 (n=2229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.607 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1996` → IC=+0.242 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1996 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.721` → IC=+0.270 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.721 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2332` → IC=+0.229 (n=2495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2332 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.228 (n=2495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2361` → IC=+0.250 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2361 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.5125` → IC=+0.249 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5125 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=3234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2653.0544` → IC=+0.237 (n=1663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2653.0544 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.247 (n=1176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.234 (n=2434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.5094` → IC=+0.265 (n=2595)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5094 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.196` → IC=+0.257 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.196 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.256 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.298 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4357` → IC=+0.229 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4357 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2421.5477` → IC=+0.229 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2421.5477 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.220 (n=2345)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.226)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=4574)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.238 (n=1550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.5025` → IC=+0.208 (n=4624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5025 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=1658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=2133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9402` → IC=+0.245 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9402 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.1717` → IC=+0.204 (n=1776)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1717 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.4338` → IC=+0.207 (n=3303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4338 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.154` → IC=+0.214 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.154 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.646` → IC=+0.200 (n=4132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.646 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.216 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.886` → IC=+0.204 (n=2252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.886 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.219 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.207 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.262` → IC=+0.203 (n=2066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.262 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=3576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2597.7472` → IC=+0.206 (n=4624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2597.7472 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.231 (n=1152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.4897` → IC=+0.200 (n=3442)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4897 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=1164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=1548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.199 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.18 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.6721` → IC=+0.196 (n=600)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6721 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.2382` → IC=+0.181 (n=3097)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2382 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.12` → IC=+0.191 (n=3449)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.12 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.0971` → IC=+0.195 (n=2859)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 1.0971 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.190 (n=3144)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5327` → IC=+0.191 (n=1494)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.5327 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.811` → IC=+0.191 (n=2263)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.811 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=4574)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.195 (n=2965)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 162.0 (IC base=+0.184)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.253 (n=565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.270 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.240 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.4994` → IC=+0.261 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4994 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` < `0.3329` → IC=+0.247 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3329 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.111` → IC=+0.241 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.111 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.615` → IC=+0.237 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.615 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.241 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2151 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `0.8602` → IC=+0.251 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8602 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.331 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.8362` → IC=+0.242 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8362 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `12382.594` → IC=+0.250 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12382.594 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.243 (n=523)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.369` → IC=+0.176 (n=1181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.369 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.191 (n=451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 5.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.192 (n=520)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1435 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.169 (n=536)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6078 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.6858` → IC=+0.208 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6858 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.1571` → IC=+0.164 (n=1158)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1571 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.181 (n=1163)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.883` → IC=+0.199 (n=788)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.883 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.0681` → IC=+0.181 (n=543)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.0681 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.170 (n=392)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.804` → IC=+0.178 (n=784)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.804 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `11340.2858` → IC=+0.175 (n=1181)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 11340.2858 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `698.0` → IC=+0.175 (n=1135)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 698.0 (IC base=+0.163)

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

- **PATRÓN** `volumen_pendiente_norm` < `0.3521` → IC=+0.172 (n=834)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.3521 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.226 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `3.3854` → IC=+0.184 (n=232)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3854 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2525.266` → IC=+0.217 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2525.266 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `2.0` → IC=+0.267 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 2.0 (IC base=+0.227)

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

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.215 (n=1324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4612` → IC=+0.206 (n=1323)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4612 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5142` → IC=+0.216 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5142 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.8779` → IC=+0.204 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8779 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.171` → IC=+0.207 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.171 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.882` → IC=+0.201 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.882 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2372` → IC=+0.211 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2372 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.203 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.1645` → IC=+0.203 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1645 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.4147` → IC=+0.221 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4147 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.246 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.205 (n=1066)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.199 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.7503` → IC=+0.186 (n=1066)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7503 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.183 (n=1066)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.0847 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.6564` → IC=+0.194 (n=191)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6564 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.355` → IC=+0.187 (n=964)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 4.355 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.6373` → IC=+0.221 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6373 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.197 (n=450)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1797` → IC=+0.192 (n=919)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.1797 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `7173.1135` → IC=+0.194 (n=1066)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7173.1135 (IC base=+0.180)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.208 (n=600)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.201 (n=698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.254 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.7421` → IC=+0.239 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7421 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.182` → IC=+0.214 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.182 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.6985` → IC=+0.235 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6985 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.186 (n=616)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.198 (n=303)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.565` → IC=+0.184 (n=292)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.565 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.4649` → IC=+0.213 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4649 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=790)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `3100.278` → IC=+0.197 (n=609)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3100.278 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.198 (n=666)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 53.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.214 (n=225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.361` → IC=+0.239 (n=331)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.361 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.231 (n=336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.7187` → IC=+0.219 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7187 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.8823` → IC=+0.215 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8823 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.3111` → IC=+0.209 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3111 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.913` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.913 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.926` → IC=+0.206 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.926 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.6785` → IC=+0.214 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6785 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.9323` → IC=+0.203 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9323 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1067` → IC=+0.232 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1067 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.1876` → IC=+0.229 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1876 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2990.7396` → IC=+0.223 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2990.7396 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.238 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.201)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.160 (n=663)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0038 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.4079` → IC=+0.149 (n=1403)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.4079 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.151 (n=511)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.384` → IC=+0.178 (n=309)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.384 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.1905` → IC=+0.261 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1905 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` < `0.0941` → IC=+0.137 (n=665)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0941 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.617` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 10.617 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.200 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` < `2.6035` → IC=+0.123 (n=630)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.6035 (IC base=+0.063)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.139 (n=505)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0056 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.145 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.5456` → IC=+0.197 (n=424)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5456 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.4234` → IC=+0.121 (n=433)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.4234 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.5664` → IC=+0.193 (n=278)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5664 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.2024` → IC=+0.132 (n=346)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2024 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.167 (n=130)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `2.5247` → IC=+0.120 (n=293)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.5247 (IC base=+0.078)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7058` → IC=-0.185 (n=71)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7058
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=214)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.155 (n=326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0046 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.6598` → IC=+0.208 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6598 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.185 (n=246)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.373` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.373 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.5851` → IC=+0.139 (n=153)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.5851 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.7834` → IC=+0.124 (n=269)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7834 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `1767.0561` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1767.0561 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.0163` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0163 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.031` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.031 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.136` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.136 (IC base=+0.022)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1304` → IC=-0.232 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1304
  - _Potencial_: sin este filtro IC_bueno=+0.261 (n=165)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.161 (n=322)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.75 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.874` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 7.874 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.030)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.167 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0094 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.1304` → IC=+0.261 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1304 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.2139` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2139 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.3658` → IC=+0.169 (n=179)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3658 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.847` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.847 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `1.0763` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0763 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.084` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.084 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.5298` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5298 (IC base=+0.084)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.207 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.084)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1839` → IC=-0.319 (n=70)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1839
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=212)

- **FILTRO** `dist_vwap_pct` > `0.2344` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2344
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=267)

- **FILTRO** `volumen_regimen` < `0.7708` → IC=-0.336 (n=71)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7708
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=213)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.369 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=179)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=216)

- **FILTRO** `sigma_ewma_delta_pct` > `10.676` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.676
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=214)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=127)

- **FILTRO** `libro_liquidez` < `1285.3712` → IC=-0.303 (n=59)

  - _Acción_: SKIP cuando `libro_liquidez` < 1285.3712
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=179)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.266 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=48)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=63)

- **FILTRO** `volumen_regimen` < `0.8417` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8417
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=70)

- **FILTRO** `volumen_spike_ratio` > `3.5274` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.5274
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.286 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=78)

- **FILTRO** `sigma_ewma_delta_pct` > `2.402` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.402
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=71)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=79)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.441 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=65)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=67)

- **FILTRO** `dist_vwap_pct` > `0.1189` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1189
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=62)

- **FILTRO** `volumen_spike_ratio` < `1.4507` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4507
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=39)

- **PATRÓN** `ibs_20min` > `0.9508` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.9508 (IC base=-0.167)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0062` → IC=-0.318 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=63)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=78)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=68)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.173 (n=215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0058 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.6786` → IC=+0.148 (n=473)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6786 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.5013` → IC=+0.192 (n=105)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.5013 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `0.8609` → IC=+0.138 (n=316)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8609 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` < `0.2332` → IC=+0.137 (n=411)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.2332 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `2.5313` → IC=+0.141 (n=371)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5313 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.165 (n=485)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.156 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.159` → IC=+0.189 (n=133)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.159 (IC base=+0.069)

- **PATRÓN** `libro_liquidez` > `3182.789` → IC=+0.148 (n=367)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3182.789 (IC base=+0.069)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6592` → IC=-0.240 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6592
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=145)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.221 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.171 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 12.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=94)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.201 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1361 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1185` → IC=+0.163 (n=268)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1185 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.257` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.257 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.809` → IC=+0.167 (n=199)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 4.809 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8617` → IC=+0.147 (n=168)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8617 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.158 (n=252)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6197 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0772` → IC=+0.172 (n=193)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.0772 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.5308` → IC=+0.176 (n=220)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.5308 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5221.482` → IC=+0.159 (n=168)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 5221.482 (IC base=+0.147)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.131` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.131
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=157)

- **FILTRO** `ibs_20min` > `0.2075` → IC=-0.146 (n=94)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2075
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=183)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.125 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0047 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.8015 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` < `0.131` → IC=+0.129 (n=157)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.131 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.7926` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.7926 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.2075` → IC=+0.138 (n=183)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.2075 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.041)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=92)

- **FILTRO** `dist_vwap_pct` > `0.2725` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=98)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.306 (n=106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.273 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=158)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.6436` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6436 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.224` → IC=+0.244 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.224 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.333` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.333 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `1.0021` → IC=+0.280 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0021 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.25` → IC=+0.302 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.25 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.250 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `667.907` → IC=+0.248 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 667.907 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.081)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=57)

- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.373 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.292)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.354 (n=53)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.292)

- **PATRÓN** `drift_ventana_pct` |x|> `0.356` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.356 (IC base=+0.210)

- **PATRÓN** `elapsed_s` > `185.1` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.1 (IC base=+0.210)

- **PATRÓN** `elapsed_s` < `214.9` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.9 (IC base=+0.210)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.275 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.210)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.210)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=57)

- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.373 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.292)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.354 (n=53)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.292)

- **PATRÓN** `drift_ventana_pct` |x|> `0.356` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.356 (IC base=+0.210)

- **PATRÓN** `elapsed_s` > `185.1` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.1 (IC base=+0.210)

- **PATRÓN** `elapsed_s` < `214.9` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.9 (IC base=+0.210)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.275 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.210)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.210)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1167)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2864.0516` → IC=+0.131 (n=532)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2864.0516 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1167)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2864.0516` → IC=+0.131 (n=532)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2864.0516 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=172)

- **FILTRO** `libro_liquidez` < `2715.711` → IC=-0.214 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2715.711
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=141)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=64)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

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

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=3199)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=57)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=89)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.217 (n=58)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=122)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=219)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=+0.036)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=1171)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1125)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=705)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=396)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=377)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.143 (n=155)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.017)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=808)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=808)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=703)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=703)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=182)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=206)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=249)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=187)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=221)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=326)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=326)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=239)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=178)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=1059)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=2700)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.55 (IC base=+0.071)

- **PATRÓN** `restante_min` > `9.94` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` > 9.94 (IC base=+0.071)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.071)

- **PATRÓN** `lag_apertura_s` < `303.82` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `lag_apertura_s` < 303.82 (IC base=+0.071)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `restante_min` < `3.89` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.127 (n=247)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=131)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.192 (n=118)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.46 (IC base=+0.026)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.182 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=194)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.5 (IC base=+0.038)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.216 (n=79)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=267)

- **FILTRO** `profundidad_ratio` < `37.2` → IC=-0.182 (n=86)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.2
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=260)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=259)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.46 (IC base=-0.027)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.138 (n=205)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=218)

- **FILTRO** `restante_min` < `3.8` → IC=-0.137 (n=210)

  - _Acción_: SKIP cuando `restante_min` < 3.8
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=213)

- **FILTRO** `lag_apertura_s` > `98.75` → IC=-0.176 (n=143)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.75
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=280)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.185 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=271)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` > `0.48` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` > 0.48 (IC base=-0.017)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.132 (n=245)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=133)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.180 (n=101)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=367)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.165 (n=5253)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=16757)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.169 (n=5639)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=17066)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.190 (n=963)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=2995)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.165 (n=940)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3127)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=2459)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.038)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1048)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1418.98` → IC=+0.133 (n=1979)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1418.98 (IC base=+0.038)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.123 (n=1884)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1548.958` → IC=+0.145 (n=1383)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1548.958 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.176 (n=791)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2459)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.176 (n=976)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=3026)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=1029)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=3108)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.125 (n=1361)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.9643 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1857.3584` → IC=+0.129 (n=1361)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1857.3584 (IC base=+0.037)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2275)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2687)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3427)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=416)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.254 (n=132)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=409)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `libro_liquidez` < `2574.706` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2574.706
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.191 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=294)

- **FILTRO** `libro_liquidez` < `3719.1657` → IC=-0.170 (n=207)

  - _Acción_: SKIP cuando `libro_liquidez` < 3719.1657
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=208)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=842)

- **FILTRO** `libro_liquidez` < `2053.5963` → IC=-0.164 (n=343)

  - _Acción_: SKIP cuando `libro_liquidez` < 2053.5963
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=698)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=43)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=15211)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=33951)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=11914)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=37248)

- **FILTRO** `ibs_7min` < `0.2462` → IC=-0.231 (n=12288)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2462
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=36874)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=16157)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33005)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.237 (n=15106)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=47165)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.180 (n=15458)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=46813)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=2449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6019)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=4204)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=4264)

- **FILTRO** `ibs_7min` < `0.7093` → IC=-0.247 (n=2794)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7093
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=5674)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.174 (n=1943)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6525)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.271 (n=2669)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=8149)

- **FILTRO** `ibs_7min` > `0.7743` → IC=-0.209 (n=2704)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7743
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=8114)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.126 (n=2019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=6327)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=1911)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=6435)

- **FILTRO** `ibs_7min` < `0.7324` → IC=-0.195 (n=2086)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7324
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6260)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.190 (n=2077)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6269)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2055)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6431)

- **FILTRO** `ibs_7min` > `0.2677` → IC=-0.194 (n=2119)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2677
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6367)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.183 (n=2115)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6371)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.158 (n=1989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=6083)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=1953)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=6119)

- **FILTRO** `ibs_7min` < `0.7015` → IC=-0.245 (n=2662)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7015
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=5410)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.223 (n=1682)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6390)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.249 (n=2623)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=8871)

- **FILTRO** `ibs_7min` > `0.7341` → IC=-0.175 (n=2873)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7341
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=8621)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=1863)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=6185)

- **FILTRO** `ibs_7min` < `0.7336` → IC=-0.187 (n=2012)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7336
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6036)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.191 (n=1997)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=6051)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=2076)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6246)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.181 (n=2080)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=6242)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.178 (n=2031)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6291)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=2033)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=6134)

- **FILTRO** `ibs_7min` < `0.2308` → IC=-0.234 (n=2039)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2308
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=6128)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2813)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=9084)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=1993)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6068)

- **FILTRO** `ibs_7min` < `0.2195` → IC=-0.220 (n=2015)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2195
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6046)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1866)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6195)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.209 (n=2737)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=8517)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=980)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1264)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.160 (n=51)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=633)

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
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=820)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=372)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.138 (n=158)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=316)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=426)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=610)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.145 (n=1050)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `442.4725` → IC=+0.160 (n=351)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 442.4725 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3687.403` → IC=+0.136 (n=476)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3687.403 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.159 (n=344)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 13.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4367` → IC=+0.167 (n=82)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4367 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.225 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2613.543` → IC=+0.226 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.543 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.182 (n=108)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 9.0 (IC base=+0.147)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` < `3.0` → IC=+0.149 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 3.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.129 (n=251)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.04 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2011.7397` → IC=+0.128 (n=213)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2011.7397 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 9.0 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.178 (n=141)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.153 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 4.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `390.3055` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 390.3055 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `8006.9091` → IC=+0.136 (n=141)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 8006.9091 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 72.0 (IC base=+0.129)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4332` → IC=+0.247 (n=85)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4332 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.149)

- **PATRÓN** `total_vol_5m` < `4927.909` → IC=+0.185 (n=125)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 4927.909 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3267.081` → IC=+0.163 (n=167)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3267.081 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 27.0 (IC base=+0.149)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.135 (n=176)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.095)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.121 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 13.0 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=122)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `3635.4092` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3635.4092 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `sigma_h` > `0.0061` → IC=-0.296 (n=204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=398)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.167 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0034 (IC base=-0.084)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.351 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=136)

- **FILTRO** `T_h` > `87.9981` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=136)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.292 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.046)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=70)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.066)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.224 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=140)

- **FILTRO** `T_h` > `71.5479` → IC=-0.183 (n=418)

  - _Acción_: SKIP cuando `T_h` > 71.5479
  - _Potencial_: sin este filtro IC_bueno=-0.127 (n=140)

- **FILTRO** `pct_vs_K` |x|> `2.2191` → IC=-0.386 (n=234)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.2191
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=235)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=142)

- **FILTRO** `T_h` > `79.3043` → IC=-0.185 (n=125)

  - _Acción_: SKIP cuando `T_h` > 79.3043
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=129)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.302 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=54)

- **FILTRO** `T_h` > `135.9836` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `T_h` > 135.9836
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=119)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.365 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=109)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=108)

- **FILTRO** `T_h` > `57.1769` → IC=-0.306 (n=96)

  - _Acción_: SKIP cuando `T_h` > 57.1769
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.300 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=100)

- **FILTRO** `T_h` > `113.7599` → IC=-0.220 (n=73)

  - _Acción_: SKIP cuando `T_h` > 113.7599
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=75)

- **FILTRO** `sigma_h` > `0.015` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.015
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=74)

- **FILTRO** `pct_vs_K` |x|> `3.8261` → IC=-0.414 (n=33)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8261
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=65)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.475 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.337)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.357 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.337)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.378 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.337)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.337)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.337)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.354 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.337)

- **PATRÓN** `edge` > `0.096` → IC=+0.447 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.419)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.419)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.442 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.419)

- **PATRÓN** `T_h` < `0.5922` → IC=+0.429 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5922 (IC base=+0.419)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.444 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.419)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.466 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.419)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.430)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.417 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.430)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.460 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.430)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.430)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.423 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.430)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.478 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.430)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.430)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1975` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1975 (IC base=+0.434)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.465 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.434)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.434)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `edge` > `0.1961` → IC=+0.478 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.478 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.1968` → IC=+0.478 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1968 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4421` → IC=+0.485 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4421 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=283)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=363)

- **FILTRO** `streak_estiramiento` > `0.8581` → IC=-0.171 (n=80)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8581
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=242)

- **PATRÓN** `streak_estiramiento` < `0.4095` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4095 (IC base=+0.036)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

- **FILTRO** `streak_estiramiento` > `0.4764` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4764
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `volumen_racha` < `945898.4` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_racha` < 945898.4 (IC base=+0.014)

- **PATRÓN** `streak_estiramiento` < `0.2918` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `streak_estiramiento` < 0.2918 (IC base=+0.014)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.155 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 10.0 (IC base=+0.079)

- **PATRÓN** `streak_estiramiento` < `0.3243` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.3243 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 44.0 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `2312.8768` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2312.8768 (IC base=+0.079)

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

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=43)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=704)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=920)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1327)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1056)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1071)

### STRUCT_NO_15M
- **FILTRO** `libro_liquidez` < `6797.2178` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 6797.2178
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3762)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `libro_liquidez` < `6797.2178` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 6797.2178
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2032)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.203 (n=1050)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.224 (n=1049)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1667` → IC=+0.198 (n=2771)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1667 (IC base=+0.189)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3519` → IC=+0.201 (n=2813)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3519 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=2920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2880)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.268 (n=3147)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.184 (n=1519)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.4733` → IC=+0.177 (n=2702)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.4733 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.693` → IC=+0.267 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.693 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `5210.4456` → IC=+0.203 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5210.4456 (IC base=+0.189)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=1244)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.241 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.265 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.218)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.253 (n=184)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.218)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2321` → IC=+0.230 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2321 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_15` > `0.7231` → IC=+0.280 (n=552)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7231 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.245 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.196` → IC=+0.299 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.196 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.220 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `16220.2116` → IC=+0.253 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16220.2116 (IC base=+0.218)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.391` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.391
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=703)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.187 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0033 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.155 (n=276)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.161 (n=417)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.165 (n=243)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=654)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.245 (n=626)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1175` → IC=+0.159 (n=400)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1175 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.5943` → IC=+0.148 (n=705)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.5943 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.293 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3537.6258` → IC=+0.156 (n=559)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3537.6258 (IC base=+0.146)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `18.722` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.722
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=263)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.151 (n=207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0056 (IC base=+0.116)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.167 (n=205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0102 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1497` → IC=+0.154 (n=411)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1497 (IC base=+0.116)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3297` → IC=+0.134 (n=566)

  - _Acción_: Kelly boost +0.67€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3297 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.130 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.116)

- **PATRÓN** `ibs_15` > `0.9091` → IC=+0.289 (n=207)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9091 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.3712` → IC=+0.126 (n=618)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.3712 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.664` → IC=+0.145 (n=119)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 17.664 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=341)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.116)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.191` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 8.191 (IC base=+0.020)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.285 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1648` → IC=+0.221 (n=633)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1648 (IC base=+0.217)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3318` → IC=+0.245 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3318 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.234 (n=661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.217)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.298 (n=721)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.1857` → IC=+0.221 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1857 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.822` → IC=+0.263 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.822 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2994.8704` → IC=+0.289 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.8704 (IC base=+0.217)

- **PATRÓN** `ibs_15` < `0.1099` → IC=+0.163 (n=724)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.81€ cuando `ibs_15` < 0.1099 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.367 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.369 (n=585)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1515` → IC=+0.388 (n=389)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1515 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2323` → IC=+0.384 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2323 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.375 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.396 (n=587)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.391 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.387 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `3851.736` → IC=+0.372 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3851.736 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.361 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.376 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.5078` → IC=+0.361 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5078 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.394 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.394 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.388 (n=309)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2504` → IC=+0.394 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2504 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.382 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.822` → IC=+0.361 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.822 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `15285.027` → IC=+0.387 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15285.027 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.409 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.363 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.383 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.361 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0902` → IC=+0.376 (n=247)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0902 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.382 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.390 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.359)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.366 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.7557` → IC=+0.406 (n=276)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7557 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.4453` → IC=+0.367 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4453 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.362 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.293` → IC=+0.394 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.293 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `3893.6222` → IC=+0.391 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3893.6222 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.362 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.359)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.221 (n=1004)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3014)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1559)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2459)

- **FILTRO** `libro_liquidez` < `4144.8126` → IC=-0.146 (n=2651)

  - _Acción_: SKIP cuando `libro_liquidez` < 4144.8126
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=1367)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1416` → IC=+0.188 (n=646)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1416 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6347` → IC=+0.283 (n=968)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6347 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1109` → IC=+0.208 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1109 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.4224` → IC=+0.202 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4224 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2266` → IC=+0.267 (n=1095)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2266 (IC base=-0.013)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3296` → IC=+0.254 (n=3217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3296 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3519` → IC=+0.281 (n=3281)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3519 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6474` → IC=+0.274 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6474 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.205 (n=567)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1709)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=569)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1707)

- **FILTRO** `sigma_ewma_delta_pct` > `23.61` → IC=-0.264 (n=329)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.61
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1947)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2212)

- **FILTRO** `libro_liquidez` < `16223.9385` → IC=-0.205 (n=1502)

  - _Acción_: SKIP cuando `libro_liquidez` < 16223.9385
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=774)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.174 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0026 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2139` → IC=+0.290 (n=136)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2139 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.280 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.334 (n=300)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.300 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.295 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.678` → IC=+0.141 (n=157)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 24.678 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.217 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.296 (n=52)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=630)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.164 (n=486)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0033 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1111` → IC=+0.184 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1111 (IC base=+0.155)

- **PATRÓN** `drift_15min` |x|≤ `0.4034` → IC=+0.159 (n=162)

  - _Acción_: Kelly boost +0.79€ cuando `drift_15min` |x|≤ 0.4034 (IC base=+0.155)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.163 (n=324)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=+0.155)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.199 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.176 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 11.0 (IC base=+0.155)

- **PATRÓN** `ibs_15` > `0.6285` → IC=+0.258 (n=486)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6285 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.455` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.455 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.160 (n=374)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.263 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=630)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.171 (n=162)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.254 (n=505)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3507` → IC=+0.244 (n=1009)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3507 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7599` → IC=+0.254 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7599 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1543` → IC=+0.257 (n=764)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1543 (IC base=+0.243)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3306` → IC=+0.244 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3306 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.243 (n=1019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3676` → IC=+0.273 (n=1147)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3676 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.7773` → IC=+0.291 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7773 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.569` → IC=+0.255 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.569 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.679` → IC=+0.247 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.679 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.250 (n=314)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=612)

- **FILTRO** `drift_15min` |x|> `0.8765` → IC=-0.273 (n=231)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8765
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=695)

- **FILTRO** `sigma_ewma_delta_pct` > `6.585` → IC=-0.195 (n=221)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.585
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=705)

- **FILTRO** `sigma_ewma_delta_pct` > `18.169` → IC=-0.146 (n=478)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.169
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3851)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.181)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.181)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.181)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.181)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0819` → IC=+0.239 (n=461)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0819 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.283 (n=518)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4456` → IC=+0.245 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4456 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.249 (n=556)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=558)

- **FILTRO** `drift_15min` |x|> `1.2346` → IC=-0.264 (n=278)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2346
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=836)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=1095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1563` → IC=+0.272 (n=357)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1563 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1116` → IC=+0.302 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1116 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3284` → IC=+0.292 (n=788)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3284 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7735` → IC=+0.348 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7735 (IC base=-0.026)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.297 (n=864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0534` → IC=+0.321 (n=328)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0534 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2448` → IC=+0.296 (n=327)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2448 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2247` → IC=+0.305 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2247 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=1029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8379` → IC=+0.322 (n=981)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8379 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.325 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.865` → IC=+0.369 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.865 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `12693.7099` → IC=+0.312 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12693.7099 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.308 (n=233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.310 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2603` → IC=+0.309 (n=176)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2603 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.827` → IC=+0.312 (n=529)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.827 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.323 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.027` → IC=+0.376 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.027 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.284 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16322.5844` → IC=+0.327 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16322.5844 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.307 (n=453)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.296 (n=453)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.324 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1516` → IC=+0.306 (n=302)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1516 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3023` → IC=+0.312 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3023 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.314 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=409)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8737` → IC=+0.338 (n=405)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8737 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.328 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.354 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1212` → IC=-0.151 (n=81)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1212
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=243)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.136 (n=218)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=74)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.167 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=354)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=159)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1319` → IC=-0.173 (n=47)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1319
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=143)

- **FILTRO** `drift_60min` |x|> `0.2244` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2244
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=33)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1254` → IC=-0.200 (n=18)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1254
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2968` → IC=-0.375 (n=22)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2968
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0775` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0775
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `83.3501` → IC=+0.201 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.194)

- **PATRÓN** `ratio` < `0.973` → IC=+0.419 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.194)

- **PATRÓN** `T_h` > `111.996` → IC=+0.351 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0235` → IC=+0.369 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0235 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.181 (n=183)

  - _Acción_: Kelly boost +0.91€ cuando `T_h` > 103.3918 (IC base=+0.168)

- **PATRÓN** `ratio` < `0.9839` → IC=+0.333 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9839 (IC base=+0.168)

- **PATRÓN** `T_h` > `109.696` → IC=+0.303 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.696 (IC base=+0.291)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.393 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.291)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.241 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.232)

- **PATRÓN** `ratio` < `0.9849` → IC=+0.429 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.232)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.350 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.343 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1038` → IC=+0.448 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.189 a +0.268 en UPDOWN_GBM#15min (n=3147). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7231 sube el IC de +0.218 a +0.280 en UPDOWN_GBM#BTC#15min (n=552). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de +0.146 a +0.245 en UPDOWN_GBM#ETH#15min (n=626). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9091 sube el IC de +0.116 a +0.289 en UPDOWN_GBM#SOL#15min (n=207). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.217 a +0.298 en UPDOWN_GBM#XRP#15min (n=721). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1099 sube el IC de +0.066 a +0.163 en UPDOWN_GBM#XRP#15min (n=724). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6347 sube el IC de -0.065 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=968). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3519 sube el IC de -0.013 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=3281). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.095 a +0.334 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=300). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.296 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6285 sube el IC de +0.155 a +0.258 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=486). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3676 sube el IC de +0.243 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1147). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.181 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.283 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=518). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.203 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3284 sube el IC de -0.026 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=788). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8379 sube el IC de +0.290 a +0.322 en UPDOWN_GBM_IBS_ALTO (n=981). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.827 sube el IC de +0.285 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=529). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8737 sube el IC de +0.295 a +0.338 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=405). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.362 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=587). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.362 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=309). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7557 sube el IC de +0.359 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=276). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1758 | +0.089 | +193.76€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1758 | +0.089 | +193.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1383 | +0.093 | +167.44€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1383 | +0.093 | +167.44€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 272 | +0.066 | +10.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 272 | +0.066 | +10.61€ | 4 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 434 | +0.000 | +68.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 434 | +0.000 | +68.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 312 | -0.003 | +47.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 312 | -0.003 | +47.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 96 | +0.020 | +17.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 96 | +0.020 | +17.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 37395 | -0.083 | -4657.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2010 | +0.017 | -238.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 35385 | -0.089 | -4418.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4429 | -0.116 | -761.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4429 | -0.116 | -761.79€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2010 | +0.017 | -238.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2010 | +0.017 | -238.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4125 | -0.113 | -844.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4125 | -0.113 | -844.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9872 | -0.007 | -824.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9872 | -0.007 | -824.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9720 | -0.108 | -720.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9720 | -0.108 | -720.55€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7239 | -0.144 | -1267.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7239 | -0.144 | -1267.71€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 31033 | -0.018 | +3549.44€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8031 | +0.004 | +1743.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 23002 | -0.025 | +1806.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 31033 | -0.018 | +3549.44€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8031 | +0.004 | +1743.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 23002 | -0.025 | +1806.27€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 132589 | +0.114 | -5542.34€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17632 | +0.182 | -534.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 575 | -0.029 | -64.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 106325 | +0.105 | -4662.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8057 | +0.103 | -279.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 17644 | +0.106 | -1118.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 59 | -0.156 | +9.83€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 17570 | +0.108 | -1116.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 25916 | +0.128 | -409.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5067 | +0.192 | -156.23€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 17626 | +0.118 | -143.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3181 | +0.086 | -87.61€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 17691 | +0.097 | -1299.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 69 | -0.106 | -3.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 17607 | +0.098 | -1283.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 28189 | +0.124 | -499.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7389 | +0.176 | -129.36€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 17848 | +0.107 | -308.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2940 | +0.100 | -53.46€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 25487 | +0.114 | -1331.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4985 | +0.193 | -261.94€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 478 | +0.006 | -10.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 18088 | +0.093 | -919.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1936 | +0.134 | -138.85€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 17662 | +0.104 | -884.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 63 | -0.069 | +6.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 17586 | +0.105 | -891.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 21274 | +0.195 | -1312.41€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 21274 | +0.195 | -1312.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4877 | +0.177 | -430.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4877 | +0.177 | -430.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2540 | +0.202 | -52.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2540 | +0.202 | -52.25€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4819 | +0.180 | -393.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4819 | +0.180 | -393.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4205 | +0.246 | -136.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4205 | +0.246 | -136.22€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4754 | +0.187 | -314.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4754 | +0.187 | -314.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 948 | +0.427 | -31.71€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 948 | +0.427 | -31.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 375 | +0.436 | -5.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 375 | +0.436 | -5.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 367 | +0.429 | -9.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 367 | +0.429 | -9.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 193 | +0.403 | -14.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 193 | +0.403 | -14.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 74106 | +0.201 | -5374.95€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 74106 | +0.201 | -5374.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12734 | +0.185 | -1313.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12734 | +0.185 | -1313.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 11949 | +0.225 | -409.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 11949 | +0.225 | -409.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12707 | +0.179 | -1374.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12707 | +0.179 | -1374.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 12030 | +0.220 | -454.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 12030 | +0.220 | -454.20€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 12285 | +0.202 | -811.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 12285 | +0.202 | -811.77€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 12401 | +0.196 | -1011.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 12401 | +0.196 | -1011.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 28329 | +0.117 | +201.43€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 28329 | +0.117 | +201.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 14079 | +0.120 | +177.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 14079 | +0.120 | +177.47€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 14250 | +0.114 | +23.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 14250 | +0.114 | +23.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1926 | +0.292 | -6.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1926 | +0.292 | -6.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 877 | +0.284 | -11.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 877 | +0.284 | -11.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 930 | +0.291 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 930 | +0.291 | -0.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 889 | +0.442 | +4.75€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 889 | +0.442 | +4.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 431 | +0.440 | +0.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 431 | +0.440 | +0.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 412 | +0.444 | +4.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 412 | +0.444 | +4.10€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1497 | +0.071 | -60.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 566 | +0.062 | -38.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 931 | +0.077 | -22.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 70 | +0.111 | +3.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 70 | +0.111 | +3.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1156 | +0.077 | -28.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 225 | +0.077 | -5.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 931 | +0.077 | -22.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 271 | +0.035 | -35.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 271 | +0.035 | -35.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 55282 | +0.100 | -1385.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4473 | +0.093 | +61.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 50809 | +0.101 | -1446.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 30506 | +0.105 | -323.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4473 | +0.093 | +61.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 26033 | +0.108 | -384.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 11217 | +0.109 | -52.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 11217 | +0.109 | -52.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 13559 | +0.082 | -1009.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 13559 | +0.082 | -1009.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 889 | +0.194 | -113.12€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 889 | +0.194 | -113.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 889 | +0.194 | -113.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 889 | +0.194 | -113.12€ | 2 | 4 |
| ✅ GBM_LATE_15M | 38237 | +0.092 | +19554.78€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 38237 | +0.092 | +19554.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6407 | +0.210 | +5109.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6407 | +0.210 | +5109.74€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 5710 | +0.179 | +4257.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5710 | +0.179 | +4257.40€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 6816 | +0.203 | +5253.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6816 | +0.203 | +5253.46€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 5363 | +0.039 | +1440.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5363 | +0.039 | +1440.13€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 5440 | -0.030 | +1194.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5440 | -0.030 | +1194.47€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 8501 | -0.034 | +2299.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8501 | -0.034 | +2299.57€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 41323 | +0.086 | +22324.68€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 41323 | +0.086 | +22324.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7982 | +0.006 | +4108.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7982 | +0.006 | +4108.88€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8690 | +0.013 | +1955.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8690 | +0.013 | +1955.98€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5773 | +0.274 | +6101.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5773 | +0.274 | +6101.38€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7256 | +0.014 | +1738.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7256 | +0.014 | +1738.72€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6663 | +0.039 | +2742.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6663 | +0.039 | +2742.18€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4959 | +0.296 | +5677.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4959 | +0.296 | +5677.54€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 30418 | +0.179 | +24331.56€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 30418 | +0.179 | +24331.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4619 | +0.223 | +3973.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4619 | +0.223 | +3973.42€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4781 | +0.151 | +3533.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4781 | +0.151 | +3533.32€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4855 | +0.221 | +4134.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4855 | +0.221 | +4134.26€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5132 | +0.140 | +3903.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5132 | +0.140 | +3903.38€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5721 | +0.124 | +4204.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5721 | +0.124 | +4204.35€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5310 | +0.222 | +4582.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5310 | +0.222 | +4582.83€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8151 | +0.136 | +3932.60€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8151 | +0.136 | +3932.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 390 | +0.150 | +239.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 390 | +0.150 | +239.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2457 | +0.144 | +1368.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2457 | +0.144 | +1368.29€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 417 | +0.149 | +209.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 417 | +0.149 | +209.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2459 | +0.145 | +1179.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2459 | +0.145 | +1179.06€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1888 | +0.107 | +697.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1888 | +0.107 | +697.86€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 540 | +0.133 | +238.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 540 | +0.133 | +238.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 38433 | +0.184 | +30345.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 38433 | +0.184 | +30345.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6106 | +0.236 | +5554.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6106 | +0.236 | +5554.59€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5961 | +0.149 | +4016.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5961 | +0.149 | +4016.74€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6475 | +0.231 | +5734.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6475 | +0.231 | +5734.51€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6295 | +0.139 | +4498.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6295 | +0.139 | +4498.46€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6812 | +0.122 | +4671.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6812 | +0.122 | +4671.34€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6784 | +0.225 | +5870.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6784 | +0.225 | +5870.29€ | 0 | 21 |
| ✅ GBM_LATE_5M | 10754 | +0.193 | +7984.78€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 10754 | +0.193 | +7984.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2430 | +0.188 | +1911.22€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2430 | +0.188 | +1911.22€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1002 | +0.176 | +657.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1002 | +0.176 | +657.98€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 3184 | +0.191 | +2226.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3184 | +0.191 | +2226.59€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 1569 | +0.189 | +1179.93€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1569 | +0.189 | +1179.93€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1650 | +0.196 | +1195.07€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1650 | +0.196 | +1195.07€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3019 | +0.070 | +1036.89€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 3019 | +0.070 | +1036.89€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1126 | +0.088 | +408.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1126 | +0.088 | +408.27€ | 0 | 9 |
| ✅ GBM_LATE_60M#ETH | 965 | +0.073 | +385.24€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 965 | +0.073 | +385.24€ | 1 | 11 |
| ✅ GBM_LATE_60M#SOL | 928 | +0.045 | +243.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 928 | +0.045 | +243.38€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 522 | -0.242 | -18.39€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 522 | -0.242 | -18.39€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 197 | -0.234 | -8.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 197 | -0.234 | -8.90€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 186 | -0.223 | -2.02€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 186 | -0.223 | -2.02€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 139 | -0.273 | -7.47€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 139 | -0.273 | -7.47€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1364 | +0.087 | +349.74€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1364 | +0.087 | +349.74€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 528 | +0.087 | +113.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 528 | +0.087 | +113.92€ | 1 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 504 | +0.061 | +83.46€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 504 | +0.061 | +83.46€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 332 | +0.126 | +152.35€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 332 | +0.126 | +152.35€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 144 | +0.253 | +124.85€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 144 | +0.253 | +124.85€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 144 | +0.253 | +124.85€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 144 | +0.253 | +124.85€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3182 | +0.101 | +795.02€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3182 | +0.101 | +795.02€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3182 | +0.101 | +795.02€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3182 | +0.101 | +795.02€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 455 | -0.062 | -28.95€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 455 | -0.062 | -28.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 133 | -0.011 | +1.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 133 | -0.011 | +1.94€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 73 | -0.087 | -8.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 73 | -0.087 | -8.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3405 | +0.018 | +84.31€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3405 | +0.018 | +84.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 168 | +0.018 | -3.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 168 | +0.018 | -3.27€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 641 | +0.024 | +39.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 641 | +0.024 | +39.77€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1221 | +0.029 | +33.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1221 | +0.029 | +33.08€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 746 | +0.011 | +0.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 746 | +0.011 | +0.72€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 426 | +0.009 | +19.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 426 | +0.009 | +19.09€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1606 | -0.043 | -30.10€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1606 | -0.043 | -30.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 454 | -0.037 | -13.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 454 | -0.037 | -13.35€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 542 | -0.020 | +2.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 542 | -0.020 | +2.80€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 610 | -0.067 | -19.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 610 | -0.067 | -19.55€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 6812 | -0.022 | +61.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3243 | -0.031 | -33.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3569 | -0.014 | +95.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 195 | -0.003 | +11.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 96 | +0.041 | +14.05€ | 0 | 4 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 99 | -0.045 | -2.61€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1713 | -0.012 | +38.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 817 | -0.019 | +3.37€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 896 | -0.006 | +35.24€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 743 | -0.025 | +7.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 377 | -0.043 | -10.02€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 366 | -0.005 | +17.05€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1421 | -0.035 | -32.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 663 | -0.047 | -36.40€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 758 | -0.025 | +3.88€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1351 | -0.019 | +23.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 650 | -0.029 | -0.31€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 701 | -0.009 | +24.20€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1389 | -0.027 | +13.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 640 | -0.036 | -4.53€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 749 | -0.019 | +18.03€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 44715 | -0.001 | +2174.67€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 44715 | -0.001 | +2174.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8025 | +0.025 | +1017.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8025 | +0.025 | +1017.54€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6532 | -0.034 | -106.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6532 | -0.034 | -106.05€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8139 | +0.023 | +806.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8139 | +0.023 | +806.61€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6365 | -0.047 | -142.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6365 | -0.047 | -142.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7536 | -0.004 | +243.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7536 | -0.004 | +243.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8118 | +0.015 | +355.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8118 | +0.015 | +355.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6420 | -0.060 | -159.99€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6420 | -0.060 | -159.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1224 | +0.000 | -14.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1224 | +0.000 | -14.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1636 | -0.080 | -43.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1636 | -0.080 | -43.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 749 | -0.122 | -33.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 749 | -0.122 | -33.59€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1902 | -0.078 | -40.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1902 | -0.078 | -40.68€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3365 | +0.005 | -0.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3365 | +0.005 | -0.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 138 | +0.000 | -1.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 138 | +0.000 | -1.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 111433 | -0.074 | +1778.52€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 111433 | -0.074 | +1778.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 19286 | -0.075 | +1011.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 19286 | -0.075 | +1011.12€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 16832 | -0.099 | -928.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 16832 | -0.099 | -928.69€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 19566 | -0.066 | +1138.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 19566 | -0.066 | +1138.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 16370 | -0.095 | -490.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 16370 | -0.095 | -490.75€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 20064 | -0.054 | +366.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 20064 | -0.054 | +366.65€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 19315 | -0.065 | +681.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 19315 | -0.065 | +681.82€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8641 | -0.033 | -178.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8641 | -0.033 | -178.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 997 | -0.017 | -19.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 997 | -0.017 | -19.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1963 | -0.045 | -22.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1963 | -0.045 | -22.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2571 | -0.026 | -42.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2571 | -0.026 | -42.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1153 | -0.051 | -25.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1153 | -0.051 | -25.67€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 949 | -0.032 | -36.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 949 | -0.032 | -36.34€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1536 | +0.123 | +621.45€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1400 | +0.129 | +608.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 327 | +0.147 | +177.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 327 | +0.147 | +177.52€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 283 | +0.117 | +96.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 283 | +0.117 | +96.40€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 281 | +0.129 | +127.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 281 | +0.129 | +127.61€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 249 | +0.149 | +134.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 249 | +0.149 | +134.45€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 260 | +0.095 | +72.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 260 | +0.095 | +72.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1233 | -0.021 | -27.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1233 | -0.021 | -27.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 233 | -0.006 | +5.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 233 | -0.006 | +5.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 213 | -0.012 | +1.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 213 | -0.012 | +1.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 321 | -0.048 | -29.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 321 | -0.048 | -29.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 262 | -0.004 | -1.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 262 | -0.004 | -1.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 204 | -0.024 | -4.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 204 | -0.024 | -4.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 842 | -0.071 | -42.25€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 389 | -0.119 | -77.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 300 | -0.152 | -67.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 301 | -0.035 | +22.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 215 | -0.030 | +22.89€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 152 | -0.019 | +13.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 637 | -0.087 | -36.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1027 | -0.207 | -57.18€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 414 | -0.207 | -37.94€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 358 | -0.211 | -38.22€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 348 | -0.217 | -30.63€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 302 | -0.227 | -36.32€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 265 | -0.193 | +11.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 246 | -0.190 | +8.24€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 906 | -0.211 | -66.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 421 | +0.396 | +401.59€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 105 | +0.369 | +91.40€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 105 | +0.369 | +91.40€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 263 | +0.459 | +264.06€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 263 | +0.459 | +264.06€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 421 | +0.396 | +401.59€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 684 | +0.028 | +26.49€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 684 | +0.028 | +26.49€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 55 | -0.026 | -5.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 55 | -0.026 | -5.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 71 | -0.007 | -0.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 71 | -0.007 | -0.09€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 262 | +0.053 | +28.49€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 262 | +0.053 | +28.49€ | 0 | 6 |
| ✅ STREAK_FADE_5M | 3383 | -0.021 | -131.77€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3383 | -0.021 | -131.77€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 586 | -0.025 | -25.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 586 | -0.025 | -25.10€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 162 | -0.043 | -14.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 162 | -0.043 | -14.36€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1584 | -0.017 | -54.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1584 | -0.017 | -54.79€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 95 | -0.046 | -8.93€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 95 | -0.046 | -8.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 40 | -0.071 | -3.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 40 | -0.071 | -3.54€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 55 | -0.026 | -5.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 55 | -0.026 | -5.39€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10347 | +0.018 | +98.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10347 | +0.018 | +98.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2650 | +0.021 | +27.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2650 | +0.021 | +27.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2644 | +0.021 | +40.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2644 | +0.021 | +40.28€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2884 | +0.009 | -2.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2884 | +0.009 | -2.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2169 | +0.021 | +33.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2169 | +0.021 | +33.33€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9451 | +0.013 | -50.34€ | 1 | 0 |
| ✅ STRUCT_NO_15M#15min | 9451 | +0.013 | -50.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3781 | +0.017 | -9.22€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3781 | +0.017 | -9.22€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3604 | +0.011 | -27.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3604 | +0.011 | -27.64€ | 1 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2066 | +0.009 | -13.48€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2066 | +0.009 | -13.48€ | 1 | 0 |
| ✅ UPDOWN_GBM | 69533 | +0.052 | +6083.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 17315 | +0.085 | +3934.38€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2282 | +0.007 | +18.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 45694 | +0.046 | +2052.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4005 | +0.010 | +79.33€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6818 | +0.089 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1543 | +0.158 | +694.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 14201 | +0.054 | +1198.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2172 | +0.091 | +530.43€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 591 | +0.013 | +10.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 9569 | +0.058 | +599.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1783 | +0.007 | +53.66€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 86 | -0.068 | +4.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8047 | +0.066 | +843.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1529 | +0.149 | +607.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6440 | +0.047 | +237.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 15485 | +0.043 | +974.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4024 | +0.063 | +580.33€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 582 | +0.009 | +11.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9429 | +0.042 | +364.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1371 | +0.013 | +16.29€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 79 | -0.105 | +2.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 15302 | +0.030 | +693.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4194 | +0.036 | +376.59€ | 0 | 9 |
| ✅ UPDOWN_GBM#SOL#240min | 566 | -0.004 | -0.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9621 | +0.032 | +313.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 851 | +0.011 | +9.38€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 70 | -0.139 | -4.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9678 | +0.062 | +1303.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3853 | +0.103 | +1144.98€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5437 | +0.036 | +158.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 235 | -0.103 | +1.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 779 | +0.362 | +277.35€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 779 | +0.362 | +277.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 411 | +0.362 | +140.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 411 | +0.362 | +140.98€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 368 | +0.359 | +136.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 368 | +0.359 | +136.37€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 18456 | -0.024 | +4464.79€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 18456 | -0.024 | +4464.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3186 | -0.112 | +134.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3186 | -0.112 | +134.22€ | 5 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2175 | +0.217 | +1419.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2175 | +0.217 | +1419.92€ | 1 | 24 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5255 | -0.064 | +698.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5255 | -0.064 | +698.55€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5240 | -0.064 | +943.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5240 | -0.064 | +943.64€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 206 | +0.034 | +5.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 206 | +0.034 | +5.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 206 | +0.034 | +5.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 206 | +0.034 | +5.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1308 | +0.290 | +1099.59€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1308 | +0.290 | +1099.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 705 | +0.285 | +552.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 705 | +0.285 | +552.95€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 603 | +0.295 | +546.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 603 | +0.295 | +546.63€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 796 | -0.112 | -82.22€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 796 | -0.112 | -82.22€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 239 | -0.085 | -18.46€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 239 | -0.085 | -18.46€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 85 | -0.155 | -8.13€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 85 | -0.155 | -8.13€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 89 | -0.181 | -6.27€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 89 | -0.181 | -6.27€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3328 | +0.304 | +1606.07€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1210 | +0.257 | +164.75€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1278 | +0.298 | +569.42€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 840 | +0.379 | +871.90€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.013 n=863 — no justifica filtro, seguir monitorizando
  - _Datos_: n=863 IC=+0.013 PNL=+30.56€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 682 celda(s) pasan gate riguroso completo de 2603 evaluadas (n>=40) y 3611 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.036 < 0.08 — monitorear
  - _Datos_: n=4187 IC=+0.036 PNL=+377.75€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1278/15 IC=+0.298 PNL=+569.42€ | BTC: n=1210/15 IC=+0.257 PNL=+164.75€ | SOL: n=840/15 IC=+0.379 PNL=+871.90€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.139 n=729/60 | contraria IC=+0.202 n=756 | gap=-0.063 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=423, boost estimado=+0.010. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1370/40 IC=+0.013 PNL=+16.80€ | BTC#60min: n=1782/40 IC=+0.007 PNL=+54.22€ | SOL#60min: n=849/40 IC=+0.011 PNL=+9.45€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=504765 | tras_1loss IC=+0.093 n=384744 | tras_2loss IC=+0.062 n=156509/40 | gap=-0.014 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.215 > 0.08 con n=636 PNL=+508.71€
  - _Datos_: n=636 IC=+0.215 PNL=+508.71€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.183 > 0.08 con n=736 PNL=+458.14€
  - _Datos_: n=736 IC=+0.183 PNL=+458.14€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=59 PNL=+35.04€
  - _Datos_: n=59 IC=+0.189 PNL=+35.04€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=2714 PNL=+1513.88€
  - _Datos_: n=2714 IC=+0.333 PNL=+1513.88€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=583 IC=+0.078 PNL=+68.68€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=583 IC=+0.078 PNL=+68.68€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=75 IC=+0.175 PNL=+47.33€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=75 IC=+0.175 PNL=+47.33€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 5/15 ops en el filtro definido (IC actual=+0.054 PNL=+5.10€)
  - _Datos_: n=5 IC=+0.054 PNL=+5.10€

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
  - _Estado_: n=2704 IC=+0.011 PNL=+13.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2704 IC=+0.011 PNL=+13.24€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1297 IC=+0.009 PNL=+67.23€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1297 IC=+0.009 PNL=+67.23€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=863 IC=+0.013 PNL=+30.56€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=863 IC=+0.013 PNL=+30.56€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.190 > 0.1 con n=4191 PNL=+2818.99€
  - _Datos_: n=4191 IC=+0.190 PNL=+2818.99€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2171 IC=+0.090 PNL=+529.93€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2171 IC=+0.090 PNL=+529.93€

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
  - _Estado_: n=886 IC=+0.043 PNL=+92.28€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=886 IC=+0.043 PNL=+92.28€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=102 IC=+0.038 PNL=+4.09€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=102 IC=+0.038 PNL=+4.09€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.253 n=144) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=144 IC=+0.253 PNL=+124.85€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.02 con n=886 PNL=+375.64€
  - _Datos_: n=886 IC=+0.127 PNL=+375.64€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=202 IC=-0.083 PNL=+23.24€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=202 IC=-0.083 PNL=+23.24€

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
  - _Estado_: n=26816 IC=+0.074 PNL=+3971.34€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=26816 IC=+0.074 PNL=+3971.34€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.136 < -0.1 con n=416 PNL=+54.52€
  - _Datos_: n=416 IC=-0.136 PNL=+54.52€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2892 IC=+0.065 PNL=+356.49€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2892 IC=+0.065 PNL=+356.49€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=126 IC=-0.109 PNL=+3.80€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=126 IC=-0.109 PNL=+3.80€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.1 con n=706 PNL=+190.50€
  - _Datos_: n=706 IC=+0.117 PNL=+190.50€

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
  - _Estado_: n=28476 IC=-0.135 PNL=+2190.31€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=28476 IC=-0.135 PNL=+2190.31€

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
  - _Estado_: n=2864 IC=+0.136 PNL=+1717.70€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2864 IC=+0.136 PNL=+1717.70€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=7145 IC=+0.048 PNL=+558.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7145 IC=+0.048 PNL=+558.84€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=3127 PNL=+1658.81€
  - _Datos_: n=3127 IC=+0.090 PNL=+1658.81€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=2922 PNL=-220.73€
  - _Datos_: n=2922 IC=-0.224 PNL=-220.73€

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
  - _Estado_: n=62 IC=-0.016 PNL=+3.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=62 IC=-0.016 PNL=+3.71€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=1618) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1618 IC=+0.099 PNL=+350.11€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=538) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=538 IC=+0.413 PNL=+773.91€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=12725 IC=+0.185 PNL=-1312.35€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=12725 IC=+0.185 PNL=-1312.35€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.1 con n=211 PNL=+134.64€
  - _Datos_: n=211 IC=+0.214 PNL=+134.64€
